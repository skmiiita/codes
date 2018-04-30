#include <iostream>
#include <cstdio> 
#include <cstdlib>
using namespace std;
 
void quick_sort(long[],long,long);
int partition(long[],long,long);
int findPivot(int[],int, int); 
 
void quick_sort(long a[],long l,long u)
{
//    int j;
    if(l<u)
    {
       int  j=partition(a,l,u);
        quick_sort(a,l,j-1);
	        quick_sort(a,j+1,u);
    }
}
void swap(long &a, long &b){
        int temp = b;
        b = a;
        a = temp;
}

int findPivot(int arr[],int start, int end){
        int pivot = arr[end];
        int i = start;
        int j = 0,k=0;
        for (;j<=end;j++){
                if (arr[j] <= pivot){
                        
                        swap(arr[i],arr[j]);
			i++;
                }
        }

        swap(arr[i+1],arr[end]);

        return  i;

}
//{5,2,8,1,9,6}
 
int partition(long a[],long l,long u)
{
    int v,i,j,temp;
    v=a[l];
    i=l;
    j=u+1;
    
    do
    {
        do
            i++;
            
        while(a[i]<v&&i<=u);
        
        do
            j--;
        while(v<a[j]);
        
        if(i<j)
        {
            temp=a[i];
            a[i]=a[j];
            a[j]=temp;
        }
    }while(i<j);
    
    a[l]=a[j];
    a[j]=v;
    
    return(j);
}

int main()
{
//        signed long size = 429496729;
	signed long size = 10000000;
	signed long *arr = new signed long[size];
//	cout<<"m"<<endl;
//        long arr[size];
        for (signed long i = 0;i<size;i++) {
                arr[i] = i+1;
        }

        for (signed long i = 0;i<size;i++) {
                signed long r1,r2;
                r1 = rand()%(size);
                r2 = rand()%(size);
                swap(arr[r1],arr[r2]);
        }

   //     for (int i=0;i<size;i++) {
     //           cout<<arr[i]<<endl;
      //  }
 //       long n = sizeof(arr)/sizeof(arr[0]);

//	cout << n <<endl;
	
    quick_sort(arr,0,size);
    for (signed long i = 0;i<size;i++) {
                printf("%lu ",arr[i]);
    }
    cout << endl;

    return 0;
}

