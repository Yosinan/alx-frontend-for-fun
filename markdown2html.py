#!/usr/bin/python3
""" Markdown to HTML """
import sys
import os
import markdown


'''
argv[1] = input file
argv[2] = output file
'''


if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py <input_file> <output_file>\n")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(input_file):
    sys.stderr.write("Missing {}\n".format(input_file))
    sys.exit(1)

with open(input_file, 'r') as f:
    markdown_text = f.read()

html = markdown.markdown(markdown_text)

with open(output_file, 'w') as f:
    f.write(html)

sys.exit(0)
