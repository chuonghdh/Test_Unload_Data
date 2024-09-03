import streamlit as st
import pandas as pd
import os

# File path for the CSV in the Streamlit environment
local_file_path = 'local_data.csv'

# Load CSV data
def load_data(file_path):
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        st.info("Data loaded from local storage.")
    else:
        # Initial load from a repository, as a fallback (if needed)
        df = pd.read_csv('Data/UserData.csv')  # Replace with your default CSV
        df.to_csv(file_path, index=False)  # Save to local environment
        st.info("Data loaded from repository and saved to local storage.")
    return df

# Save data back to CSV
def save_data(df, file_path):
    df.to_csv(file_path, index=False)
    st.success("Data saved successfully!")

# Main Streamlit app
def main():
    st.title("Editable CSV Data Grid - update code")

    # Load the data (from local storage or repository)
    df = load_data(local_file_path)

    # Check if DataFrame is empty
    if df.empty:
        st.warning("No data to display. Please check your file.")
        return

    # Display the editable dataframe
    edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)

    # If changes were made, update the data
    if st.button('Update Data'):
        save_data(edited_df, local_file_path)

if __name__ == "__main__":
    main()
