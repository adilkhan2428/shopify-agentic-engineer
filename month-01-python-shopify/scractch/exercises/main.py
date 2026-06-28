# main.py

from utils import validate_email

print(validate_email("adil@test.com"))   # should print True
print(validate_email("not-an-email"))    # should print False