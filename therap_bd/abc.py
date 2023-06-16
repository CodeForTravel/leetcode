
def sortExcept(arr, k, n):
	arr[k], arr[-1] = arr[-1], arr[k]
	arr = sorted(arr, key = lambda i: (i is arr[-1], i))
	last = arr[-1]
	i = n - 1
	while i > k:
		arr[i] = arr[i - 1]
		i -= 1
	arr[k] = last
	return arr

if __name__ == '__main__':
	a = [10, 4, 11, 7, 6, 20]
	k = 2
	n = len(a)
	a = sortExcept(a, k, n)
	print(" ".join(list(map(str, a))))
	
