#!/usr/bin/env python3
"""Extract ASVs from a fasta file based on a list of taxon IDs."""

import argparse
import sys
from Bio import SeqIO

parser = argparse.ArgumentParser(
    description="Extract UNITE sh sequences based on taxonomic group"
)
parser.add_argument(
    "-i",
    "--input",
    type=argparse.FileType("r"),
    nargs="?",
    default=sys.stdin,
    help="Input fasta file with an ID and description that is qiime taxonomy string",
)

parser.add_argument(
    "-o",
    "--output",
    nargs="?",
    type=argparse.FileType("w"),
    default=sys.stdout,
    help="Write FASTA output to filename or stdout by default",
)

parser.add_argument(
    "--query",
    type=str,
    nargs="+",
    default="k__Fungi",
    help="Input taxon string to search",
)

args = parser.parse_args()

inhandle = args.input

# open the fasta file to parse out the sequences
# matching taxonomic group
for record in SeqIO.parse(inhandle, "fasta"):
    (id, taxon_string) = record.description.split(" ", 2)
    taxon_list = taxon_string.split(";")
    seen = set()
    for taxon in taxon_list:
        for q in args.query:
            if q in taxon:
                if id not in seen:
                    seen.add(id)
                    SeqIO.write(record, args.output, "fasta")
