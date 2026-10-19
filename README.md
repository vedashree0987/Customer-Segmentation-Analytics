# Customer Insights & Segmentation Dashboard

**Transforming Customer Data into Actionable Business Insights**

## 📌 About the Project

Understanding customer behavior is essential for businesses that want to improve marketing effectiveness and build stronger customer relationships. This project explores customer demographics, purchasing habits, product preferences, and campaign engagement to identify meaningful customer groups.

Using Python for data analysis, K-Means clustering for customer segmentation, and Microsoft Power BI for interactive reporting, the project presents customer patterns in a visual and business-friendly format.

The analysis divides customers into five clusters and compares their characteristics to help identify differences in spending behavior, income, and purchase recency.

## 🎯 Business Goals

- Understand variations in customer purchasing behavior.
- Identify groups of customers with similar characteristics.
- Compare spending patterns and income levels across customer segments.
- Explore customer engagement with marketing campaigns.
- Present analytical results through an interactive business intelligence dashboard.

## 🧰 Technology Stack

| Technology | Application |
|---|---|
| Python | Data exploration and preparation |
| Pandas | Dataset manipulation and transformation |
| NumPy | Numerical computations |
| Scikit-learn | K-Means clustering |
| Jupyter Notebook | Analysis and experimentation |
| Microsoft Power BI | Interactive reporting and visualization |
| DAX | Dashboard measures and calculated metrics |

*Visualization libraries such as Matplotlib and Seaborn can also be listed if they were used in the analysis.*

## 📊 Data Overview

The project uses customer marketing data covering several dimensions of customer behavior.

### Customer Information
Demographic characteristics, income, education, marital status, and household composition.

### Product Preferences
Spending on wine, meat, fish, fruit, sweets, and gold products.

### Purchasing Activity
Purchase behavior across web, catalogue, and store channels, along with deal purchases and website visits.

### Marketing Engagement
Campaign acceptance indicators and customer response information.

These attributes provide a foundation for analyzing customer similarities and differences.

## 🔍 Analytical Approach

### 1. Data Exploration

The dataset was inspected to understand its structure, identify missing information, and examine the distribution of relevant customer attributes.

### 2. Data Preparation

Data preprocessing and feature engineering were used to prepare customer information for analysis. Aggregated features were created to summarize spending, purchase activity, household composition, and campaign acceptance.

Key derived features include:

- `Total_Spend`
- `Total_Purchases`
- `Total_Children`
- `Total_Campaign_Accepted`

### 3. Customer Grouping

The K-Means clustering algorithm was used to group customers into five clusters based on the features selected for the model.

This unsupervised learning approach identifies groups according to similarities in the chosen feature space, without requiring predefined customer categories.

### 4. Interactive Visualization

The prepared customer data and cluster labels were used to develop a Power BI dashboard. The report enables users to explore the distribution of customers and compare key behavioral measures across clusters.

## 📈 Power BI Report

The dashboard is organized into two analytical views.

### View 1 — Customer Segmentation Overview

This page presents the overall picture of the customer base.

**Included visualizations:**
- Total customer count
- Number of customer segments
- Average customer spending
- Customer distribution across clusters
- Product category spending
- Purchase channel analysis
- Customer cluster profiles

### View 2 — Customer Segment Analysis

This page focuses on differences between the five customer groups.

**Included visualizations:**
- Customer count by cluster
- Average income comparison
- Average spending comparison
- Average purchase recency
- Customer profile table
- Cluster selection slicer

The slicer allows users to focus on individual clusters and explore the corresponding data across compatible visuals.

## 💼 Business Questions Explored

The dashboard is designed to investigate questions such as:

1. How is the customer base distributed across the five clusters?
2. Which customer groups have higher average incomes?
3. How does average spending vary between customer segments?
4. Which groups have gone longer without making a purchase?
5. How do product preferences and purchase channels vary across the dataset?
6. How can these patterns inform customer targeting and retention strategies?

The findings should be interpreted from the actual model results and dashboard values.

## 💡 Potential Business Value

Customer segmentation can support several business activities:

- **Targeted marketing:** Tailor promotional messages to different customer groups.
- **Customer retention:** Investigate segments with higher purchase recency values.
- **Product strategy:** Understand differences in category-level spending.
- **Campaign planning:** Explore customer engagement patterns.
- **Customer profiling:** Compare segments to support more informed business decisions.

These are potential applications of the analysis; actual improvements in marketing performance would require further validation.

## ⚙️ Running the Project

### Requirements

- Python
- Jupyter Notebook
- Microsoft Power BI Desktop
- The project dataset, where available and permitted for use

### 1. Clone the Repository

```bash
git clone https://github.com/Sinchan-hub/Customer-Segmentation-Analytics.git
cd Customer-Segmentation-Analytics
```

### 2. Install Python Libraries

If the repository includes a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Alternatively, install the main analysis libraries:

```bash
pip install pandas numpy scikit-learn jupyter
```

Install additional libraries if required by the notebook.

### 3. Launch Jupyter Notebook

```bash
jupyter notebook
```

Open the customer segmentation notebook and execute the analysis cells in order.

### 4. Explore the Power BI Dashboard

Open the `.pbix` file in Power BI Desktop. If prompted, update the data source path to point to the dataset available on your computer.

## 📁 Suggested Repository Layout

```text
Customer-Segmentation-Analytics/
│
├── notebook/
│   └── customer_segmentation.ipynb
│
├── dashboard/
│   └── customer_segmentation.pbix
│
├── data/
│   └── customer_segmentation_powerbi.csv
│
├── screenshots/
│   ├── overview.png
│   └── segment_analysis.png
│
├── requirements.txt
└── README.md
```

This is a suggested folder structure. Adjust the paths to match the files included in the repository, and only publish datasets that you are permitted to redistribute.

## 🚀 Possible Future Improvements

- Evaluate clustering quality using the Silhouette Score.
- Compare clustering configurations to assess the choice of five clusters.
- Develop evidence-based profiles for individual customer groups.
- Explore relationships between campaign acceptance and customer behavior.
- Add further interactive drill-through views to the Power BI report.

## 🧠 Skills Applied

- Data Cleaning and Preprocessing
- Exploratory Data Analysis
- Feature Engineering
- Unsupervised Machine Learning
- K-Means Clustering
- Python-Based Data Analysis
- Power BI Reporting
- Data Visualization
- Business Intelligence
- Customer Behavior Analysis

## 📝 Conclusion

This project combines customer data analysis, unsupervised machine learning, and interactive reporting to explore customer segmentation. By grouping similar customers and comparing their income, spending, and purchase recency, the analysis provides a structured way to understand customer behavior and investigate potential business opportunities.

**Project Domain:** Data Analytics | Machine Learning | Business Intelligence

**Technologies:** Python · Pandas · NumPy · Scikit-learn · Jupyter Notebook · Power BI
