#include <float.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

struct node
{
    int          payload;
    struct node* next_ptr;
};

struct node* create_list_of_N(unsigned int n) {
    if(n == 0) {
        return (struct node*)0;
    }
    struct node* head   = calloc(1, sizeof(*head));
    struct node* walker = head;
    for(int x = 0; x < n - 1; x++) {
        walker->next_ptr = calloc(1, sizeof(*head));
        walker           = walker->next_ptr;
    }
    return head;
}

struct node* create_list_from_array(unsigned int n, int array[]) {
    if(n == 0) {
        return (struct node*)0;
    }
    struct node* head   = calloc(1, sizeof(*head));
    struct node* walker = head;
    head->payload       = array[0];
    for(int x = 1; x < n; x++) {
        walker->next_ptr = calloc(1, sizeof(*head));
        walker           = walker->next_ptr;
        walker->payload  = array[x];
    }
    return head;
}

bool is_list_sorted(struct node* head) {
    struct node* follower = head;
    for(struct node* walker = head->next_ptr; walker != 0; walker = walker->next_ptr) {
        if(follower->payload > walker->payload) {
            return false;
        }
        follower = walker;
    }
    return true;
}
struct node* bubble_sort_list(struct node* head) {
    bool is_sorted = false;
    while(!is_sorted) {
        is_sorted             = true;
        struct node* follower = head;
        for(struct node* walker = head->next_ptr; walker != 0; walker = walker->next_ptr) {
            if(follower->payload > walker->payload) {
                // Not garuanteed to be sorted
                is_sorted = false;
                // Swap the pair
                int tmp           = follower->payload;
                follower->payload = walker->payload;
                walker->payload   = tmp;
            }
            follower = walker;
        }
    }
    return head;
}

struct node* bubble_sort_list2(struct node* head) {
    bool is_sorted = false;
    while(!is_sorted) {
        struct node* follower = head;
        is_sorted = true;
        for(struct node* leader = head->next_ptr; follower->next_ptr != 0; leader = leader->next_ptr) {
            if (follower->payload > leader->payload) {
                is_sorted = false;
                int tmp = leader->payload;
                leader->payload = follower->payload;
                follower->payload = tmp;
            }
            follower = follower->next_ptr;
        }

    }
    return head;
}

void print_list(struct node* head) { // Print list
    for(struct node* walker = head; walker != 0; walker = walker->next_ptr) {
        printf("%zX\t -> ", (size_t)walker);
    }

    printf("NULL\n");
    for(struct node* walker = head; walker != 0; walker = walker->next_ptr) {
        printf("%d\t -> ", walker->payload);
    }
    printf("NULL\n");
}

int main() {
    printf("List Program\n");

    // struct node* head = calloc(1, sizeof(*head));
    // head->payload = 8;
    // printf("%d\n", head->payload);

    // TODO:
    // 1. Create a linked list of size N
    // 2. Convert an array of N integers into a linked list of N
    // 3. Drop an element at index i < N
    // 4. Sort the list using bubble sort
    // 5. Sort the list using insertion sort
    // 6. Sort the list using selection sort
    // 7. Unions: Understand the difference between structures and unions
    // 8. Enumerations: Declaring and using enum

    printf("\nCreate a list of size {4}\n");
    {
        struct node* head = create_list_of_N(4);
        print_list(head);
    }

    printf("\nCreate a list of size {4} with values [45, 23, 190, 1]\n");
    {
        int          array[] = {45, 23, 190, 1};
        struct node* head    = create_list_from_array(4, array);
        print_list(head);
        printf("\nSort list with bubble sort\n");
        bubble_sort_list(head);
        print_list(head);
    }
    printf("\nCreate a list of size {8} with values [45, 23, 190, 1, 142, 17, 36, 72]\n");
    {
        int          array[] = {45, 23, 190, 1, 142, 17, 36, 72};
        struct node* head    = create_list_from_array(8, array);
        print_list(head);
        printf("\nSort list with bubble sort 2\n");
        bubble_sort_list2(head);
        print_list(head);
    }

    printf("\n\nExiting");
    return 0;
}