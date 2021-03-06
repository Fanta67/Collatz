#!/usr/bin/env python3

# ----------
# Collatz.py
# ----------

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------
# imports
# -------

from typing import IO, List

# ------------
# collatz_read
# ------------


def collatz_read(s: str) -> List[int]:
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]


# ------------
# collatz_eval
# ------------

cache = [0, 1] + [0 for x in range(999998)]


def collatz_eval(i: int, j: int) -> int:
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    global cache

    maxcyclength = 0
    if i > j:
        temp = i
        i = j
        j = temp
    assert i <= j
    assert i >= 0
    assert j >= 0

    # optimization from quiz 4
    if i < j // 2:
        i = j // 2

    for x in range(i, j + 1):
        curr = x
        cyclength = 1

        # already stored in cache
        if cache[curr] != 0:
            cyclength = cache[curr]

        # not in cache yet
        else:
            while curr != 1:

                if curr % 2 == 0:
                    curr //= 2
                else:
                    # optimization from quiz 3
                    curr += (curr << 1) + 1
                    # do 2 steps at once for odd numbers
                    curr //= 2
                    cyclength += 1

                if curr < len(cache) and cache[curr] != 0:
                    cyclength += cache[curr]
                    break

                cyclength += 1

            # lazily fill cache
            cache[x] = cyclength
        assert cyclength > 0

        if cyclength > maxcyclength:
            maxcyclength = cyclength

    assert maxcyclength > 0
    assert maxcyclength >= cyclength
    return maxcyclength


# -------------
# collatz_print
# -------------


def collatz_print(w: IO[str], i: int, j: int, v: int) -> None:
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")


# -------------
# collatz_solve
# -------------


def collatz_solve(r: IO[str], w: IO[str]) -> None:
    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
