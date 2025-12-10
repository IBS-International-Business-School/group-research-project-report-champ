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
### **Project Overview**

As university students, we constantly hear that we need to "work harder" to succeed. But with all the digital tools available today—from ChatGPT to Notion planners—we wanted to find out if working *longer* actually means working *better*. This project investigates the link between study hours, stress, and grades (GPA).

### **What We Did**
We surveyed 100 students to track their habits. We used GitHub to manage our data and ensure our analysis was clean and reproducible.

### **Key Findings**

The results were surprising. We found that studying more isn't always the answer.

**The Limit:** Students who study **10–15 hours a week** actually get the best grades.

**The Burnout:** Those who study more than 15 hours saw their grades drop and their stress levels spike to a dangerous **9.2/10**.

**Tools Matter:** The top students mostly use planning apps (Calendar/Notion) rather than just relying on AI to do the work for them.

### **Recommendation:**

Universities should stop pushing students to just "study more." Instead, they need to teach us **how to organize**. Our recommendation is to introduce workshops on digital workflow and time management to help students stay in that efficient 10–15 hour zone.

## 2. Introduction

Education has changed rapidly in recent years, giving university students powerful tools such as AI assistants and digital planners. In theory, these should make studying easier, yet many students appear more stressed than ever. Within our peer group, we noticed no clear link between hours spent studying and final grades: some students work long hours with limited results, while others study less and achieve higher marks. This suggests that how students study may matter more than how much.

**Research Question**

Does the use of structured digital planning tools correlate with higher academic performance compared to simply increasing study hours?

**Research Objective**

To answer this, we focused on three specific areas:
1. Examine whether more study hours actually improve GPA or become counterproductive.
2. Measure how long study hours relate to stress levels.
3. Evaluate whether students using digital planning tools perform better than those who cram or rely mainly on AI.

Our aim is to understand what it means to “work smart” in modern university life.

## 3. Methodology

### 3.1 Research Design

We chose a **quantitative cross-sectional survey**. We wanted to capture a snapshot of current student habits to see if we could find statistical patterns. We didn't have the time to track students over a whole year (longitudinal), so a snapshot was the most practical approach for this semester.

### 3.2 Data Collection

We used a **convenience sampling** method. We created a Google Form with 21 questions covering demographics, study habits, stress levels (on a scale of 1-10), and self-reported GPA.
**Distribution:** We shared the link via WhatsApp student groups, Discord servers, and LinkedIn.
**Sample Size:** We received 102 responses. After cleaning, we kept **100 valid responses**.
**Bias Note:** Since we distributed this mostly within our own network (Business and Management students), our sample might be biased towards students who are already somewhat familiar with digital tools.

### 3.3 GitHub-Based Data Workflow

To meet the "Agile" and technical requirements of this project, we didn't just email Excel files back and forth. We used GitHub to act as a central source of truth.

1.  **Raw Data Storage:** We uploaded the original CSV from Google Forms to a folder named `data/raw`. This file was set to "read-only" in our minds—we never touched it directly to ensure we didn't accidentally delete data.
2.  **Data Cleaning:** We wrote a Python script (documented in `analysis.py` in the repo) to clean the data. This was necessary because some people answered "10-15 hours" while others wrote "about 12". The script standardized these into numbers we could actually plot.
3.  **Version Control:** When one of us wanted to try a new graph, we created a new **Branch** on GitHub. This prevented us from breaking the main report if the code didn't work. We used **Pull Requests** to review each other's changes before merging them into the final `main` branch.

This workflow was a bit difficult to learn at first, but it saved us a lot of panic later on because we always had a backup of previous versions.

## 4. Results & Data Analysis

After running our cleaned data through Python (using the Pandas and Seaborn libraries), three major patterns emerged that answered our research question.

### **4.1 The Distribution of Effort**
First, we looked at how much students are actually working

<img width="1628" height="938" alt="Picture1" src="https://github.com/user-attachments/assets/153eb627-e682-4a45-912f-3c46a1add31a" />

*Figure 1: Distribution of weekly study hours among respondents (N=100).*

Most students in our sample (about 36%) fall into the "moderate" category, studying between 10 and 15 hours a week outside of class. However, we noticed a significant tail of "over-workers"—students logging 20, 25, or even 30+ hours. We initially assumed these students would be the top performers.

### 4.2 The Efficiency Paradox
When we mapped these hours against GPA (on a 4.0 scale), the results surprised us. We expected a straight line going up (more hours = better grades). Instead, we got a curve.
This visually demonstrates the law of diminishing returns in academic effort.
<img width="1841" height="1042" alt="Picture2" src="https://github.com/user-attachments/assets/6463e2e0-3087-4350-b690-e73e382e21dc" />

