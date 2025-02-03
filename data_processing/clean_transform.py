import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

def load_data(filepath):
    try:
        df = pd.read_csv(filepath)
        logger.info(f"Loaded data from {filepath}")
        return df
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        return None

def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()
    # Handle missing values – here using forward fill; modify as needed.
    df = df.fillna(method='ffill')
    # Standardize formats – e.g., trim strings.
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()
    logger.info("Data cleaning completed")
    return df

def save_data(df, filepath):
    try:
        df.to_csv(filepath, index=False)
        logger.info(f"Cleaned data saved to {filepath}")
    except Exception as e:
        logger.error(f"Error saving data: {e}")

def main():
    input_file = '../raw_data/raw_data.csv'      # Ensure this file exists
    output_file = '../raw_data/cleaned_data.csv'
    df = load_data(input_file)
    if df is not None:
        df_clean = clean_data(df)
        save_data(df_clean, output_file)

if __name__ == "__main__":
    main()
