#include <stdio.h>

int main() {
    int n, frames, i, j, pointer = 0, pageFaults = 0, flag;
    
    printf("Enter number of pages: ");
    scanf("%d", &n);
    
    int pages[n];
    printf("Enter page reference sequence: ");
    for(i = 0; i < n; i++)
        scanf("%d", &pages[i]);
    
    printf("Enter number of frames: ");
    scanf("%d", &frames);
    
    int frameArr[frames], refBit[frames];
    for(i = 0; i < frames; i++) {
        frameArr[i] = -1;   // initialize frames
        refBit[i] = 0;      // initialize reference bits
    }
    
    printf("\nPage\tFrames\n");
    
    for(i = 0; i < n; i++) {
        flag = 0;
        
        // Check if page is already in frame
        for(j = 0; j < frames; j++) {
            if(frameArr[j] == pages[i]) {
                refBit[j] = 1; // give second chance
                flag = 1;      // page hit
                break;
            }
        }
        
        if(flag == 0) { // page fault
            while(refBit[pointer] == 1) {
                refBit[pointer] = 0;       // give second chance
                pointer = (pointer + 1) % frames;
            }
            frameArr[pointer] = pages[i]; // replace page
            refBit[pointer] = 0;
            pointer = (pointer + 1) % frames;
            pageFaults++;
        }
        
        // Print current state of frames
        printf("%d\t", pages[i]);
        for(j = 0; j < frames; j++) {
            if(frameArr[j] != -1)
                printf("%d ", frameArr[j]);
            else
                printf("- ");
        }
        printf("\n");
    }
    
    printf("\nTotal Page Faults: %d\n", pageFaults);
    return 0;
}

