import pytest
from app.core.math_utils import PerceptualColorMath

def test_math_conversions():
    math_tool = PerceptualColorMath()
    
    # Red (255,0,0) em HSL decimal é (0, 1.0, 0.5)
    h, s, l = math_tool.rgb_to_hsl(255, 0, 0)
    assert h == 0
    assert s == 1.0  # Ajustado de 100 para 1.0
    assert l == 0.5  # Ajustado de 50 para 0.5

def test_calculate_distance():
    math_tool = PerceptualColorMath()
    hsl1 = (0, 100, 50) # Vermelho
    hsl2 = (0, 100, 55) # Vermelho ligeiramente mais claro
    
    dist = math_tool.calculate_distance(hsl1, hsl2)
    assert dist > 0
    assert math_tool.calculate_distance(hsl1, hsl1) == 0