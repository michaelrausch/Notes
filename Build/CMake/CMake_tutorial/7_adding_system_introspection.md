# Adding System Introspection

Let us consider adding some code to our project that depends on features the target platform may not have. For this example, we will add some code that depends on whether or not the target platform has the `log` and `exp` functions. Of course almost every platform has these functions but for this tutorial assume that they are not common.

If the platform has `log` and `exp` then we will use them to compute the square root in the `mysqrt` function. We first test for availability of these functions using the `CheckCXXSourceCompiles` module in `MathFunctions/CMakeLists.txt`.

Add the checks for `log` and `exp` to `MathFunctions/CMakeLists.txt`, after the call to `target_include_directories()`;

```CMake
target_include_directories(MathFunctions
          INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
          )

# link our compiler flags interface library
target_link_libraries(MathFunctions tutorial_compiler_flags)

# does this system provide the log and exp functions?
include(CheckCXXSourceCompiles)
check_cxx_source_compiles("
  #include <cmath>
  int main() {
    std::log(1.0);
    return 0;
  }
" HAVE_LOG)

check_cxx_source_compiles("
  #include <cmath>
  int main() {
    std::exp(1.0);
    return 0;
  }
" HAVE_EXP)
```

An additional note here is that [CheckCXXSourceCompiles](https://cmake.org/cmake/help/latest/manual/cmake-modules.7.html) is a module and therefore needs to be imported using the `include()` function. Additionally, check_cxx_source_compiles checks that the source supplied in `<code>` can be compiled as a C++ source file and linked as an executable (so it must contain at least a main() function).

```CMake
check_cxx_source_compiles(<code> <resultVar>
                          [FAIL_REGEX <regex1> [<regex2>...]])
```

The result will be stored in the internal cache variable specified by `<resultVar>`, with a boolean true value for success and boolean false for failure.

If available, we want to use `target_compile_definitions` to specify `HAVE_LOG` and `HAVE_EXP` as `PRIVATE` compile definitions.

```CMake
if(HAVE_LOG AND HAVE_EXP)
  target_compile_definitions(MathFunctions
                             PRIVATE "HAVE_LOG" "HAVE_EXP")
endif()
```

If `log` and `exp` are available on the system, then we will use them to compute the square root in the `mysqrt` function. Add the following code to the `mysqrt` function in MathFunctions/mysqrt.cxx (don't forget the #endif before returning the result!):

# Further Explanation

From our previous use of

```CMake
target_compile_options(tutorial_compiler_flags INTERFACE
  "$<${gcc_like_cxx}:$<BUILD_INTERFACE:-Wall;-Wextra;-Wshadow;-Wformat=2;-Wunused>>"
  "$<${msvc_cxx}:$<BUILD_INTERFACE:-W3>>"
)
```

We know these flags are passed into the compiler configuration, for example if `gcc_like_css` is `1` then this could be equivalent as;

```
gcc -Wall -Wextra -Wshadow -Wformat=2 -Wunused
```

So now, what is

```CMake
if(HAVE_LOG AND HAVE_EXP)
  target_compile_definitions(MathFunctions
                             PRIVATE "HAVE_LOG" "HAVE_EXP")
endif()
```

accomplishing? Well these are defining the variables to be used in the source code.
For example, let us remove the "HAVE_LOG" from `target_compile_definitions` and see what will happen.

![](./images/23.PNG)

Now, the definition of "HAVE_LOG" is not found, this evaluation will return False and it will return the code below. By including it back in, it will calculate the square root using `log` and `exp` given that both have been found.

The reason it is not found, unlike when we used `configure_file()` is due to them being defined directly on the compiler command line. This is done using the [-D flag](https://www.rapidtables.com/code/linux/gcc/gcc-d.html). For example the equivalent above would be

```
gcc -D HAVE_LOG=1 HAVE_EXP=1
```

