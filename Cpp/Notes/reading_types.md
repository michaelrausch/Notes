# Reading C++/C Types

The general advice is to read it backwards, as given by the clockwise/spiral rule.

To discover whether `const` applies to pointer or pointed to data, split the statement at the asterix sign. If the `const` keyword appears on the left (`const int * foo`), it then belongs to the pointed data. If it is on the right part (`int * const bar`), then it is about the pointer.

```C++
int * t;             // pointer to int
int const * t;       // pointer to const int
int * const t;       // const pointer to int
int const * const t; // const pointer to const int
```

Now, the first `const` can be on either side of the type,

`const int *` is equal to `int const *`, they're both a pointer to a  constant integer.

`const int * const` is equal to `int const * const`.

If we want to go really crazy, we can do things such as,

```C++
int **t;                // pointer to pointer to an int
int ** const t;         // cost pointer to pointer to an int
int * const * t;        // pointer to const pointer to int
int const ** t;         // pointer to pointer to const int
int * const * const t;  // const pointer to const pointer to int
```