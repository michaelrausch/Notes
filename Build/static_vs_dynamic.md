# Static vs Dynamic libraries

When creating a class library in C++, you can choose between dynamic and static libraries. Here we discuss the difference and when to use each one.

Firstly, we need to know what a library is. Basically, a library is a collection of functions. You may have noticed that we are using functions which are not defined in our code, or in that particular file. To have access to them, we include a header file, that contains declarations of those functions. After compile, there is a process called linking, that links those funcion declarations with their definitions, which are in another file. The result of this is an actual executeable.

## Static libraries

Static libraries are `.a` (or in Windows `.lib`) files. All the code relating to the library is in this file and it is directly linked into the program at compile time. A program using a static library **takes copies of the code that it uses from the static library and makes it part of the program**. Windows also has `.lib` files which are used to reference `.dll` files, but they act the same way as the first one.

## Dynamic libraries

Dynamic libraries are `.so` (or in Windows `.dll`, or in OS X `.dylib`) files. All the code relating to the library is in this file, and it is referenced by programs using it at run-time. A program using a dynamic library **only makes references to the code** that it uses in the dynamic library.

## Advantages and Disadvantages

Now, the linking as I described above is static linking. This means that every executeable file contains in it every library (collection of functions) that it needs. This is potentially a waste of space, as there are many programs that may need the same functions. In this case, in memory there would be more copies of the same function. Dynamic linking prevents this, by linking at run-time, not at compile time. This means all the functions are in a special memory space and every program can access them, without have multiple copies of them. This reduces the amount of memory required.

### Static libraries

Static libraries increase the overall size of the binary, but it means that you don't need to carry along a copy of the library that is being used. As the code is connected at compile time there are not any additional run-time loading costs. The code is simply there.

### Dynamic libraries

Dynamic libraries reduce the amount of code that is duplicated in each program that makes use of the library, keeping the binaries small. It also allows you to replace the dynamic object with one that is functionally equivalent, but may have added performance benefits without needing to recompile the program that makes use of it. Dynamic libraries will, however have a small additional cost for the execution of the functions as well as a run-time loading cost as all the symbols in the library need to be connected to the things they use. Additionally, dynamic libraries can be loaded into an application at run-time, which is the general mechanism for implementing binary plug-in systems.

