// Project Euler #7


#include <iostream>
#include <cmath>

using namespace std;


bool isprime(long number)
{
	for(long i = 2; i < sqrt(number) + 1; i++)
	{
		if(number%i == 0)
		{
			return false;
		}
	}
	return true;
}


int main()
{
	long primefound = 0;
	long lastprime = 0;
	for(long j = 2; primefound < 10000; j++)
	{
		if(isprime(j))
		{
			lastprime = j;
			primefound++;
			cout << primefound +1 <<"th prime is " << lastprime << endl;
		}
	}
	cout << lastprime << " is the " << primefound +1 << "th prime" << endl;
}
