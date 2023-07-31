# PUBLIC, PRIVATE and INTERFACE

If I have a CMake-library `add_library(libhelper helper.cpp)` and I want to include the source files via `target_include_directories`. Then I have to choose between the parameters `PRIVATE`, `PUBLIC` and `INTERFACE`. Here, I will explain the difference.

`PRIVATE` - The includes can **only** be used by the `libhelper`-library itself.

`PUBLIC` - The includes can be used by the `libhelper`-library itself **and** any target that uses the `libhelper`-library, e.g. via `target_link_libraries(MainApplication PUBLIC libhelpers)`.

`INTERFACE`-The includes **cannot be used** by the `libhelper`-library, only by the targets **that use** the `libhelper`-library.

# Example

`File Structure`

```
│   CMakeLists.txt
│   helper.cpp
│   main.cpp
│
├───details_interface
│       details_interface.cpp
│
├───details_private
│       details_private.cpp
│
└───details_public
        details_public.cpp
```

`CMakeLists.txt`

```CMake
cmake_minimum_required(VERSION 3.1)
set(CMAKE_CXX_STANDARD 17)
project(cmake_experiment)

add_executable(cmake_experiment main.cpp)

target_link_libraries(cmake_experiment libhelper)

add_library(libhelper helper.cpp)

target_include_directories(libhelper
        INTERFACE details_interface
        PUBLIC details_public
        PRIVATE details_private)
```

`cmake_experiment` (That uses `main.cpp`) links to `libhelper`. This means it can use the library
`PUBLIC` and `INTERFACE`, but **not** `PRIVATE`. 


`main.cpp`

```C++
#include <iostream>

#include "details_public.cpp"
#include "details_interface.cpp"

// fatal error: details_private.cpp: No such file or directory:
// #include "details_private.cpp"

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```


The library `libhelper` uses the single file `helper.cpp`. Inside `helper.cpp` it can only use
`PUBLIC` and `PRIVATE` and **not** `INTERFACE`.

`helper.cpp`

```C++
#include "details_public.cpp"
#include "details_private.cpp"

// fatal error: details_interface.cpp: No such file or directory:
// #include "details_interface.cpp"
```
