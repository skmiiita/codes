def fib(n):
	mem = {0:0,1:1}
	if n not in mem:
		mem[n] = fib(n-1) + fib(n-2)
		print mem[n]
	return mem[n]

def fibi(n):
	mem = {0:0,1:1}
	for index in range(2,n+1):
		#print index
		if index not in mem:
			mem[index] = mem[index-1] + mem[index-2]
	#print mem
	return mem[n] 
if __name__ == "__main__":
	print fib(10)
