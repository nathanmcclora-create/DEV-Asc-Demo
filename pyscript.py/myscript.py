#!/usr/bin/env python3

"""Basic Python script scaffold."""
# Copyright (c) 2024, Your Name
# All rights reserved. making changes for demo

import sys


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    print("Hello from myscript.py")
    print(f"Arguments: {argv}")


if __name__ == "__main__":
    main()

    print("Done.")
    print("Exiting with code 0.")
