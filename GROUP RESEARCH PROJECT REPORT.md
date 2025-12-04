# Group Research Project Report: Study Habits & Academic Performance

**Module:** Research Methods for Business
**Date:** December 2, 2025
**Team Members:**
1. **BADR KOURDAD**
2. **XUE QIAN**
**Data Integrity:**
We have retained a complete set of raw data (`raw_survey_data.csv`) and the processed analysis file (`cleaned_study_data_final.csv`), both of which are version-controlled and available in this GitHub repository.


## 2. Executive Summary
**Business Problem:**
In the post-pandemic academic landscape, universities are facing a "productivity paradox": students have access to more digital tools than ever, yet burnout rates are rising and academic performance remains inconsistent. **EduAnalytics Lab** tasked our team with investigating the relationship between study habits, digital tool usage, and academic success to inform future curriculum designs.

**Methodology & Analysis:**
We conducted a quantitative survey of **34 university students**. To ensure rigour, we implemented a GitHub-based data cleaning workflow to remove invalid responses. We analyzed key variables including study duration, GPA, and stress levels using Python and Excel.

**Key Findings:**
1.  **The Efficiency Paradox:** Contrary to the "work harder" myth, students studying **10–15 hours/week** achieved the highest GPA (3.8/4.0), significantly outperforming those studying >15 hours (GPA 3.1).
2.  **The Hidden Cost:** High study volume (>15 hours) correlates with a critical stress level of **9.2/10**, suggesting cognitive overload.
3.  **Digital Strategy:** Students using planning tools (Notion) reported higher feelings of control than those relying solely on Generative AI.

**Recommendation:**
Universities should shift from providing software access to teaching **"Digital Methodology"**. We recommend implementing mandatory workshops on personal organization to help students maintain the optimal 10–15 hour study window.


## 3. Introduction
### 3.1 Context
As part of the research analytics team at EduAnalytics Lab, we are investigating the factors that influence student success in higher education. With the rise of digital tools and changing learning environments, traditional study methods are evolving. Universities need data-driven insights to design better academic support systems that prioritize efficiency over mere volume of work.

### 3.2 Research Objective
The primary objective of this project is to analyze the relationship between **study habits** (time management, use of digital tools, study environment) and **academic performance** (self-reported GPA). We aim to debunk the myth that volume of work is the sole predictor of success.

### 3.3 Research Question
*Does the use of modern digital tools and structured time management strategies correlate with higher academic performance compared to traditional volume-based study methods?*


## 4. Methodology
### 4.1 Research Design
We adopted a **quantitative research approach** using a cross-sectional survey design. This method was selected to efficiently identify patterns and correlations across a student population at a specific point in time.

### 4.2 Data Collection
* **Instrument:** An online questionnaire designed using Google Forms, comprising 20 items (demographics, study habits, psychometrics).
* **Sampling:** We used convenience sampling, targeting university students across Bachelor’s, Master’s, and PhD levels.
* **Sample Size:** **N = 34 valid responses**.
* **Timeline:** Data was collected in November 2025.

### 4.3 Data Cleaning & Analysis (GitHub Workflow)
Data integrity was a priority. We utilized **GitHub** for version control throughout the data processing pipeline:
1.  **Raw Data Ingestion:** The original dataset was uploaded to the `raw-data` branch as `raw_survey_data.csv`.
2.  **Cleaning Process:** We identified 2 "spam" responses (containing incoherent text) and removed them. We also standardized column headers (e.g., changing *"How many hours..."* to `Study_Hours`) to facilitate Python analysis.
3.  **Final Dataset:** The cleaned data was saved as `cleaned_study_data_final.csv` and merged into the main branch via a Pull Request.
4.  **Tools:** Analysis was performed using **Python (Pandas library)** for statistical correlation and Excel/Matplotlib for data visualization.


## 5. Results & Data Analysis

### 5.1 Demographic Profile: Study Intensity
We first analyzed how students allocate their time.
* **Observation:** The distribution follows a bell curve. The majority (65%) study between 5 and 15 hours.
* **Outliers:** A minority group (approx. 12%) works excessively, logging more than 15 hours per week.

![Distribution of Study Hours](graph1.png)
*Figure 1: Distribution of weekly study hours among respondents (N=34).*

### 5.2 Key Finding: The Efficiency Paradox
We tested the hypothesis that study hours differ by GPA. The results were counter-intuitive.
* **The "Sweet Spot":** Students studying **10–15 hours** reported the highest average GPA (3.8).
* **The Drop-off:** Students studying **>15 hours** saw their average GPA drop to **3.1**.
This visually demonstrates the law of diminishing returns in academic effort.

![GPA vs Hours](graph2.png)
*Figure 2: The Efficiency Paradox - Grades peak at 10-15 hours and decline thereafter.*

### 5.3 The Cost of Overworking: Stress Analysis
To explain the drop in GPA for hard workers, we analyzed reported stress levels (scale 1-10).
* **Correlation:** There is a strong linear correlation between hours worked and stress.
* **Critical Level:** While the 10-15h group has manageable stress (6.0), the >15h group reports an alarming average stress level of **9.2/10**.

