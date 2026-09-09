import os
import time
import pandas as pd
import streamlit as st
from src.file_organizer import organize_files
from src.data_extractor import extract_emails

# Page Configuration & Styling
st.set_page_config(
    page_title="AutoFlow UI | CodeAlpha Suite",
    page_icon="⚡",
    layout="wide"
)

# Custom CSS for UI Enhancement
st.markdown("""
    <style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #4F46E5;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        color: #6B7280;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #F3F4F6;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #4F46E5;
    }
    </style>
""", unsafe_allow_html=True)

# Application Header
st.markdown("<div class='main-header'>⚡ CodeAlpha Task Automation Suite</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Interactive Web Interface for Automated File Sorting, Data Extraction & Performance Metrics</div>", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.image("https://img.icons8.com/color/96/python.png", width=80)
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Select Tool", ["📁 File Sorter", "📧 Email Extractor", "📊 Execution Logs"])

st.sidebar.markdown("---")
st.sidebar.info("**Internship Deliverable**\nDeveloped for CodeAlpha Python Internship (MSME Verified).")

# ---------------------------------------------------------
# TAB 1: FILE SORTER
# ---------------------------------------------------------
if menu == "📁 File Sorter":
    st.header("Directory & File Organizer")
    st.write("Automatically categorize raw files inside `data/raw/` into organized sub-folders.")

    col1, col2 = st.columns([2, 1])

    with col1:
        target_dir = st.text_input("Target Directory Path", value="data/raw")
        
        if st.button("🚀 Run File Organizer", type="primary"):
            start_time = time.time()
            count = organize_files(target_dir)
            elapsed = time.time() - start_time

            st.success(f"Successfully processed and organized {count} file(s)!")

            # Log record
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            log_line = f"[{timestamp}] Action: File Organization | Duration: {elapsed:.4f}s | Details: Organized {count} files\n"
            os.makedirs("logs", exist_ok=True)
            with open("logs/execution_log.txt", "a", encoding="utf-8") as f:
                f.write(log_line)

    with col2:
        st.subheader("Directory Preview")
        if os.path.exists(target_dir):
            items = os.listdir(target_dir)
            st.write(f"**Current Items ({len(items)}):**")
            st.json(items)
        else:
            st.warning("Directory does not exist.")

# ---------------------------------------------------------
# TAB 2: EMAIL EXTRACTOR
# ---------------------------------------------------------
elif menu == "📧 Email Extractor":
    st.header("Regex Pattern Email Extractor")
    st.write("Extract clean, deduplicated email addresses from unstructured raw text files.")

    uploaded_file = st.file_uploader("Upload a raw text/data file", type=["txt", "csv", "log"])

    if uploaded_file is not None:
        # Save temp file
        temp_path = os.path.join("data/raw", uploaded_file.name)
        os.makedirs("data/raw", exist_ok=True)
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.info(f"File uploaded to `{temp_path}`")

        out_path = "data/processed/extracted_emails.txt"

        if st.button("🔍 Extract Emails", type="primary"):
            start_time = time.time()
            count = extract_emails(temp_path, out_path)
            elapsed = time.time() - start_time

            st.success(f"Found {count} unique email address(es)!")

            # Metric Columns
            m1, m2 = st.columns(2)
            m1.metric("Emails Found", count)
            m2.metric("Processing Time", f"{elapsed:.4f} sec")

            # Display extracted results
            if os.path.exists(out_path):
                with open(out_path, "r", encoding="utf-8") as f:
                    emails = f.readlines()
                
                st.subheader("Extracted Results")
                st.code("".join(emails) if emails else "No emails found.", language="text")

                # Download Button
                st.download_button(
                    label="📥 Download Extracted Emails",
                    data="".join(emails),
                    file_name="extracted_emails.txt",
                    mime="text/plain"
                )

            # Log Record
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            log_line = f"[{timestamp}] Action: Email Extraction | Duration: {elapsed:.4f}s | Details: Extracted {count} emails\n"
            os.makedirs("logs", exist_ok=True)
            with open("logs/execution_log.txt", "a", encoding="utf-8") as f:
                f.write(log_line)

# ---------------------------------------------------------
# TAB 3: EXECUTION LOGS
# ---------------------------------------------------------
elif menu == "📊 Execution Logs":
    st.header("System Performance & Logs")
    log_file = "logs/execution_log.txt"

    if os.path.exists(log_file):
        with open(log_file, "r", encoding="utf-8") as f:
            log_data = f.readlines()

        if log_data:
            st.subheader("Real-Time Execution History")
            st.text_area("System Log File (`logs/execution_log.txt`)", value="".join(log_data), height=300)

            if st.button("🗑️ Clear Log History"):
                open(log_file, "w").close()
                st.experimental_rerun()
        else:
            st.info("Log file is empty.")
    else:
        st.warning("No execution logs found yet. Run an action first!")