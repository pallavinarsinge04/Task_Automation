import time
from src.file_organizer import organize_files
from src.data_extractor import extract_emails_from_file

def main():
    print("========================================")
    print("  CodeAlpha Task Automation Suite v1.0  ")
    print("========================================")
    print("1. Organize Files in Raw Directory")
    print("2. Extract Emails from Raw Text")
    print("3. Exit")
    
    choice = input("\nSelect an option (1-3): ")
    
    start_time = time.time()
    
    if choice == '1':
        organize_files('./data/raw')
    elif choice == '2':
        extract_emails_from_file('./data/raw/sample.txt', './data/processed/extracted_emails.txt')
    elif choice == '3':
        print("Exiting application...")
        return
    else:
        print("Invalid choice!")

    execution_time = time.time() - start_time
    print(f"\nExecution completed in {execution_time:.4f} seconds.")

if __name__ == "__main__":
    main()