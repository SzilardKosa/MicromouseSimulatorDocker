#include "api.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <stdlib.h>

std::vector<std::string> Api::history;

std::string Api::request(const std::string &cmd) {
  std::cout << MSG_START << cmd;
  std::string response;
  std::getline(std::cin, response);
  if (response == "err")
    forceShutdown();
  return response;
}

void Api::pushToHistory(const std::string &cmd){
  history.push_back(cmd);
}

void Api::forceShutdown(){
  saveHistory();
  exit(1);
}

void Api::saveHistory(){
  std::ofstream fout("shared/history.txt");
  for(auto const& x : history)
    fout << x;
}

// Sensor
bool Api::frontWallExists() {
  pushToHistory("fw\n");
  return request("fw\n") == "True";
}

bool Api::leftWallExists() {
  pushToHistory("lw\n");
  return request("lw\n") == "True";
}

bool Api::rightWallExists() {
  pushToHistory("rw\n");
  return request("rw\n") == "True";
}

// Control
void Api::moveForward(int steps){
  std::string cmd = "mf " + std::to_string(steps) + "\n";
  pushToHistory(cmd);
  request(cmd);
}

void Api::turnLeft(){
  pushToHistory("tl\n");
  request("tl\n");
}

void Api::turnRight(){
  pushToHistory("tr\n");
  request("tr\n");
}


// Maze info
int Api::getMazeWidth(){
  return std::stoi(request("mw\n"));
}

int Api::getMazeHeight(){
  return std::stoi(request("mh\n"));
}

GoalArea Api::getGoalArea(){
  std::istringstream iss( request("ga\n"));
  int x1, y1, x2, y2;
  iss >> x1 >> y1 >> x2 >> y2;
  return {{x1, y1}, {x2, y2}};
}

bool Api::isFullSize(){
  return request("if\n") == "True";
}


// Feedback: Wall
void Api::setWall(int x, int y, char direction){
  std::string cmd = "sw " +
  std::to_string(x) + " " +
  std::to_string(y)+ " " +
  std::to_string(direction) + "\n";
  pushToHistory(cmd);
}

void Api::clearWall(int x, int y, char direction){
  std::string cmd = "cw " +
  std::to_string(x) + " " +
  std::to_string(y)+ " " +
  std::to_string(direction) + "\n";
  pushToHistory(cmd);
}


// Feedback: Console
void Api::consoleLog(const std::string &text){
  std::string cmd = "cl " + text + "\n";
  pushToHistory(cmd);
}


// Feedback: Cell color
void Api::setColor(int x, int y, char color){
  std::string cmd = "sc " +
  std::to_string(x) + " " +
  std::to_string(y)+ " " +
  std::to_string(color) + "\n";
  pushToHistory(cmd);
}

void Api::clearColor(int x, int y){
  std::string cmd = "cc " +
  std::to_string(x) + " " +
  std::to_string(y)+ "\n";
  pushToHistory(cmd);
}

void Api::clearAllColor(){
  pushToHistory("cac\n");
}


// Feedback: Cell text
void Api::setText(int x, int y, const std::string& text){
  std::string cmd = "st " +
  std::to_string(x) + " " +
  std::to_string(y)+ " " +
  text + "\n";
  pushToHistory(cmd);
}

void Api::clearText(int x, int y){
  std::string cmd = "ct " +
  std::to_string(x) + " " +
  std::to_string(y)+ "\n";
  pushToHistory(cmd);
}

void Api::clearAllText(){
  pushToHistory("cat\n");
}
