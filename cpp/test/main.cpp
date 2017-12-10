#include <iostream>
#include <constants.h>

using namespace std;

enum class Color {
  BLACK,
  RED,
};

auto add(int x, int y) -> int {
  return x+y;
}

int main() {
	int i1 = 10;
  i1 = i1/2.7;

  cout << "Hello World! " << i1 << ", " << add(5,3) << endl;
  return 0;
}

