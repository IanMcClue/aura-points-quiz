import streamlit as st

def quiz():
    st.title("Welcome to the Multiple Choice Quiz!")
    
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
    
    score = 0
    
    for i, q in enumerate(questions):
        st.write(f"**Question {i+1}:** {q['question']}")
        selected_option = st.radio("Options", options=q['options'])
        
        if selected_option == q['answer']:
            st.write("Correct!")
            score += 1
        else:
            st.write("Incorrect! The correct answer is:", q['answer'])
    
    st.write(f"Your final score is: {score}/{len(questions)}")

quiz()
