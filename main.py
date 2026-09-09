import os
import time
from src.file_organizer import organize_files
from src.data_extractor import extract_emails

def log_execution(action_name, duration, details):
    """Appends execution metrics to the execution log file."""
    log_file = "logs/execution_log.txt"
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Action: {action_name} | Duration: {duration:.4f}s | Details: {details}\n"
    
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)

def main():
    while True:
        print("\n==============================================")
        print("  CodeAlpha Task Automation & Data Suite v1.0 ")
        print("==============================================")
        print("1. Organize raw files in 'data/raw/'")
        print("2. Extract email patterns from 'data/raw/sample.txt'")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ").strip()

        if choice == '1':
            start_time = time.time()
            count = organize_files('data/raw')
            elapsed = time.time() - start_time
            print(f"Execution Time: {elapsed:.4f} seconds")
            log_execution("File Organization", elapsed, f"Moved {count} files")

        elif choice == '2':
            start_time = time.time()
            raw_sample = 'data/raw/sample.txt'
            output_path = 'data/processed/extracted_emails.txt'
            
            if not os.path.exists(raw_sample):
                print(f"[Notice] Creating a test file at '{raw_sample}'...")
                os.makedirs('data/raw', exist_ok=True)
                with open(raw_sample, 'w', encoding='utf-8') as f:
                    f.write("Contact support at info@codealpha.tech or admin@example.org. Duplicate: info@codealpha.tech")

            count = extract_emails(raw_sample, output_path)
            elapsed = time.time() - start_time
            print(f"Execution Time: {elapsed:.4f} seconds")
            log_execution("Email Extraction", elapsed, f"Extracted {count} emails")

        elif choice == '3':
            print("\nExiting application. Goodbye!")
            break
        else:
            print("[Invalid] Please select a valid choice (1, 2, or 3).")

if __name__ == "__main__":
    main()