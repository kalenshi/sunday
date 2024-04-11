import re
from rest_framework.exceptions import ValidationError


def validate_email(email):
	"""
	Validates that the given string is a valid email address
	Args:
		email(str): A valid email address:

	Returns:
		bool: True if the passed string is valid, False otherwise
	Raises:
		ValueError: If the passed string is not  a valid email address
	"""
	# Regular expression pattern for basic email validation
	pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

	# Use re.match to check if the email matches the pattern
	if re.match(pattern, email):
		return True
	else:
		return False


def validate_boolean(value):
	"""
	Validates that the given value is either true or false
	Args:
		value(bool): the value to be evaluated

	Returns:
		bool : True if the given value is either true or false

	Raises
		ValidationError: when the passed item is not of specified type
	"""
	if value in (0, 1):
		return True
	raise ValidationError(f"{value} is not a valid boolean value")
