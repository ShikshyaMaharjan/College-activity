#include <stdio.h>

int main() {
    int n, i, j, temp;
    printf("Enter the number of processes: ");
    scanf("%d", &n);

    int burstTime[n], priority[n], waitingTime[n], 
	turnaroundTime[n], process[n];
    float totalWT = 0, totalTAT = 0;

    for(i = 0; i < n; i++) {
        process[i] = i + 1;
        printf("Enter process %d (burst time priority): ", i + 1);
        scanf("%d %d", &burstTime[i], &priority[i]);
    }

    // Sorting processes based on priority (lower number = higher priority)
    for(i = 0; i < n-1; i++) {
        for(j = i+1; j < n; j++) {
            if(priority[i] > priority[j]) {
                // Swap priority
                temp = priority[i];
                priority[i] = priority[j];
                priority[j] = temp;

                // Swap burst time
                temp = burstTime[i];
                burstTime[i] = burstTime[j];
                burstTime[j] = temp;

                // Swap process number
                temp = process[i];
                process[i] = process[j];
                process[j] = temp;
            }
        }
    }

    // Waiting time for first process is 0
    waitingTime[0] = 0;

    // Calculate waiting time
    for(i = 1; i < n; i++) {
        waitingTime[i] = waitingTime[i-1] + burstTime[i-1];
    }

    // Calculate turnaround time
    for(i = 0; i < n; i++) {
        turnaroundTime[i] = waitingTime[i] + burstTime[i];
        totalWT += waitingTime[i];
        totalTAT += turnaroundTime[i];
    }

    printf("\nProcess\tBurst Time\tPriority\tWaiting Time\tTurnaround Time\n");
    for(i = 0; i < n; i++) {
        printf("P%d\t%d\t\t%d\t\t%d\t\t%d\n", process[i],
		 burstTime[i], 
		priority[i], waitingTime[i], turnaroundTime[i]);
    }

    printf("\nAverage Waiting Time = %.2f", totalWT / n);
    printf("\nAverage Turnaround Time = %.2f\n", totalTAT / n);

    return 0;
}

