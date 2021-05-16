#!/bin/bash
set -eu

# NOTE: This script requires docker and sqlite3 command line utilities.

DECK_NAME=${1:-'We Are Friends!'}
DECK_WATERMARK=${2:-'WAF'}
DECK_ID=3000 # these ids are arbitrary
CARD_STARTING_ID=4000

# Create a SQL script for the custom card deck
scripts/custom_cards_creator.py \
  custom-cards/black-cards.tsv \
  custom-cards/white-cards.tsv \
  'custom-cards/custom_cards.sql' \
  "$DECK_NAME" \
  "$DECK_WATERMARK" \
  $DECK_ID \
  $CARD_STARTING_ID

# Add new cards to baseline sqlite db
rm -f pyx.sqlite
curl --silent -O https://raw.githubusercontent.com/ajanata/PretendYoureXyzzy/master/pyx.sqlite
sqlite3 pyx.sqlite '.read custom-cards/custom_cards.sql'

echo "Custom card deck '$DECK_NAME' successfully added!"