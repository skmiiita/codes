#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// #define MAX 1000000
#define MAX	    9999999
vector<long> primes;
int numprimefactors(int n) {
	int i = 2;
	vector<int>v;
	for (i=2; i*i<=n;i++){
		if (n%i == 0) {
			v.push_back(i);
		}
	}
	for(int i; i < v.size();i++) {
        	cout << v[i] << endl;
	}

}

int findprimeseive(int max_limit){
	int i,j;
	int seive[max_limit] = {0};
	for(i =2; i * i <= max_limit; i++){
		for (j=i*2;j<=max_limit;j = j + i){
			if (j % i == 0 and seive[j] == 0){ 
				seive[j] = 1;
			}
		}
	}
	for (i = 0;i<=max_limit;i++) {
                if (seive[i] == 0 and i>=2) {
                        cout<<i<<endl;
                        primes.push_back(i);

                }
        }

}	
void primesinrange(int low,int high){
	if (primes.size() == 0){
		findprimeseive(high-low+1);
		return;
	}
	bool isprime[high-low+1] = {0};
	for (int j=0;j<primes.size();j++){
		 int div = low/primes[j];
                 int mul = div * primes[j];
		 mul = mul + primes[j];
		for(int index=low;index<=high;index++){
			cout<< index <<" "<< low<<" "<<high<<endl;
			if (primes[j] * primes[j] <= index ) {
				isprime[mul-low] = 1;
			}
			else {
				break;
			}
				 
			mul = mul + primes[j];
		}
		cout<<low<<endl;
	}
	cout<<"m"<<endl;
	for (int i = 0;i<=high-low;i++){
		if (isprime[i] == 0) {
			primes.push_back(i+low);
		}
	}
}
	
/*		
int segmentedseive(){
	segmentsize = MAX / int(sqrt(MAX));
	if (MAX % int(sqrt(MAX)) !=0) {
		segmentsize = segmentsize + 1;
	}

*/	
int main() {
	primesinrange(1,100);
	primesinrange(1,100);
	cout<<"--------------------------"<<endl;
	for (int i=0;i<primes.size();i++) {
		cout<< primes[i] <<endl;
	}
}
			

