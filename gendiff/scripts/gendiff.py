import argparse
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '-f', '--format', help='set format of output',
        default='stylish', type=str
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-r', '--replacer', help='only works with stylish (default) output',
        default=' ', type=str
    )
    parser.add_argument(
        '-i', '--increment', help='only works with stylish (default) output',
        default=4, type=int
    )
    args = parser.parse_args()

    if args.format != 'stylish' and (args.replacer != ' ' or args.increment != 4):
        raise ValueError(
            "The --replacer and --increment flags can only be used"
            "with the default --format argument (stylish)"
        )

    diff = generate_diff(
        file_path1=args.first_file,
        file_path2=args.second_file,
        formatter=args.format,
        replacer=args.replacer,
        increment=args.increment
    )

    # with open('tests/fixtures/nested_diff_result.txt', 'w') as f:
    #     f.write(diff)

    print(diff)


if __name__ == "__main__":
    main()
