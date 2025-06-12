#!/usr/bin/python3
"""Convert CSV data to JSON format and save to data.json."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Read a CSV file and convert its rows to a list of dictionaries,
    then serialize to JSON and write to data.json.

    Args:
        csv_filename (str): Path to the input CSV file.

    Returns:
        bool: True if conversion succeeded, False otherwise.
    """
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            rows = [row for row in reader]
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(rows, json_file)
        return True
    except (FileNotFoundError, IOError, csv.Error, json.JSONDecodeError):
        return False
