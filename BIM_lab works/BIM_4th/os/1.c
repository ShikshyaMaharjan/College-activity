#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t pid;

    pid = getpid(); // Get current process ID

    printf("HELLO WORLD,process ID (PID) : %d\n", pid);

    return 0;
}

