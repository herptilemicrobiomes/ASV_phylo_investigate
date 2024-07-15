#!/bin/bash -l

../scripts/make_ASV_fasta.py --intsv data/asv_tax_UNITE_example.tsv --inseq data/ASVs.fa --out testing__ASVs_UNITE_taxa.fa
../scripts/extract_taxon_ASVfasta.py --input testing__ASVs_UNITE_taxa.fa --query p__Ascomycota --output testing__ASVs_UNITE_taxa_Ascomycota.fa
