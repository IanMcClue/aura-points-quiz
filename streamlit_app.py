import streamlit as st

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

    # Start Quiz button
    if 'start_quiz' not in st.session_state:
        st.session_state.start_quiz = False

    if not st.session_state.start_quiz:
        if st.button("Start Quiz"):
            st.session_state.start_quiz = True
            st.session_state.score = 0
            st.session_state.current_question_index = 0
            st.experimental_rerun()
    else:
        # Calculate progress
        progress = st.session_state.current_question_index / len(questions)
        st.progress(progress)

        # Check if quiz is finished
        if st.session_state.current_question_index < len(questions):
            # Display current question
            current_question = questions[st.session_state.current_question_index]
            st.write(f"**Question {st.session_state.current_question_index + 1}:** {current_question['question']}")
