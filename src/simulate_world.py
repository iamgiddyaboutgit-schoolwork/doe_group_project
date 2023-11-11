#!/usr/bin/env python3
"""This script runs a simulation and writes the results to disk.
"""
from pathlib import Path
import os
import argparse

import networkx as nx
from pyvis.network import Network

PARENT_PATH = Path(__file__).resolve().parents[1]

def main():
    ...

def get_user_args() -> argparse.Namespace:
    """Get arguments from the command line and validate them."""
    parser = argparse.ArgumentParser()
    # Optional arguments are prefixed by single or double dashes.
    # The remaining arguments are positional.
    parser.add_argument("-o", required=True, \
        help="path to the output file")
    parser.add_argument(
        "--kdno", 
        required=False,
        help="The old kernelspec display name. DEFAULT: Python [conda env:root] *"
    )
    parser.add_argument(
        "--kdnn", 
        required=False,
        help="The new kernelspec display name. DEFAULT: Python (all_of_us)"
    )
    parser.add_argument(
        "--kno", 
        required=False,
        help="The old kernelspec name. DEFAULT: conda-root-py"
    )
    parser.add_argument(
        "--knn", 
        required=False,
        help="The new kernelspec name. DEFAULT: all_of_us"
    )
    parser.add_argument(
        "--pvo", 
        required=False,
        help="The old Python version. DEFAULT: 3.7.12"
    )
    parser.add_argument(
        "--pvn", 
        required=False,
        help="The new Python version. DEFAULT: 3.12.0"
    )

    args = parser.parse_args()

    return args

def get_simulation_results():
    ...

def write_simulation_results():
    ...





if __name__ == "__main__":
    main()