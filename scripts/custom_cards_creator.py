#!/usr/bin/env python3

# This is a script to take two tsv files (black cards and white cards) and create
# a SQL script to load this data into db

# Example usage:
# python main.py ./black_cards.tsv ./white_cards.tsv ./output.sql "We are friends!" 3000

import csv
import sys

# Process args
args = sys.argv
black_cards_tsv_path = args[1]
white_cards_tsv_path = args[2]
output_file_path = args[3]
deck_name = args[4]
deck_watermark = args[5]
deck_id = int(args[6])
card_starting_id = int(args[7])

with open(output_file_path, 'w') as output:
  def escape_row(row):
    return list(map(lambda el: el.replace("'", "''"), row))

  # Card Set
  card_set_id = deck_id
  deck_weight = 1000 # make it the highest
  print("INSERT INTO card_set (id, active, base_deck, description, name, weight) VALUES ({}, {}, {}, '{}', '{}', {});".format(card_set_id, "true", "false", deck_name, deck_name, deck_weight), file=output)

  # Black cards
  with open(black_cards_tsv_path) as f:
    read_tsv = csv.reader(f, delimiter='\t')

    card_id = card_starting_id
    for raw_row in read_tsv:
      row = escape_row(raw_row)
      print("INSERT INTO black_cards (id, draw, pick, text, watermark) VALUES ({}, {}, {}, '{}', '{}');".format(card_id, *row, deck_watermark), file=output)
      # Populate join table
      print("INSERT INTO card_set_black_card (card_set_id, black_card_id) VALUES ({}, {});".format(card_set_id, card_id), file=output)
      card_id += 1

  # White cards
  with open(white_cards_tsv_path) as f:
    read_tsv = csv.reader(f, delimiter='\t')

    card_id = card_starting_id
    for raw_row in read_tsv:
      row = escape_row(raw_row)
      print("INSERT INTO white_cards (id, text, watermark) VALUES ({}, '{}', '{}');".format(card_id, *row, deck_watermark), file=output)
      # Populate join table
      print("INSERT INTO card_set_white_card (card_set_id, white_card_id) VALUES ({}, {});".format(card_set_id, card_id), file=output)
      card_id += 1
