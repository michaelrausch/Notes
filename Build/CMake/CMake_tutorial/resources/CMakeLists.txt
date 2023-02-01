cmake_minimum_required(VERSION 3.15)

project(My_Project VERSION 1.0)

add_library(tutorial_compiler_flags INTERFACE)
target_compile_features(tutorial_compiler_flags INTERFACE cxx_std_11)

# add compiler warning flags just when building this project via
# the BUILD_INTERFACE genex
set(gcc_like_cxx "$<COMPILE_LANG_AND_ID:CXX,ARMClang,AppleClang,Clang,GNU,LCC>")
set(msvc_cxx "$<COMPILE_LANG_AND_ID:CXX,MSVC>")

target_compile_options(tutorial_compiler_flags INTERFACE
  "$<${gcc_like_cxx}:$<BUILD_INTERFACE:-Wall;-Wextra;-Wshadow;-Wformat=2;-Wunused>>"
  "$<${msvc_cxx}:$<BUILD_INTERFACE:-W3>>"
)

option(USE_MYMATH "Use tutorial provided math implementation" TRUE)

configure_file(src/sqrt.h.in src/sqrt.h)

if(USE_MYMATH)
  add_subdirectory(MathFunctions)
  list(APPEND EXTRA_LIBS MathFunctions)
endif()
 
add_executable(compute_square_root 
    src/sqrt.cxx)

target_link_libraries(compute_square_root PUBLIC 
                        ${EXTRA_LIBS} tutorial_compiler_flags
                      )

target_include_directories(compute_square_root PUBLIC
                            "${PROJECT_BINARY_DIR}/src"
                           )

install(TARGETS compute_square_root DESTINATION bin)
install(FILES "${PROJECT_BINARY_DIR}/src/sqrt.h"
  DESTINATION include
  )


###### Tests ######

include(CTest)

add_test(NAME Runs COMMAND compute_square_root 25)

add_test(NAME NoArgumentsGiven COMMAND compute_square_root)
set_tests_properties(NoArgumentsGiven
  PROPERTIES PASS_REGULAR_EXPRESSION "Usage:.*number"
  )

add_test(NAME StandardUse COMMAND compute_square_root 4)
set_tests_properties(StandardUse
  PROPERTIES PASS_REGULAR_EXPRESSION "The square root of 4 is 2"
  )

function(do_test target arg result)
  add_test(NAME Comp${arg} COMMAND ${target} ${arg})
  set_tests_properties(Comp${arg}
    PROPERTIES PASS_REGULAR_EXPRESSION ${result}
    )
endfunction()

# do a bunch of result based tests
do_test(compute_square_root 4 "The square root of 4 is 2")
do_test(compute_square_root 9 "The square root of 9 is 3")
do_test(compute_square_root 5 "The square root of 5 is 2.236")
do_test(compute_square_root 7 "The square root of 7 is 2.645")
do_test(compute_square_root 25 "The square root of 25 is 5")
do_test(compute_square_root -25 "The square root of -25 is (-nan|nan|0)")
do_test(compute_square_root 0.0001 "The square root of 0.0001 is 0.01")

# setup installer
include(InstallRequiredSystemLibraries)
set(CPACK_RESOURCE_FILE_LICENSE "${CMAKE_CURRENT_SOURCE_DIR}/License.txt")
set(CPACK_PACKAGE_VERSION_MAJOR "${My_Project_VERSION_MAJOR}")
set(CPACK_PACKAGE_VERSION_MINOR "${My_Project_VERSION_MINOR}")
set(CPACK_SOURCE_GENERATOR "TGZ")
include(CPack)
