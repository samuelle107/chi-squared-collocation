import collections
import json
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
import string
import sys

if (len(sys.argv) != 3):
    print('Enter the file name as the first arguement and the output file as the second arguement.')
    sys.exit()

stopword = stopwords.words('english')

# Remove the residual HTML, remove punctuation, remove digits, convert to lowercase
text = open(sys.argv[1], 'r').read().replace('&quot', '').translate(str.maketrans('', '', string.punctuation)).translate(str.maketrans('', '', string.digits)).lower()

tokenList = nltk.word_tokenize(text)
# Add words to tokens if the current token is not a stopword
tokens = [word for word in tokenList if word not in stopword]

bigramFrequency = {}
tokenFrequency = {}

# Add the bigrams to the hash table and count the words
for i in range(len(tokens)):
    if i < len(tokens) - 1:
        bigram = tokens[i] + ' ' + tokens[i + 1]

        # Attempt to increase the frequency of the bigram by 1.  If it cannot, create a new entry
        try:
            bigramFrequency[bigram] += 1
        except KeyError:
            bigramFrequency[bigram] = 1

    # Attempt to increase the freuqnecy of the word by 1.  If it cannot, create a new entry
    try:
        tokenFrequency[tokens[i]] += 1
    except KeyError:
        tokenFrequency[tokens[i]] = 1

# To sort the bigrams, convert the hash table to tuples, sort, and then convert it back to a dictionary
bigramFrequency = collections.OrderedDict(sorted(bigramFrequency.items(), key=lambda kv: kv[1], reverse=True))

# Create a hash table with the bigrams, tokens, and number of tokens
tokenData = {
    "bigramFrequency": bigramFrequency,
    "tokenFrequency": tokenFrequency,
    "tokenLength": len(tokens)
}

# Write the hash table to a json file
with open(sys.argv[2] + '_token_data.json', 'w') as file:
    file.write(json.dumps(tokenData, indent=4))
