def fibo(limit, sumE = 0, fc = 1, fp = 1):
	
	if limit < fc:
		return sumE

	if fc % 2 == 0:
		sumE += fc

	return fibo(limit, sumE, fc + fp, fp = fc)