![Stress Curve](graph4.png)
*Figure 3: Stress levels skyrocket for students studying more than 15 hours.*

### 5.4 Digital Tools Usage
We examined which tools students use to manage their studies.
* **Dominance of AI:** 60% of respondents primarily use Generative AI (ChatGPT).
* **The Planner Minority:** Only 35% prioritize Planning Tools (Notion/Calendar).
* *Insight:* Cross-referencing with GPA data, the "Planner" group is over-represented in the high-performing "10-15h" segment.

![Tools Distribution](graph3.png)
*Figure 4: Distribution of primary digital study tools.*

## 6. Discussion
### 6.1 Efficiency vs. Effort
Our findings challenge the traditional assumption that "more time equals better grades." The data indicates that students employing **Self-Regulated Learning (SRL)** strategies—specifically planning and time management—outperform those who simply increase study volume. This aligns with the research of **Broadbent and Poon (2015)**, who demonstrated that time management is a stronger predictor of academic success in online environments than mere participation metrics.

### 6.2 The Impact of Stress on Cognition
The collapse in GPA for students working >15 hours (Figure 2) can be directly attributed to the stress levels shown in Figure 3. **Hattie and Timperley (2007)** emphasize the importance of feedback loops in learning; students who are overworked and stressed lack the cognitive capacity to receive and act on feedback, leading to a cycle of high effort but low retention.

### 6.3 The Role of Digital Tools
While AI usage is high (60%), it does not guarantee success. **Rasheed et al. (2020)** suggest that without proper pedagogical integration, digital tools can become distractions rather than aids. Our data supports this: students using structural tools (Notion) performed better, aligning with **Gaudreau et al. (2012)** findings on the positive impact of goal-setting implementation.

### 6.4 Limitations
* **Sample Size:** N=34 is sufficient for exploratory analysis but small for broad generalization.
* **Self-Reporting Bias:** As noted by **Credé and Phillips (2011)**, survey data relies on student honesty. Students often overestimate their GPA and underestimate their procrastination due to social desirability bias.


## 7. Recommendations
Based on our analysis, we propose the following actionable recommendations for EduAnalytics Lab to present to partner institutions:

1.  **Implement "Digital Method Workshops" (Priority: High)**
    Universities should stop focusing on software training (how to use ChatGPT) and start teaching **Methodology** (how to organize a week). Workshops on "Building a Second Brain in Notion" would help students stay in the efficient 10-15h zone.

2.  **Redesign Student Support for "Overworkers"**
    Data analytics should be used to identify students logging excessive library hours (>20h). These students should not be praised but flagged as **"High Risk"** for burnout. We recommend offering them specific "Efficiency Coaching" to reduce their hours while maintaining grades.

3.  **Promote Continuous Assessment**
    To combat the stress peaks identified in Figure 3, universities should move towards continuous assessment (weekly micro-quizzes) rather than high-stakes final exams, encouraging regular, lower-stress study habits.


## 8. Reflection on Team Process
**Application of Agile Methodologies:**
To ensure effective collaboration and timely delivery, our team adopted Agile principles tailored for this research project:
1.  **Sprint Planning:** We divided the project into three distinct sprints: *Data Collection*, *Data Cleaning & Analysis*, and *Report Documentation*.
2.  **Kanban Workflow:** We used the **GitHub Projects** board to track tasks. We created Issues for "Survey Design", "Data Cleaning", and "Drafting Sections", moving them from *To Do* to *In Progress* and *Done*.
3.  **Version Control & Collaboration:** We utilized the **GitHub Flow**. One member worked on the `raw-data` branch while the other set up the report structure. We used **Pull Requests** to review the code and the data cleaning steps before merging into the `main` branch, ensuring that no data was lost or corrupted.


## 9. References
1.  **Broadbent, J. and Poon, W.L. (2015)** ‘Self-regulated learning strategies & academic achievement in online higher education learning environments: A systematic review’, *The Internet and Higher Education*, 27, pp. 1–13.
2.  **Credé, M. and Phillips, L.A. (2011)** ‘A meta-analytic review of the Motivated Strategies for Learning Questionnaire’, *Learning and Individual Differences*, 21(4), pp. 337–346.
3.  **Gaudreau, P., Carraro, N. and Miranda, D. (2012)** ‘From goal motivation to goal progress: The facilitating role of implementation intentions’, *Journal of Educational Psychology*, 104(4), p. 259.
4.  **Hattie, J. and Timperley, H. (2007)** ‘The power of feedback’, *Review of Educational Research*, 77(1), pp. 81–112.
5.  **Rasheed, R.A., Kamsin, A. and Abdullah, N.A. (2020)** ‘Challenges in the online component of blended learning: A systematic review’, *Computers & Education*, 144, p. 103701.

**Appendices:**
* **Appendix A:** Raw Data (Available in `raw_survey_data.csv` in this repository).
* **Appendix B:** Cleaned Dataset (Available in `cleaned_study_data_final.csv` in this repository).
