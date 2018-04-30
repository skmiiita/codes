#include<iostream>
#include<cstdio>
using namespace std;

#define parent(i) i
#define leftchild(i) (i<<1)+1
#define rightchild(i) (i<<1)+2

void swap(int &a, int &b) {
	int temp = a;
	a = b;
	b  = temp;
}
void printarray(int arr[],int size){
        for (int index = 0;index<size;index++){
                cout<< arr[index]<< " ";
        }
        cout<<"........."<<endl;
}

void minHeapify(int arr[], int size,int i){

		int p = parent(i);
		int min;
		int left = leftchild(i);
		int right = rightchild(i);
//		cout << parent(i) << " "<< leftchild(i) << " "<< rightchild(i) <<endl;

		if (left < size and arr[left] < arr[i] ){
			min  = left;
		}
		else {
			min = i;
		}
		if (right < size and arr[right] < arr[min] ){
			min = right;
		}
//		cout<< "min : "<<min<<endl;		
		if (min != i){
			swap(arr[i],arr[min]);
			minHeapify(arr,size,min);
		}
}

void maxHeapify(int arr[],int size,int i){
	 	int p = parent(i);
                int max;
                int left = leftchild(i);
                int right = rightchild(i);
//                cout <<  leftchild(i) << " "<< rightchild(i) <<endl;

                if (left < size and arr[left] > arr[i] ){
                        max  = left;
                }
                else {
                        max = i;
                }
                if (right < size and arr[right] > arr[max] ){
                        max = right;
                }
//		cout << "max : " << max<<endl;
                if (max != i){
                        swap(arr[i],arr[max]);
                        maxHeapify(arr,size,max);
                }
}


void buildminheap(int arr[], int size){
	for (int i=0;i<=size/2;i++){
		minHeapify(arr,size,i);
	}
}
		

void buildmaxheap(int arr[],int size){
	 for (int i=size/2;i>=0;i--){
                maxHeapify(arr,size,i);
        }
	for (int i = size-1;i>=0;i--){
		swap(arr[i],arr[0]);
		maxHeapify(arr,i,0);
//		printarray(arr,size);
	}
}
/*
void printarray(int arr[],int size){
	for (int index = 0;index<size;index++){
		cout<< arr[index]<< " ";
	}
	cout<<"........."<<endl;
}
*/	 
void heapify(int arr[], int n, int i)
{
    int largest = i;  // Initialize largest as root
    int l = 2*i + 1;  // left = 2*i + 1
    int r = 2*i + 2;  // right = 2*i + 2
 
    // If left child is larger than root
    if (l < n && arr[l] > arr[largest])
        largest = l;
 
    // If right child is larger than largest so far
    if (r < n && arr[r] > arr[largest])
        largest = r;
 
    // If largest is not root
    if (largest != i)
    {
        swap(arr[i], arr[largest]);
 
        // Recursively heapify the affected sub-tree
        heapify(arr, n, largest);
    }
}
int main() {
	int i = 2;
//	cout << parent(i) << " "<< leftchild(i) << " "<< rightchild(i) <<endl;

	int arr[] = {3,6,1,9,10,2,5};
	int size = sizeof(arr)/sizeof(arr[0]);
//	maxHeapify(arr,size,0);
	printarray(arr,size);
//	maxHeapify(arr,size,0);
//	printarray(arr,size);	
//	buildminheap(arr,size);
//	printarray(arr,size);
	buildmaxheap(arr,size);
	printarray(arr,size);
	return 0;
}
