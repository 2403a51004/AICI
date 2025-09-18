def is_valid_credit_card(card_number: str) -> bool:
    """Check if the string is a 16-digit numeric credit card number."""
    return card_number.isdigit() and len(card_number) == 16

def mask_credit_card(card_number: str) -> str:
    """Return masked credit card number, showing only last 4 digits."""
    if not is_valid_credit_card(card_number):
        return "Invalid credit card number"
    return '*' * 12 + card_number[-4:]

# Example usage
card = input("Enter your 16-digit credit card number: ")
if is_valid_credit_card(card):
    print("Valid credit card number.")
    print("Masked:", mask_credit_card(card))
else:
    print("Invalid credit card number.")