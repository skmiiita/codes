#include <iostream>
#include <cstdlib>
using namespace std;

void insertionsort(int arr[], int n) {
	int i,j;
	for (i = 1;i<n;i++){
		int key = arr[i];
		j = i-1;
		while(j>=0 and key < arr[j] ) {
			arr[j+1] = arr[j];
			j--;
		}
		arr[j+1] = key;
	}
}
void swap(int &a,int &b) { 
	int temp = a;
	a = b;
	b = temp;
}
int main(){
	int arr[] = {1,2,4,2,4,4};
	int size = 100000;
	/*
	int arr[size];
	for (int i = 0;i<size;i++) { 
		arr[i] = i+1;
	}
	for (int i = 0;i<size;i++) { 
		int r1,r2;
                r1 = rand()%(size);
		r2 = rand()%(size);
		swap(arr[r1],arr[r2]);
	}
		
	for (int i=0;i<size;i++) { 
		cout<<arr[i]<<endl;
	}	
	*/
	int n = sizeof(arr)/sizeof(arr[0]);

	insertionsort(arr,n);
	for (int i=0;i<n;i++) { 
		cout<<arr[i] << " ";
	}

} 
	
