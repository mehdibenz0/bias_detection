import pandas as pd

data = pd.DataFrame({
    'gender': ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female'],
    'math_score': [78, 65, 85, 60, 80, 58, 90, 59, 75, 62],
    'passed': ['yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no']
})

# Save to CSV for reuse
data.to_csv("data/students.csv", index=False)
print("✅ Dataset created and saved to data/students.csv")