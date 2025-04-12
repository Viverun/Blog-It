import re


def validate_phone(phone):
    pattern = re.compile(r'^(\+91[\s-]?)?[6789]\d{9}$')
    return bool(pattern.match(phone))


def validate_email(email):
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(pattern.match(email))


phone = input("Enter your phone number: ")
email = input("Enter your email ID: ")

if validate_phone(phone):
    print("Valid phone number")
else:
    print("Invalid phone number")

if validate_email(email):
    print("Valid email ID")
else:
    print("Invalid email ID")
