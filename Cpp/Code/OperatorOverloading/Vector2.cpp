#include "Vector2.h"

#include <iostream>

Vector2 Vector2::operator+(const Vector2& other) {
    /* 
    On function return, a copy of the object is returned,
    not the object inside this function call. This is
    to prevent it from being cleaned from the Stack.

    i.e. 
    
    Vector2 t = Vector2(this->u + other.u, this->v + other.v);
    std::cout << &t << "\n";

    &t will not be equal to the object memory address when
    returned from Vector2(a, b) + Vector2(c, d).
    */
    return Vector2(this->u + other.u, this->v + other.v);
}
