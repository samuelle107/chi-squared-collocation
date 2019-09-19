## Introduction
This project is divided into two parts:
- CountBigrams.py
- FindCollocations.py

The first program will take in the corpus and the filename for the results.  It will count the bigrams and save the results in sorted ordered by frequency in a JSON file.
The second program will take in the JSON from the second result and the filename for the results.  It will use chi-squared statistics to determine the collocations, save the results in sorted order by chi-squared value in a JSON file.

## GETTING STARTED
- Run `python CountBigrams <input> <output_file>` to get a sorted JSON file of all the words.
- Run `python FindCollocations <output_file> <second_output_file> to get a JSON file containing the bigrams and collocations`