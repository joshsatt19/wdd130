import pytest
from pytest import approx
import math

from shapes import circle_circumference, circle_area, triangle_perimeter, triangle_area, hemisphere_surface_area

def test_circle_circumference():
    assert circle_circumference(0) == 0 
    assert circle_circumference(5) == approx(31.41593)
    assert circle_circumference(100) == approx(628.31853)
    # assert circle_circumference(-5) == approx(-31.41593)

def test_hemisphere_surface_area():
    zero_result = hemisphere_surface_area(0)
    assert zero_result == 1, "Zero case should have been zero"

pytest.main()