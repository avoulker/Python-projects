import pandas as pd
import streamlit as st  #Importing libraries

def data_analysis(data_frame):  #Function for the developer, intended only for viewing and exploring data in the terminal
    print("\n")
    print("Column names")
    name_columns = data_frame.columns.tolist()
    print(name_columns)

    print("\n")
    print("Global information")
    global_describe = data_frame.describe()
    print(global_describe)

    print("\n")
    print("Number of rows and columns")
    rows_count, columns_count = data_frame.shape
    print(rows_count, columns_count)

    print("\n")
    print("Missing values in columns")
    missing_values = data_frame.isnull().sum()
    print(missing_values)

    number_cols_with_categorical_name = data_frame.select_dtypes(include=["object", "string", "category"]).columns
    if len(number_cols_with_categorical_name) == 0:
        print("\n")
        print("No columns with categorical values")
    else:
        print("\n")
        print("Number of categorical columns")
        print(len(number_cols_with_categorical_name))

    return rows_count, global_describe, name_columns, columns_count, missing_values, number_cols_with_categorical_name  #Returning data (variables) for their further use in another function

def visualization():    #Data visualization
    st.title("Analysis of the 100 Tallest Buildings in the World")

    st.subheader("User Information")
    st.metric("Total buildings in this top list", rows)
    st.write("Cities, countries, and continents with the most tall buildings")
    st.table(describe)

    st.subheader("Technical Information")
    st.write("Column names")
    for column in name:
        st.write(f"- {column}")

    st.metric("Number of columns", cols)
    st.metric("Number of rows", rows)

    st.write("Number of missing values in each column")
    for column_name, count in missing.items():
        st.write(f"- {column_name}: {count}")

    st.metric("Number of columns with categorical values", len(number_categorical))

    st.write("Dataset")
    st.dataframe(df)

try:    #Handling potential errors
    df = pd.read_csv("top_100_tallest_buildings_world.cs")
except FileNotFoundError:
    print("File not found")
    st.title("File not found")
    exit()
else:
    rows, describe, name, cols, missing, number_categorical = data_analysis(df)
    visualization()

#The code works reliably and performs the task as intended. It is designed for a specific database, but it can serve as a template for analyzing other databases containing similar data, if needed.
#In the future, the plan is to improve this code in terms of its structure. (possibly)

#I am in great need of feedback.