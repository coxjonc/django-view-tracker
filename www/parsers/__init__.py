#!/usr/bin/python

# List of parsers to import and use based on parser.domains
from kt import KTParser

parser_dict = {}

#Import the parsers and fill in parser_dict: domain -> parser
for domain in KTParser.domains:
    parser_dict[domain] = KTParser

def get_parser(url):
    return parser_dict[url.split('/')[2]]
