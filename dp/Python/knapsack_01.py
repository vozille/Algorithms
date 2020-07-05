def knapsack_01(weights: list, values: list, target_weight: int):
    dp = [[0 for _ in range(target_weight + 1)] for _ in range(len(values) + 1)]

    for i in range(len(values) + 1):
        for weight in range(target_weight + 1):
            if i == 0 or weight == 0:
                continue
            if weights[i - 1] <= weights:
                dp[i][weight] = max(dp[i - 1][weight], values[i - 1] + dp[i - 1][ - weights[i - 1]])
            else:
                dp[i][weight] = dp[i - 1][weight]

    return dp
