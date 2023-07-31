# Executable vs Libraries

An executable and a library are two different types of software components that serve different purposes in a software project.

## Executable

An executable is a file that can be run by a computer to perform a specific task or set of tasks. It contains machine code that the computer can execute directly. Executables are typically created by compiling source code files written in a programming language such as C++ or Java into machine code, and are usually saved with a file extension such as `.exe` or `.out`. The most common use of an executable file is to run an application, such as a game, a text editor, a web browser, etc.

## Library

On the other hand, a library is a collection of pre-compiled code that can be used by an executable to perform specific tasks or provide specific functionality. They are typically created by compiling source code files into object code and then linking them together to create a library file. Libraries are usually saved with file extensions such as `.dll`, `.so`, `.lib`, `.a` etc. A library can be used in multiple executables and can be shared among many projects.

## Summary

In summary, the core difference between an executable and a library is that an executable is a stand-alone file that can be run by the computer to perform a specific task, while a library is a collection of pre-compiled code that can be used by an executable to perform specific tasks or provide specific functionality. Libraries files cannot be executed directly and are only used.

## Utilization in CMake

## add_executable

`add_executable` is a CMake function that is used to create an executable file from one or more source files. It takes the name of the executable as the first argument and the source files to be included in the executable as additional arguments. The executable file created by this function can be run by the computer to perform a specific task or set of tasks, and is typically created by compiling the source code files passed to the function.

For example, in the CMake tutorial I utilized,

```
add_executable(MakeTable MakeTable.cxx)
```

Therefore, inside `build/MathFunctions/Debug` we can see a `MakeTable.exe`. We can execute this executable directly with parameters in the command line, unlike libraries.

## add_library

`add_library` is a CMake function that is used to create a library from one or more source files. It takes the name of the library as the first argument and the source files to be included in the library as additional arguments. The library file created by this function is not executable, it is a collection of pre-compiled code that can be used by an executable to perform specific tasks or provide specific functionality. It's usually created by compiling the source code files passed to the function.

For example, in the CMake tutorial I utilized,

```
add_library(MathFunctions
            mysqrt.cxx
            ${CMAKE_CURRENT_BINARY_DIR}/Table.h
)
```

Therefore, inside `build/MathFunctions/Debug` we can see a `MathFunctions.lib`. This file is not directly executable, but other executables will link to it.


## Summary

In summary, `add_executable` is used to create an executable file that can be run by the computer, while `add_library` is used to create a library file that can be used by an executable to perform specific tasks or provide specific functionality.

If a target represents an executable, this means it will be a collection of functions and data in binary that **has a main-function or entrypoint (a program)**. If the target is a library, this means it is a collection of functions and data in binary **with no main-function/entrypoint** in a buildsystem.
