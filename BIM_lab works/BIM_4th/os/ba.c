#include <stdio.h>
#include <stdlib.h>

int fifoPageFaults(const int *pages, int n, int frames) {
    int *frame = (int *)malloc(frames * sizeof(int));
    int pageFaults = 0, next = 0;
    int i, j, page, found;

    if (!frame) {
        perror("malloc failed");
        return -1;
    }

    /* Initialize frames to empty */
    for (i = 0; i < frames; i++) {
        frame[i] = -1;
    }

    for (i = 0; i < n; i++) {
        page = pages[i];
        found = 0;

        /* Check hit */
        for (j = 0; j < frames; j++) {
            if (frame[j] == page) {
                found = 1;
                break;
            }
        }

        /* FIFO replace on miss */
        if (!found) {
            frame[next] = page;
            next = (next + 1) % frames;
            pageFaults++;
        }
    }

    free(frame);
    return pageFaults;
}

int main(void) {
    /* Classic sequence that shows Belady's anomaly under FIFO */
    int pages[] = {1,2,3,4,1,2,5,1,2,3,4,5};
    int n = (int)(sizeof(pages) / sizeof(pages[0]));

    int frames1 = 3;
    int frames2 = 4;

    int pf1 = fifoPageFaults(pages, n, frames1);
    int pf2 = fifoPageFaults(pages, n, frames2);

    int i;

    printf("Reference string: ");
    for (i = 0; i < n; i++) printf("%d ", pages[i]);
    printf("\n");

    printf("\nPage Faults with %d frames = %d", frames1, pf1);
    printf("\nPage Faults with %d frames = %d\n", frames2, pf2);

    if (pf2 > pf1) {
        printf("\n=> Belady's Anomaly occurs\n");
    } else {
        printf("\n=> No Belady's Anomaly\n");
    }

    return 0;
}

