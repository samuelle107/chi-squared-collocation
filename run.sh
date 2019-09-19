#!/bin/bash
python CountBigrams.py amazon_reviews.txt amazon_reviews
python FindCollocations.py amazon_reviews_token_data.json amazon_reviews
