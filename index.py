def luhn_algorithm(card_number):
    """
    Validates a credit card number using the Luhn algorithm.
    
    Args:
        card_number (str): The credit card number as a string.
    
    Returns:
        bool: True if the card number is valid, False otherwise.
    """
    total = 0
    reverse_digits = card_number[::-1]
    
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:  # Double every second digit
            n *= 2
            if n > 9:  # If the result is greater than 9, subtract 9
                n -= 9
        total += n
    
    return total % 10 == 0


def validate_credit_card(card_number):
    """
    Validates a credit card number and determines its bandeira (brand).
    
    Args:
        card_number (str): The credit card number as a string.
    
    Returns:
        str: The bandeira of the card if valid, otherwise "Invalid card number".
    """
    card_number = card_number.strip()
    
    # Validate the card number using the Luhn algorithm
    if not card_number.isdigit() or not luhn_algorithm(card_number):
        return "Invalid card number"
    
    # Determine the bandeira (brand)
    if card_number.startswith('4'):
        return "Visa"
    elif card_number[:2] in ['51', '52', '53', '54', '55'] or 2221 <= int(card_number[:4]) <= 2720:
        return "MasterCard"
    elif card_number[:4] in ['4011', '4312', '4389'] or card_number[:6] in ['401178', '401179']:  # Add more Elo ranges as needed
        return "Elo"
    elif card_number[:2] in ['34', '37']:
        return "American Express"
    elif card_number[:2] in ['30']:
        return "Diners Club"
    elif card_number[:2] in ['35']:
        return "JCB"
    elif card_number[:2] in ['50']:
        return "Aura"
    elif card_number.startswith('6011') or card_number[:2] == '65' or 644 <= int(card_number[:3]) <= 649:
        return "Discover"
    elif card_number.startswith('6062'):
        return "Hipercard"
    elif card_number.startswith('2014'):
        return "En Route"
    elif card_number.startswith('8699'):
        return "Voyager"
    else:
        return "Invalid card number"

# Example usage
card_number = "869939467601927"
print(validate_credit_card(card_number))  # Output: Voyager (if valid)