#include <stdio.h>

float branch_test(int x) {
    float result = 0.0;
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
    float a = 10.5, b = 5.9;
    float total = 0.0;

    // Simple arithmetic operation on int
    float sum = a + b;
    float diff = a - b;

    printf("Sum: %f, Difference: %f \n", sum, diff);

    // Branching operations
    for (int i = 0; i < 100; i++) {
        total += branch_test(i);
    }

    printf("Total: %f\n", total);
    return 0;
}