import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load the dataset
data = pd.read_csv("data/students.csv")
print("📊 Dataset loaded:")
print(data)

# Step 2: Encode categorical variables
data['gender_encoded'] = data['gender'].map({'male': 0, 'female': 1})
data['passed_encoded'] = data['passed'].map({'no': 0, 'yes': 1})

# Step 3: Split data for training/testing
X = data[['math_score', 'gender_encoded']]
y = data['passed_encoded']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Step 4: Train the model
model = LogisticRegression()
model.fit(X_train, y_train)
print("🤖 Model trained!")

# Step 5: Make predictions
y_pred = model.predict(X_test)

# Step 6: Check overall accuracy
overall_accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Overall Accuracy: {overall_accuracy:.2f}")

# Step 7: Evaluate by gender
test_data = X_test.copy()
test_data['true'] = y_test
test_data['pred'] = y_pred
test_data['gender'] = test_data['gender_encoded'].map({0: 'male', 1: 'female'})

print("\n🎯 Accuracy by gender:")
for gender in ['male', 'female']:
    group = test_data[test_data['gender'] == gender]
    acc = accuracy_score(group['true'], group['pred'])
    print(f"{gender.capitalize()}: {acc:.2f}")

# Step 8: Show a detailed classification report
print("\n📋 Classification Report:")
print(classification_report(y_test, y_pred))