*Figure 2: The Efficiency Paradox - Grades peak at 10-15 hours and decline thereafter.*

**Group A (<10 hours):** Average GPA of 2.9. These students likely aren't putting in enough effort to master the material.

**Group B (10-15 hours):** The "Sweet Spot." Average GPA of **3.6**. These students seem to balance effort with understanding.

**Group C (>15 hours):** The "Burnout Zone." Average GPA drops to **3.1**.

This visually demonstrates the law of diminishing returns. After 15 hours, every extra hour spent studying doesn't just stop adding value—it actually seems to hurt performance.


### 4.3 The Cost of Overworking: Stress Analysis
To explain the drop in GPA for hard workers, we analyzed reported stress levels (scale 1-10).

<img width="1820" height="1049" alt="Picture3" src="https://github.com/user-attachments/assets/6173cea8-b9da-4df5-95b0-8086ea91a7b0" />

*Figure 3: Stress levels skyrocket for students studying more than 15 hours.*

The correlation here was alarming. The 10-15 hour group reported manageable stress (average 6.1/10). But the students studying over 15 hours reported an average stress level of **9.2/10**. At this level of stress, cognitive function drops. It’s hard to retain information when you are in a state of panic or exhaustion. This explains the GPA drop: they are working harder, but their brains are too tired to absorb the information effectively.

### 4.4 Digital Tools Usage
Finally, we checked *how* they studied. We categorized students by their primary tool..

<img width="1349" height="895" alt="Picture4" src="https://github.com/user-attachments/assets/01fd98aa-3c03-4a1e-9ad6-801d947b1cec" />

*Figure 4: Distribution of  digital study tools*

We found that students in the high-performing "Sweet Spot" (10-15h) were twice as likely to use **Structured Planning Tools** (like Notion, Google Calendar, or physical planners) compared to the other groups. In contrast, the group studying >15 hours relied heavily on **Generative AI** (ChatGPT) or had no specific system. This suggests that high performers use tools to *manage their time*, while lower performers might be using AI to try and catch up on work they haven't planned for.

## **5. Discussion**

Our findings challenge the traditional "hustle culture" often seen in business schools. The data suggests that success isn't about raw effort; it's about **Strategic Regulation**

### **5.1 Efficiency vs Effort**

The most significant insight from our project is the "Efficiency Paradox." It aligns with the theory of Self-Regulated Learning (SRL). According to Broadbent and Poon (2015), students who succeed are not the ones who read the most pages, but the ones who plan *when* to read and monitor their own understanding. Our data backs this up: the 10-15 hour group isn't lazy; they are efficient. They likely stop studying when they hit a point of diminishing returns, whereas the >15 hour group pushes through, achieving less with more effort.

### **5.2 The Cognitive Load of Stress**

The correlation between high stress (9.2/10) and lower GPA in our heavy-studier group is consistent with Cognitive Load Theory. Hattie and Timperley (2007) argue that when a learner is under high cognitive strain or anxiety, their "working memory" gets clogged. They can't process new information because they are too busy managing their stress. In our study, the students working 25+ hours are likely "rereading" notes without actually absorbing them—a phenomenon often called "passive studying." They feel productive because they are tired, but the learning isn't happening.

### **5.3 The Role of Digital Tools**

It was interesting to see that ChatGPT usage didn't guarantee good grades. In fact, heavy reliance on AI was common in the "overworked" group. This mirrors the findings of Rasheed et al. (2020), who warn that digital tools can sometimes create a false sense of competence. A student might use ChatGPT to summarize a lecture and *think* they understand it, but they haven't done the deep cognitive work required to retain it. On the other hand, the high performers used tools like Notion. This supports Gaudreau et al. (2012), who discuss "implementation intentions." Planning *when* and *how* to do a task (using a calendar) is statistically more effective than just trying to do the task with an AI assistant at the last minute.

### **5.4 Limitations and Bias**
We have to be honest about the flaws in our research.
1.  **Sample Size:** We only had 100 people. To be truly scientific, we would need 500+ across different universities.
2.  **Self-Reporting:** We asked people for their GPA and stress. People often lie about their grades (making them higher) or their stress (exaggerating it). Credé and Phillips (2011) note that self-reported data always has a "social desirability bias."
3.  **Causality:** We found a correlation (more hours = more stress), but we can't prove causation. Maybe students who are *already* stressed tend to study more because they are anxious, rather than the studying *causing* the stress.

## 6. Recommendations
Based on the clear drop-off in performance after 15 hours of study, we propose the following actions for both students and universitiess.

