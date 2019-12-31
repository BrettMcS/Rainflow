# rainflow.py
"""
Rainflow cycle counting function based on Downing's Method 1 of the
paper "Simple rainflow counting algorithms" by S.D.Downing and D.F.Socie
International Journal of Fatigue, January 1982.

This method is for limited histories where the data has been obtained
and stored. Method 2 from the same paper (not implemented here) is
designed for open-ended histories, typically in a monitoring situation.

Method 1 requires that the signal be first re-arranged so that signal
starts and finishes with the largest (magnitude) peak or trough (we just
say 'turn' to include both from now on).
"""
import numpy as np
from numba import jit


@jit(nopython=True)
def data_turns(data):
    """
    Returns the turns (peaks and troughs) of data. Eliminates repeats
    """
    was_going_up = data[0] <= 0
    was_going_down = not was_going_up
    num_turns = 0

    for curr_idx in range(1, len(data)):
        now_going_down = data[curr_idx] < data[curr_idx-1]
        now_going_up = data[curr_idx] > data[curr_idx-1]
        if (was_going_up and now_going_down) or (was_going_down and now_going_up):
            num_turns += 1
            data[num_turns] = data[curr_idx - 1]
            was_going_up = not was_going_up
            was_going_down = not was_going_down

    num_turns += 1
    data[num_turns] = data[-1]
    num_turns += 1

    return data[:num_turns]


@jit(nopython=True)
def data_rearranged_for_rainflow_counting(data):
    """
    Return data in the format required for Rainflow counting.
    """
    max_idx = np.argmax(np.abs(data))  # find the max value
    data = np.roll(data, len(data) - max_idx)  # start at the max value
    data = np.concatenate((data, data[0:1]))  # also finish on the max value

    return data_turns(data)


@jit(nopython=True)  # gives ~20x speed improvement
def ranges_means(data):
    """
    Return ranges, means of cycles counted using Downing's method 1.
    """
    turns = data_rearranged_for_rainflow_counting(data)
 
    values = []  # of the current turns being processed
    ranges = []
    means = []

    for turn in turns:
        values.append(turn)
        while len(values) > 2:
            X = abs(values[-1] - values[-2])
            Y = abs(values[-2] - values[-3])
            if X < Y:
                break
            ranges.append(Y)
            means.append(0.5*(values[-2] + values[-3]))
            values[-3] = values[-1]
            values.pop()
            values.pop()

    return ranges, means


def get_int_ranges_means(data, scale):
    """
    Return ranges, means of a 1D array using Rainflow cycle counting

    :Parameters:
        data: ndarray. The data to be analysed
        scale: float. Scale data by this value before converting to int

    :Returns:
        ranges, means: ndarrays. The cycle ranges and mean values

    :References:
        Rainflow cycle counting method based on Downing's Method 1 of
        the paper "Simple rainflow counting algorithms" by S.D.Downing
        and D.F.Socie, International Journal of Fatigue, January 1982.
    """
    data = np.array(np.rint(data * scale), dtype=np.int32)

    turns = data_rearranged_for_rainflow_counting(data)

    if len(turns) < 2:
        return [], []

    ranges, means = ranges_means(turns)

    return np.array(ranges) / scale, np.array(means) / scale
