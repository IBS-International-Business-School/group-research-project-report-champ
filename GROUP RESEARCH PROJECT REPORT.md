<h1 align="center">
  Group Research Project Report : Study Habits & Academic Performance
</h1>

**Module:** Research Methods for Business

**Date:** December 2, 2025

**Team Members:**

BADR KOURDAD

XUE QIAN
   
## **Declaration**

We declare that this report is the original work of our group. Any use of AI tools was restricted to idea generation and structural planning in accordance with Level 2 AI guidelines. All sources have been properly acknowledged using Harvard referencing. Raw data and all analysis files are retained and available upon request.

## GitHub Repository Link
All project files, including raw data, code, and documentation, are available at:
https://github.com/IBS-International-Business-School/group-research-project-report-champ

## 1. Executive Summary
### **1.1 Business Problem**

Post-pandemic universities face a “productivity paradox”: despite increased access to digital study tools, academic inconsistency and burnout remain significant challenges. EduAnalytics Lab commissioned this project to investigate how study habits—particularly the integration of digital tools and time-management strategies—influence academic success.

### **1.2 Methodology**
A cross-sectional quantitative survey collected responses from 34 university students. Data cleaning and validation were conducted using GitHub-based workflows. Statistical analysis (correlation, descriptive metrics, visualisation) was performed using Python (Pandas) and Excel.

### **1.3 Key Findings**

**The Efficiency Paradox:** Students studying 10–15 hours weekly reported the highest GPA (3.8).

**Stress as a Limiting Factor:** Students exceeding 15 hours of study displayed critically high stress (9.2/10), explaining the observed decline in GPA.

**Digital Tool Insight:** Students who used structured planning tools (Notion/Calendar) were over-represented in the high-performing group, compared to those relying primarily on generative AI.

### **2.4 Recommendation:**

Integrate Digital Methodology into the curriculum.
Provide mandatory productivity and self-regulation workshops.
Promote structured collaborative learning environments.
Adopt continuous assessment to reduce stress-related performance decline.

## 2. Introduction

The rapid digital transformation of higher education has reshaped how students study and how institutions design learning ecosystems. While students today have more resources than ever, academic performance remains inconsistent. This project examines whether structured study behaviours—such as planned study routines and the use of digital organisational tools—lead to better outcomes than high-volume studying alone.

**Research Question**

Does the use of digital planning tools and structured time-management strategies correlate with higher academic performance compared to traditional high-volume study &nbsp;approaches?

**Research Objective**

To analyse the relationship between study habits, digital tool usage, stress levels, and self-reported GPA among university students.

## 3. Methodology

### 3.1 Research Design

A quantitative cross-sectional survey approach was used to capture relationships between study hours, tool usage, stress, and GPA at a single point in time.

### 3.2 Data Collection

**Instrument:** Google Forms questionnaire, 20 items covering study habits, demographics, and psychometric indicators.

**Sampling:** Convenience sampling of higher-education students (BA–PhD).

**Sample Size:** N = 34 valid responses.

**Timeline:** Data was collected in November 2025.

### 3.3 GitHub-Based Data Workflow

Data integrity was a priority. We utilized **GitHub** for version control throughout the data processing pipeline:

**Raw Data upload:** raw_survey_data.csv committed to a dedicated branch.

**Cleaning Process:** We identified 2 "spam" responses (containing incoherent text) and removed them. We also standardized column headers (e.g., changing *"How many hours..."* to `Study_Hours`) to facilitate Python analysis.

**Final Dataset:** The cleaned data was saved as `cleaned_study_data_final.csv` and merged into the main branch via a Pull Request.

**Tools:** Analysis was performed using **Python (Pandas library)** for statistical correlation and Excel/Matplotlib for data visualization.

## 4. Results & Data Analysis

### 4.1 Demographic Profile: Study Intensity
We first analyzed how students allocate their time.
* **Observation:** The distribution follows a bell curve. The majority (65%) study between 5 and 15 hours.
* **Outliers:** A minority group (approx. 12%) works excessively, logging more than 15 hours per week.

![Distribution of Study Hours](graph1.png)
*Figure 1: Distribution of weekly study hours among respondents (N=34).*

### 4.2 Key Finding: The Efficiency Paradox
We tested the hypothesis that study hours differ by GPA. The results were counter-intuitive.
* **The "Sweet Spot":** Students studying **10–15 hours** reported the highest average GPA (3.8).
* **The Drop-off:** Students studying **>15 hours** saw their average GPA drop to **3.1**.
This visually demonstrates the law of diminishing returns in academic effort.

![GPA vs Hours](graph2.png)
*Figure 2: The Efficiency Paradox - Grades peak at 10-15 hours and decline thereafter.*

### 4.3 The Cost of Overworking: Stress Analysis
To explain the drop in GPA for hard workers, we analyzed reported stress levels (scale 1-10).
* **Correlation:** There is a strong linear correlation between hours worked and stress.
* **Critical Level:** While the 10-15h group has manageable stress (6.0), the >15h group reports an alarming average stress level of **9.2/10**.

![Stress Curve](graph4.png)
*Figure 3: Stress levels skyrocket for students studying more than 15 hours.*

### 4.4 Digital Tools Usage
We examined which tools students use to manage their studies.
* **Dominance of AI:** 60% of respondents primarily use Generative AI (ChatGPT).
* **The Planner Minority:** Only 35% prioritize Planning Tools (Notion/Calendar).
* *Insight:* Cross-referencing with GPA data, the "Planner" group is over-represented in the high-performing "10-15h" segment.

