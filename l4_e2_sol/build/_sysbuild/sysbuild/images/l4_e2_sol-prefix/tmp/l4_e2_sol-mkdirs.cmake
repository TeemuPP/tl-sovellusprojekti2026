# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file LICENSE.rst or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION ${CMAKE_VERSION}) # this file comes with cmake

# If CMAKE_DISABLE_SOURCE_CHANGES is set to true and the source directory is an
# existing directory in our source tree, calling file(MAKE_DIRECTORY) on it
# would cause a fatal error, even though it would be a no-op.
if(NOT EXISTS "C:/Users/teemu/NordicSW/BLEteht/bt-fund/l4/l4_e2_sol")
  file(MAKE_DIRECTORY "C:/Users/teemu/NordicSW/BLEteht/bt-fund/l4/l4_e2_sol")
endif()
file(MAKE_DIRECTORY
  "C:/Users/teemu/NordicSW/BLEteht/bt-fund/l4/l4_e2_sol/build/l4_e2_sol"
  "C:/Users/teemu/NordicSW/BLEteht/bt-fund/l4/l4_e2_sol/build/_sysbuild/sysbuild/images/l4_e2_sol-prefix"
  "C:/Users/teemu/NordicSW/BLEteht/bt-fund/l4/l4_e2_sol/build/_sysbuild/sysbuild/images/l4_e2_sol-prefix/tmp"
  "C:/Users/teemu/NordicSW/BLEteht/bt-fund/l4/l4_e2_sol/build/_sysbuild/sysbuild/images/l4_e2_sol-prefix/src/l4_e2_sol-stamp"
  "C:/Users/teemu/NordicSW/BLEteht/bt-fund/l4/l4_e2_sol/build/_sysbuild/sysbuild/images/l4_e2_sol-prefix/src"
  "C:/Users/teemu/NordicSW/BLEteht/bt-fund/l4/l4_e2_sol/build/_sysbuild/sysbuild/images/l4_e2_sol-prefix/src/l4_e2_sol-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "C:/Users/teemu/NordicSW/BLEteht/bt-fund/l4/l4_e2_sol/build/_sysbuild/sysbuild/images/l4_e2_sol-prefix/src/l4_e2_sol-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "C:/Users/teemu/NordicSW/BLEteht/bt-fund/l4/l4_e2_sol/build/_sysbuild/sysbuild/images/l4_e2_sol-prefix/src/l4_e2_sol-stamp${cfgdir}") # cfgdir has leading slash
endif()
