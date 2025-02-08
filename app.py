import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialize DataFrame (Replace this with a database connection for production)
data = {
    'Employee': ['John Doe', 'Jane Smith', 'Ali Khan', 'Sarah Lee'],
    'Role': ['Developer', 'Artist', 'UI Designer', 'Support Staff'],
    'Technical Mastery': [8, 7, 9, 6],
    'Innovation & Impact': [7, 8, 6, 7],
    'Leadership & Mentorship': [6, 7, 8, 5],
    'Collaboration & Culture': [9, 8, 7, 9],
    'Performance Score': [80, 85, 78, 75]
}
df = pd.DataFrame(data)

# Streamlit UI
st.title("Game District Meritocracy Dashboard")
st.write("Tracking employee performance, growth, and cultural impact.")

# Show Data
st.dataframe(df)

# Performance Visualization
st.subheader("Performance Breakdown")
fig, ax = plt.subplots(figsize=(8, 5))
df.set_index("Employee")[['Technical Mastery', 'Innovation & Impact', 'Leadership & Mentorship', 'Collaboration & Culture']].plot(kind='bar', ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Employee Detail View
st.subheader("Employee Performance Review")
selected_employee = st.selectbox("Select an Employee", df['Employee'])
emp_data = df[df['Employee'] == selected_employee].T
st.write(emp_data)

# Add Performance Review
st.subheader("Update Employee Performance")
emp_name = st.selectbox("Select Employee to Update", df['Employee'])
metric = st.selectbox("Metric", ['Technical Mastery', 'Innovation & Impact', 'Leadership & Mentorship', 'Collaboration & Culture'])
new_value = st.slider("New Score (0-10)", 0, 10, 5)

if st.button("Update Score"):
    df.loc[df['Employee'] == emp_name, metric] = new_value
    st.success(f"Updated {metric} for {emp_name} to {new_value}")
