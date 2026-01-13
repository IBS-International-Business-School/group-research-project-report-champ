<h1 align="center">
  Group Research Project Report : Study Habits and Academic Performance: A Data-Driven Analysis
</h1>

**Module:** SKIB353_25A

**Date:** January 12th, 2026

**Team Members:**

BADR KOURDAD

XUE QIAN
   
## **Declaration**

ChatGPT (GPT-5) was used to brainstorm themes and structure for this group research project report on the topic of Study Habits and Academic Performance.
Prompt example: “Help structure a survey-based research report examining study habits and academic performance for a data analytics module.
No AI-generated text was included verbatim in the final submission. All analysis, interpretation, and written content were independently produced by the student group.
Accessed: 13 January 2026. Available at: https://chat.openai.com/
We confirm that a complete set of raw data has been retained, including the original survey questionnaire, downloaded survey records, and data analysis files, in accordance with the module’s academic conduct and data retention requirements.

## **GitHub Repository Link**
All project files, including raw data, code, and documentation, are available at:
https://github.com/IBS-International-Business-School/group-research-project-report-champ

## **1. Executive Summary**
### **1.1 Project Overview**

This project examines the relationship between students’ study habits and academic performance in higher education. As universities increasingly adopt data-driven approaches to enhance learning outcomes, understanding which learning behaviours have the greatest impact on student success is essential. The study was conducted within the context of EduAnalytics Lab’s mission to inform academic support services and curriculum design through empirical research.

### **1.2 What We Did**
A survey-based research approach was used to collect data from 169 students across different levels of study. The questionnaire measured five key study habit constructs: time management, self-regulated learning, revision strategies, digital tool usage, and group study dynamics, alongside self-reported academic performance (GPA). After data cleaning and preparation, including Likert-scale transformation, reverse coding, and construct aggregation, Pearson correlation and multiple regression analyses were conducted to evaluate the relationships between study habits and academic performance.

### **1.3 Key Findings**

The analysis revealed that while all study habit constructs were positively correlated with academic performance, only digital tool usage and time management demonstrated statistically significant unique effects on GPA when controlling for other variables. Digital tool usage emerged as the strongest predictor of academic performance, highlighting the importance of purposeful and effective engagement with digital learning technologies.

### **1.4 Recommendation**

The study recommends that higher education institutions prioritise the development of students’ digital learning competencies and time management skills through targeted academic support initiatives. Rather than relying on generic study skills programmes, universities should adopt focused, data-informed interventions that address the learning behaviours most strongly associated with academic success.

## **2. Introduction**
### **2.1 Background and Context**

Academic performance is influenced by a range of behavioural, cognitive, and contextual factors, among which students’ study habits play a central role. In higher education, students are expected to manage increasing levels of autonomy, workload, and digital engagement, making effective study behaviours essential for academic success. As universities continue to expand flexible and technology-mediated learning environments, understanding how different study habits relate to academic performance has become an important concern for educators and academic support services.

### **2.2 Research Motivation**

The objective of this study is to examine the relationship between key study habit constructs and academic performance using a data-driven approach. Specifically, the study investigates five dimensions of study habits: time management, self-regulated learning, revision strategies, digital tool usage, and group study dynamics. By applying correlation and multiple regression analyses, the research aims to identify which study habits are most strongly associated with academic performance and which demonstrate unique predictive value when controlling for overlapping behaviours.

### **2.3 Structure of the Report**

The remainder of this report is organised as follows. The next section outlines the research methodology, including survey design, data collection, and analytical methods. This is followed by the presentation of results from the correlation and regression analyses. The discussion section interprets the findings in relation to existing literature and addresses limitations. Finally, the report concludes with practical recommendations and a reflection on the team’s collaborative research process.

## **3. Methodology**

### **3.1 Research Design**

A quantitative, survey-based research design was employed to examine the relationship between students’ study habits and academic performance. This approach was selected to enable systematic data collection and statistical analysis across multiple learning constructs.

### **3.2 Data Collection**

Data were collected through an online questionnaire distributed to university students. Participation was voluntary, and the survey was conducted anonymously. No personally identifiable information was collected.

