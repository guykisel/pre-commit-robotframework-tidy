from __future__ import print_function

import argparse

from robot.errors import DataError
from robot.tidy import Tidy


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to run')
    parser.add_argument('--use-pipes', action='store_true', dest='use_pipes',
                        default=False)
    parser.add_argument('--space-count', type=int, dest='space_count',
                        default=4)
    args = parser.parse_args(argv)

    tidier = Tidy(use_pipes=args.use_pipes,
                  space_count=args.space_count,
                  format='robot')
    for filename in args.filenames:
        try:
            tidier.inplace(filename)
        except (DataError, OSError):
            pass

    return 0

if __name__ == '__main__':
    exit(main())
