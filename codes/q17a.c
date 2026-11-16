#include <stdio.h>
#include <math.h>

int main() {
    double R = 500.0;        // Annual payment (Rs.)
    double i = 0.15;         // Annual interest rate (15%)
    int n = 12;              // Number of years

    // Using the exact value: (1 + i)^(-n)
    double discount_factor_exact = pow(1.0 + i, -n);
    double pv_exact = R * ((1.0 - discount_factor_exact) / i);

    // Using the given approximation in the problem: (1.15)^(-12) = 1 / 5.35
    double discount_factor_approx = 1.0 / 5.35;
    double pv_approx = R * ((1.0 - discount_factor_approx) / i);

    printf("Present Value (using exact (1.15)^-12 = %.6f): Rs. %.2f\n", discount_factor_exact, pv_exact);
    printf("Present Value (using given 1/5.35 = %.6f):     Rs. %.2f\n", discount_factor_approx, pv_approx);

    return 0;
}
