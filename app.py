import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Netflix Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 CSV Dashboard")

# File Upload
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    # Read Dataset
    df = pd.read_csv(uploaded_file)

    st.success("Dataset Loaded Successfully!")

    # Sidebar Filters
    st.sidebar.header("Filters")

    if "type" in df.columns:
        content_type = st.sidebar.multiselect(
            "Select Type",
            options=df["type"].dropna().unique(),
            default=df["type"].dropna().unique()
        )

        filtered_df = df[
            df["type"].isin(content_type)
        ]
    else:
        filtered_df = df

    # Dataset Preview
    st.subheader("Dataset Preview")
    st.dataframe(filtered_df.head())

    # Dataset Overview
    st.subheader("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", filtered_df.shape[0])

    with col2:
        st.metric("Columns", filtered_df.shape[1])

    with col3:
        st.metric(
            "Missing Values",
            filtered_df.isnull().sum().sum()
        )

    # Missing Values Table
    st.subheader("Missing Values")

    missing_df = pd.DataFrame({
        "Column": filtered_df.columns,
        "Missing Values": filtered_df.isnull().sum().values
    })

    st.dataframe(missing_df)

    # Movies vs TV Shows
    if "type" in filtered_df.columns:

        st.subheader("Movies vs TV Shows")

        st.bar_chart(
            filtered_df["type"].value_counts()
        )

    # Top Countries
    if "country" in filtered_df.columns:

        st.subheader("Top 10 Countries")

        country_data = (
            filtered_df["country"]
            .dropna()
            .str.split(", ")
            .explode()
            .value_counts()
            .head(10)
        )

        st.bar_chart(country_data)

    # Ratings Distribution
    if "rating" in filtered_df.columns:

        st.subheader("Ratings Distribution")

        st.bar_chart(
            filtered_df["rating"]
            .value_counts()
            .head(10)
        )

    # Release Year Trend
    if "release_year" in filtered_df.columns:

        st.subheader("Content by Release Year")

        release_data = (
            filtered_df["release_year"]
            .value_counts()
            .sort_index()
        )

        st.line_chart(release_data)

    # Dynamic Analysis
    st.subheader("Dynamic Analysis")

    selected_column = st.selectbox(
        "Select Column",
        filtered_df.columns
    )

    chart_data = (
        filtered_df[selected_column]
        .astype(str)
        .value_counts()
        .head(10)
    )

    st.bar_chart(chart_data)

    # Dataset Information
    st.subheader("Dataset Information")

    st.write("Column Names:")
    st.write(filtered_df.columns.tolist())

    st.write("Data Types:")
    st.write(filtered_df.dtypes)