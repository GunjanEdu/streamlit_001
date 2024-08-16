import streamlit as st
import pickle
import pandas as pd

# Load the DataFrame from the .plk file
with open('sample_data.plk', 'rb') as file:
    df = pickle.load(file)

# Streamlit app
st.title("Data Interaction App samples....")

# Display the DataFrame
st.write("Data loaded from the .plk file:")
st.write(df)

# User interaction: filter the DataFrame
st.write("Filter the data based on Feature1 value:")
feature1_min = st.slider("Minimum Feature1", min_value=int(df['Feature1'].min()), max_value=int(df['Feature1'].max()), value=int(df['Feature1'].min()))
filtered_df = df[df['Feature1'] >= feature1_min]

st.write("Filtered data:")
st.write(filtered_df)




# Option to download the filtered data
if st.button("Download"):
    with open('filtered_data.plk', 'wb') as file:
        pickle.dump(filtered_df, file)
    
    with open('filtered_data.plk', 'rb') as file:
        st.download_button(
            label="Download .plk file",
            data=file,
            file_name="filtered_data.plk",
            mime="application/octet-stream"
        )
