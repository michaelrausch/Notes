# C++ Classes

## Outside the Class Function Definitions

Member functions that are **declared** inside a class have to be **defined** seperately outside the class. Their definitions are very much like normal functions they should have a function header and a function body.

An important difference between a member function and a normal function is that a member function incorporates a membership identity label in the header. This 'label' tells the compiler which class the function belongs to. The general form of a member function definition is,

```C++
return-type class-name::function_name(argument declaration){
    function body
}
```

The membership label `class-name::` tells the compiler that the function `function-name` belongs to the class `class-name`. That is, the scope of the function is restricted to the `class-name` specified in the header line. The symbol `::` is called the **scope resolution operator**.

## Inside the Class Function Definitions

Another method of defining a member function is to replace the function declaration by the actual function definition inside the class, e.g.

```C++
class item 
{
    int number;
    float cost;

    public:
            void getdata(int a, float b); //declaration

            void putdata(void) // definition inside class
            {
                cout << number << "\n";
                cout << cost << "\n":
            }
}
```

When a function is defined inside a class, it is treated as an inline function. Therefore, all the restrictions and limitations that apply to an inline function are also applicable here. **Normally only small functions are defined inside the class definition**.

## Example Class

```C++
#include <iostream>

using namespace std;

class item
{
    int number; // Private by default
    float cost; //Private by default

public:
    void getdata(int a, in b): //Prototype declaration, to be defined.

    // Function defined inside class
    void putdata(void)
    {
        cout << "number :" << number << "\n";
        cout << "cost :" << cost << "\n";
    }

}

// ----------- Member Function Definition -----------

void item::getdata(int a, float b) // Use membership label
{
    number = a; // Private variables directly used
    cost = b;
}

// ----------- Main Program -----------
int main()
{
    item x; // Create object 'x'

    x.getdata(100, 299.95);
    x.putdata();

    item y;
    y.getdata(200, 175.50);
    y.putdata();
    return 0;
}
```

# Static Data Members

A data member of a class can be qualified as `static`. The properties of a static member variable are similar to that of a `C` static variable. A static member variable has certain special characteristics.

- It is initialized to zero when the first object of it's class is created. No other initialization is permitted.
- Only one copy of that member is created for the entire class and is **shared by all the objects of that class**, no matter how many objects are created.
- It is visible only within the class, but it's lifetime is the entire program.

Static variables are normally used to maintain values common to the entire class. For example, a static data member can be used as a counter that records the occurences of all of objects.

```C++
#include <iostream>

using namespace std;

class Item
{
    static int count;

    public:
            Item() {
                count++;
            }
            
            void getcount(void) {
                cout << "count: " << count << "\n";
            }
};

int Item::count; // <-- Note this line 

int main() {
    Item a;
    Item b;
    b.getcount(); // 2
    return 0;
}

```

**Note:** The following statement in the program; `int Item::count`.

The type and scope of each static member variable must be defined outside the class definition. This is necessary because the static data members are stored separetely rather than as part of an object. Since they are associated with the class itself, rather than with any class object, they are also known as class variable.

# Static Member Functions

Like static member variable, we can also have static member functions. A member function that is declared static has the following properties.

- A static function can have access to any other static members (function or variable) declared in the same class.
- A static member function can be called using the class name (instead of its objects) as follows:

```C++
class-name::function-name;
```

e.g.

```C++
class Test
{
    static int count;
    ...
    static void showcount(void);
    {
        cout << "count: " << count << "\n";
    }
}

Test::showcount();
```

# Static Functions

At namespace scope, `static` gives a name internal linkage, meaning that **it only accessible within the translation unit that contains the definition**. Without `static`, it has external linkage and it accessible in any translation unit.

So you use `static` (or, alternatively, an unnamed namespace) when writing a function that is intended for use within this unit. The internal linkage means that other units can define different functions within the same name without causing naming conflicts.

Non-static functions (and global names in general) are better declared in a header, to make sure that every translation unit that uses them gets the same declaration.

# Making Objects

```C++
#include <iostream>

using namespace std;

class Entity
{
    private:
            string my_name;
    public:
            // Zero parameter constructor
            // Entity(): my_name("Default") is the initialization member list
            // {} is the function body
            Entity(): my_name("Default"){}
            
            // const string & constructor
            // my_name(name) will set "my_name" to "name"
            Entity(const string& name): my_name(name){}
            
            // Function declaration
            const string & getName() const;
};

// Function definition
const string & Entity::getName() const {
    return my_name;
}

int main()
{
    // These 3 are on the stack, they will be automatically free
    // when leaving the function
    Entity a;
    cout << a.getName() << endl; // "Default"
    
    Entity b("b");
    cout << b.getName() << endl; // "b"
    
    Entity c = Entity("c");
    cout << c.getName() << endl; // "c"
    
    // Needs to be manually freed because it is on the heap, not the stack
    Entity* d = new Entity("d");
    cout << d->getName() << endl; // "d"
    delete d;
    return 0;
}

```

