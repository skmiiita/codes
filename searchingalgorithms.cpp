#include<iostream>
#include <algorithm> 
using namespace std;
long binarysearchrec(long arr[], long low,long high, long x){
	if (high>=low){
	long mid = low + (high-low)/2;
	if (arr[mid] == x) {
		return mid;
	}
	else if (arr[mid] > x) {
		return binarysearchrec(arr,low,mid-1,x);
	}
	else if (arr[mid] < x){
		return binarysearchrec(arr,mid+1,high,x);
	}
	}
	return -1;
}

long binarysearchiterative(long arr[],long low, long high, long x) {
	while (low<=high){
		long mid = low + (high-low)/2;
        	if (arr[mid] == x) {
                	return mid;
        	}
        	else if (arr[mid] > x) {
			high = mid-1;
		}
		else {
			low = mid+1;
		}
	}
	return -1;
}


int main() {
//	int arr[] = {1,2,3,4,5};
	signed long size = 10000000;
	signed long *arr = new signed long[size];
        for (signed long i = 0;i<size;i++) {
                arr[i] = i+1;
        }
	for (signed long i = 0;i<size;i++) {
                signed long r1,r2;
                r1 = rand()%(size);
                r2 = rand()%(size);
                swap(arr[r1],arr[r2]);
        }
	sort(arr,arr+size);
	cout<< binarysearchiterative(arr,0,size,10000000)<<endl;
}

