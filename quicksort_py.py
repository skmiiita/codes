import array
def partition(arr,start,end) :
	i = start -1
	pivot = arr[end]
	for j in range(0,end+1):
		if arr[j] < pivot:
			i = i + 1
			arr[j],arr[i] = arr[i],arr[j]
		
	arr[i+1],arr[end] = arr[end],arr[i+1]
	print arr
	return i+1

def quicksort(arr,start,end):
	try:
		if start < end:
			pivot  = partition(arr,start,end)
			print pivot
			quicksort(arr,start,pivot-1)
			quicksort(arr,pivot+1,end)
	except IndexError:
		pass


if __name__=="__main__":
	arr = array.array('i',[5,2,9,1,6,7])
	print arr
	print partition(arr,0,5)
	quicksort(arr,0,5)
	print arr
