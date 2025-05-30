#!/usr/bin/env python3

import json
import os
import re
from pathlib import Path
from datetime import datetime

def create_filename(title):
    """Create a filename from the title by converting to lowercase and replacing non-alphanumeric chars with hyphens."""
    # Convert to lowercase and replace non-alphanumeric chars with hyphens
    filename = re.sub(r'[^a-z0-9]+', '-', title.lower())
    # Remove leading and trailing hyphens
    filename = filename.strip('-')
    return filename

def normalize_date(date_str):
    """Normalize date string to DD Month YYYY format.
    
    Args:
        date_str (str): Date string in various formats
        
    Returns:
        str: Date string in DD Month YYYY format
        
    Raises:
        ValueError: If date_str is empty, None, or in an invalid format
    """
    if not date_str or not date_str.strip():
        raise ValueError("Date cannot be empty or None")
    
    # Replace various dash types with regular hyphen
    date_str = re.sub(r'[‑–—]', '-', date_str.strip())
    
    try:
        # Handle year-only format (e.g. "2017")
        if re.match(r'^\d{4}$', date_str):
            return f"01 January {date_str}"
            
        # Handle year-month format (e.g. "2019-09")
        if re.match(r'^\d{4}-\d{2}$', date_str):
            date_obj = datetime.strptime(date_str, "%Y-%m")
            return date_obj.strftime("%d %B %Y")
            
        # Handle full date format (e.g. "2024-01-01")
        if re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            return date_obj.strftime("%d %B %Y")
            
        # Handle slash format (e.g. "2024/03/15")
        if re.match(r'^\d{4}/\d{2}/\d{2}$', date_str):
            date_obj = datetime.strptime(date_str, "%Y/%m/%d")
            return date_obj.strftime("%d %B %Y")
            
        raise ValueError("Invalid date format")
    except ValueError as e:
        raise ValueError("Invalid date format or value") from e

def extract_youtube_id(url):
    """Extract YouTube video ID from a URL.
    
    Args:
        url (str): YouTube URL
        
    Returns:
        str: YouTube video ID or None if not found
        
    >>> extract_youtube_id('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    'dQw4w9WgXcQ'
    >>> extract_youtube_id('https://youtu.be/dQw4w9WgXcQ')
    'dQw4w9WgXcQ'
    >>> extract_youtube_id('https://www.youtube.com/embed/dQw4w9WgXcQ')
    'dQw4w9WgXcQ'
    >>> extract_youtube_id('https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=123s')
    'dQw4w9WgXcQ'
    >>> extract_youtube_id('https://example.com')
    >>> extract_youtube_id(None)
    >>> extract_youtube_id('')
    """
    if not url:
        return None
        
    # Match patterns like:
    # - https://www.youtube.com/watch?v=VIDEO_ID
    # - https://youtu.be/VIDEO_ID
    # - https://www.youtube.com/embed/VIDEO_ID
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\n?#]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def create_front_matter(item):
    """Create the front matter dictionary for a portfolio item.
    
    Args:
        item (dict): Portfolio item data
        
    Returns:
        dict: Front matter dictionary
        
    Raises:
        ValueError: If required fields are missing or invalid
            - date is missing or invalid
            - type is missing or empty
            - language is not 'English' or 'French'
    """
    # Validate and normalize date
    try:
        date = normalize_date(item['Date'])
    except ValueError as e:
        raise ValueError(f"date: {e}")
    
    # Validate type
    if not item.get('Type'):
        raise ValueError("type: missing")
    
    # Validate language
    language = item.get('Language', '').strip()
    if not language:
        language = 'English'  # Default to English if not specified
    elif language == 'English/French':
        language = 'English'  # Default to English for bilingual content
    elif language not in ['English', 'French']:
        raise ValueError(f"language: must be 'English' or 'French', got '{language}'")
    
    # Extract YouTube video ID if URL is present
    video_id = None
    if item.get('url'):
        video_id = extract_youtube_id(item['url'])
    
    front_matter = {
        'layout': 'portfolio-item',
        'title': item['Title / Name'],
        'type': item['Type'],
        'date': date,
        'language': language,
        'guests': item['Guests'],
        'source_link': item['url'],
        'duration': item['Duration']
    }
    
    # Add video_id to front matter if found
    if video_id:
        front_matter['video_id'] = video_id
    
    return front_matter

def write_portfolio_file(filename, front_matter, content):
    """Write a portfolio item to a markdown file."""
    # Create the _portfolio directory if it doesn't exist
    Path('_portfolio').mkdir(exist_ok=True)
    
    # Format the front matter
    front_matter_str = '\n'.join(f'{k}: {json.dumps(v)}' for k, v in front_matter.items())
    
    # Write the file
    with open(f'_portfolio/{filename}.md', 'w', encoding='utf-8') as f:
        f.write(f'''---
{front_matter_str}
---

{content}
''')

def main():
    # Read the portfolio.json file
    with open('portfolio.json', 'r', encoding='utf-8') as f:
        portfolio_data = json.load(f)
    
    # Convert each item to a Jekyll collection file
    for item in portfolio_data:
        try:
            # Create a filename from the title
            filename = create_filename(item['Title / Name'])
            
            # Create the front matter
            front_matter = create_front_matter(item)
            
            # Get the content
            content = item['Description / Summary']
            
            # Write the file
            write_portfolio_file(filename, front_matter, content)
            print(f"Created {filename}.md")
        except ValueError as e:
            print(f"Error in {filename}.md: {e}")
            continue
    
    print("Conversion complete! Portfolio items have been created in the _portfolio directory.")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main() 
