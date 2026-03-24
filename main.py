from mean_var_std import calculate
import unittest
import test_module

# Quick functional test
print("=" * 60)
print("TEST 1: calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])")
print("=" * 60)
result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
for key, value in result.items():
    print(f"{key}: {value}")

print()
print("=" * 60)
print("TEST 2: ValueError test (less than 9 elements)")
print("=" * 60)
try:
    calculate([1, 2, 3])
except ValueError as e:
    print(f"ValueError caught: {e}")

print()
print("=" * 60)
print("RUNNING UNIT TESTS")
print("=" * 60)
unittest.main(module=test_module, argv=[''], verbosity=2, exit=False)
