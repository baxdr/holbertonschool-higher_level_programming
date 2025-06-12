#!/usr/bin/python3
"""Defines a function that reads a text file and prints it to stdout."""
d = __import__("0-read_file").__doc__


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
