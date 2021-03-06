"""
Compute the GC content and report the sequence with the highest content

Author: Dominique Massau
"""

# imports
from sys import argv


# functions
def parse_fasta(file_name: str) -> dict:
    """
    Parse a fasta file into a dictionary

    :param file_name: str, name of the fasta file
    :return: dict, contains fasta header: DNA sequence
    """

    with open(file_name, 'r') as lines:
        fasta_dict = {}
        for line in lines:
            if line.startswith('>'):
                current_header = line.strip('>').strip()
                fasta_dict[current_header] = []
            else:
                fasta_dict[current_header].append(line.strip().lower())

    for header, seq in fasta_dict.items():
        fasta_dict[header] = ''.join(seq)
    return fasta_dict


def calculate_gc_content(fasta_dict: dict) -> list:
    """
    Calculate the GC percentage for every fasta sequence

    :param fasta_dict:
    :return: list, contains tuple with fasta header, GC perc
    """

    gc_perc_list = []
    for header, seq in fasta_dict.items():
        gc_perc_list.append((header, (seq.count('c') + seq.count('g'))
                             / len(seq) * 100))
    return gc_perc_list


def highest_gc_perc(gc_perc_list: list):
    """
    Reports the header of the sequence with the largest GC percentage

    :param gc_perc_list: list, contains tuple with fasta header, GC perc
    """

    highest_gc_fasta = sorted(gc_perc_list, key=lambda tup: tup[1])[-1]
    print("{}\n{:.6f}".format(highest_gc_fasta[0], highest_gc_fasta[1]))


if __name__ == "__main__":
    fasta_seqs = parse_fasta(argv[1])
    gc_perc_list = calculate_gc_content(fasta_seqs)
    highest_gc_perc(gc_perc_list)
