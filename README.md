# Sales Data Analysis & Visualization Program

## Project Overview

This project is a Python-based **Sales Data Analysis and Visualization Program** designed to demonstrate practical data analysis using **Pandas, NumPy, Matplotlib, and Seaborn**.

The program provides a menu-driven interface that allows users to load CSV datasets, explore data, perform DataFrame operations, handle missing values, generate descriptive statistics, create visualizations, and save generated plots.

If the default dataset does not exist, the program automatically creates a sample `sales_data.csv` file.

---

# Objectives

The project aims to help learners understand:

- Python file handling
- CSV data processing
- Pandas DataFrames
- NumPy arrays
- Data exploration
- Data searching
- Data sorting
- Data filtering
- Pivot tables
- Missing data handling
- Descriptive statistics
- Data visualization
- Matplotlib
- Seaborn
- Object-Oriented Programming
- Menu-driven programming
- Exception handling

---
# Features

## 1. Automatic Sample Dataset Creation

The program checks whether the default CSV dataset exists.

If `sales_data.csv` does not exist, the program automatically creates a sample dataset containing:

- Sales ID
- Product
- Region
- Sales
- Year

The sample dataset is saved as:

`sales_data.csv`

---
## 2. Load Dataset

- Users can load a CSV dataset by providing its file path.

- If no path is entered, the program uses the default file:

`sales_data.csv`

- The program validates whether the file exists before attempting to load it.
---
## 3. Explore Data

The program allows users to explore the loaded dataset.

### Available options include:

- Display the first 5 rows
- Display the last 5 rows
- Display column names
- Display column data types
- Display basic DataFrame information
---
## 4. DataFrame Operations

The program provides several DataFrame operations.

### Search

Search for a value inside a selected column.

The search is case-insensitive and can find matching text values.

### Sort

Sort the dataset using a selected column.

Users can choose:

- Ascending order
- Descending order
### Filter

Filter numerical data using a threshold.

For example:

Sales > 500
### Pivot Table

Create a Pandas pivot table using:

- Index column
- Values column
- Aggregation function
### Convert DataFrame Column to NumPy Array

Users can select a DataFrame column and convert it into a NumPy array using:

to_numpy()

---
## 5. Handle Missing Data

The program provides multiple options for handling missing values.

Users can:

- Display rows containing missing values
- Fill missing numerical values with the column mean
- Drop rows containing missing values
- Replace missing values with a user-provided value

---
## 6. Generate Descriptive Statistics

The program generates descriptive statistical information using Pandas.

It displays:

- Count
- Mean
- Standard deviation
- Minimum
- 25th percentile
- Median
- 75th percentile
- Maximum

For numerical columns, the program also calculates:

- Variance
- 25th percentile
- 75th percentile

---
## Data Visualization

The program supports multiple types of visualizations using **Matplotlib and Seaborn.**

### 1. Bar Plot

Displays values using bars based on selected X-axis and Y-axis columns.

---

### 2. Line Plot

Displays trends between selected X-axis and Y-axis columns.

---

### 3. Scatter Plot

Displays the relationship between two selected numerical columns.

---

### 4. Pie Chart

Displays the distribution of categories from a selected column.

---

### 5. Histogram

Displays the distribution of values in a selected numerical column.

The histogram also includes a Kernel Density Estimate (KDE).

---

### 6. Stack Plot

Creates a stacked visualization using available numerical columns.

The program uses up to three numerical columns for the stack plot.

---

## Save Visualization

After generating a visualization, users can save the active plot to a file.

For example:

`scatter_plot.png`

The visualization is saved with:

- 300 DPI resolution
- Tight bounding box

---  
## Main Menu

After running the program, the following options are available:

1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit

The user can select an option by entering the corresponding number.

---

## Example Workflow
1. Start the Program
        ↓
2. Sample Dataset is Created if Needed
        ↓
3. Load Dataset
        ↓
4. Explore Data
        ↓
5. Perform DataFrame Operations
        ↓
6. Handle Missing Data
        ↓
7. Generate Descriptive Statistics
        ↓
8. Create Data Visualizations
        ↓
9. Save Visualization
        ↓
10. Exit
---
### Example Dataset

The program automatically creates a sample dataset with data similar to:

