#pragma once

class Vector2
{
    public:
        int u, v;

    Vector2(int u, int v): u(u), v(v){ };
    /*
    We can add our own operator+ when we have access to the
    classes easily, however when interfacing with libraries
    or external classes a global function is easier and
    ideal. 

    Interpret this as "This Class Type" (Left Operand) + "Parameter Type" (Right Operand), 
    i.e. Vector2 + Vector2 in this example
    */
    Vector2 operator+(const Vector2& other);
};

