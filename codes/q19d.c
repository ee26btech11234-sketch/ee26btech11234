#include <stdio.h>

int main() {
    double lines[5][3] = {
        {1.0, 0.0, 0.0},
        {0.0, 1.0, 0.0},
        {12.0, 6.0, 360.0},
        {18.0, 0.0, 360.0},
        {6.0, 9.0, 360.0}
    };

    double max_profit = -1.0;
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
                if (lines[k][0] * x + lines[k][1] * y > lines[k][2] + 1e-7) {
                    feasible = 0;
                    break;
                }
            }

            if (feasible) {
                double profit = 0.75 * x + 0.50 * y;
                if (profit > max_profit) {
                    max_profit = profit;
                    best_x = x;
                    best_y = y;
                }
            }
        }
    }

    printf("Optimal Production: Type A = %.0f cups, Type B = %.0f cups\n", best_x, best_y);
    printf("Maximum Daily Profit: Rs. %.2f\n", max_profit);

    return 0;
}
