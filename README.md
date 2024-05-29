# FINANCIAL INCLUSION IN AFRICA

![](https://www.shutterstock.com/image-photo/wooden-blocks-words-financial-inclusion-260nw-2288020367.jpg)

Financial inclusion in Africa refers to the ongoing effort to provide access to affordable financial services to all segments of the population, particularly those historically excluded from the formal financial system. This includes services such as savings, credit, insurance, and payment transactions. Africa's diverse socioeconomic landscape presents unique challenges to achieving widespread financial inclusion, including limited infrastructure, low literacy rates, and informal economies. However, governments, financial institutions, and development organizations are increasingly recognizing the importance of inclusive financial systems for economic growth and poverty alleviation. Initiatives leveraging mobile technology, agent banking, and innovative fintech solutions have shown promise in expanding access to financial services, empowering individuals, and fostering economic resilience. By promoting transparency, accountability, and tailored solutions, the pursuit of financial inclusion in Africa aims to mitigate disparities, promote sustainable development, and unlock the continent's vast economic potential.


Research on financial inclusion in Africa is crucial due to its immense importance in driving inclusive economic growth and reducing poverty. Understanding the barriers to financial access and usage is essential for designing effective policies and interventions. Moreover, research can shed light on the impact of financial inclusion initiatives on various socioeconomic indicators, such as income inequality, employment, and entrepreneurship. By identifying best practices and lessons learned, research can inform the development of scalable and sustainable solutions tailored to the diverse needs of African communities. Furthermore, given the rapid technological advancements and evolving financial landscapes, continuous research is necessary to adapt strategies and address emerging challenges. Ultimately, research on financial inclusion in Africa serves as a catalyst for informed decision-making, resource allocation, and collaborative efforts among stakeholders, driving progress towards achieving inclusive and resilient economies across the continent.

# Financial Inclusion Data Analysis and Prediction

This repository contains a project for analyzing and predicting financial inclusion using machine learning techniques. The project utilizes a dataset that is sourced from Google Drive and implements various preprocessing steps, exploratory data analysis, and machine learning models to achieve the prediction goal.

## Table of Contents
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Data](#data)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Preprocessing](#preprocessing)
- [Modeling](#modeling)
- [Model Saving](#model-saving)
- [Authors](#authors)


## Getting Started

To get a copy of the project up and running on your local machine, follow these instructions.

### Prerequisites

Ensure you have the following software installed:
- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your_username/financial-inclusion.git
    cd financial-inclusion
    ```

2. Install the required Python packages:
    ```sh
    pip install pandas numpy matplotlib scikit-learn seaborn ydata_profiling
    ```

3. Download the dataset from the given URL and ensure it is accessible.

## Dependencies

This project requires the following Python libraries:
- pandas
- numpy
- matplotlib
- scikit-learn
- seaborn
- ydata_profiling

These can be installed via the requirements file if available:
```bash
pip install -r requirements.txt
```

## Data

The dataset used in this project is downloaded from Google Drive. It contains information related to financial inclusion in various countries. The URL for the dataset is embedded within the code, and the data is read directly into a pandas DataFrame.

## Exploratory Data Analysis

Exploratory Data Analysis (EDA) is performed using the `ydata_profiling` library which generates a comprehensive report of the dataset. This report is saved as `financialinclusiondata.html`.

## Preprocessing

Data preprocessing steps include:
1. Dropping irrelevant columns: `uniqueid`, `bank_account`, `country`, `year`.
2. Encoding categorical variables using `LabelEncoder`.

## Modeling

The project implements a voting classifier using two different classifiers:
- RandomForestClassifier
- Support Vector Classifier (SVC)

The model is trained on the preprocessed data and then used to make predictions.

### Training and Testing

Data is split into training and testing sets using `train_test_split` from `scikit-learn`:
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

### Voting Classifier

A voting classifier combining Random Forest and SVC is created and trained:
```python
from sklearn.ensemble import VotingClassifier

clf1 = RandomForestClassifier(n_estimators=100)
clf2 = SVC(probability=True)
eclf = VotingClassifier(estimators=[('rf', clf1), ('svc', clf2)], voting='hard')
eclf.fit(X_train, y_train)
y_pred = eclf.predict(X_test)
```

## Model Saving

The trained model is saved to a file using `pickle`:
```python
import pickle
with open('model.pkl', 'wb') as file:
    pickle.dump(eclf, file)
```

## Authors

- [Your Name](https://github.com/Olubunmi_kufoniyi)


---

This README file provides an overview of the project, the steps to get started, and the main components of the code. If you have any questions or need further assistance, please refer to the contact details provided.