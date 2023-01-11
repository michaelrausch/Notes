# Generator Expressions

Generator expressions are evaluated during build system generation to produce information specific to each build configuration. They have the form `$<...>` and can be broken down into three main categories `Logical Expressions`, `Informational Expressions` and `Output Expressions`. This is a quick reference for generators and for more indepth explanation of each method [the main documentation](https://cmake.org/cmake/help/latest/manual/cmake-generator-expressions.7.html) is required.

Generator expressions are allowed in the context of many target properties, such as LINK_LIBRARIES, INCLUDE_DIRECTORIES, COMPILE_DEFINITIONS and others. They may also be used when using commands to populate those properties, such as `target_link_libraries()`, `target_include_directories()`, `target_compile_definitions()` and others.

This means that they enable conditional linking, conditional definitions used when compiling, and conditional include directories and more. The conditions may be based on the build configuration, target properties, platform information or any other queryable information.

# Logical Expressions

Logical expressions are used to create conditional output. The basic expressions are the 0 and 1 expressions. A `$<0:...>` results in the empty string, and `<1:...>` results in the content of `...`. They can also be nested.

For example,

- `$<0:...>`
  - Empty string (ignores `...`)
- `<$<1:...>` 
  - Content of `...` 

Keep in mind this is not entirely true for some string comparison expressions, for example.

- `$<STREQUAL:a,b>`
  - `1` if `a` is STREQUAL `b`, else `0` 

likewise with

- `$<CXX_COMPILER_ID:comp>`
  - `1` if the CMake-id of the CXX compiler matches `comp`, otherwise `0`.

# Informational Expressions

These expressions expand to some information. The information may be used directly, eg:

```CMake
include_directories(/usr/include/$<CXX_COMPILER_ID>/)
```

expands to `/usr/include/GNU/` or `/usr/include/Clang/` etc, depending on the Id of the compiler.

These variables used inside the generator are CMake variables and cannot be custom made. Therefore, the list of variables are available on the online documentation.

# Output Expressions

These expressions generate output, in some cases depending on an input. These expressions may be combined with other expressions for information or logical comparison:

- `$<JOIN:list,...>`
  - Joins the list with the content of `...` 
- `$<BUILD_INTERFACE:...>`
  - Content of `...` when the property is exported using `export()`, or when the target is used by another target in the same buildsystem. Expands to the empty string otherwise. 
- `$<UPPER_CASE:...>`
  - Content of `...` converted to upper case. 