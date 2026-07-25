import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DEFAULT_CSV_PATH = "sales_data.csv"

def ensure_sample_dataset_exists(file_path=DEFAULT_CSV_PATH):
    if not os.path.exists(file_path):
        sample_data = {
            'SalesID': [101, 102, 103, 104, 105],
            'Product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
            'Region': ['North', 'East', 'West Coast', 'South', 'Central'],
            'Sales': [500, 600, 700, 800, 550],
            'Year': [2022, 2022, 2022, 2022, 2022]
        }
        df = pd.DataFrame(sample_data)
        df.to_csv(file_path, index=False)
        print(f"[System Setup] Sample dataset created automatically at '{file_path}'.")


class SalesDataAnalyzer:

    def __init__(self, file_path=None):
        self.data = None
        self.last_fig = None
        if file_path:
            self.load_data(file_path)

    def __del__(self):
        plt.close("all")

    def load_data(self, file_path):
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' not found.")
            return False
        try:
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
            return True
        except Exception as e:
            print(f"Error loading CSV file: {e}")
            return False

    def explore_data(self, option):
        if self.data is None:
            print("No dataset loaded. Please load a dataset first.")
            return

        if option == 1:
            print("\n-- First 5 rows --")
            print(self.data.head())
        elif option == 2:
            print("\n-- Last 5 rows --")
            print(self.data.tail())
        elif option == 3:
            print("\n-- Column Names --")
            print(list(self.data.columns))
        elif option == 4:
            print("\n-- Column Data Types --")
            print(self.data.dtypes)
        elif option == 5:
            print("\n-- Basic Info --")
            print(self.data.info())
        else:
            print("Invalid option.")

    def search_sort_filter(self):
        if self.data is None:
            print("No dataset loaded.")
            return

        print("\n-- Search, Sort, & Filter --")
        print("1. Search by value in a column")
        print("2. Sort data by column")
        print("3. Filter data (e.g., numeric thresholds)")
        
        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            col = input("Enter column name: ").strip()
            val = input("Enter value to search: ").strip()
            if col in self.data.columns:
                results = self.data[self.data[col].astype(str).str.contains(val, case=False, na=False)]
                print(results)
            else:
                print("Column not found.")

        elif choice == "2":
            col = input("Enter column to sort by: ").strip()
            ascending = input("Sort ascending? (y/n): ").strip().lower() == 'y'
            if col in self.data.columns:
                sorted_df = self.data.sort_values(by=col, ascending=ascending)
                print(sorted_df.head(10))
            else:
                print("Column not found.")

        elif choice == "3":
            col = input("Enter numeric column name to filter: ").strip()
            if col in self.data.columns and np.issubdtype(self.data[col].dtype, np.number):
                val = float(input(f"Filter rows where {col} > : "))
                filtered_df = self.data[self.data[col] > val]
                print(filtered_df)
            else:
                print("Invalid numeric column.")

    def create_pivot_table(self, index_col, values_col, agg_func='sum'):
        if self.data is None:
            print("No dataset loaded.")
            return
        
        try:
            pivot = pd.pivot_table(self.data, values=values_col, index=index_col, aggfunc=agg_func)
            print("\n-- Pivot Table --")
            print(pivot)
        except Exception as e:
            print(f"Error creating pivot table: {e}")

    def clean_data(self, option):
        if self.data is None:
            print("No dataset loaded.")
            return

        missing_count = self.data.isnull().sum().sum()

        if option == 1:
            if missing_count == 0:
                print("\nNo missing values found in the dataset!")
            else:
                print("\n-- Rows with missing values --")
                print(self.data[self.data.isnull().any(axis=1)])
        elif option == 2:
            num_cols = self.data.select_dtypes(include=[np.number]).columns
            self.data[num_cols] = self.data[num_cols].fillna(self.data[num_cols].mean())
            print("Missing numerical values filled with mean.")
        elif option == 3:
            self.data.dropna(inplace=True)
            print("Rows with missing values dropped.")
        elif option == 4:
            val = input("Enter replacement value: ").strip()
            self.data.fillna(val, inplace=True)
            print(f"Missing values replaced with '{val}'.")

    def statistical_analysis(self):
        if self.data is None:
            print("No dataset loaded.")
            return
        print("\n-- Descriptive Statistics --")
        print(self.data.describe())
        
        num_cols = self.data.select_dtypes(include=[np.number])
        if not num_cols.empty:
            print("\nVariance:\n", num_cols.var())
            print("\n25th & 75th Percentiles:\n", num_cols.quantile([0.25, 0.75]))

    def visualize_data(self, plot_type):
        if self.data is None:
            print("No dataset loaded.")
            return

        fig, ax = plt.subplots(figsize=(8, 5))
        sns.set_theme(style="whitegrid")

        try:
            if plot_type == 1:  # Bar Plot
                x_col = input("Enter x-axis column name: ").strip()
                y_col = input("Enter y-axis column name: ").strip()
                sns.barplot(data=self.data, x=x_col, y=y_col, ax=ax)
                plt.title(f"Bar Plot: {y_col} vs {x_col}")

            elif plot_type == 2:  # Line Plot
                x_col = input("Enter x-axis column name: ").strip()
                y_col = input("Enter y-axis column name: ").strip()
                sns.lineplot(data=self.data, x=x_col, y=y_col, ax=ax)
                plt.title(f"Line Plot: {y_col} vs {x_col}")

            elif plot_type == 3:  # Scatter Plot
                x_col = input("Enter x-axis column name: ").strip()
                y_col = input("Enter y-axis column name: ").strip()
                print("Generating scatter plot...")
                sns.scatterplot(data=self.data, x=x_col, y=y_col, ax=ax)
                plt.title(f"Scatter Plot: {y_col} vs {x_col}")

            elif plot_type == 4:  # Pie Chart
                col = input("Enter category column for Pie Chart: ").strip()
                counts = self.data[col].value_counts()
                ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
                plt.title(f"Pie Chart of {col}")

            elif plot_type == 5:  # Histogram
                col = input("Enter numeric column name for Histogram: ").strip()
                sns.histplot(self.data[col], kde=True, ax=ax)
                plt.title(f"Histogram of {col}")

            elif plot_type == 6:  # Stack Plot
                numeric_cols = self.data.select_dtypes(include=[np.number]).columns[:3]
                if len(numeric_cols) > 1:
                    ax.stackplot(range(len(self.data)), [self.data[c] for c in numeric_cols], labels=numeric_cols)
                    ax.legend(loc='upper left')
                    plt.title("Stack Plot")
                else:
                    print("Insufficient numeric columns for Stack Plot.")
                    plt.close(fig)
                    return

            else:
                print("Invalid plot choice.")
                plt.close(fig)
                return

            self.last_fig = fig
            plt.tight_layout()
            print("Plot generated successfully!")
            plt.show()

        except Exception as e:
            print(f"Error generating plot: {e}")
            plt.close(fig)

    def save_visualization(self, filename):
        if self.last_fig is None:
            print("No active plot available to save. Generate a plot first.")
            return
        try:
            self.last_fig.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"Visualization saved as {filename} successfully!")
        except Exception as e:
            print(f"Error saving visualization: {e}")


