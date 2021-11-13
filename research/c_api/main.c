#include <stdio.h>

#include "api.h"

int main(int argc, char* argv[]) {
    // Sensor
    int isFront = Api_frontWallExists();
    printf("is front: %d\n", isFront);
    int isLeft = Api_leftWallExists();
    printf("is left: %d\n", isLeft);
    int isRight = Api_rightWallExists();
    printf("is right: %d\n", isRight);

    // Control
    Api_moveForward(12);
    Api_turnLeft();
    Api_turnRight();

    // Maze info
    int w = Api_getMazeWidth();
    printf("width: %d\n", w);
    int h = Api_getMazeHeight();
    printf("height: %d\n", h);
    int isFullSize = Api_isFullSize();
    printf("is full: %d\n", isFullSize);
    struct GoalArea ga = Api_getGoalArea();
    printf("goal: %d %d %d %d\n", ga.topLeftX, ga.topLeftY, ga.bottomRightX, ga.bottomRightY);


    // Feedback
    Api_consoleLog("hello");
    Api_setCellText(1, 2, "AB2");

    // Stop simulation
    Api_stopSimulation();
}