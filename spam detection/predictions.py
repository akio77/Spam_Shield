from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from joblib import load
import warnings
import nltk


nltk.download('stopwords')
warnings.filterwarnings("ignore", category=RuntimeWarning)


MODEL_PATH = 'spam_model_final.pkl'

def load_model():
    try:
        with open(MODEL_PATH, 'rb') as file:
            model = load(file)
        return model
    except FileNotFoundError:
        print(f"❌ Error: Model file '{MODEL_PATH}' not found.")
        return None

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    porter = PorterStemmer()
    words = text.lower().split()
    words = [porter.stem(word) for word in words if word not in stop_words]
    return [" ".join(words)]  

def predict_message(text):
    model = load_model()
    if model is None:
        return "❌ Model could not be loaded."
    
    try:
        processed = preprocess_text(text)
        prediction = model.predict(processed)[0]  
        if prediction == 1:
            return "Your message is: 🚫 SPAM"
        else:
            return "Your message is: ✅ NOT SPAM"
    except Exception as e:
        return f"❌ Prediction error: {e}"


user_input = input("📨 Enter your message to check if it's spam:\n")
result = predict_message(user_input)
print(result)