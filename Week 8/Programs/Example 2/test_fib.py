# Set directory
import os
os.chdir(r'C:\Users\nicho\Desktop\1 Modern Data Structures - GR5072\QMSS-GR5072_Spring2024\Week 8\Programs\Example 2')

# Import module
from fib_module import fib

def test_fib0():
    # test edge 0
    obs = fib(0)
    assert obs == 0

def test_fib1():
    # test edge 1
    obs = fib(1)
    assert obs == 1

def test_fib6():
    # test internal point
    obs = fib(6)
    assert obs == 8
    
# python -m pytest  # Run this in your PC's terminal

