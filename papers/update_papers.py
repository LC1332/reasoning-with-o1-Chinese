"""
Helper script to maintain papers.md
Usage: python update_papers.py add_paper --title "Paper Title" --authors "Author1, Author2" --link "https://arxiv.org/..."
"""

import argparse
import datetime
import re

def add_paper(title, authors, link, year=None):
    if year is None:
        year = datetime.datetime.now().year
    
    # Create paper entry in markdown format
    paper_entry = f"""- [{title}]({link})
  - {authors}
"""
    
    # Read current papers.md
    with open('papers.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find year section and add paper
    year_pattern = f"## {year} Papers"
    if year_pattern in content:
        # Add under existing year
        insert_position = content.find(year_pattern) + len(year_pattern)
        new_content = content[:insert_position] + f"\n\n{paper_entry}" + content[insert_position:]
    else:
        # Create new year section
        new_content = content + f"\n\n## {year} Papers\n\n{paper_entry}"
    
    # Write updated content
    with open('papers.md', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update papers.md')
    parser.add_argument('--title', required=True, help='Paper title')
    parser.add_argument('--authors', required=True, help='Paper authors (comma separated)')
    parser.add_argument('--link', required=True, help='Paper link')
    parser.add_argument('--year', type=int, help='Publication year')
    
    args = parser.parse_args()
    add_paper(args.title, args.authors, args.link, args.year)