import time

# List of dates in various formats
dates = ['2024-02-28', '02-28-2024', '28-02-2024', '123-02-2024']

def fix_date(date):
	"""
	Tries to correct the date format to a standard format.

	Parameters:
		date (str): The date string that needs to be converted.

	Returns:
		datetime object if conversion is successful, None otherwise.
	"""
	try:
		# Try to convert using the format YYYY-MM-DD
		return time.strptime(date, '%Y-%m-%d')
	except TypeError:
		print("Invalid argument type.")
	except ValueError:
		try:
			# If the above fails, try DD-MM-YYYY
			return time.strptime(date, '%d-%m-%Y')
		except ValueError:
			try:
				# If the above fails, try MM-DD-YYYY
				return time.strptime(date, '%m-%d-%Y')
			except ValueError:
				print(f'{date} is an invalid date format')

if __name__ == '__main__':
	for value in dates:
		date_obj = fix_date(value)
		print(time.strftime("%Y-%m-%d", date_obj)) if date_obj else 'Invalid date format'