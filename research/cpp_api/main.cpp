#include <iostream>
#include <string>

#include "api.h"

int main(int argc, char* argv[]) {
  // Sensor
  bool isFront = Api::frontWallExists();
  std::cout << isFront << std::endl;
  bool isLeft = Api::leftWallExists();
  std::cout << isLeft << std::endl;
  bool isRight = Api::rightWallExists();
  std::cout << isRight << std::endl;
  // Control
  Api::moveForward();
  Api::moveForward(2);
  Api::turnLeft();
  Api::turnRight();
  // Maze info
  int width = Api::getMazeWidth();
  std::cout << width << std::endl;
  int height = Api::getMazeHeight();
  std::cout << height << std::endl;
  GoalArea ga = Api::getGoalArea();
  std::cout << ga.topLeft.x << " " << ga.topLeft.y << std::endl;
  std::cout << ga.bottomRight.x << " " << ga.bottomRight.y << std::endl;
  bool isFullSize = Api::isFullSize();
  std::cout << isFullSize << std::endl;
  // Feedback: wall
  Api::setWall(1, 2, 3);
  Api::clearWall(1, 2, 3);
  // Feedback: console
  Api::consoleLog("eyyo");
  // Feedback: cell color
  Api::setColor(1, 2, 3);
  Api::clearColor(1, 2);
  Api::clearAllColor();
  // Feedback: cell text
  Api::setText(1, 2, "chiao");
  Api::clearText(1, 2);
  Api::clearAllText();

  Api::saveHistory();
}