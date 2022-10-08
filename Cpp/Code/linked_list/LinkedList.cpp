#include <iostream>
#include <vector>

#include "Linkedlist.h"

namespace
{
    void _insert_to_head(Linkedlist* ll, Node* n) {
        if (ll->root) {
            n->next = ll->root;
            ll->root = n;
        } else {
            ll->root = n;
        }
        ll->size += 1;
    }
}


Linkedlist::Linkedlist(Node* root) {
    this->root = root;
    if (root) {
        this->size += 1;
    }
};

std::vector<int> Linkedlist::iter_values() {
    std::vector<int> values;
    Node* current_node = this->root;

    while (current_node) {
        values.push_back(current_node->value);
        current_node = current_node->next;
    }
    return values;
    
}

void Linkedlist::insert_to_head(int value) {
    /* 
    - Remember when using "new" to also "delete" it later on, preventing memory leaks.

    - Create the object using "new". Creating an object without new will create it on the stack,
      when leaving this function the object will then be destroyed. Hence, our linked list will
      be pointing to a now, deleted object.
    - The object that is returned from the function is not equal to the object created inside
      the function, a copy is created of the object that is returned. i.e. if I were to return
      `Node(value)` the memory address of the object inside the function will not be
      equal to the value returned that is assigned to the variable. This is because the object
      inside the function will be destroyed because it is on the local Stack.
    */
    Node * n = new Node(value);       
    _insert_to_head(this, n);
};

void Linkedlist::insert_to_head(Node * n) {
    _insert_to_head(this, n);
}

void Linkedlist::print_linked_list() {
   auto iter_values = this->iter_values();

    for (auto const& value : iter_values) { // https://stackoverflow.com/questions/60803776/what-does-auto-const-x-do-in-c
        std::cout << value << " --> ";
    }
    std::cout << "\n";
}

bool Linkedlist::remove_nodes_with_value(int value) {
    Node* previous_node = nullptr;
    Node* current_node = this->root;
    while (current_node) {
        if (current_node->value == value) {
            if (previous_node) {
                previous_node->next = current_node->next;
            } else { // Removing first item from list
                this->root = current_node->next;
            }
            auto to_delete = current_node;
            current_node = current_node->next;
            delete(to_delete); // Prevent memory leak
            this->size -= 1;
        } else {
            previous_node = current_node;
            current_node = current_node->next;
        }
    };
    return false;
}