**1. Teach "Workflow" not just "Work"**

Universities usually teach subjects (Marketing, Finance) but they rarely teach *how* to study those subjects. We recommend a mandatory "Digital Methodology" workshop in the first year. This shouldn't be about how to use Word or Excel, but how to build a "Second Brain" in Notion or how to use Time-Blocking in Outlook. If students learn to plan, they can stay in the 10-15 hour "Sweet Spot.".

**2. The "Red Flag" System for Advisors**

Since we know that stress hits 9/10 when study hours exceed 15, academic advisors should use this as a metric. If a student reports spending all their free time in the library, it shouldn't be seen as dedication—it should be seen as a risk of burnout. Advisors should intervene to help these students prioritize rather than encouraging them to "keep pushing".

**3. Shift to Low-Stakes Continuous Assessment**

The "binge-study" behavior often happens before big exams. To flatten the curve of stress, modules should rely more on weekly micro-quizzes. This forces students to study a little bit every week (staying in the healthy range) rather than cramming 30 hours in one week, which our data proves is ineffective.

## 7. Reflection on Team Process

Working on this project gave us a real crash course in **Agile Methodology**. It wasn't always smooth, but the structure helped us.

**Sprint Planning:**

We broke the project into three "Sprints":

**Sprint 1:** Survey design and data gathering.

**Sprint 2:** Data cleaning and Python analysis.

**Sprint 3:** Writing and report formatting.

This helped us avoid the usual student group project panic where everyone leaves everything until the night before. We knew exactly what had to be done each week.

**Using GitHub:**

Honestly, GitHub was a challenge. We had a few "merge conflicts" where two of us edited the `Analysis` section at the same time and couldn't save the file. However, this forced us to communicate better. We started using the "Issues" tab to assign tasks (e.g., "Fix the bar chart colors") so we didn't step on each other's toes. By the end, having a version history was a lifesaver when we accidentally deleted a paragraph and could restore it.

**Collaboration:**

We held short "stand-up" meetings on Discord every two days. Instead of hour-long meetings that go nowhere, we just answered three questions: "What did I do?", "What will I do?", and "Am I stuck?". This kept the momentum going and ensured the workload was balanced.
## 8.**Conclusion**
This research project started with a simple question: does working harder mean doing better? The data gave us a complicated but clear answer: **No.**

There is a clear ceiling to human productivity in an academic setting. Our study identified a "Sweet Spot" of 10-15 hours of study per week where GPA is maximized. Beyond this, the toxic combination of stress and cognitive overload causes performance to drop, creating an "Efficiency Paradox."

In a world obsessed with AI and speed, our findings suggest that the old-fashioned skill of **planning** is more valuable than ever. The students who succeed aren't the ones asking ChatGPT to write their essays; they are the ones using calendars to protect their time and mental health. For universities and businesses alike, the message is clear: we need to stop rewarding "busyness" and start teaching strategy.

## 9. References
1.  **Broadbent, J. and Poon, W.L. (2015)** ‘Self-regulated learning strategies & academic achievement in online higher education learning environments: A systematic review’, *The Internet and Higher Education*, 27, pp. 1–13.
2.  **Credé, M. and Phillips, L.A. (2011)** ‘A meta-analytic review of the Motivated Strategies for Learning Questionnaire’, *Learning and Individual Differences*, 21(4), pp. 337–346.
3.  **Gaudreau, P., Carraro, N. and Miranda, D. (2012)** ‘From goal motivation to goal progress: The facilitating role of implementation intentions’, *Journal of Educational Psychology*, 104(4), p. 259.
4.  **Hattie, J. and Timperley, H. (2007)** ‘The power of feedback’, *Review of Educational Research*, 77(1), pp. 81–112.
5.  **Rasheed, R.A., Kamsin, A. and Abdullah, N.A. (2020)** ‘Challenges in the online component of blended learning: A systematic review’, *Computers & Education*, 144, p. 103701.


## **Appendices**


* **Appendix A: Survey Questionnaire**
The data collected in this research was gathered using the following online instrument:

 [Click here to view the Google Form Questionnaire](https://docs.google.com/forms/d/e/1FAIpQLScRzhAviRfp85oceeVOFlmKVNbpbCsb-YC7wac2P-LqPSgN1g/viewform?usp=header)
* **Appendix B: Python Analysis Script**
The complete Python script used to clean the data and generate the visualizations is available in this repository:

 [Click here to view the analysis.py script](code/analysis.py)
* **Appendix C:** Raw Data Sample (First 5 rows of `survey_data_cleaned.csv`)
