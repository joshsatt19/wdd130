import pytest
from LEGO_mosaic import find_lego_color, color_distance

test_lego_colors = {
        "White": (242, 243, 242),
        "Black": (27, 42, 52),
        "Red": (196, 40, 28),
        "Blue": (13, 105, 172),
        "Yellow": (245, 205, 47),
        "Green": (40, 127, 71),
        "Orange": (218, 133, 65),
        "Light Gray": (160, 165, 169),
        "Dark Gray": (99, 95, 98),
        "Brown": (88, 57, 39),
        "Tan": (228, 205, 158),
        "Pink": (255, 152, 195),
        "Purple": (129, 0, 123),
        "Light Blue": (180, 210, 227),
    }

def test_color_distance():
    assert color_distance((242, 243, 242), (242, 243, 242)) == 0
    assert color_distance((162, 48, 30), (242, 243, 242)) == 298.946
    assert color_distance((0, 0, 0), (242, 243, 242)) == 419.734

def test_find_lego_color():
    assert find_lego_color((162, 48, 30), test_lego_colors) == "Red"
    assert find_lego_color((242, 243, 242), test_lego_colors) == "White"
    assert find_lego_color((14, 109, 169), test_lego_colors) == "Blue"




pytest.main(["-v", "--tb=line", "-rN", __file__])   