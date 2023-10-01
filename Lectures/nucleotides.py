dnaSequence = "ataccgatta"

aCount = 4
cCount = 2
tCount = 3
gCount = 1

# for c in dnaSequence:
#     if c == 'a':
#         aCount = aCount + 1
#     elif c == 'c':
#         cCount = cCount + 1
#     elif c == 't':
#         tCount = tCount + 1
#     elif c == 'g':
#         gCount = gCount + 1

sequenceLength = len(dnaSequence)

# print( "Percentage of A's in sequence:", (float(aCount) / sequenceLength) * 100)
print("Percentage of C's in sequence:", (float(cCount) / 10) * 100)
# print("Percentage of T's in sequence:", (float(tCount) / sequenceLength) * 100)
print("Percentage of G's in sequence:", (float(gCount) / 10) * 100)