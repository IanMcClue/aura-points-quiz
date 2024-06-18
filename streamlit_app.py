import streamlit as st

st.set_page_config(page_title="Official Aurapoints Quiz",
                   page_icon=":sparkle:",
                   layout="wide")

st.markdown("# :rainbow[Official Aurapoints Quiz]🧠💣")

# Define the quiz function
def quiz():
    st.title("Find out if you will graduate with brainrot🎓")
    # Add the image
    st.image("gallery/brain_rot_quiz.png")

    # Define the scenarios and answers
    fill_in_the_blank_questions = {
        "Fill in the blank: 'Skibbidi dop, dop, dop ______'": {
            "answer": "'yes, yes'",
            "options": ["'yes, yes'", "'no, no'", "'maybe, maybe'"]
        },
        "Fill in the blank: 'And she was a ______'": {
            "answer": "fairy",
            "options": ["fairy", "witch", "mermaid"]
        },
        "Fill in the blank: 'my girl got diamonds in her ______'": {
            "answer": "diamonds on her arm, diamonds on her ear",
            "options": ["diamonds on her arm, diamonds on her ear", "pockets", "hair"]
        }
    }

    questions_and_answers = {
        "What is a big back?": {
            "answer": "someone who enjoys eating snacks",
            "options": ["someone who enjoys eating snacks", "a large backpack", "a big backbone"]
        },
        "What is an almond mom?": {
            "answer": "obessive mom",
            "options": ["obessive mom", "a mom who loves almonds", "a mom from Almond, USA"]
        },
        "What is an ick?": {
            "answer": "when a man breathes",
            "options": ["when a man breathes", "a type of insect", "a disgusting thing"]
        },
        "What is girl hobbying?": {
            "answer": "Going on wholistic activities",
            "options": ["Going on wholistic activities", "Hobbying only for girls", "Collecting girls as a hobby"]
        },
        "What is called when someone steals 20% of your food?": {
            "answer": "Fanum Tax",
            "options": ["Fanum Tax", "Partial theft", "Food tax"]
        },
        "What is the tiktok national anthem?": {
            "answer": "Carnival",
            "options": ["Carnival", "TikTok Song", "National Anthem of TikTokia"]
        }
    }

    scenarios = list(fill_in_the_blank_questions.items()) + list(questions_and_answers.items())

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
            st.markdown(f'<p style="color: white; font-weight: bold;">Scenario {st.session_state.current_scenario_index + 1}:</p>', unsafe_allow_html=True)
            st.markdown(f'<p style="color: white; font-weight: bold;">{current_scenario[0]}</p>', unsafe_allow_html=True)

            # Create a form for the scenario
            with st.form(key=f'scenario_{st.session_state.current_scenario_index}'):
                selected_option = st.radio("Options", options=current_scenario[1]["options"])

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
                if st.session_state[f'answer_{i}'] == s[1]["answer"]:
                    st.session_state.score += 1
            st.markdown(f"<h1 style='text-align: center;'><b>Your final score is: {st.session_state.score}/{len(scenarios)}</b></h1>", unsafe_allow_html=True)

            # Display result message
            with st.form(key='result_form'):
                if st.session_state.score <= 3:
                    st.markdown("<b>You're <span style='color: red;'>cooked😳</span> you're <span style='color: red;'>aura debt</span> cooked  you suffer from brainrot </b>", unsafe_allow_html=True)
                else:
                    st.markdown("<b>😮‍💨Your <span style='color: green;'>aura is bountiful</span> you're boring and need to live a little aura</b>", unsafe_allow_html=True)

                # Button to repeat the quiz
                if st.form_submit_button("Repeat Quiz"):
                    st.session_state.start_quiz = False
                    st.experimental_rerun()

            # Add option to share the quiz
            share_link = "https://aura-points-quiz.streamlit.app/"  # Replace with your Streamlit sharing link
            st.markdown(f"Share the quiz: [Share]({share_link})")

            # Add social media links and points earned message
            st.markdown(
                """
                ---
                Follow us on:

                Tiktok → [@cr8ing](https://tiktok.com/@fiatluxlabs)
                
                🔮📈Gain aura each time you send us scenarios on Tiktok (real)
                
                🧙🏼‍♂️You've been granted +100 points for completing this quiz share on Tiktok for an extra +100,000 points
                """
            )

    # Footer
    st.divider()
    footer = """<div style="text-align: center;">
                    <p>A <a href="http://fiat-lux-labs-tmp.vercel.app/" target="_blank">Fiat Lux Labs</a> Project</p>
                    <a href="https://visitorbadge.io/status?path=https%3A%2F%2Fbrainrottest.streamlit.app%2F">
                        <img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fbrainrottest.streamlit.app%2F&label=brainrot-visitors&labelColor=%23ffffff&countColor=%23000000&style=plastic" />
                    </a>
                </div>"""
    st.markdown(footer, unsafe_allow_html=True)

# Call the quiz function
quiz()
