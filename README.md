![Screenshot 2024-09-15 101758](https://github.com/user-attachments/assets/b0b6dfaf-2cff-473d-a3e3-9c01c67e584b)

# Telecom Customer Churn Attrition Prediction

In today's competitive telecom industry, retaining customers is more important than ever. Customer churn, or when users leave for another provider, can significantly impact a company's bottom line. This project focuses on building a predictive model to help identify which customers are likely to leave based on their usage patterns, behavior, and other factors. By understanding these patterns, companies can act early to keep customers happy and reduce churn.

This repository includes everything needed to analyze customer churn, from the dataset to the code used for predictions. It also offers insights into key factors driving customer attrition and suggests strategies to help telecom companies improve customer retention. For a quick overview, watch the YouTube video linked below.




---

## Table of Contents
- [Problem Statement](#problem-statement)
- [Objective](#objective)
- [Methodology](#methodology)
- [Data Insights](#data-insights)
- [Power BI Visuals](#power-bi-visuals)
- [Key Findings](#key-findings)
- [References](#references)
- [Usage Instructions](#usage-instructions)
- [Running the Project](#Running-the-Project)
- [Deployment Steps](#Deployment-Steps)

---

## Problem Statement

In the dynamic landscape of the telecommunications industry, customers wield the power to choose from a plethora of service providers for their communication and internet needs. Customer satisfaction plays a pivotal role as users often form opinions about an entire company based on a single interaction. The ubiquitous nature of communication services, intertwined with our daily lives, underscores the significance of understanding and mitigating customer churn.

Churn rate, a key metric representing the number of customers who terminate or do not renew their subscriptions, directly impacts revenue. Given the high costs associated with acquiring new customers, an in-depth churn analysis is imperative. Insights derived from this analysis empower companies to formulate strategic approaches, target specific segments, enhance service quality, and ultimately foster trust with their customers. Building predictive models and generating comprehensive reports through churn analysis thus becomes instrumental in driving sustainable growth.

---

## Objective

The primary objective is to develop a robust predictive model capable of classifying potential churn customers based on a comprehensive set of numerical and categorical features. This poses a binary classification challenge, considering the inherent imbalance in the dataset.

1. **Dataset Overview and Attributes:**
   Providing an in-depth look into the dataset, detailing various attributes such as customerID, gender, SeniorCitizen status, partnership, dependents, tenure, phone services, and more.

2. **Customer Profile Details:**
   Highlighting key customer-related information, covering aspects like demographics, service usage, contract terms, billing preferences, and payment methods.

3. **Internet and Service Features:**
   Elaborating on the availability of internet services and specific features such as online security, backup, device protection, tech support, streaming TV, and streaming movies.

4. **Contract and Billing Information:**
   Describing the terms of customer contracts, paperless billing preferences, payment methods employed, and the associated monthly and total charges.

5. **Churn Status and Analytics Process:**
   Delving into the critical aspect of customer churn, outlining the notebook's contents, which include Dataset Information, Exploratory Data Analysis (EDA), Summary of EDA, Feature Engineering, Modeling, and a Conclusion.

6. **Utilize Power BI for Visual Insights:**
   Implementing Power BI to create interactive visualizations and dashboards that provide deep insights into churn patterns, customer segments, and predictive model performance. This includes visual representations of churn trends, customer demographics, and service usage patterns to facilitate strategic decision-making.


---

## Methodology

1. **Data Collection and Preparation:**
   - Curated a comprehensive dataset comprising customer demographics, service usage details, contract specifics, and billing preferences.
   - Employed rigorous data cleaning and preprocessing techniques to ensure data integrity and consistency.

2. **Exploratory Data Analysis (EDA):**
   - Conducted in-depth EDA to uncover hidden patterns, correlations, and anomalies within the dataset.
   - Visualized key metrics such as customer segmentation by contract type and churn propensity across different customer segments using tools like Power BI for interactive visualizations.

3. **Predictive Modeling:**
   - Developed and fine-tuned machine learning models including Logistic Regression, Random Forest, and Gradient Boosting.
   - Evaluated model performance based on metrics such as accuracy, precision, recall, and ROC-AUC score to select the optimal model for churn prediction.

4. **Power BI for Visual Insights:**
   - Implemented Power BI to create interactive dashboards and visualizations that provide intuitive insights into churn patterns.
   - Visualized model predictions, feature importance, and customer segmentation to facilitate strategic decision-making and operational planning.
---

## Data Insights


Explore profound insights and analytics gleaned from our extensive dataset. Uncover a deeper understanding of customer behaviors, patterns in service usage, and the pivotal factors that influence churn dynamics.


| Feature                                      | Visualization                                                                                       |
|----------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Categorical Features                         | ![Categorical Features](https://github.com/virajbhutada/Telecom-Customer-Churn-Prediction/assets/143819712/ce2e270e-2118-41b5-8207-1fccd2e98982)   |
| Churn Target Variable                        | ![Churn Target Variable](https://github.com/virajbhutada/Telecom-Customer-Churn-Prediction/assets/143819712/681e2805-d61e-4d56-be55-fa0495a5bfd5)  |
| Customer Information                         | ![Customer Information](https://github.com/virajbhutada/Telecom-Customer-Churn-Prediction/assets/143819712/234d902f-f514-4d2f-b28a-6d5813c67909)   |
| Distribution Analysis                        | ![Distribution Analysis](https://github.com/virajbhutada/Telecom-Customer-Churn-Prediction/assets/143819712/e72dbd50-9c94-4c44-bf89-1b3baa090a64)   |
| Mean Tenure                                  | ![Mean Tenure](https://github.com/virajbhutada/Telecom-Customer-Churn-Prediction/assets/143819712/0f8feb7e-d723-4061-beb6-62275d6a54b9)         |
| Churn Tenure Analysis                        | ![Screenshot](https://github.com/virajbhutada/Telecom-Customer-Churn-Prediction/assets/143819712/5942dbb4-47c7-467e-a075-14dc47ca7572)          |


---

## Power BI Visuals

Explore interactive Power BI visualizations designed to enhance data exploration and decision-making. Visualize customer churn trends, contract preferences, and revenue impact through intuitive and actionable dashboards.

| Overview and Key Metrics | Attrition Insights |
|---------------|-------------|
| ![Overview](https://github.com/virajbhutada/Telecom-Customer-Churn-Prediction/assets/143819712/18855f1b-fefe-4317-bede-fb8219d67e9f) | ![detailed_insights](https://github.com/virajbhutada/Telecom-Customer-Churn-Prediction/assets/143819712/7c068b03-4cdb-4659-b3e3-c15dc481cd59) |
| Gain a high-level view of customer churn trends, contract preferences, and revenue impact. This interactive dashboard provides insights into overall churn metrics and key business indicators. | Explore detailed analytics on customer segments, service usage patterns, and churn predictors. This visualization offers a deeper dive into specific data points and trends influencing churn decisions. |


---

## Key Findings

### Strategic Insights

- **Customer Segmentation:** Identify high-risk customer segments prone to churn.
- **Service Optimization:** Evaluate the impact of service features and contract terms on customer retention.
- **Financial Impact:** Quantify revenue loss due to churn and explore strategies for revenue recovery.


---

## References

- [Average Customer Acquisition Cost by Industry](https://hockeystack.com/blog/average-customer-acquisition-cost-by-industry/)
- [Subscriber Acquisition Cost Examples](https://www.klipfolio.com/resources/kpi-examples/call-center/subscriber-acquisition-cost)
- [Understanding Customer Churn Rate](https://www.zendesk.com/in/blog/customer-churn-rate/#georedirect)
- [Churn Prevention Strategies](https://www.profitwell.com/customer-churn/churn-prevention)

---

## Usage Instructions

### Getting Started

- **Clone the Repository**

  ```` 
   git clone https://github.com/HarshalKapse21/teleco_customer_churn_attrition_prediction.git
   cd teleco-customer-churn-attrition-prediction
   ````

- Install the project dependencies by running the following command

   ```
   pip install -r requirements.txt
   ```

- Navigate through the project's directories and files to get acquainted with its structure.


- **Dataset Handling:**

   - Load the dataset using Python, R, or your preferred data analysis tool.
   - Explore and preprocess data to prepare for churn prediction modeling.

- **Model Development:**

   - Train and evaluate machine learning models to predict customer churn.
   - Fine-tune models based on performance metrics to optimize predictions.

---
## Running the Project

To run the Telecom Customer Churn Prediction project locally, use Streamlit.

### Start the Application

Open the terminal or Git Bash inside the project folder and run the following command:


```bash
streamlit run app.py
```

### Deployment Steps

**Select a Hosting Service:**  
For this project, I used **Streamlit Community Cloud** because it is simple, free, and suitable for deploying machine learning web applications.

**Create a Streamlit Cloud Account:**  
I signed in to Streamlit Cloud using my GitHub account.

**Upload Project to GitHub:**  
The complete project files were uploaded to a GitHub repository, including:
- `app.py`
- `requirements.txt`
- `models/random_forest_model.pkl`
- `models/standard_scaler.pkl`
- `models/label_encoder.pkl`

**Prepare for Deployment:**  
The `requirements.txt` file was added to include all required Python libraries such as Streamlit, pandas, numpy, and scikit-learn.

**Deploy the Project:**  
On Streamlit Cloud, I selected my GitHub repository, chose the `main` branch, and set the main file path as `app.py`.

**Access the Deployed Application:**  
After deployment, Streamlit Cloud generated a public application URL that can be used to access and interact with the Telecom Customer Churn Prediction web app.

**Deployed Application:**  
st.link_button(
    "Teleco_customer_churn_attrition_app",
    "https://harshalkapse21-telecom-customer-churn-attrition-pred-app-pcphb6.streamlit.app/#prediction-result"
)


### Dataset Usage

1. Load the dataset using Python with Pandas.
2. Explore and analyze the dataset attributes and patterns.
3. Use the dataset for Telco Customer Churn Classification analysis.

---

### Connect With Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Harshal%20Kapse-blue?logo=linkedin)](https://www.linkedin.com/in/harshal-kapse-0b4331260/)  
[![GitHub](https://img.shields.io/badge/GitHub-Harshal%20Kapse-2b3137?logo=github)](https://github.com/HarshalKapse21/telco_customer_churn_prediction)
