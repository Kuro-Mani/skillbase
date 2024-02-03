def count_primes_up_to_n(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0と1は素数ではない

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False

    return sum(primes)

lower_limit = 0
upper_limit = 1073741823

count_of_primes = count_primes_up_to_n(upper_limit)
print(f"0から{upper_limit}までの範囲内には{count_of_primes}個の素数があります。")
