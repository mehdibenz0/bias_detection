# 🤖 Bias in AI – TechSpark Hands-On Project

Welcome to your first AI fairness project! In this activity, you'll train a small AI model and learn how to spot and fix **bias** in the data it learns from.

---

## 📚 What You'll Learn

- What AI bias means
- How unfair data leads to unfair predictions
- How to train a model using Python
- How to measure bias in AI
- How to fix or reduce bias by changing the data

---

## 📂 Project Structure

```
bias-in-ai/
├── create_dataset.py       ← creates a small, biased dataset
├── bias_detection.ipynb    ← the main project notebook
├── data/
│   └── students.csv         ← the dataset used by the model
└── README.md               ← you're reading this!
```

---

## 🧪 How It Works

1. We create a tiny dataset of students with:
   - **gender** (male/female)
   - **math_score** (0 to 100)
   - **passed** (yes/no)

2. We train a simple model to guess: **Did the student pass?**

3. Then we ask:  
   ❓ Does the model treat boys and girls the same?

4. If it doesn’t…  
   ➕ We try to **balance the data** or  
   ❌ Remove the **gender feature** from the model

---

## 🚀 How to Run the Project

### Option 1: In Jupyter Notebook

1. Clone this repo or download it as a ZIP  
2. Open `bias_detection.ipynb` in Jupyter  
3. Run all cells step by step

### Option 2: In Google Colab

Click this link to open in Colab:  
[📎 Open in Colab](https://colab.research.google.com/github/YOUR-USERNAME/bias-in-ai/blob/main/bias_detection.ipynb)

> Don’t forget to run `create_dataset.py` first or run the cell that generates the dataset.

---

## 🎯 Try This!

After running the project:

- Can you change the dataset to add more girls who passed?
- What happens if you **remove the gender column**?
- Can you make the AI treat both genders more fairly?

---

## 🧠 What Is Bias?

AI bias happens when a robot learns from **unfair examples**.  
If the data is unbalanced, the robot will make **unfair decisions**.

🧊 Think of it like making ice cream based only on chocolate lovers.  
The AI will always pick chocolate — but that’s not fair to strawberry fans!

---

## 🏁 Goal

Make the AI **as fair as possible** to both boys and girls.  
You're now an **AI fairness detective** — good luck! 🔍✨

---

## 👩‍💻 Credits

Made with ❤️ by TechSpark Academy  
For curious young coders learning the future of AI
