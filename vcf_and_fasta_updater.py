import pandas as pd
import sys
import textwrap
import os

def parse_fasta(filename):
    with open(filename, 'r') as file:
        genome = ''
        for line in file:
            if not line.startswith('>'):
                genome += line.strip()
    return genome

def get_bases_before(genome, pos, num_bases=30):
    return genome[max(0, pos-num_bases-1):pos-1]

def find_sequence_after(genome, sequence):
    position = genome.find(sequence)
    if position == -1:
        return -1
    else:
        return position + len(sequence) + 1

def replace_bases_ALT_with_REF(genome, pos, ref, alt):
    if pos == -1:
        return genome
    else:
        return genome[:pos-1] + genome[pos-1:pos-1+len(alt)].replace(alt, ref) + genome[pos-1+len(alt):]

def main_one_at_a_time(vcf_file, ref_fasta_file, target_fasta_file, out_vcf_file, out_fasta_file):
    vcf_data = pd.read_csv(vcf_file, comment='#', delimiter='\t', header=None)
    vcf_data.columns = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT', 'OTHER']

    ref_genome = parse_fasta(ref_fasta_file)

    vcf_data['30_bases'] = vcf_data['POS'].apply(lambda x: get_bases_before(ref_genome, x))

    target_genome = parse_fasta(target_fasta_file)

    target_genome_updated = target_genome
    for idx, row in vcf_data.iterrows():
        alt_pos = find_sequence_after(target_genome_updated, row['30_bases'])
        target_genome_updated = replace_bases_ALT_with_REF(target_genome_updated, alt_pos, row['REF'], row['ALT'])
        vcf_data.loc[idx, 'ALT pos'] = alt_pos

    # Convert the ALT pos column to integers
    vcf_data['ALT pos'] = vcf_data['ALT pos'].astype(int)

    vcf_data.to_csv(out_vcf_file, sep='\t', index=False)

    with open(out_fasta_file, 'w') as file:
        file.write('>' + os.path.splitext(os.path.basename(target_fasta_file))[0] + '\n')
        file.write('\n'.join(textwrap.wrap(target_genome_updated, 80)))

if __name__ == '__main__':
    main_one_at_a_time(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
