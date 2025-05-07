#!/usr/bin/env python3
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='update_version',
                    description='What the program does',
                    epilog='Text at the bottom of help')

    parser.add_argument('new_version')
    args = parser.parse_args()
    print(args.new_version)

