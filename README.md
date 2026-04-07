# 🚀 LangChain Chains Playground

This repository documents my hands-on learning and implementation of different types of **chains in LangChain**.

The goal of this project is to understand how to build **LLM pipelines** using:
- Prompt engineering  
- Output parsing  
- Sequential, Parallel, and Conditional workflows  

---

## 📌 What I Learned

Through this project, I explored:

- How to interact with LLMs using structured prompts  
- How to control outputs using parsers  
- How to design multi-step AI workflows using chains  

---

# 🔗 Types of Chains Implemented

---

## 1️⃣ Simple Chain

### 💡 Description
A basic chain where a prompt is sent to the model and output is returned.

### 🧪 Example
- Prompted the model to generate:
  > “5 value-for-money cars based on engine performance”

### 🎯 Learning
- Basic prompt → model → output flow  
- Understanding LLM responses  

---

## 2️⃣ Sequential Chain

### 💡 Description
Output of one chain becomes input to another.

### 🧪 Example
1. First chain:
   - Generate **best cars under ₹20,00,000**
2. Second chain:
   - Filter **best value-for-money cars based on engine performance**

### 🔄 Flow
```
Input → Chain 1 → Chain 2 → Output
```
### 🎯 Learning
- Dependency between steps  
- Building multi-stage pipelines  

---

## 3️⃣ Parallel Chain

### 💡 Description
Multiple chains run **simultaneously** on the same input.

### 🧪 Example
Input: **Information about Iron Man (MCU)**

- Chain 1 → Generate **summary**  
- Chain 2 → Generate **QnA (questions & answers)**  

### 🔄 Flow
```
      Input
        ↓
┌───────────────┐
│               │
Summary        QnA
│               │
└──── Combine ──┘
```
### 🎯 Learning
- Running independent tasks in parallel  
- Improving efficiency and multi-output generation  

---

## 4️⃣ Conditional Chain

### 💡 Description
Routing logic based on conditions (like if-else).

### 🧪 Example
**Review Sentiment Analysis System**

1. Classify review as:
   - Positive  
   - Negative  

2. Based on sentiment:
   - Positive → Generate appreciation response  
   - Negative → Generate apology/feedback response  

### 🔄 Flow
```
 User Review
      ↓
Sentiment Classifier
       ↓
┌───────────────┐
│               │
Positive     Negative
│               │
Reply A       Reply B
```
### 🎯 Learning
- Dynamic routing of tasks  
- Building intelligent AI systems  

---

# 🛠️ Tech Stack

- Python 🐍  
- LangChain  
- OpenAI / OpenRouter APIs  
- HuggingFace Models  
- Pydantic (for structured outputs)  

---

# 🧠 Key Concepts Covered

- Prompt Engineering  
- Output Parsing (Structured JSON)  
- Runnable APIs  
- Multi-model workflows  
- LLM pipeline design  

---

# 🚀 Future Improvements

- Add **RAG (Retrieval-Augmented Generation)**  
- Integrate **vector databases (FAISS/Chroma)**  
- Build **Streamlit UI**  
- Add **LangGraph workflows**  

---

# 💡 Key Takeaway

> This project helped me understand how to move from simple LLM calls to building structured, multi-step AI systems using LangChain.

---

# 🙌 Author

**Pranav Landge**  
Aspiring AI Engineer 🚀  
