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
    
    # Initialize session state to store score and current question index
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'current_question_index' not in st.session_state:
        st.session_state.current_question_index = 0
    
    # Calculate progress
    progress = st.session_state.current_question_index / len(questions)
    st.progress(progress)
    
    # Check if quiz is finished
    if st.session_state.current_question_index < len(questions):
        # Display current question
        current_question = questions[st.session_state.current_question_index]
        st.write(f"**Question {st.session_state.current_question_index + 1}:** {current_question['question']}")
        selected_option = st.radio("Options", options=current_question['options'])
        
        # Store answer in session state
        st.session_state[f'answer_{st.session_state.current_question_index}'] = selected_option
        
        # Display "Next" button
        if st.button("Next"):
            st.session_state.current_question_index += 1
    else:
        # Quiz finished, calculate score and display final score
        for i, q in enumerate(questions):
            if st.session_state[f'answer_{i}'] == q['answer']:
                st.session_state.score += 1
        st.markdown(f"<h1 style='text-align: center;'><b>Your final score is: {st.session_state.score}/{len(questions)}</b></h1>", unsafe_allow_html=True)
        
        # Add option to repeat the quiz
        if st.button("Repeat Quiz"):
            st.session_state.current_question_index = 0
            st.session_state.score = 0
            for i in range(len(questions)):
                if f'answer_{i}' in st.session_state:
                    del st.session_state[f'answer_{i}']
        
        # Add option to share the quiz
        share_link = "https://share.streamlit.io/your-username/your-app-name/main.py"  # Replace with your Streamlit sharing link
        st.markdown(f"Share the quiz: [Share]({share_link})")

# Call the quiz function
quiz()
