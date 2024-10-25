#include <stdio.h>

int branch_test(int x) {
    int result = 0;
    for (int i = 0; i < 100; i++) {
        if (x % 2 == 0) {
            result += x * i;
        } else {
            result += x - i;
        }
    }
    return result;
}

int main()
{
    // Assigning value to a variable
    int a = 10, b = 5;
    int total = 0;

    // Simple arithmetic operation on int
    int sum = a + b;
    int diff = a - b;

    printf("Sum: %d, Difference: %d \n", sum, diff);

    // Branching operations
    for (int i = 0; i < 100; i++) {
        total += branch_test(i);
    }

    printf("Total: %d\n", total);
    return 0;
}