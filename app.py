import streamlit as st
import pandas as pd

# Load CSV data
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.warning("File not found. Please check the file path.")
        return pd.DataFrame()  # Return an empty DataFrame if file not found
    except pd.errors.EmptyDataError:
        st.warning("File is empty. Please provide a valid CSV file.")
        return pd.DataFrame()  # Return an empty DataFrame if file is empty
    except Exception as e:
        st.warning(f"An error occurred while loading the file: {e}")
        return pd.DataFrame()  # Return an empty DataFrame if another error occurs

# Main Streamlit app
def main():
    st.title("Editable CSV Data Grid - ignore")

    # Specify the file path
    file_path = 'Data/UserData.csv'  # Change this to your actual file path

    # Load the data
    df = load_data(file_path)

    # Check if DataFrame is empty
    if df.empty:
        st.warning("No data to display. Please check your file.")
        return

    # Display the editable dataframe
    edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)

    # If changes were made, update the data
    if st.button('Update Data'):
        edited_df.to_csv(file_path, index=False)
        st.success("Data updated successfully!")

if __name__ == "__main__":
    main()
