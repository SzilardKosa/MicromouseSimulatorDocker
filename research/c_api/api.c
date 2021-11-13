#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "api.h"

#define BUFFER_SIZE 32


char history[] = "";

void pushToHistory(char* cmd){
    strcat(history, cmd);
    strcat(history, "\n");
}

void saveHistory(){
    FILE *out=fopen("shared/history.txt","w");
	fputs(history, out);
	fclose(out);
}

void forceShutdown(){
    saveHistory();
    exit(0);
}

void sendRequest(char* cmd, char* response){
    printf("$%s\n", cmd);
    fflush(stdout);
    fgets(response, BUFFER_SIZE, stdin);
    if (strcmp(response, "end\n") == 0)
        forceShutdown();
}

void request(char* cmd){
    char response[BUFFER_SIZE];
    sendRequest(cmd, response);
}

int requestInt(char* cmd){
    char response[BUFFER_SIZE];
    sendRequest(cmd, response);
    int value = atoi(response);
    return value;
}

int requestBool(char* cmd){
    char response[BUFFER_SIZE];
    sendRequest(cmd, response);
    int value = (strcmp(response, "True\n") == 0);
    return value;
}

struct GoalArea requestGoalArea(char* cmd){
    char response[BUFFER_SIZE];
    sendRequest(cmd, response);
    struct GoalArea ga;
    ga.topLeftX = atoi(strtok(response, " "));
    ga.topLeftY = atoi(strtok(NULL, " "));
    ga.bottomRightX = atoi(strtok(NULL, " "));
    ga.bottomRightY = atoi(strtok(NULL, " "));
    return ga;
}

// Sensor
int Api_frontWallExists() {
    pushToHistory("fw");
    return requestBool("fw");
}

int Api_leftWallExists() {
    pushToHistory("lw");
   return requestBool("lw");
}

int Api_rightWallExists() {
    pushToHistory("rw");
    return requestBool("rw");
}

// Control
void Api_moveForward(int steps) {
    char cmd[6];
    snprintf(cmd, 6, "mf %d", steps % 100);
    pushToHistory(cmd);
    request(cmd);
}

void Api_turnLeft() {
    pushToHistory("tl");
    request("tl");
}

void Api_turnRight() {
    pushToHistory("tr");
    request("tr");
}

// Maze info
int Api_getMazeWidth() {
    return requestInt("mw");
}

int Api_getMazeHeight() {
   return requestInt("mh");
}

struct GoalArea Api_getGoalArea() {
    return requestGoalArea("ga");
}

int Api_isFullSize() {
    return requestBool("if");
}

// Feedback
void Api_consoleLog(char* str) {
    char cmd[] = "cl ";
    strcat(cmd, str);
    pushToHistory(cmd);
}

void Api_setCellText(int x, int y, char* str) {
    char cmd[15];
    snprintf(cmd, 15, "st %d %d %s", x % 100, y % 100, str);
    pushToHistory(cmd);
}

// Stop simulation
void Api_stopSimulation() {
    request("ss");
};