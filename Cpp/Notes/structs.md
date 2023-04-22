# C++ structs

C and C++ both have the `struct` keyword available, in C it can hold several data types.

The C style struct will be,

```C
struct [structure tag] {
    member definition;
    ...
} [one or more structure definition];
```

However, in C++ `struct` can be closely thought of as a class because it can do everything a class can do. The better comparison would be, what is the difference between `struct` and `class` in C++.

In terms of language, except one little detail, there is no difference between `struct` and `class`. Contrary to what individuals coming from C first think, a `struct` can have constructors, methods (even `virtual` ones), public, private and protected members, use inheritance and be templated. All like a class.

The only difference is if you don't specify the visibility (`public`, `private` or `protected`) of the members, **they will be `public` in the `struct` and `private` in the class**.

The visibility by default goes just a little further than members, for inheritance if you don't specify anything then the struct will inherit publically from its base class.

```C++
struct T : Base // Same as, struct T: public Base
{
    ...
}
```

Whereas the class will do private inheritance by default,

```C++
class T : Base // Same as, class T : private Base
{
    ...
}
```
