# Prokka annoted genes of the cgMSLT scheme of Enterococcus faecium
The Enterococcus faecium reference strain (for the SeqSphere+ cgMLST scheme) consists of 2930 sequences.<br>
The cgMLST scheme itself consists of 1423 sequences.<br><br>

How was [Enterococcus_faecium_Aus0004_cgMLST.gff3](https://github.com/zmeel/cgMSLT-Entfae/blob/main/Enterococcus_faecium_Aus0004_cgMLST.gff3) created?<br>
1) The [sequence](https://raw.githubusercontent.com/zmeel/cgMSLT-Entfae/main/Enterococcus%20faecium%20strain%20Aus0004.fasta) of the reference strain Enterococcus faecium Aus0004 was imported in SeqSphere+ and run throught the cgMLST scheme.<br>
2) The [results](https://github.com/zmeel/cgMSLT-Entfae/blob/main/Enterococcus_faecium_cgMLST_scheme.fasta) were exported and used in ChatGPT <br>


ChatGPT Code Interpreter was used with the following prompts:
```
ChatGPT:
Generate a table with all entries from Enterococcus_faecalis.gff3. 
Column 1: ID (like HGKNLNPO_00001)
Column2: Start position
Column3: End position
```
This generated the following table:<br>
```
                  ID      start        end
0     HGKNLNPO_00001        1.0     1335.0
1     HGKNLNPO_00002     1533.0     2663.0
2     HGKNLNPO_00003     2826.0     3134.0
3     HGKNLNPO_00004     3121.0     4245.0
4     HGKNLNPO_00005     4242.0     6188.0
...              ...        ...        ...
```
```
ChatGPT: Now add to the table 60 bases from Enterococcus_faecium_Aus0004.ffn.
To find the right sequence in this file use the ID from the table
```
```
	ID	start	end	sequence
0	HGKNLNPO_00001	1.0	1335.0	ATGGTATCCCTCGATGCTTTATGGAATGAATTAAAAGCAACATACC...
1	HGKNLNPO_00002	1533.0	2663.0	ATGAAAGTTACTTTAAACCGAGCTAGCTTTATGCAGGAATTGCAAA...
2	HGKNLNPO_00003	2826.0	3134.0	TTGTTTTATTGCGAAAAAAAAGGTATAATAGAGTATACTTTTAATA...
3	HGKNLNPO_00004	3121.0	4245.0	ATGAGGCTGAATAAGCTGTATTTAAAAAATTATCGAAATTACGAAG...
4	HGKNLNPO_00005	4242.0	6188.0	ATGACAGAAGAAAGAAGTTTAGTAGAACGCGCTAAAGAGTATGATG...
```
```
ChatGPT: Now add to the table (as the second column with the name SeqSphere+ ID) the names of the sequences in Enterococcus_faecalis_cgMLST_scheme.fasta
To find the right sequence use the 60 bases from the table to search in Enterococcus_faecalis_cgMLST_scheme.fasta.
```
```
	ID	SeqSphere+ ID	start	end	sequence
0	HGKNLNPO_00001	EFAU004_00001	1.0	1335.0	ATGGTATCCCTCGATGCTTTATGGAATGAATTAAAAGCAACATACC...
1	HGKNLNPO_00002	EFAU004_00002	1533.0	2663.0	ATGAAAGTTACTTTAAACCGAGCTAGCTTTATGCAGGAATTGCAAA...
2	HGKNLNPO_00003	NaN	2826.0	3134.0	TTGTTTTATTGCGAAAAAAAAGGTATAATAGAGTATACTTTTAATA...
3	HGKNLNPO_00004	EFAU004_00004	3121.0	4245.0	ATGAGGCTGAATAAGCTGTATTTAAAAAATTATCGAAATTACGAAG...
4	HGKNLNPO_00005	EFAU004_00005	4242.0	6188.0	ATGACAGAAGAAAGAAGTTTAGTAGAACGCGCTAAAGAGTATGATG...
```
```
ChatGPT: Now filter the table and only keep the entries that have a SeqSphere+ ID
```
```
	ID	SeqSphere+ ID	start	end	sequence
0	HGKNLNPO_00001	EFAU004_00001	1.0	1335.0	ATGGTATCCCTCGATGCTTTATGGAATGAATTAAAAGCAACATACC...
1	HGKNLNPO_00002	EFAU004_00002	1533.0	2663.0	ATGAAAGTTACTTTAAACCGAGCTAGCTTTATGCAGGAATTGCAAA...
3	HGKNLNPO_00004	EFAU004_00004	3121.0	4245.0	ATGAGGCTGAATAAGCTGTATTTAAAAAATTATCGAAATTACGAAG...
4	HGKNLNPO_00005	EFAU004_00005	4242.0	6188.0	ATGACAGAAGAAAGAAGTTTAGTAGAACGCGCTAAAGAGTATGATG...
5	HGKNLNPO_00006	EFAU004_00006	6208.0	8679.0	ATGAGTGAAGAAATCAGAGAAAACATCCATGATGTCAATCTAACCA...
```
filtered_sequences.csv was downloaded from ChatGPT and reuploaded and ChatGPT was asked to perform the following task:
```
ChatGPT: Replace entries in the first column of Enterococcus_faecium_Aus0004.gff3 with the SeqSphere+ ID (column 2) from filtered_sequences.csv.
Use the ID (colum 1) from filtered_sequences.csv to find the right entry in Enterococcus_faecium_Aus0004.gff3.
If an entry from Enterococcus_faecium_Aus0004.gff3 does not existst in filtered_sequences.csv then write this entry to a log file and count the total number of entries in this log file
```
ChatGPT made a mistake so I aksed to correct it:
```
I asked to replace the first column of Enterococcus_faecium_Aus0004.gff3 with the SeqSphere+ ID from filtered_sequences.csv.
You replaced the ID tag. Please correct.
```
The result was still not what I asked but the result was sufficient:
```
NC_017022.1	Prodigal:002006	CDS	1.0	1335.0	.	+	0	ID=EFAU004_00001;Name=dnaA;db_xref=COG:COG0593;gene=dnaA;inference=ab initio prediction:Prodigal:002006,similar to AA sequence:UniProtKB:P05648;locus_tag=EFAU004_00001;product=Chromosomal replication initiator protein DnaA
NC_017022.1	Prodigal:002006	CDS	1533.0	2663.0	.	+	0	ID=EFAU004_00002;Name=dnaN;db_xref=COG:COG0592;gene=dnaN;inference=ab initio prediction:Prodigal:002006,similar to AA sequence:UniProtKB:P05649;locus_tag=EFAU004_00002;product=Beta sliding clamp
NC_017022.1	Prodigal:002006	CDS	3121.0	4245.0	.	+	0	ID=EFAU004_00004;Name=recF_1;db_xref=COG:COG1195;gene=recF_1;inference=ab initio prediction:Prodigal:002006,similar to AA sequence:UniProtKB:Q8RDL3;locus_tag=EFAU004_00004;product=DNA replication and repair protein RecF
NC_017022.1	Prodigal:002006	CDS	4242.0	6188.0	.	+	0	ID=EFAU004_00005;eC_number=5.6.2.2;Name=gyrB;db_xref=COG:COG0187;gene=gyrB;inference=ab initio prediction:Prodigal:002006,similar to AA sequence:UniProtKB:Q839Z1;locus_tag=EFAU004_00005;product=DNA gyrase subunit B
```
Last but not least the all entries not belonging to the cgMLST scheme were filtered out:
```
ChatGPT: Filter out all entries that don't have an ID that starts with "EFAU004_"
```
