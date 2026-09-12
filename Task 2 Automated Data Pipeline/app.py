import streamlit as st
import pandas as pd

from data_pipeline import (
    validate_data,
    clean_data,
    transform_data,
    calculate_statistics,
    save_clean_data,
    save_error_log
)

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="DataFlow Hub",
    page_icon="🔗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* ================================
   GENERAL
================================ */

.stApp {
    background: linear-gradient(135deg, #f8f7fc 0%, #f0edf8 100%);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}

/* ================================
   SIDEBAR
================================ */

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #21145c 0%, #171044 100%);
    min-width: 270px;
}

[data-testid="stSidebar"] > div:first-child {
    padding: -80px 18px;
}

.sidebar-brand {
    padding: 10px 12px 30px 12px;
}

.sidebar-logo {
    font-size: 38px;
    color: #c7a8ff;
}

.sidebar-name {
    color: white;
    font-size: 23px;
    font-weight: 750;
    margin-top: 6px;
}

.sidebar-caption {
    color: #aaa1d1;
    font-size: 12px;
    margin-top: 3px;
}

.sidebar-divider {
    height: 1px;
    background: rgba(255,255,255,0.12);
    margin: 0 5px 22px 5px;
}

/* Sidebar buttons */

[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    min-height: 50px;
    border: none;
    border-radius: 12px;
    background: transparent;
    color: #e7e2f5;
    text-align: left;
    font-size: 15px;
    font-weight: 550;
    padding-left: 18px;
    margin-bottom: 7px;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(143, 91, 232, 0.22);
    color: white;
    border: none;
}

/* ================================
   TOP HEADER
================================ */

.top-header {
    display: block;
    width: 100%;
    margin-bottom: 24px;
    padding: 4px 2px;
    overflow: visible;
}

.page-label {
    display: ck;
    width: 100%;
    color: #766b91;
    font-size: 16px;
    line-height: 1.5;
    font-weight: 700;
    letter-spacing: 0.5px;
    white-space: normal;
    overflow: visible;
    text-overflow: clip;
    margin-bottom: 3px;
    margin-top: 20px
}

.page-heading {
    display: block;
    color: #241653;
    font-size: 25px;
    line-height: 1.3;
    font-weight: 750;
    margin: 0;
}

/* ================================
   DASHBOARD HERO
================================ */

.hero {
    background: white;
    border: 1px solid #e4dff0;
    border-radius: 20px;
    padding: 32px 36px;
    min-height: 280px;
    box-shadow: 0 8px 30px rgba(55, 35, 100, 0.08);
    margin-bottom: 28px;
    box-sizing: border-box;
    overflow: hidden;
}

.hero-title {
    color: #21145c;
    font-size: 34px;
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 15px;
}

.hero-description {
    color: #5f5870;
    font-size: 16px;
    line-height: 1.7;
    max-width: 550px;
}

.hero-badge {
    display: inline-block;
    margin-top: 25px;
    padding: 9px 17px;
    background: #eee6ff;
    color: #6335a4;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 650;
}

.hero-chart {
    width: 100%;
    padding: 5px 0;
}

.hero-chart-title {
    color: #756b88;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 8px;
}

/* ================================
   RESPONSIVE
================================ */

@media (max-width: 900px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .hero {
        padding: 25px;
    }

    .hero-title {
        font-size: 28px;
    }

    .hero-description {
        font-size: 14px;
    }

    .page-label {
        font-size: 12px;
    }

    .page-heading {
        font-size: 22px;
    }
}
/* ================================
   SECTION TITLES
================================ */

.section-title {
    color: #241653;
    font-size: 24px;
    font-weight: 750;
    margin-bottom: 5px;
}

.section-description {
    color: #81788f;
    font-size: 14px;
    margin-bottom: 18px;
}

/* ================================
   OVERVIEW CARD
================================ */

.overview-card {
    background: white;
    border: 1px solid #e4dff0;
    border-radius: 18px;
    padding: 30px;
    min-height: 190px;
    box-shadow: 0 7px 25px rgba(55, 35, 100, 0.06);
}

.empty-icon {
    font-size: 55px;
    text-align: center;
}

.empty-title {
    color: #241653;
    font-size: 21px;
    font-weight: 750;
    margin-top: 10px;
}

.empty-text {
    color: #81788f;
    font-size: 14px;
    margin-top: 7px;
}

/* ================================
   METRIC CARDS
================================ */

.metric-card {
    background: white;
    border: 1px solid #e4dff0;
    border-radius: 15px;
    padding: 22px;
    box-shadow: 0 6px 20px rgba(55, 35, 100, 0.06);
}

.metric-label {
    color: #81788f;
    font-size: 13px;
    font-weight: 600;
}

.metric-value {
    color: #29175f;
    font-size: 26px;
    font-weight: 800;
    margin-top: 8px;
}

/* ================================
   CONTENT CARDS
================================ */

.content-card {
    background: white;
    border: 1px solid #e4dff0;
    border-radius: 16px;
    padding: 25px;
    box-shadow: 0 6px 22px rgba(55, 35, 100, 0.05);
}

.card-title {
    color: #29175f;
    font-size: 19px;
    font-weight: 750;
}

.card-description {
    color: #81788f;
    font-size: 13px;
    margin-top: 5px;
    margin-bottom: 18px;
}

/* ================================
   BUTTONS
================================ */

.stButton > button {
    border-radius: 10px;
    border: 1px solid #d8cde9;
    background: white;
    color: #4b3572;
    font-weight: 650;
    min-height: 43px;
}

.stButton > button:hover {
    background: #eee8fa;
    border-color: #9b78d0;
    color: #321b67;
}

/* ================================
   DOWNLOAD BUTTON
================================ */

.stDownloadButton > button {
    border-radius: 10px;
    min-height: 44px;
    font-weight: 650;
    border: 1px solid #d6c8e9;
}

/* ================================
   STATUS
================================ */

.status-card {
    background: #faf8fe;
    border: 1px solid #e3dbef;
    border-radius: 12px;
    padding: 17px;
    text-align: center;
}

.status-icon {
    font-size: 23px;
}

.status-title {
    color: #382265;
    font-size: 13px;
    font-weight: 700;
    margin-top: 5px;
}

/* ================================
   FILE UPLOADER
================================ */

[data-testid="stFileUploader"] {
    background: #faf8fe;
    border: 2px dashed #cfc0e4;
    border-radius: 14px;
    padding: 10px;
}

/* ================================
   DATAFRAME
================================ */

[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
}

/* ================================
   MOBILE
================================ */

@media (max-width: 900px) {
    .hero-title {
        font-size: 27px;
    }

    .hero {
        padding: 25px;
    }
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "data" not in st.session_state:
    st.session_state.data = None

if "errors" not in st.session_state:
    st.session_state.errors = pd.DataFrame()

if "final_data" not in st.session_state:
    st.session_state.final_data = None

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
<div class="sidebar-brand">
<div class="sidebar-logo">⌁</div>
<div class="sidebar-name">DataFlow Hub</div>
<div class="sidebar-caption">Automated Data Pipeline</div>
</div>
<div class="sidebar-divider"></div>
""", unsafe_allow_html=True)

    if st.button("⌂   Dashboard", key="side_dashboard"):
        st.session_state.page = "Dashboard"
        st.rerun()

    if st.button("↑   Upload Data", key="side_upload"):
        st.session_state.page = "Upload Data"
        st.rerun()

    if st.button("♡   Validation", key="side_validation"):
        st.session_state.page = "Validation"
        st.rerun()

    if st.button("⚙   Processing", key="side_processing"):
        st.session_state.page = "Processing"
        st.rerun()

    if st.button("⌁   Analytics", key="side_analytics"):
        st.session_state.page = "Analytics"
        st.rerun()

    if st.button("⇩   Export Results", key="side_export"):
        st.session_state.page = "Export Results"
        st.rerun()

# =========================================================
# DASHBOARD
# =========================================================

if st.session_state.page == "Dashboard":

    st.markdown("""
    <div class="top-header">
        <div class="page-label">DATA OPERATIONS</div>
        <div class="page-heading">Dashboard</div>
    </div>
    """, unsafe_allow_html=True)

    hero_left, hero_right = st.columns([1.05, 0.95], gap="large")

    with hero_left:
        st.markdown(
        '<div class="hero">'
        '<div class="hero-title">Automated Data Pipeline</div>'
        '<div class="hero-description">'
        'Orchestrate, monitor, and automate your entire data journey '
        'from source to insight.'
        '</div>'
        '<div class="hero-badge">'
        '✦ Smart &nbsp;•&nbsp; Reliable &nbsp;•&nbsp; Scalable'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
            
    with hero_right:

        st.markdown("""
        <div class="hero-chart-title">
            Pipeline Progress
        </div>
        """, unsafe_allow_html=True)

        chart_data = pd.DataFrame({
            "Stage": [
                "Start",
                "Ingest",
                "Validate",
                "Process",
                "Enrich",
                "Load"
            ],
            "Progress": [
                20,
                37,
                56,
                82,
                70,
                87
            ]
        })

        st.line_chart(
            chart_data.set_index("Stage"),
            height=250
        )

    st.markdown("""
    <div class="section-title">
        Pipeline Overview
    </div>

    <div class="section-description">
        Monitor your current data processing workflow.
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.final_data is None:

        st.markdown("""
        <div class="overview-card">
            <div style="text-align: center;">
                <div class="empty-icon">🗄️</div>
                <div class="empty-title">No dataset processed yet</div>
                <div class="empty-text">
                    Go to Upload Data to begin.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 1.2, 1])

        with col2:

            if st.button(
                "↑   Start New Pipeline",
                use_container_width=True,
                key="dashboard_start"
            ):
                st.session_state.page = "Upload Data"
                st.rerun()

    else:

        stats = calculate_statistics(
            st.session_state.final_data
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">
                    Processed Records
                </div>
                <div class="metric-value">
                    {stats["total_records"]}
                </div>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">
                    Average Salary
                </div>
                <div class="metric-value">
                    Rs. {stats["average_salary"]:,.0f}
                </div>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">
                    Maximum Salary
                </div>
                <div class="metric-value">
                    Rs. {stats["maximum_salary"]:,.0f}
                </div>
            </div>
            """, unsafe_allow_html=True)

        with c4:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">
                    Detected Errors
                </div>
                <div class="metric-value">
                    {len(st.session_state.errors)}
                </div>
            </div>
            """, unsafe_allow_html=True)


# =========================================================
# UPLOAD DATA
# =========================================================

elif st.session_state.page == "Upload Data":

    st.markdown("""
    <div class="top-header">
        <div>
            <div class="page-label">DATA INPUT</div>
            <div class="page-heading">Upload Data</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
                <div class="hero">
                <div class="hero-title">Bring Your Data In</div>
                <div class="hero-description">
                Upload a CSV dataset and let DataFlow Hub handle
                validation, cleaning, transformation and analysis.
                </div>
                <div class="hero-badge">
                CSV DATA SOURCE
                </div>
                </div>
                """, unsafe_allow_html=True)

    with st.container(border=True):

        st.markdown(
            '<div class="card-title">📂 Dataset Upload</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="card-description">'
            'Choose a CSV file to start a new pipeline.'
            '</div>',
            unsafe_allow_html=True
        )

        uploaded_file = st.file_uploader(
            "Upload CSV",
            type=["csv"],
            key="csv_uploader"
        )

        if uploaded_file:

            df = pd.read_csv(uploaded_file)

            st.session_state.data = df

            st.success(
                f"Dataset uploaded successfully — "
                f"{len(df)} records found."
            )

            st.markdown("### Data Preview")

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )


# =========================================================
# VALIDATION
# =========================================================

elif st.session_state.page == "Validation":

    st.markdown("""
    <div class="top-header">
        <div>
            <div class="page-label">QUALITY CONTROL</div>
            <div class="page-heading">Data Validation</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
                <div class="hero">
                <div class="hero-title">Validate Your Dataset</div>
                <div class="hero-description">
                Identify missing values, invalid fields and inconsistent records
                before the data moves to the processing stage.
                </div>
                <div class="hero-badge">
                QUALITY CHECK
                </div>
                </div>
                """, unsafe_allow_html=True)
                
    if st.session_state.data is None:

        st.info(
            "No dataset available. Please upload your data first."
        )

    else:

        errors = validate_data(
            st.session_state.data
        )[1]

        st.session_state.errors = errors

        if errors.empty:

            st.success(
                "✓ Validation completed — no issues found."
            )

        else:

            st.warning(
                f"{len(errors)} validation issue(s) detected."
            )

            st.dataframe(
                errors,
                use_container_width=True,
                hide_index=True
            )


# =========================================================
# PROCESSING
# =========================================================

elif st.session_state.page == "Processing":

    st.markdown("""
    <div class="top-header">
        <div>
            <div class="page-label">DATA ENGINE</div>
            <div class="page-heading">Clean & Transform</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
                <div class="hero">
                <div class="hero-title">Process Your Dataset</div>
                <div class="hero-description">
                Clean invalid records, remove duplicates and transform
                your raw dataset into analysis-ready data.
                </div>

                <div class="hero-badge">
                PROCESSING ENGINE
                </div>
                </div>
                """, unsafe_allow_html=True)

    if st.session_state.data is None:

        st.info(
            "No dataset available. Please upload your data first."
        )

    else:

        st.markdown("""
                    <div class="content-card">
                    <div class="card-title">
                    ⚙ Processing Engine
                    </div>

                    <div class="card-description">
                    Run the complete cleaning and transformation workflow.
                    </div>
                    </div>
                    """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button(
            "⚙   Process Dataset",
            use_container_width=True,
            key="process_dataset"
        ):

            errors = validate_data(
                st.session_state.data
            )[1]

            cleaned = clean_data(
                st.session_state.data
            )

            final_data = transform_data(
                cleaned
            )

            st.session_state.errors = errors
            st.session_state.final_data = final_data

            save_clean_data(final_data)
            save_error_log(errors)

            st.success(
                "✓ Dataset processed successfully!"
            )

        if st.session_state.final_data is not None:

            st.markdown(
                "### Clean & Transformed Data"
            )

            st.dataframe(
                st.session_state.final_data,
                use_container_width=True,
                hide_index=True
            )


# =========================================================
# ANALYTICS
# =========================================================

elif st.session_state.page == "Analytics":

    st.markdown("""
    <div class="top-header">
        <div>
            <div class="page-label">INSIGHTS</div>
            <div class="page-heading">Analytics</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
                <div class="hero">
                <div class="hero-title">Dataset Insights</div>

                <div class="hero-description">
                Explore summary statistics generated from your processed dataset.
                </div>

                <div class="hero-badge">
                DATA ANALYTICS
                </div>
                </div>
                """, unsafe_allow_html=True)

    if st.session_state.final_data is None:

        st.info(
            "Process a dataset first to view analytics."
        )

    else:

        stats = calculate_statistics(
            st.session_state.final_data
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Total Records",
            stats["total_records"]
        )

        c2.metric(
            "Average Salary",
            f'Rs. {stats["average_salary"]:,.0f}'
        )

        c3.metric(
            "Maximum Salary",
            f'Rs. {stats["maximum_salary"]:,.0f}'
        )

        c4.metric(
            "Minimum Salary",
            f'Rs. {stats["minimum_salary"]:,.0f}'
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            '<div class="section-title">'
            'Processed Dataset'
            '</div>',
            unsafe_allow_html=True
        )

        st.dataframe(
            st.session_state.final_data,
            use_container_width=True,
            hide_index=True
        )


# =========================================================
# EXPORT RESULTS
# =========================================================

elif st.session_state.page == "Export Results":

    st.markdown("""
    <div class="top-header">
        <div>
            <div class="page-label">OUTPUT CENTER</div>
            <div class="page-heading">Export Results</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
                <div class="hero">
                <div class="hero-title">Your Results Are Ready</div>

                <div class="hero-description">
                Download the cleaned dataset and validation report
                generated by your automated pipeline.
                </div>

                <div class="hero-badge">
                EXPORT CENTER
                </div>
                </div>
                """, unsafe_allow_html=True)

    uploaded = st.session_state.data is not None
    processed = st.session_state.final_data is not None

    s1, s2, s3, s4 = st.columns(4)

    with s1:

        st.markdown(f"""
                    
                    <div class="status-card">
                    <div class="status-icon">
                    {"✓" if uploaded else "○"}
                    </div>

                    <div class="status-title">
                    Uploaded
                    </div>
                    </div>
                    """, unsafe_allow_html=True)

    with s2:

        st.markdown(f"""
                    <div class="status-card">
                    <div class="status-icon">
                    {"✓" if uploaded else "○"}
                    </div>

                    <div class="status-title">
                    Validated
                    </div>
                    </div>
                    """, unsafe_allow_html=True)

    with s3:

        st.markdown(f"""
                    <div class="status-card">
                    <div class="status-icon">
                    {"✓" if processed else "○"}
                    </div>

                    <div class="status-title">
                    Processed
                    </div>
                    </div>
                    """, unsafe_allow_html=True)

    with s4:

        st.markdown(f"""
                    <div class="status-card">
                    <div class="status-icon">
                    {"✓" if processed else "○"}
                    </div>

                    <div class="status-title">
                    Ready to Export
                    </div>
                    </div>
                    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if not processed:

        st.markdown("""
                    <div class="overview-card">
                    <div style="text-align:center;">

                    <div class="empty-icon">
                    📁
                    </div>

                    <div class="empty-title">
                    No Processed Dataset Yet
                    </div>

                    <div class="empty-text">
                    Upload your data and run the processing pipeline first.
                    Your downloadable results will appear here.
                    </div>

                    </div>
                    </div>
                    """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        c1, c2, c3 = st.columns([1, 1.3, 1])

        with c2:

            if st.button(
                "↑   Start New Pipeline",
                use_container_width=True,
                key="export_start_pipeline"
            ):

                st.session_state.page = "Upload Data"
                st.rerun()

    else:

        st.success(
            "✓ Processing complete. Your results are ready to download."
        )

        st.markdown("<br>", unsafe_allow_html=True)

        left, right = st.columns(2, gap="large")

        with left:

            st.markdown("""
                        <div class="content-card">
                        <div style="font-size:36px;">
                        📄
                        </div>

                        <div class="card-title">
                        Cleaned Dataset
                        </div>

                        <div class="card-description">
                        Validated, cleaned and transformed CSV data
                        ready for use.
                        </div>

                        </div>
                        """, unsafe_allow_html=True)

            st.download_button(
                "↓   Download Clean Data",
                st.session_state.final_data.to_csv(index=False),
                "clean_data.csv",
                "text/csv",
                use_container_width=True,
                key="download_clean_data"
            )

        with right:

            st.markdown("""
                        <div class="content-card">

                        <div style="font-size:36px;">
                        ⚠️
                        </div>

                        <div class="card-title">
                        Validation Error Log
                        </div>

                        <div class="card-description">
                        Review the issues detected during
                        the validation stage.
                        </div>

                        </div>
                        """, unsafe_allow_html=True)

            if st.session_state.errors.empty:

                st.success(
                    "✓ No validation errors detected."
                )

            else:

                st.warning(
                    f"{len(st.session_state.errors)} issue(s) detected."
                )

                with st.expander(
                    "View Error Details"
                ):

                    st.dataframe(
                        st.session_state.errors,
                        use_container_width=True,
                        hide_index=True
                    )

            st.download_button(
                "↓   Download Error Log",
                st.session_state.errors.to_csv(index=False),
                "error_log.csv",
                "text/csv",
                use_container_width=True,
                key="download_error_log"
            )