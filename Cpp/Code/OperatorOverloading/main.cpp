#include "Vector2.h"

#include <iostream>

/*

Overloaded binary operator calls are looked up as member functions of the first operand,
and also as free functions on both operands

It is not possible for us the edit the ostream class and implement
our own, "operator<<(Vector2& other)" because the class already exists
and we do not get to modify classes in the std namespace. This is where
the usage of operator<< global functions are utilized.

The ostream does not have operator<< for user-defined classes,
it only supports a certain amount found at https://en.cppreference.com/w/cpp/io/basic_ostream/operator_ltlt

We utilize operator<< as a global function as a means of gathering the
two objects we want, but will then grab the properties we want
to print from our object and pass then to the passed ostream object
and utilizing the operator<< on the class, for the types that it supports.
This is why we use pass by reference, so that it passes the actual
object instead of a copy.

When we write a function "std::ostream& operator<<(std::ostream& stream, const Type&other) { ... }"
we can interpret as "When we see a `ostream << Type` in the code base, call this function and
pass the two objects by reference". When inside, in our example below we have `stream << other.u`,
this is now interpreted as "Check if the Type of `stream` (first operand) has a method for operator<<
that supports the Type of `other.u` then call it, otherwise check for a global function".

*/
std::ostream& operator<<(std::ostream& stream, const Vector2& other) {
    // This is calling, "basic_ostream& operator<<(int value);"
    stream << other.u << ", " << other.v << "\n";

    //It is possible to have a StackOverflow by calling "stream << other" inside of the global function because
    //it will keep calling this each time, passing both objects as parameters.

    // stream << other; -- StackOverflow
    return stream;
}

int main() {
    // Search for `ostream << Vector2` type definition, which can either be on the `ostream` class method, or in this
    // example it is defined above as a global function.
    std::cout << Vector2(10, 20);

    // Also, note that operator<< "is" a function, it can also be called as
    operator<<(std::cout, Vector2(100, 200));

    Vector2 v = Vector2(15, 15) + Vector2(35, 35);
    return 0;
}