def main():
    ensure_sample_dataset_exists(DEFAULT_CSV_PATH)
    analyzer = SalesDataAnalyzer()

    while True:
        print("\n" + "---------- Data Analysis & Visualization Program ----------")
        print("Please select an option:")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("-" * 58)

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            print("\n-- Load Dataset --")
            path = input("Enter the path of the dataset (CSV file): ").strip()
            if not path:
                path = DEFAULT_CSV_PATH
            analyzer.load_data(path)

        elif choice == "2":
            print("\n-- Explore Data --")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            exp_choice = input("Enter your choice: ").strip()
            if exp_choice.isdigit():
                analyzer.explore_data(int(exp_choice))

        elif choice == "3":
            print("\n-- Perform DataFrame Operations --")
            print("1. Search, Sort, or Filter Data")
            print("2. Create Pivot Table")
            print("3. Convert DataFrame Column to NumPy Array")
            op_choice = input("Enter choice (1-3): ").strip()

            if op_choice == "1":
                analyzer.search_sort_filter()
            elif op_choice == "2":
                idx = input("Enter index column: ").strip()
                val = input("Enter values column: ").strip()
                analyzer.create_pivot_table(idx, val)
            elif op_choice == "3":
                col = input("Enter column name to convert: ").strip()
                if analyzer.data is not None and col in analyzer.data.columns:
                    arr = analyzer.data[col].to_numpy()
                    print(f"NumPy Array: {arr}")
                else:
                    print("Invalid column or dataset not loaded.")

        elif choice == "4":
            print("\n-- Handle Missing Data --")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")
            clean_choice = input("Enter your choice: ").strip()
            if clean_choice.isdigit():
                analyzer.clean_data(int(clean_choice))

        elif choice == "5":
            print("\n-- Generate Descriptive Statistics --")
            analyzer.statistical_analysis()

        elif choice == "6":
            print("\n-- Data Visualization --")
            print("1. Bar Plot\n2. Line Plot\n3. Scatter Plot\n4. Pie Chart\n5. Histogram\n6. Stack Plot")
            viz_choice = input("Enter your choice: ").strip()
            if viz_choice.isdigit():
                analyzer.visualize_data(int(viz_choice))

        elif choice == "7":
            print("\n-- Save Visualization --")
            filename = input("Enter file name to save the plot (e.g., scatter_plot.png): ").strip()
            if filename:
                analyzer.save_visualization(filename)

        elif choice == "8":
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please select between 1 and 8.")

if __name__ == "__main__":
    main()
