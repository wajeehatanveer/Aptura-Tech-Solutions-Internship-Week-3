import pandas as pd


def read_data(file_path):
    return pd.read_csv(file_path)


def validate_data(df):
    errors = []

    required_columns = ["name", "age", "salary", "department"]

    for column in required_columns:
        if column not in df.columns:
            errors.append({
                "row": "N/A",
                "error": f"Missing column: {column}"
            })

    if errors:
        return pd.DataFrame(), pd.DataFrame(errors)

    error_rows = []

    for index, row in df.iterrows():

        # Age validation
        if pd.isna(row["age"]):
            error_rows.append({
                "row": index + 2,
                "error": "Missing age"
            })
        else:
            age = pd.to_numeric(row["age"], errors="coerce")

            if pd.isna(age) or float(age) != int(age):
                error_rows.append({
                    "row": index + 2,
                    "error": "Invalid age"
                })

        # Salary validation
        salary = pd.to_numeric(row["salary"], errors="coerce")

        if pd.notna(salary) and salary < 0:
            error_rows.append({
                "row": index + 2,
                "error": "Negative salary"
            })

        # Department validation
        if pd.isna(row["department"]) or str(row["department"]).strip() == "":
            error_rows.append({
                "row": index + 2,
                "error": "Missing department"
            })

    errors_df = pd.DataFrame(error_rows)

    return df, errors_df

def clean_data(df):
    df = df.copy()

    df["name"] = df["name"].astype(str).str.strip()
    df["department"] = df["department"].astype(str).str.strip()

    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

    df = df.dropna(subset=["age", "salary", "department"])

    df = df[df["salary"] >= 0]

    df = df.drop_duplicates()

    return df


def transform_data(df):
    df = df.copy()

    df["annual_salary"] = df["salary"] * 12

    return df


def calculate_statistics(df):
    return {
        "total_records": len(df),
        "average_salary": df["salary"].mean(),
        "maximum_salary": df["salary"].max(),
        "minimum_salary": df["salary"].min(),
        "total_salary": df["salary"].sum()
    }


def save_clean_data(df, file_path="clean_data.csv"):
    df.to_csv(file_path, index=False)


def save_error_log(errors, file_path="error_log.csv"):
    errors.to_csv(file_path, index=False)