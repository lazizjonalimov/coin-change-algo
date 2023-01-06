maxint = int(1e9 + 7)


def make_change_dp(denoms, n, S):
    resulted_coins = list()
    all_coins = list()
    if S == 0:
        return 0
    coin = 0
    resulted_coins.append(0)
    i = 1
    for i in range(S + 1):
        resulted_coins.append(maxint)
        for j in range(n):
            # If denominations is less than i, then set the current count
            if denoms[j] <= i:

                curr_count = resulted_coins[i - denoms[j]]
                # If the current count is not maxint, and it is less than ith index of resulted coins
                if curr_count != maxint and curr_count + 1 < resulted_coins[i]:
                    # Set the index in that list to the curr + 1
                    resulted_coins[i] = curr_count + 1
                    coin = j

        all_coins.append(coin)

    print(all_coins)

    if resulted_coins[S] == maxint:
        return None

    else:
        return resulted_coins[S]


if __name__ == '__main__':
    coins = [1, 10, 25]
    V = 30
    size = len(coins)
    print(make_change_dp(coins, size, V))

