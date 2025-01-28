import streamlit as st
import joblib
import random
import nltk

# Download necessary NLTK data
#nltk.download('punkt')

# Load saved model and vectorizer
vectoriser = joblib.load('vectoriser.pkl')
clf = joblib.load('Model.pkl')

intents = [
    {
        "tag": "greeting",
        "patterns": ["Hi", "Hello", "Hey", "How are you", "What's up"],
        "responses": ["Hi there", "Hello", "Hey", "I'm fine, thank you", "Nothing much"]
    },
    {
        "tag": "goodbye",
        "patterns": ["Bye", "See you later", "Goodbye", "Take care"],
        "responses": ["Goodbye", "See you later", "Take care"]
    },
    {
        "tag": "thanks",
        "patterns": ["Thank you", "Thanks", "Thanks a lot", "I appreciate it"],
        "responses": ["You're welcome", "No problem", "Glad I could help"]
    },
    {
        "tag": "about",
        "patterns": ["What can you do", "Who are you", "What are you", "What is your purpose"],
        "responses": ["I am a chatbot", "My purpose is to assist you", "I can answer questions and provide assistance"]
    },
    {
        "tag": "help",
        "patterns": ["Help", "I need help", "Can you help me", "What should I do"],
        "responses": ["Sure, what do you need help with?", "I'm here to help. What's the problem?", "How can I assist you?"]
    },
    {
        "tag": "age",
        "patterns": ["How old are you", "What's your age"],
        "responses": ["I don't have an age. I'm a chatbot.", "I was just born in the digital world.", "Age is just a number for me."]
    },
    {
        "tag": "weather",
        "patterns": ["What's the weather like", "How's the weather today"],
        "responses": ["I'm sorry, I cannot provide real-time weather information.", "You can check the weather on a weather app or website."]
    },
    {
        "tag": "budget",
        "patterns": ["How can I make a budget", "What's a good budgeting strategy", "How do I create a budget"],
        "responses": ["To make a budget, start by tracking your income and expenses. Then, allocate your income towards essential expenses like rent, food, and bills. Next, allocate some of your income towards savings and debt repayment. Finally, allocate the remainder of your income towards discretionary expenses like entertainment and hobbies.", "A good budgeting strategy is to use the 50/30/20 rule. This means allocating 50% of your income towards essential expenses, 30% towards discretionary expenses, and 20% towards savings and debt repayment.", "To create a budget, start by setting financial goals for yourself. Then, track your income and expenses for a few months to get a sense of where your money is going. Next, create a budget by allocating your income towards essential expenses, savings and debt repayment, and discretionary expenses."]
    },
    {
        "tag": "credit_score",
        "patterns": ["What is a credit score", "How do I check my credit score", "How can I improve my credit score"],
        "responses": ["A credit score is a number that represents your creditworthiness. It is based on your credit history and is used by lenders to determine whether or not to lend you money. The higher your credit score, the more likely you are to be approved for credit.", "You can check your credit score for free on several websites such as Credit Karma and Credit Sesame."]
    },
    {
        "tag": "jokes",
        "patterns": ["Tell me a joke", "Make me laugh", "Do you know any jokes?", "Say something funny"],
        "responses": ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!", "I'm reading a book on anti-gravity. It's impossible to put down!"]
    },
    {
        "tag": "time",
        "patterns": ["What time is it?", "Current time", "Time please", "Can you tell me the time?"],
        "responses": ["I suggest checking your device's clock", "I don't have access to real-time data, but you can check your phone or computer clock"]
    },
    {
        "tag": "news",
        "patterns": ["What's the news?", "Any recent updates?", "Top headlines", "News today"],
        "responses": ["I recommend checking reputable news websites or apps for the latest updates", "You can find current news on platforms like BBC, CNN, or Google News"]
    },
    {
        "tag": "food",
        "patterns": ["Recommend a recipe", "What should I cook?", "Food ideas", "Easy meal suggestions"],
        "responses": ["How about trying a stir-fry with your favorite vegetables?", "Pasta dishes are always quick and delicious!", "Sheet pan meals are great for easy cleanup"]
    },
    {
        "tag": "shopping",
        "patterns": ["Where to buy...", "Online shopping", "Best deals", "Where can I purchase..."],
        "responses": ["Popular online retailers include Amazon, eBay, and Walmart", "You might want to check price comparison websites for the best deals"]
    },
    {
        "tag": "bookings",
        "patterns": ["Book a flight", "Reserve hotel", "Make a reservation", "Book tickets"],
        "responses": ["I recommend checking travel websites like Booking.com or Expedia", "Most airlines and hotels have direct booking options on their websites"]
    },
    {
        "tag": "tech_support",
        "patterns": ["My computer is slow", "Phone not working", "Tech issues", "Fix my device"],
        "responses": ["Have you tried restarting your device?", "Check for software updates", "Clearing cache often helps improve performance"]
    },
    {
        "tag": "directions",
        "patterns": ["How to get to...", "Directions to...", "Map of...", "Find location..."],
        "responses": ["I recommend using Google Maps or Apple Maps for accurate directions", "Most navigation apps can provide real-time traffic updates"]
    },
    {
        "tag": "compliments",
        "patterns": ["You're smart", "Good chatbot", "Awesome help", "You're helpful"],
        "responses": ["Thank you! I appreciate that!", "You're making me blush!", "Glden I could help!"]
    },
    {
        "tag": "feedback",
        "patterns": ["Give feedback", "Rate service", "How am I doing?", "Submit comments"],
        "responses": ["Please share your feedback with my developers!", "Your input helps me improve. Thank you!", "Feel free to suggest improvements!"]
    },
    {
        "tag": "privacy",
        "patterns": ["Privacy policy", "Data security", "How private is this?", "Where's my data stored?"],
        "responses": ["All conversations are encrypted and secure", "Your privacy is important - we don't store personal data", "Security measures are in place to protect your information"]
    }
]

def chatbot(input_text):
    input_text = vectoriser.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

def main():
    st.set_page_config(page_title="Chatbot", page_icon="🤖")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    st.title("Personal Assistant Chatbot")
    
    # Accept user input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get bot response
        response = chatbot(prompt)
        
        # Check for goodbye
        if any(word in response.lower() for word in ['goodbye', 'bye']):
            response += "\n\nThank you for your time \nYour chat session ended. Please refresh the page to start a new conversation."
        
        # Display bot response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        
        # Add bot response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Stop further processing if goodbye was detected
        if any(word in response.lower() for word in ['goodbye', 'bye']):
            st.stop()

if __name__ == "__main__":
    main()