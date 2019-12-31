# test_peak.py

import sys
sys.path.insert(0, '..\\rainflow')

import numpy as np

import rainflow


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

    peaks1 = rainflow.data_turns(data1)
    peaks2 = rainflow.data_turns(data2)
    peaks3 = rainflow.data_turns(data3)
    peaks4 = rainflow.data_turns(data4)
    peaks5 = rainflow.data_turns(data5)

    assert np.allclose(peaks1, ans1)
    assert np.allclose(peaks2, ans2)
    assert np.allclose(peaks3, ans3)
    assert np.allclose(peaks4, ans4)
    assert np.allclose(peaks5, ans5)
