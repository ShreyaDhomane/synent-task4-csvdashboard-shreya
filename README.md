# 📊 CSV Dashboard - Netflix Dataset Analysis

## Project Overview

This project is an interactive CSV Dashboard developed using Streamlit and Python. The dashboard allows users to upload a CSV dataset and explore it through visualizations, summary statistics, and dynamic analysis.

For this project, the Netflix Titles Dataset was used to analyze content distribution, ratings, countries, and release year trends.

---

## Objective

The objective of this project is to create an interactive dashboard that enables users to:

* Upload a CSV dataset
* Preview dataset records
* Analyze dataset structure
* Identify missing values
* Generate visual insights dynamically
* Filter data interactively

---

## Dataset Used

**Dataset:** Netflix Titles Dataset

The dataset contains information about Netflix Movies and TV Shows, including:

* Title
* Type (Movie / TV Show)
* Director
* Cast
* Country
* Release Year
* Rating
* Duration
* Description

---

## Features

### 1. CSV File Upload

Users can upload any CSV file through the dashboard.

### 2. Dataset Preview

Displays the first few records of the uploaded dataset.

### 3. Dataset Overview

Shows:

* Total Rows
* Total Columns
* Total Missing Values

### 4. Missing Values Analysis

Displays missing values present in each column.

### 5. Interactive Filters

Users can filter the dataset based on content type:

* Movie
* TV Show

### 6. Movies vs TV Shows Analysis

Visual comparison of Movies and TV Shows available in the dataset.

### 7. Top 10 Countries

Displays countries with the highest amount of Netflix content.

### 8. Ratings Distribution

Shows the distribution of content ratings.

### 9. Release Year Trend

Visualizes content released over different years.

### 10. Dynamic Analysis

Allows users to select any column and generate a chart dynamically.

### 11. Dataset Information

Displays column names and data types.

---

## Technologies Used

* Python
* Streamlit
* Pandas

---

## Project Structure

```text
synent-task4-csvdashboard-shreya
│
├── app.py
├── requirements.txt
├── README.md
└── netflix_titles.csv
```

---

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the application

```bash
streamlit run app.py
```

---

## Results

The dashboard successfully provides interactive analysis of the Netflix dataset through visualizations, filtering options, and dynamic chart generation.

---

## Future Improvements

* Advanced filtering options
* Additional visualizations
* Export analysis reports
* Support for multiple datasets

---

## Author

Shreya Dhomane
Data Science Internship Project
Synent Technologies
