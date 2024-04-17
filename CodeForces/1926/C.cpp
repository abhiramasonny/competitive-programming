#include <iostream>
#include <vector>

int sum_of_digits(int n) {
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int calculate_total_sum(int n, std::vector<int>& memo) {
    int total_sum = 0;
    for (int i = 1; i <= n; i++) {
        total_sum += memo[i];
    }
    return total_sum;
}

int main() {
    std::vector<int> memo(1000001, 0);

    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; i++) {
        int n;
        scanf("%d", &n);
        printf("%d\n", calculate_total_sum(n, memo));
    }

    return 0;
}
