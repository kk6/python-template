"""Tests for the example module."""

from hypothesis import given
from hypothesis import strategies as st

from python_template.example import add, multiply


class TestAdd:
    """Tests for the add function."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        assert add(-2, -3) == -5

    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        assert add(5, -3) == 2

    def test_add_zero(self):
        """Test adding with zero."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5

    @given(st.integers(), st.integers())
    def test_add_commutative(self, a: int, b: int):
        """Test that addition is commutative."""
        assert add(a, b) == add(b, a)

    @given(st.integers(), st.integers(), st.integers())
    def test_add_associative(self, a: int, b: int, c: int):
        """Test that addition is associative."""
        assert add(add(a, b), c) == add(a, add(b, c))


class TestMultiply:
    """Tests for the multiply function."""

    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        assert multiply(3, 4) == 12

    def test_multiply_negative_numbers(self):
        """Test multiplying two negative numbers."""
        assert multiply(-3, -4) == 12

    def test_multiply_mixed_numbers(self):
        """Test multiplying positive and negative numbers."""
        assert multiply(3, -4) == -12

    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert multiply(0, 5) == 0
        assert multiply(5, 0) == 0

    def test_multiply_by_one(self):
        """Test multiplying by one."""
        assert multiply(1, 5) == 5
        assert multiply(5, 1) == 5

    @given(st.integers(), st.integers())
    def test_multiply_commutative(self, a: int, b: int):
        """Test that multiplication is commutative."""
        assert multiply(a, b) == multiply(b, a)

    @given(st.integers(), st.integers(), st.integers())
    def test_multiply_associative(self, a: int, b: int, c: int):
        """Test that multiplication is associative."""
        assert multiply(multiply(a, b), c) == multiply(a, multiply(b, c))

    @given(st.integers(), st.integers(), st.integers())
    def test_multiply_distributive(self, a: int, b: int, c: int):
        """Test distributive property."""
        assert multiply(a, add(b, c)) == add(multiply(a, b), multiply(a, c))
