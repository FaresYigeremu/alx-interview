#!/usr/bin/python3
"""
Define isWinner function, a solution to the Prime Game problem
"""


def primes(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    prime = []  # List to store prime numbers
    sieve = [True] * (n + 1)  # Boolean array to mark prime numbers
    for p in range(2, n + 1):
        if (sieve[p]):  # If p is a prime number
            prime.append(p)  # Add p to the list of primes
            for i in range(p, n + 1, p):
                sieve[i] = False  # Mark multiples of p as non-prime
    return prime


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None

    Maria = Ben = 0  # Initialize scores for Maria and Ben

    for i in range(x):  # Loop through each round
        prime = primes(nums[i])  # Get the list of primes for the current round
        if len(prime) % 2 == 0:  # If the number of primes is even
            Ben += 1  # Ben wins this round
        else:
            Maria += 1  # Maria wins this round

    if Maria > Ben:
        return 'Maria'  # Maria is the overall winner
    elif Ben > Maria:
        return 'Ben'  # Ben is the overall winner
    return None  # Return None if the game is a tie
