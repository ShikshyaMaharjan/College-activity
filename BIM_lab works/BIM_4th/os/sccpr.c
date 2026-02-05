#include <stdio.h>

int main() {
    int frames, pagesCount, i, j, pageFaults = 0, pointer = 0;
    printf("Enter number of frames: ");
    scanf("%d", &frames);

    int frame[frames], referenceBit[frames];
    for (i = 0; i < frames; i++) {
        frame[i] = -1;          // initialize frames as empty
        referenceBit[i] = 0;    // all reference bits = 0
    }

    printf("Enter number of pages: ");
    scanf("%d", &pagesCount);

    int pages[pagesCount];
    printf("Enter page reference string: ");
    for (i = 0; i < pagesCount; i++)
        scanf("%d", &pages[i]);

    // Simulation
    for (i = 0; i < pagesCount; i++) {
        int page = pages[i];
        int found = 0;

        // Check if page already in frame
        for (j = 0; j < frames; j++) {
            if (frame[j] == page) {
                referenceBit[j] = 1;  // give second chance
                found = 1;
                break;
            }
        }

        if (!found) {
            // Page Fault occurs
            while (1) {
                if (referenceBit[pointer] == 0) {
                    frame[pointer] = page;   // replace
                    referenceBit[pointer] = 1;
                    pointer = (pointer + 1) % frames;
                    pageFaults++;
                    break;
                } else {
                    referenceBit[pointer] = 0;  // give second chance
                    pointer = (pointer + 1) % frames;
                }
            }
        }

        // Print current status
        printf("Page %d -> ", page);
        for (j = 0; j < frames; j++) {
            if (frame[j] == -1)
                printf("- ");
            else
                printf("%d ", frame[j]);
        }
        printf("\n");
    }

    printf("\nTotal Page Faults = %d\n", pageFaults);

    return 0;
}

