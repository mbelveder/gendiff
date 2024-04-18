import argparse
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '-f', '--format', help='set format of output', default='stylish'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()

    diff = generate_diff(
        file_path1=args.first_file,
        file_path2=args.second_file,
        formatter=args.format
    )

    # with open('tests/fixtures/nested_diff_result.txt', 'w') as f:
    #     f.write(diff)

    return diff


if __name__ == "__main__":
    main()
