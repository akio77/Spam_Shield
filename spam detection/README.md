# Spam Detection Prototype

This is a simple machine learning-based spam detection system that identifies whether a given text message is spam or not.

### 🔧 Files Included
- `predictions.py` – Script to load the trained model and predict if a message is spam.
- `spam_model_final.pkl` – Pre-trained spam detection model.
- `Spam_Classifier_Prototype.ipynb` – Jupyter Notebook used for model training and evaluation.
- `requirements.txt` – List of required Python packages.

### 🚀 How to Run

1. Install the required packages:
       pip install -r requirements.txt

2. Predict using the model:
Open `predictions.py` and run the script. It will load the model and show whether a sample message is spam or not.  
You can modify the `sample_message` variable to test other messages.

3. Explore the Notebook:
Open `spam.ipynb` in Jupyter or VS Code to see:
- Data preprocessing  
- Model training  
- Evaluation metrics  

### 📌 Notes
- This project uses classical ML algorithms like Logistic Regression, Naive Bayes, and Random Forest.
- SMOTE is used to handle imbalanced data.
- The model file must be in the same folder as `predictions.py`.


