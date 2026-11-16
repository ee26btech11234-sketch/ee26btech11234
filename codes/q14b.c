#include <stdio.h>
#include <math.h>

int main() {
    // --- Part (a): Projectile Motion Grazing Two Walls ---
    double h = 10.0;
    double x1 = 15.0, x2 = 45.0;

    // From 1 - x1/R = (x2/x1)*(1 - x2/R) => R = x1 + x2
    double R = x1 + x2;
    double tan_theta = h / (x1 * (1.0 - x1 / R));
    double theta_rad = atan(tan_theta);
    double theta_deg = theta_rad * (180.0 / M_PI);

    printf("--- Question 14(a) ---\n");
    printf("Horizontal Range (R): %.2f m\n", R);
    printf("tan(theta): %.4f (8/9 = %.4f)\n", tan_theta, 8.0 / 9.0);
    printf("Angle of Projection (theta): %.4f rad (%.2f deg)\n\n", theta_rad, theta_deg);

    // --- Part (b): Partnership Profit Sharing ---
    double k[3] = {400000.0, 600000.0, 1000000.0};
    double t[3] = {12.0, 9.0, 6.0};
    double c[3], p[3];
    double total_profit = 540000.0;
    double sum_c = 0.0;

    for (int i = 0; i < 3; i++) {
        c[i] = k[i] * t[i];
        sum_c += c[i];
    }

    char partners[3] = {'A', 'B', 'C'};
    printf("--- Question 14(b) ---\n");
    for (int i = 0; i < 3; i++) {
        p[i] = (total_profit / sum_c) * c[i];
        printf("Share of %c: Rs. %.2f\n", partners[i], p[i]);
    }

    return 0;
}
