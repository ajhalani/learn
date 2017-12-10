#include <iostream>
#include <exception>

using namespace std;

enum class Color {
  BLACK,
  RED,
};

int add(int x, int y){
  return x+y;
}

static long callcount=0;
long fib(int pos) {
	++callcount;
	if(0 == pos)
		return 0;
	else if(1 == pos)
		return 1;
	else if(2 <= pos)
		return fib(pos-1) + fib(pos-2);
	else
		throw std::logic_error("invalid position fib");
}

long fib2(int pos) {
	++callcount;
	if(0 == pos)
		return 0;
	else if(1 == pos)
		return 1;
	long sum_2_before=0;
	long sum_1_before=1;
	long sum=0;	
	for(int i=2; i <= pos; ++i) {
		sum = sum_1_before + sum_2_before;
		sum_2_before = sum_1_before;
		sum_1_before = sum;
	}
	return sum;
}

int main() {
	int i1 = 10;
  i1 = i1/2.7;

	cout << "calculated fib - " << fib2(42) << endl;
	cout << "call count - " << callcount << endl;
  return 0;
}