![Tools Distribution](graph3.png)
*Figure 4: Distribution of primary digital study tools.*

## 5. Discussion
### 5.1 Efficiency vs. Effort
Our findings challenge the traditional assumption that "more time equals better grades." The data indicates that students employing **Self-Regulated Learning (SRL)** strategies—specifically planning and time management—outperform those who simply increase study volume. This aligns with the research of **Broadbent and Poon (2015)**, who demonstrated that time management is a stronger predictor of academic success in online environments than mere participation metrics.

### 5.2 The Impact of Stress on Cognition
The collapse in GPA for students working >15 hours (Figure 2) can be directly attributed to the stress levels shown in Figure 3. **Hattie and Timperley (2007)** emphasize the importance of feedback loops in learning; students who are overworked and stressed lack the cognitive capacity to receive and act on feedback, leading to a cycle of high effort but low retention.

### 5.3 The Role of Digital Tools
While AI usage is high (60%), it does not guarantee success. **Rasheed et al. (2020)** suggest that without proper pedagogical integration, digital tools can become distractions rather than aids. Our data supports this: students using structural tools (Notion) performed better, aligning with **Gaudreau et al. (2012)** findings on the positive impact of goal-setting implementation.

### 5.4 Limitations
* **Sample Size:** N=34 is sufficient for exploratory analysis but small for broad generalization.
* **Self-Reporting Bias:** As noted by **Credé and Phillips (2011)**, survey data relies on student honesty. Students often overestimate their GPA and underestimate their procrastination due to social desirability bias.


## 6. Recommendations
Drawing on the empirical patterns identified in this study, as well as relevant literature on academic performance and digital learning, the following recommendations are proposed for higher education institutions seeking to enhance student wellbeing and learning outcomes.

**1. Integrate Digital Methodology into the Curriculum**

 Universities should move beyond software-oriented training and incorporate formal instruction in Digital Methodology, including workflow design, digital organisation, and the critical evaluation of AI-enabled tools. Structured sessions—such as “second brain” systems built in applications like Notion—may support students in maintaining the optimal 10–15 hour weekly study range identified in this research..

**2. Implement Mandatory Workshops on Productivity and Self-Regulation**

Institutions should provide compulsory workshops addressing personal productivity, time management, and self-regulation. Such interventions can mitigate cognitive overload and reduce the risk of burnout among students who consistently report more than 20 hours of study per week. These students should be classified as a high-risk group and offered tailored support to sustain performance while reducing excessive workload..

**3. Promote Structured Collaborative Learning Environments**

To combat the stress peaks identified in Figure 3, universities should move towards continuous assessment (weekly micro-quizzes) rather than high-stakes final exams, encouraging regular, lower-stress study habits.

**4. Adopt Continuous Assessment Models**

To address the stress peaks associated with end-of-term examinations, universities should consider adopting continuous assessment models. Implementing regular low-stakes assessments—such as weekly micro-quizzes—can encourage consistent learning behaviour, reduce pressure, and support long-term knowledge retention.

## 7. Reflection on Team Process
**Application of Agile Methodologies**
To ensure effective collaboration and timely delivery, our team adopted Agile principles tailored for this research project:

**Sprint Planning:**
The project was divided into three short sprints: (1) survey design and deployment, (2) data cleaning and statistical analysis, and (3) report writing and review. Each sprint had clear objectives and task allocations, which improved efficiency and focus.

**Kanban Workflow:**
The team used GitHub Projects to maintain a To Do / In Progress / Done board, enabling real-time monitoring of task progress and dependencies. This visual workflow reduced delays and strengthened coordination.

**Version Control:**
We adopted GitHub Flow, using branches and Pull Requests for structured review of code and documentation. This ensured transparency in data processing, prevented version conflicts, and maintained overall accuracy.

**Collaboration Successes:**
Regular stand-ups facilitated timely communication, while sprint retrospectives supported continuous process improvement. Team members provided mutual support during high-workload stages, demonstrating adaptability and effective collaboration.

## 9. References
1.  **Broadbent, J. and Poon, W.L. (2015)** ‘Self-regulated learning strategies & academic achievement in online higher education learning environments: A systematic review’, *The Internet and Higher Education*, 27, pp. 1–13.
2.  **Credé, M. and Phillips, L.A. (2011)** ‘A meta-analytic review of the Motivated Strategies for Learning Questionnaire’, *Learning and Individual Differences*, 21(4), pp. 337–346.
3.  **Gaudreau, P., Carraro, N. and Miranda, D. (2012)** ‘From goal motivation to goal progress: The facilitating role of implementation intentions’, *Journal of Educational Psychology*, 104(4), p. 259.
4.  **Hattie, J. and Timperley, H. (2007)** ‘The power of feedback’, *Review of Educational Research*, 77(1), pp. 81–112.
5.  **Rasheed, R.A., Kamsin, A. and Abdullah, N.A. (2020)** ‘Challenges in the online component of blended learning: A systematic review’, *Computers & Education*, 144, p. 103701.

**Appendices:**
* **Appendix A:** Raw Data (Available in `raw_survey_data.csv` in this repository).
* **Appendix B:** Cleaned Dataset (Available in `cleaned_study_data_final.csv` in this repository).
