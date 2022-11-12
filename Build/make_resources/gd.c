#include <stdio.h>

// Prompt user to enter a double.
// Re-prompt if the input is out of bounds
// Given: prompt (print), min (double) and max (double)
// Returns: the inputted double

double get_double(char *prompt, double min, double max) {
    double input;

    do {
        printf("%s", prompt);
        scanf("%lf", &input);
        if (input < min) printf("Must be at least %lf\n", min);
        if (input > max) printf("Must be at most %lf\n", max);
    }
    while (input < min || input > max);

    return input;
}
