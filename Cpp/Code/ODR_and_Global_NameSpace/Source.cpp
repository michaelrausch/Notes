#include <iostream>
#include "HelloWorldPrinter.h"
/*
Illustration of the One Defintion Rule of C++

Uncomment the method below "print_hello_world" to receive a linking error for an already
defined function.

Explanation:

Compilation is performed on each and every translation unit, typically a .cpp file and the header files it includes.
The Compiler takes one translation unit at a time and reads it to produce an internal list of classes and their members.
It then produces assembly code of each function in the given unit. If the function call is not inlined (e.g. it is defined
in another translation unit), the compiler produces a "link" - i.e. "please insert function C here" for the linker to read.

The linker takes all of the compiled translation units and merges them into one binary, substituting al the links specified
in the compiler.

Therefore, the ODR is there to protect programmers from themselves. If they were to accidentally define a function twice,
the linker will notice that and the executeable will not be produced. This is also true for variables, but not classes.
Class definitions are required in every translation unit and therefore the ODR does not apply.
*/


//void print_hello_world()
//{
//    std::cout << five << "\n";
//}


/*
uncomment to use a hack to change the variable inside HelloWorldPrinter.cpp when outside an unnamed namespace.
*/
//extern std::string helloWorld;


/*

This line will result in a compilation error, why?

The .h file already contains "extern std::string five". During preprocessing stage when the content
is dumped from the .h file into here, by writing "std::string five" we are redeclaring the variable
"five" again, causing a compilation error.

std::string five;
*/

int main() {
    std::cout << five << "\n";
    //helloWorld = "Hello Everyone";
    print_hello_world();
    return 0;
}