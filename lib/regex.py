import re

# Matches names with capitalized first letters, hyphens, or apostrophes
name_regex = re.compile(r"^[A-Z][a-zA-Z']+([ -][A-Z][a-zA-Z']+)*$")

# Matches phone numbers in different formats
phone_regex = re.compile(r"^(\(\d{3}\) |\d{3}-?)\d{3}-?\d{4}$")

# Matches valid email addresses
email_regex = re.compile(r"^[a-zA-Z][a-zA-Z0-9.]*@[a-zA-Z]+\.[a-zA-Z]{2,}$")
