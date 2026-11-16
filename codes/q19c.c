#include <stdio.h>

int main() {
    double lines[5][3] = {
        {1.0, 0.0, 0.0},
        {0.0, 1.0, 0.0},
        {1.0, 2.0, 10.0},
        {2.0, 2.0, 12.0},
        {3.0, 1.0, 8.0}
    };

    double min_cost = 1e9;
    double best_x = 0.0, best_y = 0.0;

    for (int i = 0; i < 5; i++) {
        for (int j = i + 1; j < 5; j++) {
            double det = lines[i][0] * lines[j][1] - lines[i][1] * lines[j][0];
            if (det == 0.0) continue;

            double x = (lines[i][2] * lines[j][1] - lines[i][1] * lines[j][2]) / det;
            double y = (lines[i][0] * lines[j][2] - lines[i][2] * lines[j][0]) / det;

            int feasible = 1;
            if (x < -1e-7 || y < -1e-7) feasible = 0;

            for (int k = 2; k < 5; k++) {
                if (lines[k][0] * x + lines[k][1] * y < lines[k][2] - 1e-7) {
                    feasible = 0;
                    break;
                }
            }

            if (feasible) {
                double cost = 6.0 * x + 10.0 * y;
                if (cost < min_cost) {
                    min_cost = cost;
                    best_x = x;
                    best_y = y;
                }
            }
        }
    }

    printf("Optimal Diet Mixture: Food X = %.2f kg, Food Y = %.2f kg\n", best_x, best_y);
    printf("Minimum Cost: Rs. %.2f\n", min_cost);

    return 0;
}
