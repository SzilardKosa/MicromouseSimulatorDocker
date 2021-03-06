#pragma once
#ifndef API_H
#define API_H

#include <string>

struct Cell
{
  int x;
  int y;
};

struct GoalArea
{
  Cell topLeft;
  Cell bottomRight;
};

class Api {
private:
  static char const MSG_START = '$';
  static std::string history;
  static std::string request(const std::string &cmd);
  static void pushToHistory(const std::string &cmd);
  static void forceShutdown();
  static void saveHistory();

public:
  // Sensor
  static bool frontWallExists();
  static bool leftWallExists();
  static bool rightWallExists();

  // Control
  static void moveForward(int steps = 1);
  static void turnLeft();
  static void turnRight();

  // Maze info
  static int getMazeWidth();
  static int getMazeHeight();
  static GoalArea getGoalArea();
  static bool isFullSize();

  // Feedback: Console
  static void consoleLog(const std::string &text);

  // Feedback: Cell text
  static void setCellText(int x, int y, const std::string& text);

  // Stop simulation
  static void stopSimulation();
};

#endif // API_H
