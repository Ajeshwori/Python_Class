def is_palindrome(value):
    # Convert to string, remove spaces, make lowercase
    cleaned = str(value).replace(" ", "").lower()
    return cleaned == cleaned[::-1]
