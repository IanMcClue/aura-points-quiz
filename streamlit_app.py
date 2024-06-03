import streamlit as st

# Define the quiz function
def quiz():
    st.title("Find out if you have +♾️ Aura or -♾️ Aura")
# Add the image
    st.image("gallery/aura_quiz_wiz.png")
    # Define the scenarios and answers
    scenarios = [
        {
            "Scenario": "Have you confidently answered a question in front of the huzz but you were wrong",
            "options": ["Real😏", "I’m a NPC 🤓", "Not real😒"],
            "answer": "Real 😏"
        },
        {
            "Scenario": "Has your gum fallen out when you’re laughing",
            "options": ["Real😏", "I’m a NPC 🤓", "Not real😒"],
            "answer": "I’m a NPC 🤓"
        },
        {
            "Scenario": "Has the teacher looked at your test and reminded the class to check their answers",
            "options": ["Real😏", "I’m a NPC 🤓", "Not real😒"],
            "answer": "I’m a NPC 🤓"
        }
    ]

    # Start Quiz button
    if 'start_quiz' not in st.session_state:
        st.session_state.start_quiz = False

    if not st.session_state.start_quiz:
        if st.button("Start Quiz"):
            st.session_state.start_quiz = True
            st.session_state.score = 0
            st.session_state.current_scenario_index = 0
            st.experimental_rerun()
    else:
        # Calculate progress
        progress = st.session_state.current_scenario_index / len(scenarios)
        st.progress(progress)

        # Check if quiz is finished
        if st.session_state.current_scenario_index < len(scenarios):
            # Display current scenario
            current_scenario = scenarios[st.session_state.current_scenario_index]
            st.write(f"**Scenario {st.session_state.current_scenario_index + 1}:** {current_scenario['Scenario']}")

            # Create a form for the scenario
            with st.form(key=f'scenario_{st.session_state.current_scenario_index}'):
                selected_option = st.radio("Options", options=current_scenario['options'])

                # Submit button for the form
                submit_button = st.form_submit_button("Next")

                # Store answer in session state when the form is submitted
                if submit_button:
                    st.session_state[f'answer_{st.session_state.current_scenario_index}'] = selected_option
                    st.session_state.current_scenario_index += 1
                    st.experimental_rerun()
        else:
            # Quiz finished, calculate score and display final score
            for i, s in enumerate(scenarios):
                if st.session_state[f'answer_{i}'] == s['answer']:
                    st.session_state.score += 1
            st.markdown(f"<h1 style='text-align: center;'><b>Your final score is: {st.session_state.score}/{len(scenarios)}</b></h1>", unsafe_allow_html=True)

            # Add option to repeat the quiz
            if st.button("Repeat Quiz"):
                st.session_state.start_quiz = False
                st.experimental_rerun()

            # Add option to share the quiz
            share_link = "https://share.streamlit.io/your-username/your-app-name/main.py"  # Replace with your Streamlit sharing link
            st.markdown(f"Share the quiz: [Share]({share_link})")

# Call the quiz function
quiz()
