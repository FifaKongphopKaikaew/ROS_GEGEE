#include "rclcpp/rclcpp.hpp"

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  rclcpp::spin_some(std::make_shared<YourNode>());
  rclcpp::shutdown();
  return 0;
}
