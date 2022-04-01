Your program must create a file called "output" which contains exactly 3 lines as shown below:

24
ELVISLIVES
ELVI--IVES
The first line contains the score of the alignment between the two sequences, using the gap penalty Sigma = 5, and the scores provided by the PAM250 matrix.  The second and third lines contain the sequences provided in the input, in the same order, with gap (-) characters inserted to form the alignment.  Note that the two lines must have the same exact length after the gap characters are added.

Unlike the prior assignment, the two strings can be substrings extracted from the input file. For example, if the input contains the strings:

KYVILIVGN
DDVISLIVPL
The output is simply:

19
VI-LIV
VISLIV
