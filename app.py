import os
import time
import pandas as pd
import plotly.express as px
import streamlit as st

# Import core modules
from src.file_organizer import organize_files
from src.data_extractor import extract_emails
from src.speed_optimizer import measure_execution_time

# ---------------------------------------------------------
# PAGE CONFIGURATION & STYLING
# ---------------------------------------------------------
st.set_page_config(
    page_title="AutoFlow | CodeAlpha Task Automation",
    page_icon="⚡",
    layout="wide"
)

st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%);
        padding: 1.5rem 2rem;
        border-radius: 12px;
        color: white;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #F8FAFC;
        border-left: 5px solid #2563EB;
        padding: 1rem;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.markdown("""
    <div class="main-header">
        <h1>⚡ AutoFlow Automation Engine</h1>
        <p>File Sorting • Data Pattern Extraction • Performance Benchmark Optimization</p>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
st.sidebar.image("https://img.icons8.com/color/96/python.png", width=60)
st.sidebar.title("Automation Hub")

menu = st.sidebar.radio(
    "Select Feature",
    ["📁 File Sorting", "📧 Data Extraction", "⚡ Performance Metrics & Logs"]
)

st.sidebar.markdown("---")
st.sidebar.info("**CodeAlpha Internship Project**\nPython Task Automation Suite")

# Log Helper Function
def log_metric(action, duration, details):
    os.makedirs("logs", exist_ok=True)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} | Action: {action} | Duration: {duration:.6f}s | Details: {details}\n"
    with open("logs/execution_log.txt", "a", encoding="utf-8") as f:
        f.write(log_entry)

# ---------------------------------------------------------
# FEATURE 1: FILE SORTING
# ---------------------------------------------------------
if menu == "📁 File Sorting":
    st.subheader("📁 Automated File Sorter")
    st.write("Scan and organize raw unstructured files into designated subdirectories based on extension.")

    col1, col2 = st.columns([1.5, 1])

    with col1:
        dir_path = st.text_input("Target Directory Folder", value="data/raw")
        
        if st.button("🚀 Run File Sorter", type="primary"):
            if not os.path.exists(dir_path):
                st.error(f"Directory `{dir_path}` does not exist.")
            else:
                # Wrap execution using speed optimizer measurement
                @measure_execution_time
                def execute_sorting(path):
                    return organize_files(path)

                with st.spinner("Sorting files..."):
                    count, exec_time = execute_sorting(dir_path)

                st.success(f"Organized {count} file(s) in {exec_time:.4f} seconds!")
                log_metric("File Sorting", exec_time, f"Sorted {count} files")

                m1, m2 = st.columns(2)
                m1.metric("Files Moved", count)
                m2.metric("Latency", f"{exec_time:.4f}s")

    with col2:
        st.markdown("##### Folder Explorer")
        if os.path.exists(dir_path):
            files = os.listdir(dir_path)
            st.dataframe(pd.DataFrame(files, columns=["Directory Contents"]), use_container_width=True, height=250)

# ---------------------------------------------------------
# FEATURE 2: DATA EXTRACTION
# ---------------------------------------------------------
elif menu == "📧 Data Extraction":
    st.subheader("📧 Regex Data Extraction Engine")
    st.write("Extract, clean, and deduplicate valid email address patterns from unstructured raw input files.")

    uploaded_file = st.file_uploader("Upload raw file for scanning", type=["txt", "csv", "log"])

    if uploaded_file is not None:
        raw_path = os.path.join("data/raw", uploaded_file.name)
        os.makedirs("data/raw", exist_ok=True)
        with open(raw_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.info(f"File uploaded to `{raw_path}`")
        out_path = "data/processed/extracted_emails.txt"

        if st.button("🔍 Extract Email Patterns", type="primary"):
            @measure_execution_time
            def execute_extraction(inp, out):
                return extract_emails(inp, out)

            with st.spinner("Executing regex pattern parsing..."):
                count, exec_time = execute_extraction(raw_path, out_path)

            st.success(f"Successfully extracted {count} unique email pattern(s)!")
            log_metric("Data Extraction", exec_time, f"Extracted {count} emails")

            c1, c2 = st.columns(2)
            c1.metric("Extracted Emails", count)
            c2.metric("Execution Speed", f"{exec_time:.4f}s")

            if os.path.exists(out_path):
                with open(out_path, "r", encoding="utf-8") as f:
                    results = f.read()
                
                st.subheader("Extracted Email Output")
                st.code(results if results else "No valid email patterns found.")
                st.download_button("📥 Download Extracted Emails", data=results, file_name="extracted_emails.txt")

# ---------------------------------------------------------
# FEATURE 3: PERFORMANCE METRICS & LOGS
# ---------------------------------------------------------
elif menu == "⚡ Performance Metrics & Logs":
    st.subheader("⚡ Performance Metrics & Execution Benchmarks")
    st.write("Track runtime performance trends, execution latencies, and speed optimization benchmarks.")

    log_file = "logs/execution_log.txt"

    if os.path.exists(log_file):
        with open(log_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        parsed_metrics = []
        for line in lines:
            try:
                parts = line.strip().split(" | ")
                if len(parts) == 4:
                    timestamp, action, duration, details = parts
                    dur_val = float(duration.replace("Duration: ", "").replace("s", ""))
                    parsed_metrics.append({
                        "Timestamp": timestamp,
                        "Feature": action.replace("Action: ", ""),
                        "Execution Latency (Seconds)": dur_val,
                        "Details": details.replace("Details: ", "")
                    })
            except Exception:
                continue

        if parsed_metrics:
            df = pd.DataFrame(parsed_metrics)

            # Metric Summary Cards
            col_a, col_b, col_c = st.columns(3)
            col_a.metric("Total Operations", len(df))
            col_b.metric("Avg Latency", f"{df['Execution Latency (Seconds)'].mean():.4f}s")
            col_c.metric("Optimal Fast Run", f"{df['Execution Latency (Seconds)'].min():.4f}s")

            st.markdown("---")
            st.markdown("##### Real-Time Execution Latency Chart")

            fig = px.line(
                df, 
                x="Timestamp", 
                y="Execution Latency (Seconds)", 
                color="Feature",
                markers=True,
                title="Performance Optimization Benchmark (Latency over Time)"
            )
            fig.update_layout(template="plotly_white")
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("##### System Log History Table")
            st.dataframe(df, use_container_width=True)
        else:
            st.info("Log file is currently empty.")
    else:
        st.warning("No performance metrics available yet. Execute File Sorting or Data Extraction first!")