The questionnaire consisted of demographic items, self-reported academic performance (GPA category), and Likert-scale items measuring study habits. Responses were recorded using a five-point Likert scale ranging from 1 (Strongly Disagree) to 5 (Strongly Agree).

### **3.3 Data Preparation**

Data cleaning was conducted in multiple stages. System-generated metadata were removed, variables were standardised, and Likert-scale responses were converted to numeric values. One reverse-coded item related to procrastination was recoded to ensure directional consistency. Composite constructs were then created by averaging relevant items for each study habit category. GPA was converted from categorical responses into an ordinal numeric variable ranging from 1 to 4.

### **3.4 Analytical Methods**

Descriptive statistics, Pearson correlation analysis, and multiple linear regression were used to analyse the data. Cronbach’s alpha was calculated to assess the internal consistency of each construct. All analyses were conducted using Python-based statistical tools.

## **4. Results**

### **4.1 Correlation Analysis**

Pearson correlation analysis revealed positive relationships between all study habit constructs and academic performance. Digital tool usage demonstrated the strongest correlation with GPA (r = 0.38), while time management, self-regulated learning, revision strategies, and group study dynamics exhibited weaker positive correlations (r ≈ 0.20–0.22). Strong intercorrelations were observed among the study habit constructs themselves, indicating that effective learning behaviours tend to co-occur.
<img width="994" height="844" alt="image" src="https://github.com/user-attachments/assets/e900b7ac-2a4a-453d-a9d3-7e6a476833e5" />


### **4.2 Multiple Regression Analysis**

A multiple linear regression analysis was conducted to assess the unique predictive power of each study habit construct. The overall model was statistically significant, F(5,163) = 6.98, p < .001, explaining 17.6% of the variance in GPA (R² = .176, adjusted R² = .151).

Digital tool usage (β = .507, p < .001) emerged as the strongest predictor of academic performance, followed by time management (β = .253, p = .040). Self-regulated learning, revision strategies, and group study dynamics did not show statistically significant unique effects when controlling for other variables.
<img width="1169" height="819" alt="image" src="https://github.com/user-attachments/assets/a00b3e27-5976-4021-8c10-c965addb4031" />


## **5. Discussion**

### **5.1 Key finds**

a) The findings indicate that while multiple study habits are associated with academic performance, only certain behaviours retain predictive power when examined simultaneously.

b) Digital tool usage emerged as the most influential predictor of GPA, suggesting that effective engagement with digital learning technologies plays a central role in supporting academic success.

c) This result aligns with prior research emphasising the growing importance of digital competence in contemporary learning environments.

### **5.2 Role of Time Management**

a) Time management demonstrated a statistically significant independent effect on GPA, reinforcing its role as a foundational self-management skill in higher education.

b) This finding supports existing literature that identifies effective time management as critical in contexts characterised by high autonomy and flexible learning structures.

### **5.3 Non-Significant Predictors and Behavioural Overlap**

a) Self-regulated learning, revision strategies, and group study dynamics did not independently predict GPA in the regression model, despite their positive correlations with academic performance.

b) This pattern likely reflects the interconnected nature of learning behaviours and the presence of overlapping effects among constructs when analysed simultaneously.

### **5.4 Methodological Implications and Limitations**

a) From a methodological perspective, the results highlight the value of multivariate analysis in educational research.

b) While correlation analysis identifies general associations, regression analysis provides deeper insight into the relative importance of predictors.

c) Limitations of the study include the use of self-reported GPA and the cross-sectional research design, which restricts causal inference. the stress.

## **6. Recommendations**

### **6.1 Prioritise digital learning competencies**

Higher education institutions should prioritise the development of students’ digital learning competencies. Training initiatives should emphasise the strategic use of digital tools for organisation, learning support, and academic planning, rather than focusing solely on technology adoption.

### **6.2 Embed time management support in early-stage programmes**

Time management support should be integrated into early-stage academic programmes, particularly for first-year students. Interventions such as structured planning tools and workload management workshops may help students translate learning intentions into effective and sustainable study behaviours.

### **6.3 Adopt integrated academic support approaches**