# Friendly Functions

We have been emphasizing throughout that private members cannot be accessed from outside the class. That is, a non-member function cannot have an access to the private data of a class. However, there could be a situation where two classes want to share a particular function that operates on both classes. In such situations, C++ allows the common function to be made *friendly* with both classes, thereby allowing the function to have **access to private data of these classes**. Such a function need not be a member of any of these classes.

To make an outside function "friendly" to a class, we have to simply declare this function as a "friend" of the class as shown,

```C++
class Example
{
    ...

    public:
            friend void xyz(void); // Declaration
}
```

The function declaration should be preceded by the keyword `friend`. The function is defined elsewhere in the program like a normal C++ function. The **function definition does not use either the keyword friend or the scope operator ::**. The functions that are declared with the keyword `friend` are known as friend functions. A friend function, although not a member function, **has full access rights to the private members of the class**.

A friend function posses certain special characteristics

- It is not in the scope of the class to which it has been declared as a friend
- Since it is not in the scope of the class, it cannot be called using the object of that class
- It can be called/invoked like a normal function without the help of any object
- Unlike member functions, it cannot access the member names directly and has to use an object name and a dot membership operator with each member name.
- It can be declared either in the public or the private part of a class without affecting its meaning.
- Usually, it has the objects as arguments.

```C++
#include <iostream>

using namespace std;

class Sample
{
    int a; // Private by default
    int b;
    
    public:
            void setValue(int a, int b);
            friend float mean(Sample s); // friend the function "mean"
};

void Sample::setValue(int a, int b)
{
    this->a = a;
    this->b = b;
}

float mean(Sample s)
{
    return float(s.a + s.b) / 2;
}

int main()
{
    Sample s;
    s.setValue(100, 200);
    cout << "Mean value = " << mean(s) << endl;
    return 0;
}
```

The friend function accesses the variable `a` and `b` which are **private members**.

# `const` Member Functions

If a member function **does not alter any data in the class**, then we may declare it as a `const` member function as follows.

```C++
void mul(int, int) const;
double get_balance() const;
```

The qualifier `const` is appended to the function prototypes (in both declaration and definition). The compiler will generate an error message if such functions try to alter the data values.

# `const` Objects

We may create and use constant objects, using `const` keyword before object declaration.

```C++
const Matrix m(m, n); // Object m is constant
```

Any attempt to modify the values of `m` and `n` will generate compile-time errors. Further a constant object can call only `const` member functions. As we know, a `const` member is a function prototype or function definition where the keyword `const` appears after the functions signature.

Whenever `const` objects try to invokve non-const member functions, the compiler generates errors.  

# Copy Constructor

The copy constructor is a constructor which **creates an object by initializing it with an object of the same class**, which has been created previously. The copy constructor is used to −

- Initialize one object from another of the same type.
- Copy an object to pass it as an argument to a function.
- Copy an object to return it from a function.

Here is a full example,

```C++
#include <iostream>

using namespace std;

class Point
{
    int x;
    int y;
    
    public:
        Point(int x, int y): x(x), y(y){}
    
        Point(Point & obj) 
        {
            cout << "Copy constructor called" << endl;
            // Create the new "Point" from double the previous x and y values
            x = obj.x * 2;
            y = obj.y * 2;
        }
        
        int getX() const
        {
            return x;
        }
        
        int getY() const
        {
            return y;
        }
};


void print_point(const Point & point){
    cout << "X: " << point.getX() << endl;
    cout << "Y: " << point.getY() << endl;
}

int main(void)
{
    Point p1(1, 2);   //normal constructor
    print_point(p1); // 1, 2
    
    Point p2 = p1;   // copy constructor
    print_point(p2); // 2, 4
    
    Point p3(p2);    // copy constructor
    print_point(p3); // 4, 8
}
```

# Destructors

A destructor is used to destroy the objects that have been created by a constructor. Like a constructor, the destructor is a member function whose name is the same as the class but is precedded by a tilde, e.g. the destructor for the class Point can be defined as,

```C++
~Point(){}
```

