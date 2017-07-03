"""Sorts a CSV file by a specified value, prints results in new CSV file."""
import argparse
import csv
import operator


def sort_file(input_file, sort_by):
    sorted_list = sorted(input_file, key=operator.itemgetter(sort_by))
    return sorted_list


def write_sorted_csv(field_names, rows, output_file_name):
    output_file = csv.DictWriter(
        open(output_file_name, 'w'), field_names
    )
    output_file.writeheader()
    for row in rows:
        output_file.writerow(row)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i',
        '--input_file',
        type=str,
        required=True,
        help='The csv file you would like to sort.'
    )
    parser.add_argument(
        '-s',
        '--sort_by',
        type=str,
        required=True,
        help='The value you would like to sort your csv file by.'
    )
    parser.add_argument(
        '-o',
        '--output_file_name',
        type=str,
        default='new.csv',
        help='Name of new sorted csv. Set to new.csv by default.'
    )
    args = parser.parse_args()
    input_file = csv.DictReader(open(args.input_file, 'r'))
    field_names = input_file.fieldnames
    transactions = sort_file(input_file, args.sort_by)

    write_sorted_csv(field_names, transactions, args.output_file_name)


if __name__ == '__main__':
    main()
