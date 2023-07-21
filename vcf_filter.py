import argparse
import re

def parse_gff3_id_positions(gff3_file):
    positions_to_id = {}
    with open(gff3_file, 'r') as file:
        for line in file:
            if not line.startswith("#"):  # Skip header lines
                fields = line.strip().split("\t")
                start = int(float(fields[3]))
                end = int(float(fields[4]))
                # Extract the ID from the attributes field
                attributes = fields[8]
                id_match = re.search("ID=([^;]+)", attributes)
                if id_match:
                    id_value = id_match.group(1)
                    # Map all positions in the range to the ID
                    for position in range(start, end + 1):
                        positions_to_id[position] = id_value
    return positions_to_id

def filter_and_add_id_vcf(vcf_file, positions_to_id, output_file, skewness):
    with open(vcf_file, 'r') as vcf, open(output_file, 'w') as out:
        for line in vcf:
            if line.startswith("#"):  # Copy header lines
                out.write(line)
            else:
                fields = line.strip().split("\t")
                pos = int(fields[1])
                info = fields[7].split(";")
                # Searching for FAF and RAF in INFO field
                faf = next((float(i.split("=")[1]) for i in info if i.startswith("FAF")), None)
                raf = next((float(i.split("=")[1]) for i in info if i.startswith("RAF")), None)
                # Check conditions
                if pos in positions_to_id and faf is not None and raf is not None and abs(faf - raf) > skewness:
                    # Replace '.' in column 3 with the corresponding ID
                    fields[2] = positions_to_id[pos]
                    out.write("\t".join(fields) + "\n")

def main():
    parser = argparse.ArgumentParser(description='Filter a VCF file based on a GFF3 file and a skewness parameter.')
    parser.add_argument('--vcf', required=True, help='Input VCF file')
    parser.add_argument('--gff3', required=True, help='Input GFF3 file')
    parser.add_argument('--skewness', type=float, required=True, help='Skewness parameter')
    parser.add_argument('--output', required=True, help='Output VCF file')
    args = parser.parse_args()

    # Parse GFF3 file
    positions_to_id = parse_gff3_id_positions(args.gff3)

    # Filter VCF file and add IDs
    filter_and_add_id_vcf(args.vcf, positions_to_id, args.output, args.skewness)

if __name__ == '__main__':
    main()
