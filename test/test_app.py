import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root/"src"))

from app import add
from app import sub

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_sub():
    assert sub(3,2) == 1

def test_sub2():
    assert sub(3,2) != 0