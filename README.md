# Istanbul Traffic Accidents Analysis Project

## 🎯 Project Goal
Identify when and under what conditions traffic accidents happen most in Istanbul.

## 📊 Bonus Points Applied
- ✅ **Scraped messy web data (+10)** - Data collected from IPA, Daily Sabah, Xinhua
- ✅ **Data science analysis (+15)** - Anomaly detection using IQR method
- ✅ **Modern React.js visualization (+15)** - Interactive dashboard with Recharts
- **Total Bonus: +40 points**

---

## 📁 Project Structure
```
python_project4(istanbul_traffic_analysis)/
├── scraper.py              # Web scraping script
├── analysis.py             # Data cleaning & analysis
├── dashboard.html          # React visualization
├── scraped_accidents.csv   # Cleaned dataset
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

---

## 📊 Dashboard Preview

### Interactive Dashboard
![Dashboard Overview](screenshots/dashboard_overview.png)
*Modern React.js dashboard with real-time statistics and interactive charts*

### Anomaly Detection Analysis
![Anomaly Detection](screenshots/anomaly_detection.png)
*IQR method identifying September as statistical outlier (238 vs 118 average)*

---

## 🌐 Data Sources (Scraped Web Data)

### 1. IPA Istanbul Report
- **URL**: Traffic accident reports from Istanbul Planning Agency
- **Data**: Monthly accident counts, severity levels
- **Issues**: Inconsistent date formats, Turkish characters, missing values

### 2. Daily Sabah News
- **URL**: Annual traffic statistics articles
- **Data**: Weather conditions, time of day, accident counts
- **Issues**: Data embedded in article text, needed text parsing

### 3. Xinhua English News
- **URL**: Statistical reports on Türkiye traffic
- **Data**: Hourly distributions, yearly trends
- **Issues**: Mixed units (some in percentages), needed normalization

---

## 🧹 Data Cleaning Process (Step-by-Step)

### Step 1: Web Scraping
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Scraped HTML tables and article text from 3 sources
# Used BeautifulSoup to parse messy HTML structure
```

### Step 2: Handling Missing Data
- **Problem**: 15% of weather data was missing or marked as "N/A"
- **Solution**: Filled with "Unknown" category, later analyzed separately

### Step 3: Fixing Date Formats
- **Problem**: Dates in 3 different formats (DD/MM/YYYY, Turkish month names, timestamps)
- **Solution**: Standardized all to YYYY-MM-DD using `pd.to_datetime()`

### Step 4: Text Parsing
- **Problem**: Accident counts written in text: "iki yüz üç kaza" (203 accidents in Turkish)
- **Solution**: Created Turkish number parser dictionary to convert to integers

### Step 5: Removing Duplicates
- **Problem**: Same accidents reported by multiple sources
- **Solution**: Matched by date+time+location, kept only unique records

### Step 6: Data Normalization
- **Problem**: Some sources gave percentages, others absolute numbers
- **Solution**: Converted all to absolute counts based on yearly totals

### Step 7: Outlier Detection
- **Problem**: Some entries had impossible values (e.g., 9999 accidents in one hour)
- **Solution**: Used IQR method to identify and remove statistical outliers

---

## 📈 Analysis Methods

### Basic Statistics
- **Mean**: 118.2 accidents/month
- **Median**: 120 accidents/month
- **Min**: 87 (February)
- **Max**: 238 (September - Anomaly!)

### Advanced Statistical Analysis
**Quartile Analysis (Box Plot Method):**
- Q1 (25th percentile): 98 accidents
- Q3 (75th percentile): 142 accidents
- IQR (Interquartile Range): 44 accidents

### Anomaly Detection (IQR Method)
**Formula Used:**
```
Upper Bound = Q3 + 1.5 × IQR = 142 + 1.5 × 44 = 208
Lower Bound = Q1 - 1.5 × IQR = 98 - 1.5 × 44 = 32
```

**Result:** September (238 accidents) is a **statistical anomaly** - exceeds upper bound by 30 accidents.

---

## 🔍 Key Findings

### 1. Peak Accident Hours ⏰
- **Highest**: 16:00-18:00 (203 accidents) - Evening rush hour
- **Second**: 08:00-10:00 (189 accidents) - Morning commute
- **Lowest**: 02:00-04:00 (28 accidents) - Late night

### 2. Weather Impact 🌤️
- **Clear weather**: 645 accidents (49%) - Most common
- **Rain**: 398 accidents (30%) - Second highest
- **Fog**: 187 accidents (14%)
- **Snow**: 89 accidents (7%)

**Insight**: Clear weather has most accidents because of higher traffic volume, not danger.

### 3. September Anomaly 🚨
- Normal months: 87-156 accidents
- September: 238 accidents (101% above average!)
- **Possible reasons**: School season starts, construction projects, weather transition

---

## 💻 Technologies Used

### For Scraping (+10 points)
- Python `requests` & `BeautifulSoup4`
- HTML parsing from 3 different website structures

### For Analysis (+15 points)
- Pandas for data manipulation
- NumPy for statistical calculations
- IQR method for anomaly detection
- Quartile analysis (Q1, Q3, box plot statistics)

### For Visualization (+15 points)
- **React.js** with Recharts library
- Interactive dashboard
- Modern web-based interface
- Responsive design

---

## 📝 2-Minute Presentation Outline

**Slide 1: Problem (15 sec)**
"Istanbul has many traffic accidents. When do they happen most?"

**Slide 2: Data (15 sec)**
"I scraped data from 3 news sources: IPA, Daily Sabah, Xinhua. Cleaned messy formats and missing values."

**Slide 3: Analysis (30 sec)**
"Used statistical methods:
- Calculated mean, median, quartiles
- Applied IQR anomaly detection
- Found September is a statistical outlier (238 vs 118 average)"

**Slide 4: Results (30 sec)**
[Show dashboard]
"Key findings:
- Most dangerous: Evening rush hour (16-18)
- Clear weather has most accidents (traffic volume)
- September anomaly needs investigation"

**Slide 5: Conclusion (30 sec)**
"Drivers should be extra careful during rush hours. City should investigate September spike. Used modern React visualization and advanced statistics for this analysis."

---

## Installation

Follow the steps below to install the project requirements correctly.

**Prerequisites**

Make sure you have the following installed on your system:

- Python 3.8 or higher

- pip (Python package manager)

- (Optional but recommended) virtualenv

You can check your Python version with:

python --version

or

python3 --version

**Step 1: Clone the Repository**

git clone https://github.com/your-username/your-repository.git
cd your-repository

**Step 2: Create and Activate a Virtual Environment (Recommended)**

**On Windows:**

python -m venv venv
venv\Scripts\activate

**On macOS / Linux:**

python3 -m venv venv
source venv/bin/activate

**Step 3: Install Requirements**

Install all required dependencies using the requirements.txt file:

pip install -r requirements.txt

If pip points to Python 2, use:

pip3 install -r requirements.txt

**Step 4: Verify Installation**

To confirm everything is installed correctly:

pip list

or try running the project:

python analysis.py

**Common Issues**

Permission denied: add --user or use a virtual environment

Package build errors: update pip first

pip install --upgrade pip

---

## 🎓 Academic Integrity
All data was publicly available. Proper citations provided for sources. Analysis code written independently.

---

## 📧 Contact
[Iyad Kabel, Y.H.Y.M.Bakr Raiyan, Amro Jamal Al Ddın, Christ Barhith Boka, Muzammal Yaquib] - [eyadkabel7@gmail.com]
Software Engineering, Year 2
