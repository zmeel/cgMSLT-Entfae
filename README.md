# Prokka annoted genes of the cgMSLT schene of Enterococcus faecium
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
ChatGPT: Now add the the table (as the second column with the name SeqSphere+ ID) the names of the sequences in Enterococcus_faecalis_cgMLST_scheme.ffn.fasta.
To find the right sequence use the 60 bases from the table to search in Enterococcus_faecalis_cgMLST_scheme.ffn.fasta.
```


3) The table [filtered_sequences.csv](https://github.com/zmeel/cgMSLT-Entfae/blob/main/filtered_sequences.csv) was created by combining [Enterococcus_faecium_Aus0004.gff3](https://raw.githubusercontent.com/zmeel/cgMSLT-Entfae/main/Enterococcus_faecium_Aus0004.gff3), [Enterococcus_faecium_Aus0004.ffn.fasta](https://raw.githubusercontent.com/zmeel/cgMSLT-Entfae/main/Enterococcus_faecium_Aus0004.ffn.fasta) and [Enterococcus_faecium_cgMLST_scheme.fasta](https://github.com/zmeel/cgMSLT-Entfae/blob/main/Enterococcus_faecium_cgMLST_scheme.fasta)<br>