Academic support services should adopt integrated approaches that recognise the interconnected nature of learning behaviours. Rather than addressing study habits in isolation, data-informed targeting of support resources may improve both the efficiency and effectiveness of student success initiatives.

## **7. Reflection on Team Process**

### **7.1 Adoption of a lean and agile workflow**

Throughout the project, the team adopted a lean and agile approach to collaboration, which was particularly effective given the small team size and limited timeframe. The project was structured into short, goal-oriented sprints aligned with key milestones, such as survey design, data analysis, and report writing. This approach helped break down a complex research task into manageable phases and reduced the risk of workload bottlenecks near deadlines.

### **7.2 Use of informal stand-ups and retrospectives**
Informal stand-up meetings were used to share progress updates, clarify responsibilities, and identify issues at an early stage. These check-ins improved coordination and allowed the team to respond quickly to emerging challenges. In addition, brief retrospective discussions were held after major phases to reflect on what worked well and what could be improved, supporting continuous learning and process refinement.

### **7.3 GitHub as a central collaboration platform**
GitHub served as the primary platform for collaboration and version control. Branching enabled parallel development of different components without disrupting the main workflow, while pull requests facilitated peer review, constructive feedback, and quality control. GitHub Issues were used to track tasks and document problems, enhancing transparency and accountability.

### **7.4 Evidence of collaboration and shared ownership**
Evidence of effective collaboration can be found in the GitHub commit history, branch structure, and pull request records. These artefacts demonstrate active participation from all team members and reflect a shared sense of responsibility for the project’s outcomes.

### **7.5 Impact on teamwork and personal learning**

Overall, this workflow enhanced adaptability, accountability, and shared ownership of the project. More importantly, it strengthened my understanding of how agile principles and collaborative tools can support effective teamwork in data-driven research environments, which I intend to apply in future academic and professional projects.

## **8.Conclusion**
This study explored the relationship between students’ study habits and academic performance using a survey-based, data-driven approach. The findings indicate that although multiple study habits are positively associated with academic performance, digital tool usage and time management emerge as the most influential predictors of GPA when examined simultaneously.

These results highlight that learning behaviours do not contribute equally to academic success and that overlapping effects exist among different study habits. In particular, the strong role of digital tool usage underscores the growing importance of effective engagement with technology in contemporary higher education, while the significance of time management reinforces its role as a foundational self-management skill.

From a practical perspective, the study suggests that higher education institutions may benefit from prioritising targeted academic support initiatives focused on digital learning competencies and time management, rather than relying solely on generic study skills training.

Key limitations include the use of self-reported GPA and the cross-sectional design, which restrict causal interpretation. Future research could extend this work through longitudinal or experimental approaches to further examine the impact of specific learning interventions.

## **9. References**
1.  **Broadbent, J. and Poon, W.L. (2015)** ‘Self-regulated learning strategies & academic achievement in online higher education learning environments: A systematic review’, *The Internet and Higher Education*, 27, pp. 1–13.
2.  **Credé, M. and Phillips, L.A. (2011)** ‘A meta-analytic review of the Motivated Strategies for Learning Questionnaire’, *Learning and Individual Differences*, 21(4), pp. 337–346.
3.  **Gaudreau, P., Carraro, N. and Miranda, D. (2012)** ‘From goal motivation to goal progress: The facilitating role of implementation intentions’, *Journal of Educational Psychology*, 104(4), p. 259.
4.  **Hattie, J. and Timperley, H. (2007)** ‘The power of feedback’, *Review of Educational Research*, 77(1), pp. 81–112.
5.  **Rasheed, R.A., Kamsin, A. and Abdullah, N.A. (2020)** ‘Challenges in the online component of blended learning: A systematic review’, *Computers & Education*, 144, p. 103701.


## **Appendices**


* **Appendix A: Survey Questionnaire**
The data collected in this research was gathered using the following online instrument:
[https://v.wjx.cn/vm/wpb6PMl.aspx#]

* **Appendix B: Skills_for_Data_Analysts**
The complete Jupyter Notebook used for data cleaning, analysis, and visualisation is available in this repository.

* **Appendix C:** raw _data
* **Appendix D:** clean_data_final
