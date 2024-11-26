def makeChange(coins, total):
    """Returns the fewest number of coins needed to make a total."""
    # If total is less than or equal to 0, return 0
    if total <= 0:
        return 0

    # Create a DP array, initialized to infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins needed to make total 0

    # Iterate over each coin
    for coin in coins:
        for i in range(coin, total + 1):
            # check if using this coin reduces the number of coins
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it's not possible to form the total
    return dp[total] if dp[total] != float('inf') else -1
