# Measuring AI's Impact on the Job Search

**Nicholas Qiu** | Advised by Benjamin Golub  
Mathematical Methods in the Social Sciences, Northwestern University  
June 2026

This repository contains the data and analysis code for a survey-based study examining how job-seeking students perceive the prevalence and ethical acceptability of AI-assisted cheating in recruitment, and to what extent perceptions of peer behavior shape individual willingness to engage in it. The study pairs a human survey (n=249) with a cohort of 150 AI agents administered the same instrument.

---

## Repository Structure

```
ai-job-search-study/
├── Data Files/
│   ├── Human Survey Responses.xlsx       # Cleaned survey responses from human respondents
│   ├── AI Agent Survey Responses.xlsx    # Survey responses from the AI agent cohort
│   ├── Generated Agent Profiles.csv      # Demographic and attitudinal profiles assigned to each agent
│   └── gen_agents.py                     # Script used to generate agent profiles and administer the survey
├── Analysis Files/
│   ├── h1_descriptive_norm.ipynb         # H1: Descriptive norm effect and DeGroot peer influence model
│   ├── h2_fairness_analysis.ipynb        # H2: Fairness perceptions and moral disengagement
│   ├── h3_deterrence_analysis.ipynb      # H3: Detection confidence and deterrence
│   ├── h4_experience_normalization.ipynb # H4: Interview experience and normalization
│   └── h5_human_ai_divergence.ipynb      # H5: Human-agent distributional divergence
├── Survey Instrument/
│   ├── Thesis_Main_Survey.qsf            # Qualtrics survey file (importable into Qualtrics)
│   └── Thesis_Main_Survey.docx           # Human-readable version of the full questionnaire
├── LICENSE
└── README.md
```

---

## Data Files

### `Human Survey Responses.xlsx`
Responses from 249 U.S. undergraduate students, graduate students, and early-career professionals recruited primarily through Northwestern University, the University of Chicago, and several other institutions in the greater Chicago area. The survey was administered between December 2025 and May 2026 via Qualtrics and in-person recruitment. Respondents are concentrated in STEM and quantitative fields.

### `AI Agent Survey Responses.xlsx`
Responses from a cohort of 150 AI agents administered the identical survey instrument. Each agent was instantiated using ChatGPT 5.2 and assigned a demographic and attitudinal profile drawn from the target population. The responses were generated using [ExpectedParrot](https://www.expectedparrot.com/)

### `Generated Agent Profiles.csv`
The demographic and attitudinal profiles assigned to each of the 150 agents. Profiles vary across age, gender, education level, years of professional experience, industry, employment status, AI usage frequency, trust in AI tools, perceived fairness of AI-assisted hiring, and self-assessed interview confidence.

### `gen_agents.py`
Python script used to programmatically generate agent profiles and administer the survey instrument to each agent. Run this script to reproduce the agent cohort from scratch. Note that results may vary across runs due to model nondeterminism.

---

## Analysis Files

Each notebook corresponds to one of the five hypotheses tested in the paper. They are independent of one another and can be run in any order, though reading them in sequence (H1 through H5) follows the structure of the paper.

### `h1_descriptive_norm.ipynb`
Tests whether higher perceived prevalence of peer cheating is associated with greater individual willingness to engage in unauthorized assistance. Includes correlational analysis of peer estimates against willingness, cross-tabulation of the anonymous disclosure items, scenario-based within-respondent comparisons (Q13a vs. Q14a), and estimation of a DeGroot social contagion model using industry-segmented peer networks.

### `h2_fairness_analysis.ipynb`
Tests whether lower perceived fairness of the hiring process is associated with greater willingness to cheat. Includes cross-tabulation of fairness ratings (Q21) against behavior-specific acceptability scores (Q3), Spearman correlation of fairness against Q13a willingness, and qualitative theme analysis of open-ended responses to Q6.

### `h3_deterrence_analysis.ipynb`
Tests whether lower confidence in companies' ability to detect and act on cheating predicts higher willingness. Includes cross-tabulation of detection (Q23) and enforcement (Q24) confidence against Q13a willingness, Spearman correlations, and analysis of consequence preference distributions (Q25) against willingness.

### `h4_experience_normalization.ipynb`
Tests whether greater prior interview experience is associated with higher normalization of dishonest behavior. Respondents are grouped into four experience bands (0-1, 2-6, 7-10, 11+ interviews) and compared on peer cheating estimates (Q2), willingness (Q13a), and acceptability ratings (Q3). Includes willingness profile clustering and cross-tabulation by field of study.

### `h5_human_ai_divergence.ipynb`
Examines systematic divergence between human respondents and AI agents across all survey items. Computes mean divergence and variance ratios for each item, grouped by social contingency type. This notebook draws on outputs from all four preceding analyses and produces the summary figure (Figure 9 in the paper).

---

## Survey Instrument

### `Thesis_Main_Survey.qsf`
The complete Qualtrics survey file. This can be imported directly into Qualtrics to recreate the exact survey as administered, including block structure, question ordering, branching logic, and the raffle entry redirect. To import: log into Qualtrics, create a new project, and select "Import a QSF file."

### `Thesis_Main_Survey.docx`
A human-readable version of the full questionnaire, showing all question text, response options, and block organization. Equivalent to Appendix A.1 in the paper. Useful for reviewing the instrument without a Qualtrics account.

---


## Requirements

The analysis notebooks require Python 3 with the following packages:

```
pandas
numpy
scipy
statsmodels
matplotlib
seaborn
openpyxl
jupyter
```

Install all dependencies with:

```bash
pip install pandas numpy scipy statsmodels matplotlib seaborn openpyxl jupyter
```

---

## Reproducing the Analysis

1. Clone the repository and install dependencies (see above).
2. Open any notebook in the `Analysis Files/` folder using Jupyter:
   ```bash
   jupyter notebook
   ```
3. Each notebook loads data directly from the `Data Files/` directory using relative paths. Ensure the folder structure is preserved as cloned.
4. Run all cells in order within each notebook.

---

## Notes

- Human survey data was collected under IRB approval. Individual responses are anonymous; no personally identifiable information is stored in the data files.
- For questions about the study design or data, contact Nicholas Qiu.