A destructor **never takes any arguments nor does it return any value**. It will be invoked implicitly by the compiler upon exit from the program (or block, function, as the case may be) to clean up storage that is no longer accessible. It is good practice to declare destructors in a program since it releases memory space for future use.

Whenever `new` is used to allocate memory in the constructors, we should use `delete` to free that memory.


Constructor and Destructor example

```C++
#include <iostream>

using namespace std;

class Matrix
{
    int d1;
    int d2;
    int** matrix;
    
    public:
            Matrix(int d1, int d2): d1(d1), d2(d2) {
                cout << "Creating a matrix of size " << d1 << " by " << d2 << endl;
                matrix = new int* [d1];
                for(int i=0; i < d1; i++){
                    matrix[i] = new int[d2];
                }
            }
            
            ~Matrix(){
                cout << "Destructor called" << endl;
                for(int i = 0; i < d1; i++){
                    delete matrix[i];
                }
                delete matrix;
            }
};

int main(void)
{
    Matrix m = Matrix(5, 10);
}
```

# Operator Overloading

To define an additional task to an operator, we must specify what it means in relation to the class to which the operator is applied. This is done with the help of a special function, called operator function, which describes the task. The general form of an operator function is,

```C++
return_type classname::operator op(args)
{
    function body
}
```

where `return_type` is the type of the value returned by the specified operation and `op` is the operator being overloaded. The `op` is preceded by the keyword `operator`. `operator op` is the function name.

Operator functions must be either member functions (non-static) or `friend` functions. For member functions, the object used to invoke the member function is passed implicitly and therefore available for the member function. This is not the case with `friend` functions, arguments may be passed either by value or by reference. Operator functions are declared in the class using prototypes, such as;

```C++
vector operator +(vector);   // vector addition
vector operato -();         // unary minus
friend vector operator +(vector, vector);
friend vector operator -(vector, vector);
vector operator -(vector &a) //subtraction
int operator ==(vector);     // comparison
friend int operator ==(vector, vector) // comparison
```

## Overloading Unary Operators

Unary operators are operators which are used to calculate the result on only one operand, examples include `-`, `+`, `++`, `--`, `!`, and `&`. An example usage is `-x`.

Let us consider the unary minus operator. A minus operator when used as a unary takes just one operand. We know that this operator changes the sign of an operand when applied to a basic data item. We will see here how to overload this operator so that it can be applied to an object in much the same way as is applied to an `int` or `float`. The unary minus when applied to an object should change the sign of each of it's data items.

```C++
#include <iostream>

using namespace std;

class Point
{
    int x;
    int y;
    int z;
    
    public:
            Point(int x, int y, int z): x(x), y(y), z(z){}
            
            void operator -(); // Overload unary minus
            
            void print()
            {
                cout << x << ", " << y << ", " << z << endl;
            }
};

void Point::operator -()
{
    x = -x;
    y = -y;
    z = -z;
}

int main()
{
    Point p(1, 2, 3);
    p.print();    // 1, 2, 3
    -p;           // Invokes operator -();
    p.print();    // -1, -2, -3
    return 0;
}
```

The function `operation -()` takes no arguments. It changes the sign of data members of the object `s`. Since this function is a member function of the same class, it can directly access the members of the object when activiated.

Remember a statement like,

```C++
s2 = -s1;
```
will **not work** because the function `operator -()` does not return any value. It can work if the function is modified to return an object.

It is possible to overload a unary minus operator using a `friend` function as follows.

```C++
#include <iostream>

using namespace std;

class Point
{
    int x;
    int y;
    int z;
    
    public:
            Point(int x, int y, int z): x(x), y(y), z(z){}
            
            friend void operator -(Point &); // Declaration
            
            void print()
            {
                cout << x << ", " << y << ", " << z << endl;
            }
};

void operator -(Point &p)
{
    p.x = -p.x; // - is invoked on the `int`, not causing a recursive problem.
    p.y = -p.y;
    p.z = -p.z;
}

int main()
{
    Point p(1, 2, 3);
    p.print();    // 1, 2, 3
    -p;           // Invokes operator -();
    p.print();    // -1, -2, -3
    return 0;
}
```

The above invocation statement is equivalent to 

```C++
p.operator -();
```

because in the end, it is still a function that is called a different way via syntax sugar.

**Note:** The argument is passed by **reference**. It will not work if we pass the argument by value because only the copy of the object that activied the call is passed to `operator -()`, therefore the changes made inside the operator function will not reflect in the called object.



