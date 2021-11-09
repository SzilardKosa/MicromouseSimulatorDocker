#include <iostream>
#include <string>

#include "api.h"

int main(int argc, char* argv[]) {
  // Sensor
  for (int i = 0; i < 1024; i++)
  {
    bool isFront = Api::frontWallExists();
    bool isLeft = Api::leftWallExists();
    bool isRight = Api::rightWallExists();
  }

  // Control
  for (int i = 0; i < 10240/2; i++)
  {
    Api::moveForward();
    Api::turnLeft();
    Api::turnLeft();
  }
  for (int i = 0; i < 640; i++)
  {
    Api::turnLeft();
    Api::turnRight();
  }

  // Maze info
  int width = Api::getMazeWidth();
  int height = Api::getMazeHeight();
  GoalArea ga = Api::getGoalArea();
  bool isFullSize = Api::isFullSize();
  // Feedback: console
  for (int i = 0; i < 10240; i++)
  {
    Api::consoleLog("Hello");
  }
  // Feedback: cell text
  for (int i = 0; i < 1e7; i++)
  {
    Api::setCellText(1, 2, "123");
  }

  Api::stopSimulation();
}