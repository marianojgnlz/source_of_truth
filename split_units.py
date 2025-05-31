#!/usr/bin/env python3
"""
Script to split source_of_truth.md file by units.
Each unit starting with "# **Unidad X:" will be saved to a separate file.
"""

import re
import sys
from pathlib import Path

def split_units(input_file="source_of_truth.md"):
    """
    Split the input file by units and save each unit to a separate file.
    
    Args:
        input_file (str): Path to the input markdown file
    """
    
    # Check if input file exists
    if not Path(input_file).exists():
        print(f"Error: File '{input_file}' not found.")
        return
    
    # Read the entire file
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    # Pattern to match unit headers: # **Unidad X: Title** {#id}
    unit_pattern = r'^# \*\*Unidad (\d+):[^*]*\*\*[^\n]*$'
    
    # Find all unit headers
    matches = list(re.finditer(unit_pattern, content, re.MULTILINE))
    
    if not matches:
        print("No units found in the file.")
        return
    
    print(f"Found {len(matches)} units:")
    
    # Process each unit
    for i, match in enumerate(matches):
        unit_number = match.group(1)
        unit_start = match.start()
        
        # Determine the end of this unit (start of next unit or end of file)
        if i + 1 < len(matches):
            unit_end = matches[i + 1].start()
        else:
            unit_end = len(content)
        
        # Extract unit content
        unit_content = content[unit_start:unit_end].rstrip()
        
        # Create output filename
        output_filename = f"unidad_{unit_number}.md"
        
        # Write unit to file
        try:
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(unit_content)
            print(f"  - Unit {unit_number} saved to '{output_filename}'")
        except Exception as e:
            print(f"Error writing unit {unit_number}: {e}")

def main():
    """Main function to handle command line arguments."""
    
    # Default input file
    input_file = "source_of_truth.md"
    
    # Check if a different input file was provided
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    
    print(f"Splitting file: {input_file}")
    split_units(input_file)
    print("Done!")

if __name__ == "__main__":
    main() 