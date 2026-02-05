#include <stdio.h>

struct Process {
    int id;
    int at; // Arrival Time
    int bt; // Burst Time
    int ct; // Completion Time
    int wt; // Waiting Time
    int tat; // Turnaround Time
    int done; // Completion flag
};

int main() {
    int n, i, completed = 0, time = 0;
    float totalWT = 0, totalTAT = 0;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    struct Process p[n];

    // Input Arrival Times
    for(i = 0; i < n; i++) {
        p[i].id = i + 1;
        printf("Process %d: Arrival time: ", i + 1);
        scanf("%d", &p[i].at);
        p[i].done = 0; // process not completed
    }

    // Input Burst Times
    for(i = 0; i < n; i++) {
        printf("Process %d: Burst time: ", i + 1);
        scanf("%d", &p[i].bt);
    }

    while(completed < n) {
        int idx = -1;
        float hrr = -1;

        for(i = 0; i < n; i++) {
            if(p[i].at <= time && p[i].done == 0) {
                float response_ratio = (float)(time - p[i].a
				t + p[i].bt) / p[i].bt;
                if(response_ratio > hrr) {
                    hrr = response_ratio;
                    idx = i;
                }
            }
        }

        if(idx != -1) {
            // Execute the selected process
            time += p[idx].bt;
            p[idx].ct = time;
            p[idx].tat = p[idx].ct - p[idx].at;
            p[idx].wt = p[idx].tat - p[idx].bt;
            p[idx].done = 1;

            totalWT += p[idx].wt;
            totalTAT += p[idx].tat;
            completed++;
        } else {
            time++; // If no process has arrived, increment time
        }
    }

    // Output
    printf("\nProcess\tArrival\tBurst\tWaiting\tTurnaround\tCompletion\n");
    for(i = 0; i < n; i++) {
        printf("P%d\t%d\t%d\t%d\t%d\t\t%d\n", p[i].id, p[i].at,
		 p[i].bt, p[i].wt, p[i].tat, p[i].ct);
    }

    printf("\nAverage Waiting Time = %.2f", totalWT / n);
    printf("\nAverage Turnaround Time = %.2f\n", totalTAT / n);

    return 0;
}

