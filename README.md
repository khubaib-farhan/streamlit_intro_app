# Simple Data Dashboard

A simple data dashboard built using Streamlit, allowing users to upload CSV files, preview data, filter it, and visualize selected columns.

## Features

- Upload a CSV file and preview the data.
- Display a summary of the data with descriptive statistics.
- Filter data based on unique values of a selected column.
- Visualize data with a line chart based on user-selected axes.

## Requirements

- Python 3.x
- Streamlit
- Pandas
- Matplotlib

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/khubaib-farhan/streamlit_intro_app.git

2. Install the required packages:
   ```bash
   pip install streamlit pandas matplotlib

## Usage

1. Run the Streamlit application:
  ```bash
  streamlit run app.py
  ```
2. Open your browser and navigate to http://localhost:8501 to access the dashboard.
3. Upload a CSV file to start exploring your data.

## How to Use
Upload CSV: Use the file uploader to select and upload a CSV file.

Data Preview: View the first few rows of the uploaded data.

Data Summary: Get a statistical summary of the data.

Filter Data: Choose a column to filter by and select a specific value to see the corresponding filtered data.

Data Visualization: Select the X and Y axes to generate a line chart of the filtered data.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
Streamlit - for creating an easy-to-use framework for building web applications in Python.
Pandas - for data manipulation and analysis.
Matplotlib - for data visualization.
