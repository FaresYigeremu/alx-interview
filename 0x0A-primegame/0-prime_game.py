#!/usr/bin/python3
def isWinner(x, nums):
    # o generate prime numbers up to n using the Sieve of Eratosthenes
    def sieve_of_eratosthenes(n):
        primes = [True] * (n + 1)
        primes[0], primes[1] = False, False  # 0 and 1 are not prime numbers
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [i for i in range(2, n + 1) if primes[i]]

    # Function to simulate the game for a given n
    def play_game(n):
        primes = sieve_of_eratosthenes(n)
        numbers = set(range(1, n + 1))
        turn = 0  # Maria starts first (0 for Maria, 1 for Ben)
        while primes:
            # Maria or Ben picks the first available prime
            prime = primes.pop(0)
            # Remove the prime and its multiples
            numbers -= set(range(prime, n + 1, prime))
            # Recalculate the primes for the remaining numbers
            primes = [p for p in sieve_of_eratosthenes(n) if p in numbers]
            # Switch turns
            turn = 1 - turn

        return "Maria" if turn == 1 else "Ben"

    # Count the number of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # Return the player with the most wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
