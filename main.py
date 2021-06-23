import sys
import argparse

from MSDialCleaner import MSDialCleaner


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Full path of the file to clean')

    try:
        data = vars(parser.parse_args(args))

        cleaner = MSDialCleaner(data)
        cleaner.run()

    except argparse.ArgumentError as e:
        parser.print_help()
        exit(-1)


if __name__ == '__main__':
    main(sys.argv[1:])
