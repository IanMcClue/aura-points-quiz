import streamlit as st
from streamlit.state.session_state import SessionState

# Define the quiz function
def quiz():
    st.title("Welcome to the Multiple Choice Quiz!")
    
    # Define the questions and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "answer": "Paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Mars", "Jupiter", "Venus", "Mercury"],
            "answer": "Mars"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
            "answer": "Blue Whale"
        }
    ]
    
    # Initialize session state to store score
    if 'score' not in st.session_state:
        st.session_state.score = 0
    
    # Display questions and collect answers
    for i, q in enumerate(questions):
        st.write(f"**Question {i+1}:** {q['question']}")
        selected_option = st.radio("Options", options=q['options'], key=i)
        
        # Store answers in session state
        st.session_state[f'answer_{i}'] = selected_option
    
    # Display submit button
    if st.button("Submit"):
        # Check answers and calculate score
        for i, q in enumerate(questions):
            if st.session_state[f'answer_{i}'] == q['answer']:
                st.session_state.score += 1
        
        # Display final score
        st.write(f"Your final score is: {st.session_state.score}/{len(questions)}")

# Call the quiz function
quiz()
