#!/bin/sh
grammar_file=$1
test_sentence_file=$2
output_file=$3
python3 ./hw3_parser2.py "$grammar_file" "$test_sentence_file" "$output_file"
