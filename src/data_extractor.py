import os
import re

def extract_emails(input_file_path, output_file_path):
    """
    Reads a text file, extracts unique valid email addresses, and writes them to an output file.
    """
    if not os.path.exists(input_file_path):
        print(f"[Error] File '{input_file_path}' does not exist.")
        return 0

    # Regular expression for matching email patterns
    email_regex = r'[a-zA-Z0-9%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    try:
        with open(input_file_path, 'r', encoding='utf-8') as infile:
            content = infile.read()

        # Find all unique email addresses matching pattern
        extracted_emails = sorted(set(re.findall(email_regex, content)))

        # Ensure destination directory exists
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            for email in extracted_emails:
                outfile.write(email + '\n')

        print(f"[Success] Extracted {len(extracted_emails)} unique email(s) -> Saved to '{output_file_path}'.")
        return len(extracted_emails)

    except Exception as e:
        print(f"[Error] Failed to process file: {e}")
        return 0