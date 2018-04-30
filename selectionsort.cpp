#include <iostream>
using namespace std;
void swap(int &a,int &b){
	int temp = a;
	a = b;
	b = temp;
}

int min(int arr[],int s,int e){
	int m = arr[s];
	int mi = s;
	for (int i=s+1;i<=e;i++){
		if (arr[i] < m) {
			m = arr[i];
			mi = i;
		}
	}
	return mi;
}
void selectionsort(int arr[],int n) {
	int i=0,j=0;
	for (i = 0;i<n;i++){
		int m = min(arr,i,n-1);
		swap(arr[m],arr[j]);
		j++;
	}
}

int main() {
	int arr[] = {4,5,2,1,3};
	selectionsort(arr,5);
	for (int i = 0;i<5;i++){
		cout<< arr[i]<< " ";
	}
	cout << endl;
} 
	
