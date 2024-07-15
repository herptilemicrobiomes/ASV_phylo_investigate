#!/usr/bin/env python3
"""This is a specific script that supported a data format for the UHM project.

The data looked like

	tax.Kingdom	tax.Phylum	tax.Class	tax.Order	tax.Family	tax.Genus	tax.Species
ACAAATGTAATCCAATTACCAACCACACTGTGCACCGTTGAAGTATGCTTTGGCAGGGAGTGAAATGGCGGGAGCCCTCGGGCGCCAGTCTTTCGATCTGCCAGAGTTTTTTAAATACTAAACAAACAAACGTCTTATTATCTGACTGAACTTCATTTAAACAAATGAAAATA	k__Fungi	p__Basidiobolomycota	c__Basidiobolomycetes	o__Basidiobolales	f__Basidiobolaceae	g__Basidiobolus	NA
ACAAATGTAATCCAATTACCAACCACACTGTGCACCGTTGAAGTATGCTTTGGCAGGGAGTGAAATGGCAGGAGCCTCCGGGCGCCAGTCTTTCGATCTGCCAGAGTTTTTTAAATACTAAACAAACAAACGTCTTATTATCTGACTGAACTTCATTTAAACAAATGAAAATA	k__Fungi	p__Basidiobolomycota	c__Basidiobolomycetes	o__Basidiobolales	f__Basidiobolaceae	g__Basidiobolus	NA
"""

import csv
import argparse
import sys
from Bio import SeqIO

parser = argparse.ArgumentParser(
    description="Reformat a TSV file and match to a FASTA file to pull in names."
)
parser.add_argument(
    "--seqcolumn",
    type=int,
    default=0,
    help="The column number in the TSV file with the sequence data.",
)

parser.add_argument(
    "-i",
    "--intsv",
    type=argparse.FileType("r"),
    nargs="?",
    default=sys.stdin,
    help="Input TSV file with seqinfo and taxonomy (eg asv_tax_UNITE.tsv)",
)

parser.add_argument(
    "-s",
    "--inseq",
    type=argparse.FileType("r"),
    help="Input FASTA file with seqinfo to link (eg ASVs_ITS1.fa)",
)

parser.add_argument(
    "-o",
    "--output",
    nargs="?",
    type=argparse.FileType("w"),
    default=sys.stdout,
    help="Write FASTA output to filename or stdout by default (eg asv_tax_UNITE.fasta)",
)


args = parser.parse_args()

inASV = args.inseq  # "ASVs_ITS1.fa"
tsvfile = args.intsv  # "asv_tax_UNITE.tsv"
fastafile = args.output  # "asv_tax_UNITE.fasta"

idx_by_seq = {}


for record in SeqIO.parse(inASV, "fasta"):
    idx_by_seq[record.seq] = record

reader = csv.reader(tsvfile, delimiter="\t")
for row in reader:
    if row[0] == "" or row[1].startswith("tax"):
        continue
    if row[0] in idx_by_seq:
        seq = idx_by_seq[row[0]]
        taxstr = ";".join(row[1:8])
        seq.description = f"{seq.id} {taxstr}"
        SeqIO.write(seq, fastafile, "fasta")
    else:
        print(f"cannot find an ASV for {row[0]} in FASTA file", file=sys.stderr)
