import re
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def check_password_strength(password):
    errors = {
        "Less than 8 characters": len(password) < 8,
        "Missing lowercase letters": re.search(r"[a-z]", password) is None,
        "Missing uppercase letters": re.search(r"[A-Z]", password) is None,
        "Missing digits": re.search(r"\d", password) is None,
        "Missing symbols (!@#$%^&* etc)": re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None
    }

    score = 5 - sum(errors.values())

    if score <= 2:
        strength = "Weak"
    elif score in [3, 4]:
        strength = "Medium"
    else:
        strength = "Strong"

    # Return list of suggestions
    suggestions = [msg for msg, is_error in errors.items() if is_error]

    return strength, score, suggestions

def is_common_password(password, wordlist_path="rockyou.txt"):
    if not os.path.exists(wordlist_path):
        print(Fore.YELLOW + "rockyou.txt file not found.")
        return False

    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                if line.strip() == password:
                    return True
        return False
    except Exception as e:
        print(Fore.RED + f"Failed to open wordlist file: {e}")
        return False

if __name__ == "__main__":
    print(Fore.CYAN + Style.BRIGHT + "="*40)
    print(Fore.CYAN + Style.BRIGHT + "PASSWORD STRENGTH CHECKER".center(40))
    print(Fore.CYAN + Style.BRIGHT + "="*40)

    pw = input(Fore.WHITE + "Enter a password to check: ")

    strength, score, suggestions = check_password_strength(pw)
    print()
    print(Fore.MAGENTA + f"Complexity score: {score}/5")
    print(Fore.MAGENTA + f"Password strength: {strength}")

    if suggestions:
        print(Fore.YELLOW + "\n Suggestions for improvement:")
        for item in suggestions:
            print(Fore.YELLOW + f"- {item}")
    else:
        print(Fore.GREEN + "\nPassword meets all criteria!")

    print()
    if is_common_password(pw):
        print(Fore.RED + "This password is found in the common password list (rockyou.txt)!")
    else:
        print(Fore.GREEN + "Password is not found in the common password list.")

    print(Fore.CYAN + Style.BRIGHT + "="*40)
