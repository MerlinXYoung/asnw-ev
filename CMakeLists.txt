cmake_minimum_required(VERSION 3.15)
project(ASNW C)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/3rd/libev/include)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/3rd/libev/lib)

add_subdirectory(asnw)