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

  // Feedback: wall
  for (int i = 0; i < 3072; i++)
  {
    Api::setWall(1, 2, 3);
  }
  Api::clearWall(1, 2, 3);
  // Feedback: console
  for (int i = 0; i < 10240; i++)
  {
    Api::consoleLog("Hello");
  }
  // Feedback: cell color
  for (int i = 0; i < 1e7; i++)
  {
    Api::setColor(1, 2, 3);
  }
  Api::clearColor(1, 2);
  for (int i = 0; i < 10240; i++)
  {
    Api::clearAllColor();
  }
  // Feedback: cell text
  for (int i = 0; i < 1e7; i++)
  {
    Api::setText(1, 2, "123");
  }
  Api::clearText(1, 2);
  for (int i = 0; i < 10240; i++)
  {
    Api::clearAllText();
  }

  Api::saveHistory();
}