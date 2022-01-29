#!/usr/bin/env python3


def main(msg="Hello, World!"):
    print(f"\x1b[32m{msg}\x1b[0m")


if __name__ == '__main__':
    args = __import__('sys').argv[1:]
    if len(args) >= 1:
        args = ' '.join(args)
    if args:
        main(args)
    else:
        main()
