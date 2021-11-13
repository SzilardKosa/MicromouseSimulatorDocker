#pragma once

struct GoalArea
{
  int topLeftX;
  int topLeftY;
  int bottomRightX;
  int bottomRightY;
};

// Sensor
int Api_frontWallExists();
int Api_leftWallExists();
int Api_rightWallExists();

// Control
void Api_moveForward(int steps);
void Api_turnLeft();
void Api_turnRight();

// Maze info
int Api_getMazeWidth();
int Api_getMazeHeight();
struct GoalArea Api_getGoalArea();
int Api_isFullSize();

// Feedback
void Api_consoleLog(char* str);
void Api_setCellText(int x, int y, char* str);

// Stop simulation
void Api_stopSimulation();
