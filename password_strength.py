import re

def check_password_strength(password: str) -> str:
    # Check length
    length = len(password)
    if length < 8:
        strength = "Weak"
        reason = "Password should be at least 8 characters long."
    elif length >= 8:
        strength = "Moderate"
        reason = "Password length is sufficient."

    # Check for uppercase, lowercase, digits, and special characters
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'[0-9]', password)
    has_special = re.search(r'[@$!%*?&]', password)
    
    # Improve strength based on these factors
    if has_upper and has_lower and has_digit and has_special:
        strength = "Strong"
        reason = "Password contains uppercase, lowercase, digits, and special characters."
    elif (has_upper or has_lower) and has_digit:
        strength = "Moderate"
        reason = "Password contains a mix of letters and digits, but missing special characters."
    elif has_upper or has_lower:
        strength = "Weak"
        reason = "Password should contain both upper and lowercase letters, digits, and special characters."
    elif not (has_upper or has_lower or has_digit or has_special):
        strength = "Very Weak"
        reason = "Password lacks complexity. It should include letters, digits, and special characters."
    
    # Check for common passwords
    common_passwords = ['123456', 'password', 'qwerty', 'abc123', 'letmein', 'welcome']
    if password.lower() in common_passwords:
        strength = "Very Weak"
        reason = "Password is too common and easily guessable."
    
    return f"Password Strength: {strength}\nReason: {reason}"

# Example usage
password = input("Enter your password: ")
print(check_password_strength(password))
