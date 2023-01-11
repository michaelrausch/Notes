# Adding Generator Expressions

Generator expressions are evaluated during build system generation to produce information specific to each build configuration.

Generator expressions are allowed in the context of many target properties, such as `LINK_LIBRARIES`, `INCLUDE_DIRECTORIES`, `COMPILE_DEFINITIONS` and others. They may also be used when using commands to populate those properties, such as `target_link_libraries()`, `target_include_directories()` and `target_compile_definitions()` and others.

There are different types of generator expressions including Logical, Informational and Output expressions.

Logical expressions are used to create conditional output. The basic expressions are the `0` and `1` expressions. A `$<0:...>` results in the empty string, and `<1:...>` results in the content of `...`. They can also be nested.

## Specifying the C++ standard

In this exercise, I will refactor our code to use an `INTERFACE` library to specify the C++ standard.

To begin, we first need to remove the two previous usages of `set` calls on the variables `CMAKE_CXX_STANDARD` and `CMAKE_CXX_STANDARD_REQUIRED`. The two specific lines were,

```CMake
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)
```

Next, we need to create an interface library, `tutorial_compiler_flags`. Then, use `target_compile_features()` to add the compiler feature `cxx_std_11`. This is achieved by the two following lines,

```CMake
add_library(tutorial_compiler_flags INTERFACE)
target_compile_features(tutorial_compiler_flags INTERFACE cxx_std_11)
```

Finally, with the interface setup we need to link our executeable target and our MathFunctions library to our new `tutorial_compiler_flags` library. Respectively, the code will look like this:

`CMakeLists.txt`
```CMake
target_link_libraries(compute_square_root PUBLIC 
                        ${EXTRA_LIBS} tutorial_compiler_flags
                      )
```

`MathFunctions/CMakeLists.txt`

```CMake
target_link_libraries(MathFunctions tutorial_compiler_flags)
```

With this, all of our code still requires C++ to build. Notice though that with this method, it gives us the ability to be specific about which targets get specific requirements. In addition, we create a **single sourth of truth in our interface library**.

# Adding Compiler Warning Flags with Generator Expressions

A common usage of `generator expressions` is to conditionally add compiler flags, such as those for language levels or warnings. A nice pattern is to associate this information to an `INTERFACE` target allowing this information to propagate.

The goal here is to add compiler warning flags when building but no for installed versions.

Because generator expressions were introduced in CMake `3.15`, we first need up update `cmake_minimum_required()` to be `3.15`, thus;

```CMake
cmake_minimum_required(VERSION 3.15)
```

is used. Next, we determine which compiler our system is currently using to build since warning flags vary based on the compiler w use. This is done with the `COMPILE_LANG_AND_ID` generator expression. We set the result in the variables `gcc_like_cxx` and `msvc_cxx` as follows;

```CMake
set(gcc_like_cxx "$<COMPILE_LANG_AND_ID:CXX,ARMClang,AppleClang,Clang,GNU,LCC>")
set(msvc_cxx "$<COMPILE_LANG_AND_ID:CXX,MSVC>")
```

Next we add the desired compiler warning flags that we want for our project. Using our variables `gcc_like_cxx` and `msvc_cxx`, we can use another generator expression to apply the respective flags only when the variables are true. We use `target_compile_options()` to apply these flags to our interface library.

```CMake
target_compile_options(tutorial_compiler_flags INTERFACE
  "$<${gcc_like_cxx}:-Wall;-Wextra;-Wshadow;-Wformat=2;-Wunused>"
  "$<${msvc_cxx}:-W3>"
)
```

Lastly, we only want these warning flags to be used during builds. Consumers of our installed project should not inherit our warning flags. To specify this, we wrap our flags in a generator expression using the BUILD_INTERFACE condition. The resulting full code looks like the following,

```CMake
target_compile_options(tutorial_compiler_flags INTERFACE
  "$<${gcc_like_cxx}:$<BUILD_INTERFACE:-Wall;-Wextra;-Wshadow;-Wformat=2;-Wunused>>"
  "$<${msvc_cxx}:$<BUILD_INTERFACE:-W3>>"
)
```

## Further Gerenerator Explanation

Although different syntax exists for generators the specific line 

```CMake
set(gcc_like_cxx "$<COMPILE_LANG_AND_ID:CXX,ARMClang,AppleClang,Clang,GNU,LCC>")
```

works the following way [from the online documentation.](https://cmake.org/cmake/help/latest/manual/cmake-generator-expressions.7.html#genex:COMPILE_LANG_AND_ID) `<COMPILE_LANG_AND_ID:language,compiler_ids>`

`1` when the language used for compilation unit matches language and CMake's compiler id of the language compiler matches any one of the comma-separated entries in compiler_ids, otherwise `0`.

This can be expressed in Python as the following logic for easier understanding.

```Python
gcc_like_cxx = 0
if COMPILE_LANG = CXX and COMPILE_ID in ("ARMClang", "AppleClang" ,"Clang","GNU", "LCC"):
    gcc_like_cxx = 1

```

Therefore the use afterwards inside of 

```CMake
target_compile_options(tutorial_compiler_flags INTERFACE
  "$<${gcc_like_cxx}:$<BUILD_INTERFACE:-Wall;-Wextra;-Wshadow;-Wformat=2;-Wunused>>"
  "$<${msvc_cxx}:$<BUILD_INTERFACE:-W3>>"
)
```

Will be evaluated as (When `gcc_like_cxx=1` and `msvc=0`)

```CMake
target_compile_options(tutorial_compiler_flags INTERFACE
  "$<1:$<BUILD_INTERFACE:-Wall;-Wextra;-Wshadow;-Wformat=2;-Wunused>>"
  "$<0:$<BUILD_INTERFACE:-W3>>"
)
```

Recall one the usages of generators are for using whatever is on the content of `...` of `$<bool:...>` if `bool=1` else an empty string if `bool=0`.

The usage of `-Wall;-Wextra;-Wshadow;-Wformat=2;-Wunused` comes from the gcc compiler flag options for the [warning options](https://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html). It is identical to the `- flag` if we were to type it in the command line as,

```
gcc -Wall -Wextra -Wshadow -Wformat=2 -Wunused
```

when `gcc_like_cxx` is `1`. However this will produce a build error for a `msvc` compiler, which is why when it is evaluated to `0`. Only `-W3` is passed as a compiler for the warning severity, [also available online from the documentation](https://learn.microsoft.com/en-us/cpp/build/reference/compiler-option-warning-level?view=msvc-170).

# Debugging

Although generators will only be assigned their value during build in this example we know that the compiler ID used in the generator will be from [CMAKE_<LANG>_COMPILER_ID](https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_COMPILER_ID.html). Therefore what we can do is utilize

```CMake
message("${CMAKE_CXX_COMPILER_ID}")
```

and know that within our example, we are using the compiler `MSVC`. This means for us, we will have `msvc_css` have the value of `1` because we are using the C++ compiler and match from our previous generator,

```CMake
"$<COMPILE_LANG_AND_ID:CXX,MSVC>"
```