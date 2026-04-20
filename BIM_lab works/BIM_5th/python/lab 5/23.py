class StringUtils:
    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]

    @staticmethod
    def to_uppercase(s):
        return s.upper()

    @staticmethod
    def reverse_string(s):
        return s[::-1]


text = "madam"

print("Palindrome:", StringUtils.is_palindrome(text))
print("Uppercase:", StringUtils.to_uppercase(text))
print("Reverse:", StringUtils.reverse_string(text))