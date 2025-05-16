import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the extracted features
features_file = "datas/features.csv"
df = pd.read_csv(features_file)

# Separate features and labels
X = df.drop("label", axis=1)
y = df["label"]

# Ensure labels are correctly encoded
y = y.apply(lambda x: 0 if x == 1 else 1)  # Flipping the labels

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"✅ Model Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n", report)

# Save the trained model
model_file = "datas/phishing_model_fixed.pkl"
joblib.dump(model, model_file)

print("\n✅ Model saved to", model_file)
