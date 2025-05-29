#!/usr/bin/env python3

import os
import re
from datetime import datetime

def convert_date(date_str):
    """Convert date from YYYY-MM-DD to DD Month YYYY format.
    
    Args:
        date_str (str): Date string in YYYY-MM-DD format
        
    Returns:
        str: Date string in DD Month YYYY format
        
    Examples:
        >>> convert_date("2016-04-22")
        '22 April 2016'
        >>> convert_date("2019-06-18")
        '18 June 2019'
        >>> convert_date("2020-12-01")
        '01 December 2020'
        >>> convert_date("invalid-date")
        'invalid-date'
    """
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%d %B %Y")
    except ValueError:
        print(f"Warning: Could not parse date {date_str}")
        return date_str

def process_file(file_path):
    """Process a single markdown file to convert its date format."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the date line in the front matter
    date_pattern = r'date:\s*"(\d{4}-\d{2}-\d{2})"'
    match = re.search(date_pattern, content)
    
    if match:
        old_date = match.group(1)
        new_date = convert_date(old_date)
        new_content = content.replace(f'date: "{old_date}"', f'date: "{new_date}"')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated date in {file_path}: {old_date} -> {new_date}")
    else:
        print(f"No date found in {file_path}")

def main():
    portfolio_dir = "_portfolio"
    
    # Process all markdown files in the portfolio directory
    for filename in os.listdir(portfolio_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(portfolio_dir, filename)
            process_file(file_path)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main() 