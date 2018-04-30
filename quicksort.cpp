#include <iostream>
#include <time.h>
#include <stdio.h>
#include <execinfo.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>

using namespace std;
void swap(int &a, int &b){
	int temp = b;
	b = a;
	a = temp;
}

void handler(int sig) {
  void *array[10];
  size_t size;

  // get void*'s for all entries on the stack
  size = backtrace(array, 10);

  // print out all the frames to stderr
  fprintf(stderr, "Error: signal %d:\n", sig);
  backtrace_symbols_fd(array, size, STDERR_FILENO);
  exit(1);
}

int findPivot(int arr[],int start, int end){
	int pivot = arr[end];
	int i = start-1;
	int j = 0,k=0;
	for (;j<=end;j++){
		if (arr[j] <= pivot){
			i++;
			swap(arr[i],arr[j]);
		}
	}
	
	swap(arr[i+1],arr[end]);

	return  i+1;
			 
}
int quicksort(int *arr, int s, int e){
	if (s<e) {
		int pivot = findPivot(arr,s,e);
		cout<< s << " "<< e<<endl;
		quicksort(arr,s,pivot-1);
		cout<< "mm"<<endl;
		quicksort(arr,pivot+1,e);
	}
}
int main(){
	int arr[] = {5,2,8,1,9,6};
//	signal(SIGSEGV, handler); 
	quicksort(arr,0,5);
	int p = findPivot(arr,0,5);
	cout << p<<endl;
}

