# Arrays

An array in C++ is a collection of elements of the same type placed in contiguous memory locations that can be individually referenced by using an index to a unique identifier. A typical declaration for an array in C++ is,

```c++
type name [elements];
```

Where `type` is a valid type, such as `int`, `char`, ... <br>
`name` is a valid identifier <br>
`elements` (which is always enclosed in square brackets []), specifies the length of the array in terms of number of elements.

There, the `foo` array, with five elements of type `int` can be declared as;

```C++
int foo[5];
```

**Note:** The `elements` field within the square brackets [], representing the number of elements in the array, must be a constant expression, since array are blocks of static memory whose size must be determined at compile time, before the program runs.

## Initializing arrays

By default, regular arrays of **local scape** (for example, those defined within a function) are left uninitialized. This means that none of its elements are set to any particular value; their contents are undetermined at the point the array is declared.

The elements in an array can be explicitly initialized to specific values when it is declared, by enclosing those initial values in braces `{}`, e.g.

```C++
int foo[5] = {16, 2, 77, 40, 12071};
```

This statement declares an array that can be represented like this;

![image](images/arrays1.png)

The number of values between `{}` shall not be greater than the number of elements in the array. For example, in the example above, `foo` was declared having 5 elements (As specified by the number enclosed in the square brackets, []), and the braces `{}` contained exactly 5 values, one for each element. If declared with less, the remaining elements are set to their default values, which for fundamenal types, means they are filled with zeroes, e.g.

```C++
int bar[5] = {10, 20, 30};
```

Will create an array like this;

![image](images/arrays2.png)

The initializer can even have no values, just the braces.

```C++
int baz[5] = { };
```

This creates an array of five `int` values, each initialized with a value of 0.

![image](images/arrays3.png)

When an initialization of values is provided for an array, C++ allows the possibility of leaving the square brackets empty. In this case, the compiler will assume automatically a size for the array that matches the number of values included between the braces `{}`.

```C++
int foo[] = {1, 2, 3, 4, 5}
```

After this declaration, array `foo` would be 5 `int` long, because we have provided 5 initialization values.

Finally, the evolution of C++ has led to the adoption of *universal initialization* also for arrays. Therefore, there is no longer need for the equal sign between the declaration and the initializer. Both these statements are equivalent;

```
int foo[] = {1, 2, 3};
int foo[] {1, 2, 3};
```

Static arrays, and those declared directly in a namespace (outside any function) are always initialized. If no explicit initializer is specified, all the elements are default-initialized (with zeroes, for fundamental types).

## Character arrays

A string is a collection of characters. There are two types of strings commonly used in C++.

### C-strings

In C programming, the collection of characters is stored in the form of arrays. This is also supported in C++ programming. C-strings are arrays of type `char` terminated with null character, that is, `\0` (ASCII value of null character is 0).

```C++
char a_str[] = "C++";
```

In the above code, `a_str` is a string and it holds 4 characters. Although, "C++" has 3 characters, the null character is added to the end of the string automatically. Alternative ways of defining a C-style string are,

```C++
char a_str[4] = "C++";
char a_str[] = {'C','+','+','\0'};
char a_str[4] = {'C','+','+','\0'};
```

Like arrays, it is not necessary to use all the space allocated for a string, e.g.

```C++
char a_str[100] = "C++";
```

### string Object

The standard C++ library `std` provides us with the string class, `std::string`. Unlike using `char` arrays, `std::string` objects have no fixed length and can be extended as per your requirement.

```C++
#include <iostream>

int main()
{
    
    std::string my_string = "My string object";
    
    std::cout << my_string << "\n";
    
    my_string += " - appended";
    
    std::cout << my_string << "\n";
    std::cout << my_string[0] << "\n";
    std::cout << my_string.at(0) << "\n";
    return 0;
}
```

Will output, 

```C++
My string object
My string object - appended
M
y
```

## Multidimensional arrays

Multidimensional arrays can be described as an *array of arrays*. For example, a bidimensional array can be imagined as a two-dimensional table made of elements, all of them of the same uniform data type.

![image](images/bidimensional_arrays1.png)

`jimmy` represents a bidimensional array of 3 rows and 5 columns of type `int`. The C++ syntax for this is,

```C++
int jimmy[3][5];
```

To index the elements, for example row 1 column 3 would be;

![image](image/../images/bidimensional_arrays2.png)

Multidimensional arrays are not limited to two indicies (i.e. two dimensions). They can contain as many indicies as needed, although the amount of memory needed for an array increases exponentially with each dimension. For example,

```C++
char century [100][365][24][60][60];
```

declares an array with an element of type `char` for each second in a century. Therefore the total amount of elements being $100 * 365 * 24 * 60 * 60 = 3153600000$ `char` elements. This means 3153600000 * 1 byte is required, i.e. 3.1536 Gigabytes!
