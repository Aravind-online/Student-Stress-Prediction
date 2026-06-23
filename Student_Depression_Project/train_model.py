import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("Loading Dataset...")

# Load dataset
df = pd.read_csv("dataset/Depression Dataset.csv")

print("Dataset Loaded Successfully!")
print("Dataset Shape:", df.shape)

# Remove missing values
df = df.dropna()

print("Missing Values Removed")

# Convert ALL columns to numeric using LabelEncoder
for col in df.columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))

print("All Columns Encoded Successfully")

# Check data types
print("\nData Types:")
print(df.dtypes)

# Features and Target
X = df.drop("DEPRESSED", axis=1)
y = df["DEPRESSED"]

print("\nFeatures Shape:", X.shape)
print("Target Shape:", y.shape)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Train-Test Split Completed")

# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

print("Training Model...")

# Train model
model.fit(X_train, y_train)

print("Training Completed!")

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\n==========================")
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("==========================")

# Save model
joblib.dump(model, "model.pkl")

print("\nModel Saved Successfully as model.pkl")