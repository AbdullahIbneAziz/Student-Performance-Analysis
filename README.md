
# Student Performance Analysis

This project involves a comprehensive analysis of a student dataset to understand the factors affecting student performance. It applies various data preprocessing techniques, visualizations, and machine learning algorithms to predict and classify academic performance metrics.

## 📊 Project Overview

The notebook explores and models the performance of students based on attributes like credit hours completed, CGPA, family income, physical health, relationship status, skill development hours, and more.

### Goals:
- Analyze student performance data.
- Identify key factors influencing CGPA.
- Build predictive models to classify or regress academic outcomes.

## 🧰 Tools & Libraries Used

- **Python**
- **Pandas, NumPy, SciPy** – Data manipulation and analysis
- **Seaborn, Matplotlib** – Data visualization
- **Scikit-learn** – Machine learning models and preprocessing

## 📁 Dataset

The dataset used is loaded from an Excel file named:
```
Students_Performance_data_set.xlsx
```

It contains fields such as:
- Completed Credits
- Current CGPA
- Previous SGPA
- Monthly Family Income
- Health and Living Status
- Involvement in Co-Curricular Activities
- Daily Skill Development Hours

## ⚙️ Workflow

1. **Data Loading & Cleaning**
   - Missing value handling
   - Column renaming for easier manipulation

2. **Exploratory Data Analysis (EDA)**
   - Visualizations using Seaborn and Matplotlib
   - Correlation analysis

3. **Feature Encoding & Scaling**
   - Label encoding and normalization techniques

4. **Model Building**
   Several classifiers and regressors were trained and evaluated:
   - Decision Tree
   - Logistic Regression
   - Random Forest
   - Gaussian Naive Bayes
   - K-Nearest Neighbors
   - Support Vector Machine (SVM)
   - Linear Regression

5. **Model Evaluation**
   - Accuracy, confusion matrix, and other metrics were used to compare model performance.

## 📈 Results

Models were evaluated on their ability to classify or predict student performance. The notebook includes visual and quantitative comparison of each approach.

## 📌 How to Run

1. Clone the repository or download the `.ipynb` file.
2. Ensure you have the required libraries installed (`pip install -r requirements.txt`).
3. Place the dataset file `Students_Performance_data_set.xlsx` in the same directory.
4. Open the notebook using Jupyter or VS Code and run all cells.

## 🧾 Requirements

```bash
pandas
numpy
matplotlib
seaborn
scikit-learn
scipy
```

## 📬 Contact

For any questions or suggestions, feel free to open an issue or reach out via email.
