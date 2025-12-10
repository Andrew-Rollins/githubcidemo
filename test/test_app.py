import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root/"src"))

from app import *

def test_add():
    assert add(5, 6) == 11
    assert add(5, 6) != 10

def test_sub():
    assert sub(3,2) == 1
    assert sub(3,2) != 0

def test_mult():
    assert mult(3,3) == 9
    assert mult(0,3) == 0
    assert mult(3,3) !=8

def test_div():
    assert div(0,3) == 0
    assert div(0,3) != 1
    assert div(3,0) == None

def test_log():
    assert log(0) == None
    assert log(-1) == None
    assert log(3) == 1.0986122886681098