| SalesID | Product   | Region     | Sales | Year |
|--------:|-----------|------------|------:|-----:|
| 101     | Product A | North      | 500   | 2022 |
| 102     | Product B | East       | 600   | 2022 |
| 103     | Product C | West Coast | 700   | 2022 |
| 104     | Product D | South      | 800   | 2022 |
| 105     | Product E | Central    | 550   | 2022 |

---
## Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn

---
## Python Concepts Used
This project demonstrates:

- Variables
- Functions
- Classes
- Objects
- Constructors
- Destructors
- Instance variables
- Object-Oriented Programming
- Conditional statements
- Loops
- Exception handling 
- User input
- File handling
- CSV file processing
- DataFrames
- NumPy arrays
- Data cleaning
- Data filtering
- Data sorting
- Data aggregation
- Data visualization
- Menu-driven programming

---  
## Project Structure
```text
Sales-Data-Analysis/
│
├── main.py
├── sales_data.csv
└── README.md
```
The `sales_data.csv` file is automatically created by the program if it does not already exist.

---
## Installation
### Step 1: Install Python

Make sure Python is installed on your computer.

Check the Python version:

**python --version**
### Step 2: Install Required Libraries

Open the terminal or command prompt and run:

**pip install numpy pandas matplotlib seaborn**
### How to Run

Run the Python program using:

**python main.py**

---
## Class Used
### SalesDataAnalyzer

The `SalesDataAnalyzer`class manages the dataset and provides methods for data analysis, cleaning, statistical analysis, visualization, and saving plots.

### Main Attributes
- `data` – Stores the loaded Pandas DataFrame.
- `last_fig` – Stores the most recently generated Matplotlib figure.
### Main Methods
- `load_data()` – Loads a CSV dataset into a Pandas DataFrame.
- `explore_data()` – Displays different types of information about the dataset.
- `search_sort_filter()` – Searches, sorts, and filters the dataset.
- `create_pivot_table()` – Creates a Pandas pivot table.
- `clean_data()` – Handles missing values.
- `statistical_analysis()` – Generates descriptive statistics.
- `visualize_data()` – Creates different types of visualizations.
- `save_visualization()` – Saves the most recently generated visualization.

---
## Functions

The project contains the following main functions:

`ensure_sample_dataset_exists()`

Checks whether the default CSV dataset exists and automatically creates a sample dataset if it does not.

`main()`

Controls the main menu and manages user interaction with the program.

---
## Error Handling

The program includes validation and error handling for:

- Missing CSV files
- CSV loading errors
- Invalid column names
- Invalid menu choices
- Missing datasets
- Invalid numerical columns
- Visualization errors
- Invalid plot selections
- Insufficient numerical columns for stack plots
- Errors while saving visualizations

---
## Learning Outcomes

After completing this project, learners can understand how to use Python libraries for practical data analysis.

The project helps learners understand how to:

- Load CSV data using Pandas
- Create and work with DataFrames
- Explore datasets
- Access rows and columns
- Search for values
- Sort data
- Filter data
- Create pivot tables
- Convert Pandas columns to NumPy arrays
- Detect missing values
- Fill missing values
- Remove missing values
- Replace missing values
- Calculate descriptive statistics
- Calculate variance and percentiles
- Create different types of visualizations
- Save visualizations to image files
- Build a menu-driven data analysis application

---
## Future Improvements

The project can be extended with:

- Multiple CSV file support
- Excel file support
- JSON data support
- Database connectivity
- Advanced data cleaning
- Duplicate data detection and removal
- GroupBy operations
- Correlation analysis
- Interactive dashboards
- More visualization types
- Custom visualization settings
- Data export functionality
- Automated report generation
- Streamlit web interface
- User-friendly graphical interface
- Machine learning integration
- Sales prediction
- Advanced business analytics

---
## Conclusion

Sales Data Analysis & Visualization Program is a practical Python project that demonstrates how **NumPy, Pandas, Matplotlib, and Seaborn** can be combined to analyze and visualize structured sales data.

The project covers the complete basic data analysis workflow, including **loading data, exploring data, performing DataFrame operations, cleaning missing data, calculating descriptive statistics, creating visualizations, and saving plots.**

It also demonstrates Python programming concepts such as **Object-Oriented Programming, classes, methods, functions, exception handling, file handling, and menu-driven application design.**
