#include <string>
#include <iostream>
#include "HelloWorldPrinter.h"

std::string five = "five"; // Definition

/*
Why place this into an unnamed namespace?

Suppose you create this library, designed to print "Hello World" to the console.
It is now possible (if defined outside the namespace) for someone think to
themselves "This HelloWorldPrinter library does exactly what I want, except I want it
to print Hello Everyone, instead of Hello World." and apply a "hack" to change it.
This can be accomplished in there own .cpp like so,

extern std::string helloWorld;
helloWorld = "Hello Everyone"

"extern" tells the compiler that the variable it is pointing to will be found during linking.
This means that inside "Source.cpp" writing "extern std::string helloWorld;" translates to 
"during linking time, find me helloWorld and point me to it". However in this case,
helloWorld will be found here, and overwritten. Later this allows for the developer
to call print_hello_world and change it to print to the value they desire. Of course this
example is small, but this has happened in larger projects with more problematic data
where the developer has visibility of the source code, but not the ability to change it.
*/
namespace
{
    std::string helloWorld = "Hello World";
}


void print_hello_world()
{
    std::cout << helloWorld << "\n";
}
