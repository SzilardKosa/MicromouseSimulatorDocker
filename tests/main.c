#include <stdio.h>

#include "api.h"

int main(int argc, char* argv[]) {
    // Sensor
    for (int i = 0; i < 1024; i++)
    {
        int isFront = Api_frontWallExists();
        int isLeft = Api_leftWallExists();
        int isRight = Api_rightWallExists();
    }

    // Control
    for (int i = 0; i < 5120; i++)
    {
        Api_moveForward(1);
        Api_turnLeft();
        Api_turnLeft();
    }
    for (int i = 0; i < 640; i++)
    {
        Api_turnLeft();
        Api_turnRight();
    }

    // Maze info
    int w = Api_getMazeWidth();
    int h = Api_getMazeHeight();
    int isFullSize = Api_isFullSize();
    struct GoalArea ga = Api_getGoalArea();

    // Feedback
    for (int i = 0; i < 10240; i++)
    {
        Api_consoleLog("hello");
    }
    for (int i = 0; i < 1e5; i++)
    {
        Api_setCellText(1, 2, "AB2");
    }

    // Stop simulation
    Api_stopSimulation();
}