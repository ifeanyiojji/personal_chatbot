# 🤖 Personal Chatbot using Streamlit, NLTK & Scikit-Learn

This is a lightweight and intelligent **personal chatbot** built in Python. It uses machine learning and natural language processing (NLP) to understand user inputs and respond with relevant and predefined answers. The chatbot can recognize various intents such as greetings, help requests, jokes, budgeting advice, tech support, and more. The user interface is built with **Streamlit**, making it easy to interact with the model in real time.

---

## 📌 Key Features

- 🎯 **Intent Classification** using TF-IDF and Logistic Regression
- 🧠 **Natural Language Processing** with NLTK
- 💬 **Predefined Responses** for common user queries
- 🌐 **Streamlit Web Interface** for chatting live with the bot
- 💾 **Model Persistence** using Joblib (saves classifier and vectorizer)
- ✅ Easily extensible to include more intents and responses

---

## 🛠️ Built With

| Tool/Library         | Purpose                                |
|----------------------|----------------------------------------|
| Python 3             | Programming language                   |
| NLTK                 | Tokenization and NLP tasks             |
| Scikit-learn         | ML: TF-IDF vectorization + classifier  |
| Streamlit            | Web-based user interface               |
| Joblib               | Model saving/loading                   |

---

## 📁 Project Structure
chatbot_project/
├── chatbot.py # Main script (model training + Streamlit UI)
├── intents.json # Hardcoded in chatbot.py (patterns & responses)
├── Model.pkl # Saved Logistic Regression model
├── vectoriser.pkl # Saved TF-IDF vectorizer
├── nltk_data/ # Optional: offline NLTK data
├── README.md # Project documentation



---

## 🧠 How It Works

1. The chatbot has a list of **intents** containing patterns and responses.
2. Patterns are vectorized using **TF-IDF**.
3. A **Logistic Regression** model is trained on these patterns to classify new input.
4. When a user sends a message:
   - It’s vectorized.
   - The model predicts the matching intent.
   - A random response is chosen from that intent's response list.

---

## 💬 Sample Intents

Examples of supported intents and how the chatbot responds:

- **Greetings** → _"Hello", "Hi", "What's up?"_  
  → “Hi there!”, “Hello!”

- **Jokes** → _"Tell me a joke", "Make me laugh"_  
  → “Why don’t scientists trust atoms? Because they make up everything!”

- **Budget Advice** → _"How do I create a budget?"_  
  → “Try the 50/30/20 rule...”

- **Tech Support** → _"My computer is slow"_  
  → “Try restarting your device or clearing the cache.”

---

## 🔧 Setup Instructions

### 1. Clone this Repository

```bash
git clone https://github.com/yourusername/chatbot_project.git
cd chatbot_project
```

### 2. Create and Activate Virtual Environment (Optional but recommended)

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

### 4. Download NLTK Data
The chatbot uses the punkt tokenizer. If automatic download fails, you can manually install it:
```python
import nltk
nltk.download('punkt')
```

### 5. Run the app
```bash
streamlit run


