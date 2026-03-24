import unittest
from mean_var_std import calculate


class UnitTests(unittest.TestCase):

    def test_calculate(self):
        actual = calculate([2, 6, 2, 8, 4, 0, 1, 5, 7])
        expected = {
            'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.888888888888889],
            'variance': [[9.555555555555557, 0.6666666666666666, 8.666666666666666], [3.555555555555556, 10.666666666666666, 6.222222222222221], 6.987654320987654],
            'standard deviation': [[3.091206165165235, 0.816496580927726, 2.943920288775949], [1.8856180831641267, 3.265986323710904, 2.494438257849294], 2.6434171674156266],
            'max': [[8, 6, 7], [6, 8, 7], 8],
            'min': [[1, 4, 0], [2, 0, 1], 0],
            'sum': [[11, 15, 9], [10, 12, 13], 35]
        }
        self.assertAlmostEqual(actual['mean'][2], expected['mean'][2], places=5)
        self.assertEqual(actual['mean'][0], expected['mean'][0])
        self.assertEqual(actual['mean'][1], expected['mean'][1])
        self.assertEqual(actual['max'], expected['max'])
        self.assertEqual(actual['min'], expected['min'])
        self.assertEqual(actual['sum'], expected['sum'])

    def test_calculate2(self):
        actual = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
        expected = {
            'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[9, 12, 15], [3, 12, 21], 36]
        }
        self.assertEqual(actual, expected)

    def test_calculate_error(self):
        self.assertRaisesRegex(ValueError, "List must contain nine numbers.", calculate, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
