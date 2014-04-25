def is_palindrome(num):
	return str(num) == str(num)[::-1]

def largest_palindrome(digits):

	z = 0

	digits = 10 ** digits

	for x in xrange(digits, digits / 10, -1):

		for y in xrange(digits, digits / 10, -1):

			if is_palindrome(x * y):

				if z < x * y:
					z = x * y

	return z