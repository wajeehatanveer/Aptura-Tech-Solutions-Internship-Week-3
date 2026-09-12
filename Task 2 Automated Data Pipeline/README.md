
## Aptura Tech Solutions – Python Internship
### Week3

# 🔄 Automated Data Pipeline

A professional Python-based **Automated Data Pipeline** built as part of the **Aptura Tech Solutions Python Internship – Week 3**.

The project processes raw CSV data through multiple stages including **validation, cleaning, transformation, analysis, and export**. A Streamlit interface provides an easy-to-use dashboard for managing the complete pipeline.

---

## 📌 Project Overview

The Automated Data Pipeline is designed to convert raw and potentially inconsistent datasets into a clean, structured, and analysis-ready dataset.

The pipeline follows this workflow:

**Raw Data → Validation → Cleaning → Transformation → Analytics → Export**

It identifies invalid records, cleans the dataset, transforms selected fields, generates useful statistics, and produces both a clean dataset and an error log.

---

## ✨ Features

- 📂 Upload CSV datasets
- 🔍 Validate incoming data
- ⚠️ Detect missing and invalid values
- 🧹 Clean invalid records
- 🔄 Transform selected data fields
- 📊 Generate summary statistics
- 📈 Display processed dataset analytics
- 💾 Export cleaned data as CSV
- 📝 Generate validation/error logs
- 🖥️ Professional Streamlit dashboard
- 🔄 Multi-stage pipeline workflow
- 📋 Preview uploaded and processed data

---

## 🧩 Pipeline Stages

### 1. 📂 Data Ingestion
Reads raw CSV data into a Pandas DataFrame.

### 2. 🔍 Data Validation
Checks for missing, invalid, or inconsistent values and records errors.

### 3. 🧹 Data Cleaning
Removes invalid records and prepares clean data for processing.

### 4. 🔄 Data Transformation
Transforms selected fields, including calculating Annual Salary.

### 5. 📊 Analytics
Generates summary statistics such as average, minimum, maximum, and total salary.

### 6. 💾 Export
Exports the cleaned dataset and error log as CSV files.

---


## 🧪 Sample Dataset

A sample dataset can be used to test the pipeline:

```csv
id,name,age,department,salary
1,Ali,25,IT,55000
2,Sara,28,HR,60000
3,Ahmed,22,IT,45000
4,Ayesha,30,Finance,75000
5,Usman,26,Marketing,52000
6,Hina,24,IT,48000
7,Bilal,,HR,58000
8,Zain,27,Finance,-5000
```

The dataset intentionally contains invalid records to test the validation stage.

Expected issues include:

* Missing age
* Negative salary

---

## 📈 Example Processing Result

After validation and cleaning, the valid records can be transformed into:

| Name   | Age | Department | Salary | Annual Salary |
| ------ | --: | ---------- | -----: | ------------: |
| Ali    |  25 | IT         | 55,000 |       660,000 |
| Sara   |  28 | HR         | 60,000 |       720,000 |
| Ahmed  |  22 | IT         | 45,000 |       540,000 |
| Ayesha |  30 | Finance    | 75,000 |       900,000 |
| Usman  |  26 | Marketing  | 52,000 |       624,000 |
| Hina   |  24 | IT         | 48,000 |       576,000 |

---


## 🧪 Testing & Validation

The pipeline was tested using datasets containing both valid and invalid records.

Testing included:

* Valid age values
* Missing age values
* Negative salary values
* Valid salary values
* Invalid records
* Data cleaning
* Salary transformation
* Summary statistics
* CSV export
* Error-log generation

The pipeline successfully separates valid records from invalid records and produces a clean dataset for further analysis.

---

## 📊 Results

The completed pipeline successfully performs:

```text
Upload
   ↓
Validate
   ↓
Clean
   ↓
Transform
   ↓
Analyze
   ↓
Export
```

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **Streamlit**
- **CSV / JSON Data Processing**

---

## 📁 Project Structure

```text
Automated Data Pipeline/
├──screenshots/
├── app.py
├── clean_data.csv
├── data_pipeline.py
├── error_log.csv
├── raw_data.csv
└── README.md
```
---

## ⚙️ Installation

### 3. Install Required Libraries

```bash
pip install streamlit pandas
```

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

---

---

## 👩‍💻 Author

**Wajeeha Tanveer**

---

