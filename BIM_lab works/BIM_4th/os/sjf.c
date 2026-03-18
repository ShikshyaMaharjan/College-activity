#include <stdio.h>

int main() {
    int n, i, j, temp;
    int burstTime[20], waitingTime[20], 
	turnaroundTime[20], process[20];
    float totalWT = 0, totalTAT = 0;

    printf("Enter the number of processes: ");
    scanf("%d", &n);

    // Input burst time for each process in single line style
    for(i = 0; i < n; i++) {
        process[i] = i + 1; // process numbering
        printf("Process %d: Burst time: ", i + 1);
        scanf("%d", &burstTime[i]);
    }

    // Sorting processes according to burst time (SJF)
    for(i = 0; i < n-1; i++) {
        for(j = i+1; j < n; j++) {
            if(burstTime[i] > burstTime[j]) {
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

    // First process waiting time is 0
    waitingTime[0] = 0;

    // Calculating waiting time
    for(i = 1; i < n; i++) {
        waitingTime[i] = waitingTime[i-1] + burstTime[i-1];
    }

    // Calculating turnaround time
    for(i = 0; i < n; i++) {
        turnaroundTime[i] = waitingTime[i] + burstTime[i];
        totalWT += waitingTime[i];
        totalTAT += turnaroundTime[i];
    }

    // Output
    printf("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time\n");
    for(i = 0; i < n; i++) {
        printf("P%d\t%d\t\t%d\t\t%d\n", process[i],
		 burstTime[i], waitingTime[i], turnaroundTime[i]);
    }

    printf("\nAverage Waiting Time = %.2f", totalWT / n);
    printf("\nAverage Turnaround Time = %.2f\n", totalTAT / n);

    return 0;
}

