# ASV_phylo_investigate
Investigate the Phylogenetic relationships of ASVs with other reference DB

## extract UNITE SHs based on a phylogenetic class

Use the script `extract_taxon_UNITE.py` to generate a FASTA file of a subset of sequences based on taxonomy info.
Multiple can be provided with the --query option (eg `--query g__Hortaea g__Aspergillus`)
```bash
 ./extract_taxon_UNITE.py --query o__Chaetothyriales \
 -o Chaetothyriales_UNITE_202211120.fa -i sh_general_release_dynamic_s_all_29.11.2022_dev.fasta
 ```

## extract ASVs/Seqs from a FASTA file

Use the script `extract_taxon_ASVfasta.py` to extract taxa where there is a simple ID + description
Expect a FASTA file with and ID and a description which is a QIIME formatted taxonomy string
eg.
```text
>ASV_202 k__Fungi;p__Ascomycota;c__Dothideomycetes;o__Pleosporales;f__Pleosporaceae;g__Alternaria;NA
CACAAATATGAAGGCGGGCTGGCACCTCTCGGGGTGGCCAGCCTTGCTGAATTATTCCACCCGTGTCTTTTGCGTACTTCTTGTTTCCTTGGTGGGCTCGCCCACCACAAGGACCAACCCATAAACCTTTTTGTAATGGCAATCAGCGTCAGTAACAATGTAATAATTA
>ASV_203 k__Fungi;p__Ascomycota;c__Dothideomycetes;o__Pleosporales;f__Didymosphaeriaceae;g__Paraphaeosphaeria;NA
TCCAACCAAAACCAGCTGCGGTCGCGGCCCCCGGGGTTCTCTCTGGGTGGTAGGGGTAACACCCTCACGCGCCGTACGTCTGCATCCTTTCTTTACGAGCACCTTCGTTCTCCTTCGGCGGGGCAACCTGCCGTTGGAACCAAACAAAACCTTTTTTTGCATCTAGCAT
TACCTGTTCTGATACAAACAATCGTTA
```
