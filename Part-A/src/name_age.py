"""Prompts the user for their name and age and displays their birth year.

Input:
    name (str) entered by the user from the keyboard.
    age (int) entered by the user from the keyboard.

Process:
    Calculate the user's approximate birth year by subtracting age from
    the current year.

Output:
    Displays a greeting with the user's name and birth year on screen.

Typical usage example:
    What is your name? Alex
    How old are you? 24
    Hello Alex! You were born in 2002.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    name = input("What is your name? ")
    age = int(input("How old are you? "))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
    print(f"Hello {name}! You were born in {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# Python Software Foundation. (n.d.). datetime module.
# https://docs.python.org/3/library/datetime.html
