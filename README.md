# ped_filter_to_fasta
Code to filter heterozygous SNP in PED file and write results to fasta

If forward allele 1 or forward allele 2 are equal the one SNP value is added to the fasta file. If forward allele 1 and forward allele 2 are different the SNP value is not added to the fasta file.
If forward allele 1 or forward allele 2 is missing the SNP value (represented by the character '-' or 'D') is not added to the fasta file.
If forward allele 1 or forward allele 2 contains the character 'I'  the the value 'N' is added to the fasta file.

Running the code:
``` from a terminal run the following command with required arguments
python ped_filter_to_fasta.py -p "path/to/ped/file" -s "path/to/snp/file"
example
python ped_filter_to_fasta.py -p '/home/waa2/PycharmProjects/ped_filter_to_fasta/test_report.txt' -s '/home/waa2/PycharmProjects/ped_filter_to_fasta/input_snps.txt'

```