import collections
import json
import string
import sys

if (len(sys.argv) != 3):
    print('Enter the file name as the first arguement and the output file as the second arguement.')
    sys.exit()

# Read the text file and remove all punctuation, convert it all to lowercase, and then split the text into a list of tokens
tokens = open(sys.argv[1], 'r').read().translate(str.maketrans('', '', string.punctuation)).lower().split()

bigrams = {}

# Add the bigrams to the dictionary
for i in range(len(tokens) - 2):
    bigram = tokens[i] + ' ' + tokens[i + 1]
    try:
        bigrams[bigram] += 1
    except KeyError:
        bigrams[bigram] = 1

# Sort the bigrams.  In the process, convert the dictionary to a tuple, and then convert it back to a dictionary.
sortedBigrams = collections.OrderedDict(sorted(bigrams.items(), key=lambda kv: kv[1], reverse=True))

# Write the dictionary to a json file
with open(sys.argv[2] + '.json', 'w') as file:
    file.write(json.dumps(sortedBigrams, indent=4))