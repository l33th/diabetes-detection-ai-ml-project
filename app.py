# This AI & ML project is a diabetes detection program that can detect if someone has diabetes

# Library Imports
import streamlit as st
import pandas as pd

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from PIL import Image

# Title And Subtitle
st.write("""
# AI & ML Diabetes Detection
Detect If Someone Has Diabetes Using This Artificial Intelligence Web Appliaction.
""")

# Image To Display
image = Image.open('./img/image.jpg')
st.image(image, caption='ARTIFICIAL INTELLIGENCE & MACHINE LEARNING DIABETES DETECTION', use_column_width=True)

# Load Data
df = pd.read_csv('./data/diabetes.csv')
# Subheader
st.subheader('Data Information:')
# Data Table
st.dataframe(df)
# Data Statistics
st.write(df.describe())
# Data Chart
chart = st.bar_chart(df)

# Split Data - Independent 'X' and Dependent 'Y' Variables
X = df.iloc[:, 0:8].values
Y = df.iloc[:, -1].values

# Split data - 75% Training And 25% Testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)
