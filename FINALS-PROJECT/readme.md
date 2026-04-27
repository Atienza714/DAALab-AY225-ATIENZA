# 🌍 World Bank Health & Nutrition Explorer

A collaborative, browser‑based data analysis tool for the **World Bank Health, Nutrition and Population Statistics** dataset.  
Upload any CSV, explore the data, visualise trends, and uncover correlations – all in real time, with no server.

---

## 🎯 Project Purpose

This project was developed as a **two‑student Git collaboration exercise** for the DAA Lab.  
It demonstrates:

- Real‑world Git workflow (feature branches, pull requests, code reviews)
- CSV parsing and dynamic data exploration
- Interactive visualisations using Chart.js
- Statistical summaries and correlation analysis

---

## 👥 Team Contribution

| Branch                     | Student | Responsibilities                                                                 |
|----------------------------|---------|----------------------------------------------------------------------------------|
| `feature/data-engine`      | **Student 1** (Repo Owner) | CSV loading, table rendering, pagination, search, statistics cards, selectors   |
| `feature/viz-analysis`     | **Student 2** (Collaborator) | Bar chart (Top 10 values), scatter plot, correlation function, insights panel   |

---

## ✨ Features

### Data Engine (Student 1)
- Drag‑and‑drop CSV upload with progress bar
- Automatic detection of numeric vs. string columns
- Fully paginated, searchable data table
- Summary statistics cards: row count, column count, numeric columns, completeness
- Dynamic dropdown population for numeric columns (used by charts)

### Visualisations & Insights (Student 2)
- **Top 10 Values Bar Chart** – highest values for any selected numeric column
- **Scatter Plot** – explore relationships between any two numeric variables
- **Pearson correlation** – automatically computed between the first two numeric columns
- **Insights Panel** – highlights the column with the highest average and interprets the correlation strength.

### Dataset‑Specific
- Optimised for the **World Bank Health, Nutrition and Population Statistics** CSV  
  (country, series, year columns, many missing values handled gracefully)
- Handles large files efficiently using **PapaParse streaming**

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Atienza714/DAALab-AY225-ATIENZA.git
   cd DAALab-AY225-ATIENZA
2. Open FINALS-PROJECT/index.html in your favourite browser (Chrome, Firefox, Edge).

3. Drag and drop the World Bank CSV file (or any other CSV) onto the upload area.

4. Explore:

Use the search box to filter the table.

Change rows per page.

Select a numeric column for the Top 10 bar chart.

Pick X and Y columns for the scatter plot and click Plot.

Read the Statistical Summary panel for automatic insights.