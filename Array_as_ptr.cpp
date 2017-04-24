#include <cstdlib>
#include <stdio.h>

using namespace std;

// here we want to become framiliar with pointers as arrays, and their


int main(){
  int *array = new int[100000000] // this creates a just a pointer called array
                                 // all of the space allocated here is put on the stack
  //notice that all we have pointing to this memory is a POINTER!
  // so we must access it like it is a pointer to an array
}
