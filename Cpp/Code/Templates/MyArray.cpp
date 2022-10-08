#include "MyArray.h"

#include <iostream>
#include <stdexcept>

/**
   Capable of a resizing array that initializes newly added indexes to Zero.

   Supports Pythonic style negative number indexing, i.e. -1 is end of the array
  */
template<class T>
class DynamicArray
{
    T* v;
    int size;

public:

    DynamicArray(int initial_size)
    {
        this->size = initial_size;
        v = new T[initial_size];
        for (int i = 0; i < this->size; i++) {
            v[i] = 0;
        };
    };

    void setSize(int new_size)
    {
        if (new_size < 0) {
            throw std::invalid_argument("Cannot create a list with negative size.");
        };

        if (new_size < this->size) {
            T* temp_v = new T[new_size];
            for (int i = 0; i < new_size; i++) {
                temp_v[i] = this->v[i];
            };
            free(this->v);
            this->v = temp_v;
        }
        else {
            int extended_size = new_size - this->size;
            T* temp_v = new T[this->size + extended_size];

            for (int i = 0; i < this->size; i++) {
                temp_v[i] = this->v[i];
            };

            for (int i = this->size; i < this->size + extended_size; i++) {
                temp_v[i] = 0;
            };
            free(this->v);
            this->v = temp_v;
        }
        this->size = new_size;
    }

    void displayArrayValues() {
        for (int i = 0; i < this->size; i++) {
            std::cout << this->v[i] << " ";
        };
        std::cout << "\n";
    };

    /**
       Subscript overload to allow for better syntax to change array values, e.g. myArray[i] or myArray[i] = x
     */
    T& operator[] (const int i) {
        if (i >= this->size || i < -this->size) {
            throw std::invalid_argument("Out of range indexing");
        };

        if (i < 0) {
            return this->v[this->size + i];
        }

        return this->v[i]; // Returns a reference to the i'th element
    }
};

int main() {
    DynamicArray<int> dynamicArray = DynamicArray<int>(10);
    dynamicArray.displayArrayValues();
    dynamicArray.setSize(15);
    dynamicArray.displayArrayValues();

    dynamicArray[9] = 100;
    std::cout << dynamicArray[9] << "\n";
    std::cout << dynamicArray[-1] << "\n";
    dynamicArray.displayArrayValues();
}