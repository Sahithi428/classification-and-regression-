STUDENT GPA REGRESSION PROJECT

Target:
- GPA (continuous value 0.0 to 4.0)

Important:
- Put the exact Student_performance_data.csv used for your classification project in this folder.
- GradeClass is removed because it is derived from GPA and would cause target leakage.
- StudentID is removed because it is only an identifier.

Files:
- student_gpa_regression.ipynb : complete notebook, in title -> code -> matter order
- app.py : Streamlit deployment application
- requirements.txt : required packages
- model_regression.pkl : generated after running the model-saving cell
- scaler_regression.pkl : generated after running the model-saving cell

Run:
1. Open the folder in VS Code.
2. Install: python -m pip install -r requirements.txt
3. Open and run all cells in student_gpa_regression.ipynb.
4. The final model-saving cell creates model_regression.pkl and scaler_regression.pkl.
5. Run: python -m streamlit run app.py

Dataset source reference:
https://github.com/Forren70/students-analysis-pandas
The repository documents the 2,392-record Student_performance_data.csv dataset and its 15 columns.
