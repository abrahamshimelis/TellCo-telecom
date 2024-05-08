import pandas as pd

def check_missing_data(df):
    """
    Check for missing data in a DataFrame and return a summary of missing values.
    
    Parameters:
    - df: Pandas DataFrame
    
    Returns:
    - DataFrame or str: Summary of missing data or success message
    """
    missing_data = df.isnull().sum()
    missing_data_summary = pd.DataFrame({
        'Column Name': missing_data.index,
        'Missing Values': missing_data.values,
        'Percentage Missing': (missing_data.values / len(df)) * 100
    })
    missing_data_summary = missing_data_summary[missing_data_summary['Missing Values'] > 0]
    
    if missing_data_summary.empty:
        return "Success: No missing values."
    else:
        # Keep only the required columns
        missing_data_summary = missing_data_summary[['Column Name', 'Missing Values']]
        
        return missing_data_summary


def check_duplicates(df):
    """
    Check for duplicate rows in a DataFrame and return a summary.
    
    Parameters:
    - df: Pandas DataFrame
    
    Returns:
    - DataFrame or str: Summary of duplicate rows or success message
    """
    # Find duplicate rows
    duplicates = df[df.duplicated(keep='first')]
    
    if duplicates.empty:
        return "Success: No duplicated values."
    else:
        # Get the first column name
        first_column_name = df.columns[0]
        
        # Get the first column value from the duplicated rows
        duplicates_summary = duplicates[[first_column_name]].copy()
        duplicates_summary['Number of Duplicates'] = duplicates.groupby(first_column_name)[first_column_name].transform('count')
        
        # Drop duplicate rows from the summary
        duplicates_summary.drop_duplicates(inplace=True)
        
        return duplicates_summary



def check_data_types(df):
    """
    Check data types of columns in a DataFrame and return a summary.
    
    Parameters:
    - df: Pandas DataFrame
    
    Returns:
    - DataFrame or str: Summary of columns with different data types or success message
    """
    dtypes_summary = df.dtypes.reset_index()
    dtypes_summary.columns = ['Column Name', 'Data Type']
    
    # Group by column name and get the unique data types per column
    grouped = dtypes_summary.groupby('Column Name')['Data Type'].apply(list).reset_index()
    
    # Create a new column for the number of unique data types per column
    grouped['Number of Different Data Types'] = grouped['Data Type'].apply(len)
    
    # Filter out columns with uniform data types
    non_uniform_columns = grouped[grouped['Number of Different Data Types'] > 1].copy()
    
    if non_uniform_columns.empty:
        return "Success: Data types per column are uniform."
    else:
        # Rename the 'Data Type' column to 'List of Data Types'
        non_uniform_columns.rename(columns={'Data Type': 'List of Data Types'}, inplace=True)
        return non_uniform_columns
