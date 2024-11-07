cmake_minimum_required(VERSION 3.8)
project(my_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)

# # Include Cpp "include" directory
# include_directories(include)

# # Create Cpp executable
# add_executable(cpp_executable src/cpp_node.cpp)
# ament_target_dependencies(cpp_executable rclcpp)

# # Testing dependencies
# if(BUILD_TESTING)
#   find_package(ament_lint_auto REQUIRED)
#   set(ament_cmake_copyright_FOUND TRUE)
#   set(ament_cmake_cpplint_FOUND TRUE)
#   ament_lint_auto_find_test_dependencies()
# endif()

# Install launch files
install(
  DIRECTORY launch description
  DESTINATION share/${PROJECT_NAME}
)

# Controller file
install(
    PROGRAMS scripts/robot_control.py
    DESTINATION lib/${PROJECT_NAME}
)

# Only call ament_package once
ament_package()
