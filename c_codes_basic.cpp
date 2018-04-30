#include <iostream>
#include <cstdio>
using namespace std;

long fib(int n) {
	long mem[n+1] = {0,1};
	if (mem[n]==0){
		mem[n] = fib(n-1) + fib(n-2);
	}
	return mem[n];
}

int main() {
	cout<< fib(10)<<endl;
}	
