import re

def extract_emails_from_file(input_file, output_file):
    """Extracts valid email addresses from text data using Regular Expressions."""
    email_regex = r'[a-zA-Z0-9%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        emails = set(re.findall(email_regex, content))
        
        with open(output_file, 'w', encoding='utf-8') as file:
            for email in sorted(emails):
                file.write(email + '\n')
                
        print(f"Extracted {len(emails)} unique emails to {output_file}")
    except FileNotFoundError:
        print(f"File {input_file} not found.")