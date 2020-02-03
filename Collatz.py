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


def collatz_eval(i: int, j: int) -> int:
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    maxcyclength = 0
    cyclength = 0
    for i in range(i, j + 1):
        curr = i
        cyclength = 1
        while curr != 1:
            if curr % 2 == 0:
                curr /= 2
            else:
                curr *= 3
                curr += 1
            cyclength += 1
        if cyclength > maxcyclength:
            maxcyclength = cyclength
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
