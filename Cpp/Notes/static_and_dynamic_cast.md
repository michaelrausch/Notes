# Static Cast and Dynamic Cast

From C++, four different types of casting were introduced.

1. `static_cast`
2. `dynamic_cast`
3. `const_case`
4. `reinterpret_cast`

This tutorial will focus primarily on `static_cast` and `dynamic_cast`.

In C++, it is preferred to use these types of casting over the C style casting as it helps describe the intent. Using the C still casting will, ineffect, try out these different types of casts in a particular order. For example, a typical C style casting could be,

```C++
#include <iostream>

int main() {
    float f = 3.14;
    int i = (int) f;
    std::cout << i << std::endl;
    return 0;
}
```


## `static_cast`

`static_cast` is a compile-time cast operator used for safe and well-defined type conversions between related types. It performs conversions that can be determined **at compile-time**, without requiring runtime type information.

`static_cast` can handle the following conversions,

1. Implicit conversions (e.g., `int` to `float`, `double` to `int`)
2. Upcasting within the class hierarchy (e.g., converting a derived class pointer/reference to a base class pointer/reference)
3. Downcasting within the class hierarchy, **but without any runtime type checking** (e.g., converting a base class pointer/reference to a derived class pointer/reference)

`static_cast` does not perform any runtime checks to ensure the validity of the conversion.

Here is a code example that shows how to use `static_cast`,

```C++
#include <iostream>

class Base {
public:
    void baseFunction() {
        std::cout << "Base function" << std::endl;
    }
};

class Derived : public Base {
public:
    void derivedFunction() {
        std::cout << "Derived function" << std::endl;
    }
};

int main() {
    // Upcasting using static_cast
    Derived derivedObj;
    Base* basePtr = static_cast<Base*>(&derivedObj);
    basePtr->baseFunction();  // Calls Base::baseFunction()

    // Downcasting using static_cast
    Base baseObj;
    Derived* derivedPtr = static_cast<Derived*>(&baseObj);
    derivedPtr->derivedFunction();  // Undefined behavior!

    return 0;
}
```

The `static_cast` from a base class object to a derived class pointer is not safe because the object being cast is not actually a derived class object. This violates the type system and can result in unpredictable consequences. To avoid undefined behavior and safely perform downcasting with runtime type checking, instead `dynamic_cast` should be used.

## `dynamic_cast`

`dynamic_cast` is a runtime cast operator used for safe type conversions involving polymorphic types and performing runtime type checking. It allows conversions **between pointers or references of related classes in the class hierarchy**.

`dynamic_cast` can handle conversions like,

1. Upcasting within the class hierarchy (e.g., converting a derived class pointer/reference to a base class pointer/reference).

2. Downcasting within the class hierarchy, with runtime type checking to ensure the validity of the conversion.

`dynamic_cast` requires the classes involved to have at least one virtual function. If the conversion is not valid, `dynamic_cast` returns a null pointer (for pointers) or throws a `std::bad_cast` exception (for references). It should be used when you need to perform runtime type checks and ensure the validity of the conversion, especially in cases where you are not certain about the exact types involved.

In this code example we demonstrate how upcasting is generally safe but downcasting is not guaranteed to be safe, but we utilize `dynamic_cast` to prevent exceptions from occurring by checking the pointer returned by `dynamic_cast`,

```C++
#include <iostream>

class Base {
public:
    virtual void baseFunction() {
        std::cout << "Base function" << std::endl;
    }
    virtual ~Base() {}
};

class Derived : public Base {
public:
    void derivedFunction() {
        std::cout << "Derived function" << std::endl;
    }
};

int main() {
    // Upcasting using dynamic_cast
    Derived derivedObj;
    Base* basePtr = dynamic_cast<Base*>(&derivedObj);
    basePtr->baseFunction();

    // Downcasting using dynamic_cast
    Base baseObj;
    Derived* derivedPtr = dynamic_cast<Derived*>(&baseObj);

    if (derivedPtr != nullptr) {
        derivedPtr->derivedFunction();
    } else {
        std::cout << "Dynamic cast failed." << std::endl;
    }
    return 0;
}
```