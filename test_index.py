import unittest
from index import validate_credit_card, luhn_algorithm

class TestCreditCardValidation(unittest.TestCase):

    def test_luhn_algorithm_valid(self):
        # Valid card numbers
        self.assertTrue(luhn_algorithm("4532015112830366"))  # Visa
        self.assertTrue(luhn_algorithm("6011111111111117"))  # Discover
        self.assertTrue(luhn_algorithm("378282246310005"))   # American Express

    def test_luhn_algorithm_invalid(self):
        # Invalid card numbers
        self.assertFalse(luhn_algorithm("4532015112830367"))  # Invalid Visa
        self.assertFalse(luhn_algorithm("6011111111111118"))  # Invalid Discover
        self.assertFalse(luhn_algorithm("378282246310006"))   # Invalid American Express

    def test_validate_credit_card_visa(self):
        self.assertEqual(validate_credit_card("4532015112830366"), "Visa")

    def test_validate_credit_card_mastercard(self):
        self.assertEqual(validate_credit_card("5555555555554444"), "MasterCard")

    def test_validate_credit_card_american_express(self):
        self.assertEqual(validate_credit_card("378282246310005"), "American Express")

    def test_validate_credit_card_discover(self):
        self.assertEqual(validate_credit_card("6011111111111117"), "Discover")

    def test_validate_credit_card_hipercard(self):
        self.assertEqual(validate_credit_card("6062825624254001"), "Hipercard")

    def test_validate_credit_card_invalid(self):
        self.assertEqual(validate_credit_card("1234567890123456"), "Invalid card number")
        self.assertEqual(validate_credit_card(""), "Invalid card number")
        self.assertEqual(validate_credit_card("abcd1234"), "Invalid card number")

if __name__ == "__main__":
    unittest.main()   