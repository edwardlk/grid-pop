import pytest
import numpy as np
from grid_pop import Points


TEST_DATA = Points()


def test_corners():
    ll_points = [
        (90, 180), (90, -180), 
        (-90, 180), (-90, -180)]
    
    TEST_DATA.add_points(ll_points)

    assert np.isnan(TEST_DATA.pop_density).tolist() == [True, True, True, True]


def test__valid_lat_lon():
    ll_points = [
        (91, 0), (0, 181), (-91, 0), (0, -181), 
        (0, 0, 0)
    ]
    
    with pytest.raises(Exception) as e_info:
        for point in ll_points:
            TEST_DATA._valid_lat_lon(point)


def test__return_array_values():
    test_arr = np.array([[0, 1,], [2, 3]])

    ll_points = [
        (90, -180), (90, 180), 
        (-90, -180), (-90, 180)]
    
    for i, point in enumerate(ll_points):
        assert TEST_DATA._return_array_value(test_arr, point) == i
        