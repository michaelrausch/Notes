#pragma once

#include<stdlib.h>
#include <iostream>

class Node {
    public:
        int value;
        Node* next;
        Node(int v, Node* n = nullptr) : value(v), next(n) {};
};
