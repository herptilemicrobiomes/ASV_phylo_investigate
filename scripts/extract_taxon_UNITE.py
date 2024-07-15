#!/usr/bin/env python3
"""A short parser to extract UNITE SH sequences based on taxonomic group."""
import argparse
import sys
from Bio import SeqIO

parser = argparse.ArgumentParser(
    description="Extract UNITE sh sequences based on taxonomic group"
)
parser.add_argument(
    "-i",
    "--unite",
    type=argparse.FileType("r"),
    nargs="?",
    default=sys.stdin,
    help="Input UNITE fasta file, e.g. 'sh_general_release_dynamic_s_all_29.11.2022_dev.fasta'",
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
    "-q",
    "--query",
    nargs="+",
    default=["k__Fungi"],
    help="Input taxon string to search",
)

args = parser.parse_args()

inUNITE = args.unite

# open the UNITE fasta file to parse out the sequences
# matching taxonomic group
for record in SeqIO.parse(inUNITE, "fasta"):
    id_string = record.id
    id_list = id_string.split("|")
    SH_species_name = id_list[0]
    accession = id_list[1]
    SH_ID = id_list[2]
    SH_type = id_list[3]
    taxon_string = id_list[4]
    taxon_list = taxon_string.split(";")
    seen = set()
    for taxon in taxon_list:
        for q in args.query:
            if q in taxon:
                if SH_ID not in seen:
                    seen.add(SH_ID)
                    record.id = f"{SH_species_name}__{accession}"
                    record.description = (
                        record.id + f" {SH_ID}|{SH_type}|{taxon_string}"
                    )
                    SeqIO.write(record, args.output, "fasta")
