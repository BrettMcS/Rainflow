# test_peak.py

import sys
sys.path.insert(0, '..\\cyclecount')

import numpy as np

from rainflow import get_turns


def test_get_turns():

    data1 = np.array([4, 0, -1, -3, 2, 0, 7, 9])
    ans1 = np.array([4, -3, 2, 0, 9])

    data2 = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    ans2 = np.array([0.0, 5.0])

    data3 = np.array([1, 1])
    ans3 = np.array([1, 1])

    data4 = np.array([-1.0, 1.0, -1.0, 1.0, -1.0, 1.0])
    ans4 = np.array([-1.0, 1.0, -1.0, 1.0, -1.0, 1.0])

    data5 = np.array([4, 4, 0, -1, -1, -3, 2, 2, 2, 0, 7, 7, 3, 3, 3])
    ans5 = np.array([4, -3, 2, 0, 7, 3])


    peaks1 = get_turns(data1)
    peaks2 = get_turns(data2)
    peaks3 = get_turns(data3)
    peaks4 = get_turns(data4)
    peaks5 = get_turns(data5)

    assert np.alltrue(peaks1 == ans1)
    assert np.alltrue(peaks2 == ans2)
    assert np.alltrue(peaks3 == ans3)
    assert np.alltrue(peaks4 == ans4)
    assert np.alltrue(peaks5 == ans5)
