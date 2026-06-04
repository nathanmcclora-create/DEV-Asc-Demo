#!/usr/bin/env python3

"""Basic Python script scaffold."""

import sys


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    print("Hello from myscript.py")
    print(f"Arguments: {argv}")


if __name__ == "__main__":
    main()