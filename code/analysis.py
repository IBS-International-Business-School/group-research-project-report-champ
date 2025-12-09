import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

# --- 1. SETUP ---
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_context("paper", font_scale=1.4)

filename = 'survey_data_cleaned.csv' 

try:
    df = pd.read_csv(filename)
    print("File loaded successfully!")
except FileNotFoundError:
    print("Error: File not found.")

# --- 2. CLEANING FUNCTIONS ---

def get_number(x):
    # Extracts numbers from text. ex: "3.5 / 4.0" -> 3.5
    try:
        nums = re.findall(r"[-+]?\d*\.\d+|\d+", str(x))
        if nums:
            return float(nums[0])
    except:
        pass
    return np.nan

def clean_tools(text):
    text = str(text).lower()
    if 'notion' in text or 'calendar' in text or 'agenda' in text or 'plan' in text:
        return 'Planner (Notion/Cal)'
    elif 'gpt' in text or 'ai' in text or 'chat' in text:
        return 'AI (ChatGPT)'
    else:
        return 'Neutral / Other'

# --- 3. APPLY CLEANING ---

# Clean Hours
if 'Study_Hours' in df.columns:
    df['Study_Hours_Clean'] = df['Study_Hours'].apply(get_number)
    df = df.dropna(subset=['Study_Hours_Clean'])
    
    # Create Categories
    bins = [0, 10, 15, 100]
    labels = ['<10 Hours', '10-15 Hours', '>15 Hours']
    df['Study_Category'] = pd.cut(df['Study_Hours_Clean'], bins=bins, labels=labels)

# Clean Tools
if 'Use_Digital_Tools' in df.columns:
    df['Tool_Category'] = df['Use_Digital_Tools'].apply(clean_tools)
else:
    df['Tool_Category'] = 'Unknown'

# Clean GPA (Performance)
if 'Performance' in df.columns:
    df['GPA_Clean'] = df['Performance'].apply(get_number)

# Clean Stress
if 'Assess_Stress' in df.columns:
    df['Stress_Clean'] = df['Assess_Stress'].apply(get_number)

# --- 4. GENERATE GRAPHS ---
print("Generating graphs...")

# You can save these figures or show them
# plt.savefig('fig1.png') to save
