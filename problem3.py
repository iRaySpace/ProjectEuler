def largest_prime_factor(number):

	i = 1
	product = 1

	while number != product:

		i = i + 1

		if number % i == 0:
			product = product * i

	return i