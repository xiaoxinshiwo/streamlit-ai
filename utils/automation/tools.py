def get_clean_val(param_value, extracted_key='title'):
	if extracted_key in param_value:
		return param_value.get(extracted_key)
	else:
		return param_value


def fibonacci(n):
	fib_sequence = [0, 1]
	while len(fib_sequence) < n:
		next_fib = fib_sequence[-1] + fib_sequence[-2]
		fib_sequence.append(next_fib)
	return fib_sequence[:n]

# 生成前 10 个斐波那契数
print(fibonacci(10))

if __name__ == '__main__':
	# 生成前 10 个斐波那契数
	print(fibonacci(10))
