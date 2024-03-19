import csv
import argparse

def filter_PED_SNPs(ped_file, snp_list_path):
    """
    Function to filter a ped file based on a list of SNPs
    :param ped_file: path to tab separated ped file
    :param snp_list: path to a text file containing list of SNP names (1 SNP names per line)
    :return: a dictionary of sample IDs and their corresponding SNP values
    """
    snp_dict = {}  # Initialize an empty dictionary to store the sample IDs and their corresponding SNP values
    # Read SNP list and remove duplicates
    with open(snp_list_path, 'r') as snp_file:
        snp_list = set(line.strip() for line in snp_file)

    with open(ped_file, 'r', newline='') as input_ped:
        ped_file_reader = csv.reader(input_ped, delimiter='\t')
        for _ in range(9):  # skip the first 9 lines of the ped file
            next(ped_file_reader)
        for row in ped_file_reader:
            snp_name = row[0]
            if snp_name in snp_list:
                forward_allele1 = row[2]
                forward_allele2 = row[3]
                sample_id = row[1]
                if forward_allele1 == 'D' or forward_allele2 == 'D' or forward_allele1 == '-' or forward_allele2 == '-':
                    continue
                if forward_allele1 == 'I' or forward_allele2 == 'I':
                    if sample_id in snp_dict:
                        snp_dict[sample_id] += 'N'
                    else:
                        snp_dict[sample_id] = 'N'
                elif forward_allele1 == forward_allele2:
                    if sample_id in snp_dict:
                        snp_dict[sample_id] += forward_allele1
                    else:
                        snp_dict[sample_id] = forward_allele1
    # for sample_id, snp_value in snp_dict.items():
    #     print(sample_id, snp_value)
    return snp_dict



def print_fasta(snp_dict, snp_file_path):
    """
#     Function to write a dictionary of sample IDs and their corresponding SNP values to a fasta file
#     :param snp_dict: A dictionary of sample IDs and their corresponding SNP values
#     :param snp_file_path: A string containing the absolute path to the snp input file to extract filename
#     :return: None
#     """
    # split the snp file path on '/' and '.' and get the snp filename to append to fasta filename
    snp_filename, extension = snp_file_path.split('/')[-1].rsplit('.', 1)
    for sample_id, sequence in snp_dict.items():
        fasta_filename = f"{sample_id}_{snp_filename}.fa"
        with open(fasta_filename, 'w') as fasta_file:
            fasta_file.write(f">{sample_id}\n")
            # write the sequence in 60 characters per line
            for i in range(0, len(sequence), 60):
                fasta_file.write(sequence[i:i+60] + '\n')

    return None


# arguments parsing and help
parser = argparse.ArgumentParser(
    description='This script filters a space separated ped file and writes results to a fasta file')
parser.add_argument('-p', "--ped_file", type=str, help='absolute path to ped input file')
parser.add_argument('-s', "--snp_file", type=str, help='absolute path to snp input file containing a list of snp names')
args = parser.parse_args()
ped_file_path = args.ped_file
snp_file_path = args.snp_file

def main():
    print_fasta(filter_PED_SNPs(ped_file_path, snp_file_path), snp_file_path)


if __name__ == '__main__':
    main()

# quick example of how to run the script
# python ped_filter_to_fasta.py -p '/path/to/ped_file' -s '/path/to/snp_file.txt'
