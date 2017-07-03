# CSV Sorter

This simple program takes an input csv, sorts by a specified value, and outputs a new csv with the sorted values.

## Basic usage

To run, download sorter.py, and `cd` into the directory that you've stored it in, and run the following command:

```python sorter.py --input_file names.csv --sort_by first_name```

This will output the values in names.csv, sorted by the value first_name, to a new file (named new.csv by default).

Note that the sorted csv will be in ascending order. So depending on what data type you've sorted by, it'll start at 1, or A, or the earliest date - you get the idea :)

### Argument key

| Argument | Shorthand | Required? | Input type | Description | Example |
| -------- | --------- | --------- | ---------- | ----------- | ------- |
| --input_file | -i | Yes | string | The path to & name of the input file you would like to sort. | `-i names.csv` |
| --sort_by | -s | Yes | string | The value you wish to sort by, exact as written in the input csv. | `-s first_name` |
| --output_file | -o | No | string | The path to & name you wish to assign to the output file | `-o sorted_groups.csv` |
