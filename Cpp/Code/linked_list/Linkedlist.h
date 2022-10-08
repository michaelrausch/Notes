#pragma once
#include "Node.h"
#include <vector>

class Linkedlist {

    public:
        Node* root;
        int size;
        
        void insert_to_head(int value);
        void insert_to_head(Node * node);

        bool remove_nodes_with_value(int value);
        std::vector<int> iter_values();

        void print_linked_list();

        Linkedlist(Node* root=nullptr);
};

