#include <stdio.h>

int main() {
    int n, m, i, j;
    
    printf("Enter number of processes: ");
    scanf("%d", &n);
    
    printf("Enter number of resources: ");
    scanf("%d", &m);
    
    int max[n][m], alloc[n][m], need[n][m], avail[m];
    int finish[n], safeSeq[n];
    
    // Input Allocation Matrix
    printf("Enter Allocation Matrix:\n");
    for(i = 0; i < n; i++) {
        printf("Process %d: ", i+1);
        for(j = 0; j < m; j++) {
            scanf("%d", &alloc[i][j]);
        }
    }
    
    // Input Maximum Matrix
    printf("Enter Maximum Matrix:\n");
    for(i = 0; i < n; i++) {
        printf("Process %d: ", i+1);
        for(j = 0; j < m; j++) {
            scanf("%d", &max[i][j]);
            need[i][j] = max[i][j] - alloc[i][j]; // Calculate need
        }
        finish[i] = 0; // initially not finished
    }
    
    // Input Available resources
    printf("Enter Available resources: ");
    for(i = 0; i < m; i++) {
        scanf("%d", &avail[i]);
    }
    
    // Banker's Safety Algorithm
    int count = 0;
    while(count < n) {
        int found = 0;
        for(i = 0; i < n; i++) {
            if(finish[i] == 0) {
                int canAllocate = 1;
                for(j = 0; j < m; j++) {
                    if(need[i][j] > avail[j]) {
                        canAllocate = 0;
                        break;
                    }
                }
                if(canAllocate) {
                    // process can be allocated
                    for(j = 0; j < m; j++)
                        avail[j] += alloc[i][j]; // release resources
                    safeSeq[count++] = i+1;
                    finish[i] = 1;
                    found = 1;
                }
            }
        }
        if(!found) break; // no process could be allocated, unsafe
    }
    
    int safe = 1;
    for(i = 0; i < n; i++) {
        if(finish[i] == 0) {
            safe = 0;
            break;
        }
    }
    
    if(safe) {
        printf("\nSystem is in a SAFE state.\nSafe sequence: ");
        for(i = 0; i < n; i++) {
            printf("P%d ", safeSeq[i]);
        }
        printf("\n");
    } else {
        printf("\nSystem is in an UNSAFE state.\n");
    }

    return 0;
}

