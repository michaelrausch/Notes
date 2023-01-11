# Adding Usage Requirements for a Library

Usage requirements of a target parameters allow for far better control over a library or executable's link and include line while also giving more control over the transitive property of targets inside CMake. The primary commands that leverage usage requirements are:

```CMake
target_compile_definitions()
target_compile_options()
target_include_directories()
target_link_directories()
target_link_options()
target_precompile_headers()
target_sources()
```

In this part of the tutorial we will be refactoring our code previous written to use the more modern CMake approach. The goal is to let our library define its own usage requirements so they are passed transitively to other targets as necessary. In this case, `MathFunctions` will specify any needed include directories itself. Then, the consuming target `computer_square_root` simply needs to link to `MathFunctions` and not worry about any additional include directories that we have from `EXTRA_INCLUDES`


```CMake
# add the binary tree to the search path for include files
# so that we will find sqrt.h
target_include_directories(compute_square_root PUBLIC
                           "${PROJECT_BINARY_DIR}/src",
                           ${EXTRA_INCLUDES}
                           )
```

To achieve this we want to state that anybody linking to `MathFunctions`
needs to include the current source directory, while `MathFunctions` itself
doesn't. This can be expressed with an `INTERFACE usage requirement. Remember
`INTERFACE` means things that consumers require but the producer doesn't.

Therefore, at the end of `MathFunctions/CMakeLists.txt`, we need to use `target_include_directories` with the `INTERFACE` keyword, as follows:


```CMake
target_include_directories(MathFunctions
          INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
          )
```

Now that we've specified usage requirements for `MathFunctions` we can safely remove our uses of the `EXTRA_INCLUDES` variable from the top-level `CMakeLists.txt`.

Now we will have,

```CMake
if(USE_MYMATH)
  add_subdirectory(MathFunctions)
  list(APPEND EXTRA_LIBS MathFunctions)
endif()
```

and

```CMake
target_include_directories(Tutorial PUBLIC
                           "${PROJECT_BINARY_DIR}/src"
                           )
```

Notice with this technique, the only thing our executable does to use our library is call `target_link_libraries()` with the name of the library target. In larger projects, the classic method of specifying library dependencies manually becomes very complicated very quickly.

An additional note is that `CMAKE_CURRENT_SOURCE_DIR` is the path to the source directory that is **currently being processed**. The output of `message(STATUS ${CMAKE_CURRENT_SOURCE_DIR})` will therefore be `C:/.../MathFunctions`.

This means that `target_include_directories` will include the `MathFunctions` header files itself and not need **whoever uses the library to deal with those include problems**.