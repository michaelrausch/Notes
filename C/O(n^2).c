/*
    O(n^2) sorting algorithm.
    Performs the sort on the one list to save space.
    Not an inplace sort.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void swap_indexes(int *list, int i_one, int i_two) {
    int temp = list[i_one];
    list[i_one] = list[i_two];
    list[i_two] = temp;
}

int* sort(int *unsorted, int len) {
     int *sorted = malloc(len * sizeof(int));
     memcpy(sorted, unsorted, len * sizeof(int));
     
    for (int place = 0; place < len; place++) {
        int smallest_index = place;
        int smallest_num = sorted[place];
        
        for(int i = place; i < len; i++) {
            if(sorted[i] < smallest_num){
                smallest_index = i;
                smallest_num = sorted[i];
            }
        }
        swap_indexes(sorted, place, smallest_index);
    }
    
    return sorted;
}

int main() {
    int len = 5;
    int *unsorted = malloc(len * sizeof(int));
    for (int i = 0; i < len; i++) {
        unsorted[i] = 4 - i;
    }
    
    int* sorted = sort(unsorted, len);
    
    for(int i = 0; i < len; i++){
        printf("%d\n", sorted[i]);
    }
    return 0;
}
