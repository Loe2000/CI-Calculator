"""
Tests for caclulator.py
"""
import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3, 2)

    def test_sub(self):
        assert 5 == calculator.subtract(10, 5)