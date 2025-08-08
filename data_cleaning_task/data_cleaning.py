# Import pandas to handle CSV reading and data cleaning
import pandas as pd

def clean_user_data(input_file: str, output_file: str):
    """
    Reads a CSV file, cleans the data, and saves it to a new CSV file.
    
    Steps:
    1. Remove rows missing user_id or email.
    2. Convert user_id to integer.
    3. Convert signup_date to datetime, drop invalid dates.
    4. Lowercase all emails.
    5. Convert is_active values to boolean.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Drop rows where user_id or email is missing
    df = df.dropna(subset=['user_id', 'email'])

    # Convert user_id to integer type
    df['user_id'] = df['user_id'].astype(int)

    # Convert signup_date to datetime, coercing errors to NaT (missing)
    df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')

    # Drop rows where signup_date is invalid (NaT)
    df = df.dropna(subset=['signup_date'])

    # Make all emails lowercase
    df['email'] = df['email'].str.lower()

    # Convert is_active to boolean
    df['is_active'] = df['is_active'].astype(str).str.lower().map({
        'yes': True,
        'true': True,
        '1': True,
        'no': False,
        'false': False,
        '0': False
    })

    # Save the cleaned DataFrame to a new CSV file without the index column
    df.to_csv(output_file, index=False)

    print(f"✅ Cleaned data saved to: {output_file}")

if __name__ == "__main__":
    # Run the cleaning function with your input and output files
    clean_user_data("user_data.csv", "cleaned_user_data.csv")
