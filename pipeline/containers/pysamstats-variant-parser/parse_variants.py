#!/usr/bin/env python
import sys

POS_COL = "pos"
A_COL = "A"
C_COL = "C"
T_COL = "T"
G_COL = "G"
COLUMNS = [POS_COL, A_COL, C_COL, T_COL, G_COL]
COUNT_COLUMNS = [A_COL, C_COL, T_COL, G_COL]

VARIANT_FILE_DELIMITER = "\t"  # The delimiting character of the input variant file


ALLELES = "alleles"
NUCLEOTIDE = "nt"
COUNT = "ct"


def error(msg):
    """Writes error and exits
    """
    print("ERROR: " + msg)
    sys.exit()


def get_column_positions(header):
    """ Returns object mapping column value to its index
    :param header: string
    :return: { "col": idx, ... }
    """
    # Split on any whitespace
    columns = header.split(VARIANT_FILE_DELIMITER)
    for col in COLUMNS:
        if col not in columns:
            error("File did not container headers: %s" % str(COLUMNS))

    # Object of nucleotide indices, e.g. { "A": 11, "C": 13, "T": 15, "G": 17 }
    column_indices = map(lambda field: columns.index(field), COLUMNS)

    value_indices = {}
    for val, idx in zip(COLUMNS, column_indices):
        value_indices[val] = idx

    return value_indices


def create_af_entry(column_positions, line):
    """ Creates an object containing the allele frequency information at a genomic position

    :param column_positions: Object containing indices of important columns
    :param line:
    :return: {
        "pos": int,
        "alleles": [
            {
                "Nucleotide": "A/C/G/T",
                "count": int
            }
        ]
    }
    """
    pass


def parse_column_values(value_lines, column_positions):
    """ Returns the values for all @value_lines
    :param value_lines: String[]
    :return: { "col": String[], ... }
    """
    column_values = {}
    for key in column_positions.keys():
        column_values[key] = []

    for line in value_lines:
        values = line.split(VARIANT_FILE_DELIMITER)
        for col, idx in column_positions.items():
            try:
                column_values[col].append(values[idx])
            except IndexError:
                print(values)

    return column_values


def parse_variant_file(variant_file):
    """ Returns list of allele-frequency objects parsed from input @variant_file
    :param variant_file:
    :return: [
        {
            "pos": int,
            "alleles": [
                {
                    "nt": "A/G/C/T",
                    "ct": int
                },
                ...
            ]
        }
    ]
    """
    reader = open(variant_file, "r")
    contents = reader.read()
    lines = contents.strip("\n").split("\n")

    if len(lines) < 2:
        error("Empty or invalid file")

    header = lines[0]
    value_lines = lines[1:]

    allele_frequencies = []

    column_positions = get_column_positions(header)
    column_values = parse_column_values(value_lines, column_positions)
    positions = column_values[POS_COL]
    for idx, val in enumerate(positions):
        af_entry = {
            POS_COL: int(val),
            ALLELES: []
        }
        for col in COUNT_COLUMNS:
            ct = int(column_values[col][idx])
            if ct > 0:
                ct_entry = {NUCLEOTIDE: col, COUNT: ct}
                af_entry[ALLELES].append(ct_entry)
        allele_frequencies.append(af_entry)

    return allele_frequencies


def write_file(file_name, contents):
    """ Writes @contents to @file_name
    :param file_name:
    :param contents:
    :return:
    """
    merge_commands_file = open(file_name, "a")
    merge_commands_file.truncate(0)  # Delete any old data
    merge_commands_file.write(contents)
    merge_commands_file.close()


if __name__ == '__main__':
    if len(sys.argv) < 2 or ".variation" not in sys.argv[1]:
        print("Missing variant file. Usage is 'python parse_variants.py [VARIANT_FILE]")
        sys.exit()
    VARIANT_FILE = sys.argv[1]
    OUTPUT_FILE = "parsed_variants.txt"
    if len(sys.argv) == 3:
        OUTPUT_FILE = sys.argv[2]

    parsed_contents = parse_variant_file(VARIANT_FILE)

    print("Writing to %s" % OUTPUT_FILE)
    write_file(OUTPUT_FILE, str(parsed_contents))
