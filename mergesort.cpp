#include <iostream>
#include<cstdlib>
#include<cstdio>
using namespace std;
#define SENTINEL 2147483647

void merge(long int arr[],long int start, long int mid, long int end ) {
	long int n1 = mid-start+1;
	long int n2 = end-mid;
	signed long *L = new signed long[n1+1];
	signed long *R = new signed long[n2+1];
	// int L[n1+1],R[n2+1];
	L[n1] = SENTINEL;
	R[n2] = SENTINEL;
	long int i,j,k;

	for (i = 0; i < n1; i++)
        	L[i] = arr[start + i];
    	for (j = 0; j < n2; j++)
        	R[j] = arr[mid+ 1+ j];

	
	i=0,j=0,k=start;
	
	for (;k<=end;k++) {
		if (L[i] <= R[j]) {
			arr[k] = L[i];
			i++;
		}
		else if (R[j] < L[i]) { 
			arr[k] = R[j];
			j++;
		}
	}
	delete L;
	delete R;

}

/*
void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 =  r - m;
 
 
    int L[n1+1], R[n2+1];
    L[n1] = SENTINEL;
    L[n2] = SENTINEL;
	
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1+ j];
 
    i = 0; // Initial index of first subarray
    j = 0; // Initial index of second subarray
    k = l; // Initial index of merged subarray
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
 
}
*/

void printarray(int arr[],int n) {
	for (int i = 0;i<n;i++){
		cout<< arr[i]<< " ";
	}
	cout<<endl;
}

void mergesort(long int arr[], long int s, long int e) { 
	if (s <  e) { 
		long int mid = s + (e-s)/2;
		mergesort(arr,s,mid);
		mergesort(arr,mid+1,e);
		merge(arr,s,mid,e);
	}
}

int main() {
//	signed long size = 429496729;
	long size = 10000000;
	signed long *arr = new signed long[size];
        for (signed long i = 0;i<size;i++) {
                arr[i] = i+1;
        }
	cout<< "m" <<endl;
        for (signed long i = 0;i<size;i++) {
                signed long r1,r2;
                r1 = rand()%(size);
                r2 = rand()%(size);
                swap(arr[r1],arr[r2]);
        }
	cout<<"m"<<endl;
   //     for (int i=0;i<size;i++) {
     //           cout<<arr[i]<<endl;
      //  }
 //       long n = sizeof(arr)/sizeof(arr[0]);

//	cout << n <<endl;
	
    mergesort(arr,0,size);
    for (signed long i = 0;i<size;i++) {
                printf("%lu ",arr[i]);
    }
    cout << endl;
    delete arr;	
    return 0;
}	
