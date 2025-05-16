# Phishing Detection System 🔐

Identify phishing URLs in real-time using Machine Learning and Streamlit. This project demonstrates the complete lifecycle of building a phishing detection system, including data collection, feature extraction, model training, and interactive frontend development.

---

 Features

* Real-time URL analysis
* Machine learning-based prediction
* Streamlit-powered interactive frontend
* Confidence scoring for predictions
* Simple, clean UI with professional touches


 Installation

1. Clone the repository:

```bash
git clone https://github.com/nishat09/Phishing-Detection-System.git
cd Phishing-Detection-System
```

2. Install the required packages:

```bash
uv install -r requirements.txt
```

3. Run the app:

```bash
uv run streamlit run app.py
```

---

Usage

* **Enter a URL** to check if it's phishing or legitimate.
* **Inspect the extracted features** to understand how the model makes decisions.
* **Real-time predictions** with confidence scores.

---

 Technologies Used

* **Python** - Backend logic and model training
* **Streamlit** - Frontend UI
* **scikit-learn** - Machine learning model
* **pandas** - Data manipulation
* **joblib** - Model serialization

---

 How It Works

1. **Feature Extraction** - Extracts features like URL length, number of dots, and IP addresses.
2. **Model Training** - Trains a Random Forest model to classify URLs.
3. **Real-Time Prediction** - Uses the trained model to predict phishing URLs in real-time.

---

Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Show Your Support

If you found this project helpful, please give it a ⭐ to show your support!

---

Acknowledgements

Thanks to the open-source community for the amazing tools and datasets used in this project.
