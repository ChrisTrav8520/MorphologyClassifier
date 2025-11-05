## Machine Learning Framework for predicting morphologies of PS/PMMA blends
This repository contains information pertaining to our study published in Soft Matter (RSC, 2025):
https://pubs.rsc.org/en/content/articlelanding/2025/sm/d5sm00335k.

## Overview
As part of the study, we developed a support vector machine (SVM)-based non-linear classification model that predicts the morphology of polystyrene (PS) / polymethyl methacrylate (PMMA) blends from key experimental input parameters.

The objective of this work is to assist experimental polymer scientists in identifying processing conditions that lead to desired blend morphologies, even when data availability is limited.

## Highlights
 - Dataset Curation: Manually classified morphologies from AFM images by utilizing Gwyddion
 - Data-efficient Modelling: Trained and validated multiple algorithms on a limited dataset, demonstrating robust performance inspite of data scarcity
 - Explainable ML: Applied SHAP (SHapley Additive exPlanations) to interpret the model results and verify alignment with established polymer physics trends
 - Web-based Prediction Tool: Developed a web application for real-time morphology prediction, to promote democratization of AI (please visit [https://morphology-prediction-tool.onrender.com/](https://morphology-prediction-tool.onrender.com/))

## Tools and Libraries
 - Python libraries (pandas, numpy, matplotlib.pyplot) for data preprocessing and imputation
 - scikit-learn, joblib for classification algorithms
 - SHAP for X-AI
 - Streamlit for webapp front-end development
   
Model development code is proprietary and available upon request at the discretion of the authors.
For questions or collaborations, feel free to reach out via email (bishnuramachandran@gmail.com) or open an issue.
Thank you!
