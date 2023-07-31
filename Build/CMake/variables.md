# CMake Variables

Let us first state which variables we should ideally **not** be naming. CMake has some special variables that are either created behind the scenes or have meaning to CMake when set by project code. Many of these variables start with `CMAKE_`. Avoid this naming convention when creating variables for your projects.

Keep in mind when searching for the documentation of `CMAKE_` values  the prefix `CMAKE_` has been removed. For example the documentation page for [CMAKE_CXX_STANDARD_REQUIRED](https://cmake.org/cmake/help/latest/variable/CMAKE_CXX_STANDARD_REQUIRED.html) will direct you to the page for the variable [CXX_STANDARD_REQUIRED](https://cmake.org/cmake/help/latest/prop_tgt/CXX_STANDARD_REQUIRED.html#prop_tgt:CXX_STANDARD_REQUIRED), i.e. the `CMAKE_` is stripped away.

With CMake variables it is worth noting that using variables that are **not initialized** and attempted to use, an error will not occur. Instead, an empty string will be used.

The list of available CMake variables are available from their [online documentation](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html).

# Syntax for Passing as a Parameters

All command parameters are treated as strings in CMake. Parameters are separated by whitespace unless quoted. The exact effect of a parameter depends on the command.

The following commands have the same effect:

```cmake
add_subdirectory(MathFunctions)
add_subdirectory("MathFunctions")
```

In the case of `add_library` the first parameter is treated as the target name. CMake internally keeps track of targets and stores several pieces of information for them. The target name `MathFunctions` is entirely unrelated to the name of the subdirectory added via `add_subdirectory`; you could rename the directory to be `FooBar` and use `add_subdirectory(FooBar)` and nothing would change.

# Variable Scoping

Variable values you write are actually set for the current scope only, but reading variables CMake look into ancestor scopes, unless a variable is found in the current scope.

For example, if I have a parent CMake file that contains;

```cmake
if(USE_MYMATH)
  set(MyString "Some Text")
  add_subdirectory(MathFunctions)
  list(APPEND EXTRA_LIBS MathFunctions)
endif()

# ...

target_link_libraries(compute_square_root PUBLIC 
  ${EXTRA_LIBS} tutorial_compiler_flags
)
```

Inside the CMakeLists.txt for MathFunctions contains,

```cmake
add_library(MathFunctions mysqrt.cxx)

target_include_directories(MathFunctions
  INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
)
message(STATUS "${MyString}")
```

will correctly print "Some Text" as it can reference the variable `MyString` which was set by the parent. To define a variable in the parent directory's scope, you must define it like `set(<variable> <value>... PARENT_SCOPE)`. If you want to "pass" the definition of a variable up several scopes, you must call `set(... PARENT_SCOPE)` multiple times to go up each scope level.

# Standard Syntax

Strings using `set()`:

- `set(MyString "Some Text")`
  - `message("${MyString}")` will output `Some Text`
- `set(MyStringWithVar "Some other Text: ${MyString}")`
  - `message("${MyStringWithVar}")` will output `Some other Text: Some Text`

Or with `string()`:

- `string(APPEND MyStringWithContent " ${MyString}")`
  
Lists using `set()`:

- `set(MyList "a" "b" "c")`
  - `message("${MyList}")` will output `a;b;c`
- `set(MyList ${MyList} "d")`
  - `message("${MyList}")` will output `a;b;c;d`

Or better with `list()`:

- `list(APPEND MyList "a" "b" "c")`.
  - `message("${MyList}")` will output `a;b;c`
- `list(APPEND MyList "d")`
  - `message("${MyList}")` will output `d`, but if used after will output `a;b;c;d`

List of File Names:

- `set(MySourcesList "File.name" "File with Space.name")`
  - `message("${MySourcesList}")` will output `File.name;File with Space.name`
- `list(APPEND MySourcesList "File.name" "File with Space.name")`
  - `message("${MySourcesList}")` will output `File.name;File with Space.name`
- `add_excutable(MyExeTarget ${MySourcesList})`

# Environment Variables

You can read `$ENV{...}` and write `set(ENV{...})` environment variables.