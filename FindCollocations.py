import collections
import json
import sys

def getChiSquareValue(bigram):
    words = bigram.split()

    chiSquare = [[0 for x in range(3)] for y in range(3)]

    chiSquare[2][2] = tokenData['tokenLength']
    chiSquare[0][0] = tokenData['bigramFrequency'][bigram]
    chiSquare[0][2] = tokenData['tokenFrequency'][words[1]]
    chiSquare[0][1] = chiSquare[0][2] - chiSquare[0][0]
    chiSquare[2][0] = tokenData['tokenFrequency'][words[0]]
    chiSquare[2][1] = chiSquare[2][2] - chiSquare[2][0]
    chiSquare[1][0] = chiSquare[2][0] - chiSquare[0][0]
    chiSquare[1][1] = chiSquare[2][1] - chiSquare[0][1]
    chiSquare[1][2] = chiSquare[2][2] - chiSquare[0][2]
    
    # Modified chi square equation for a 2x2 matrix
    numerator = chiSquare[2][2] * pow((chiSquare[0][0] * chiSquare[1][1]) - (chiSquare[0][1] * chiSquare[1][0]), 2)
    denominator = (chiSquare[0][0] + chiSquare[0][1]) * (chiSquare[0][0] + chiSquare[1][0]) * (chiSquare[0][1] + chiSquare[1][1]) * (chiSquare[1][0] + chiSquare[1][1])

    return numerator / denominator

if (len(sys.argv) != 3):
    print('Enter the file name as the first arguement and the output file as the second arguement.')
    sys.exit()

tokenData = json.loads(open(sys.argv[1], 'r').read())

collocations = {}
for key, value in tokenData['bigramFrequency'].items():
    # Only calculate the chi value if the bigram has appeared more than 5 times.
    if value > 5:
        collocations[key] = getChiSquareValue(key)

# To sort the collocations, convert the hash table to tuples, sort, get the top 25 collocations, and then covert it back to a hash table.
collocations = collections.OrderedDict(sorted(collocations.items(), key=lambda kv: kv[1], reverse=True)[:100])
# convert the bigrams to tuples
bigrams = [(k, v) for k, v in tokenData['bigramFrequency'].items()]

# Create a hash table with the top 25 bigrams and collocations
collocationData = {
    'bigrams': collections.OrderedDict(bigrams[:100]),
    'collocations': collocations
}

# write the hash table to a JSON file
with open(sys.argv[2] + '_collocation_data.json', 'w') as file:
    file.write(json.dumps(collocationData, indent=4))