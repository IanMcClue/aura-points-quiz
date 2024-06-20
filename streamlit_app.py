import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

st.set_page_config(page_title="Official BrainRot Quiz",
                   page_icon=":sparkle:",
                   layout="wide")

st.markdown("# :rainbow[Official BrainRot Quiz]🧠💣")

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge, Rectangle, Circle

st.set_page_config(page_title="Official BrainRot Quiz",
                   page_icon=":sparkle:",
                   layout="wide")

st.markdown("# :rainbow[Official BrainRot Quiz]🧠💣")

# Define the function to create the degree range for the gauge
def degree_range(n): 
    start = np.linspace(0,180,n+1, endpoint=True)[0:-1]
    end = np.linspace(0,180,n+1, endpoint=True)[1::]
    mid_points = start + ((end-start)/2.)
    return np.c_[start, end], mid_points

# Define the function to rotate text for the gauge
def rot_text(ang): 
    rotation = np.degrees(np.radians(ang) * np.pi / np.pi - np.radians(90))
    return rotation

# Define the gauge chart function
def gauge(labels, colors, arrow, title, fname=False):     
    N = len(labels)
    if arrow > N: 
        raise Exception("\n\nThe category ({}) is greater than the length of the labels ({})".format(arrow, N)) 

    fig, ax = plt.subplots(figsize=(7, 5))
    fig.subplots_adjust(0, 0, 2, 1)

    ang_range, mid_points = degree_range(N)
    labels = labels[::-1]
    
    patches = []
    for ang, c in zip(ang_range, colors): 
        patches.append(Wedge((0.,0.), .4, *ang, facecolor='w', lw=2))
        patches.append(Wedge((0.,0.), .4, *ang, width=0.2, facecolor=c, lw=2, alpha=0.5))
    
    [ax.add_patch(p) for p in patches]

    for mid, lab in zip(mid_points, labels): 
        ax.text(0.42 * np.cos(np.radians(mid)), 0.42 * np.sin(np.radians(mid)), lab,
                horizontalalignment='center', verticalalignment='center', fontsize=12,
                fontweight='bold', rotation=rot_text(mid))

    r = Rectangle((-0.4,-0.1),0.8,0.1, facecolor='w', lw=2)
    ax.add_patch(r)
    
    ax.text(0, -0.1, title, horizontalalignment='center', 
            verticalalignment='center', fontsize=18)

    pos = mid_points[abs(arrow - N)]
    
    ax.arrow(0, 0, 0.225 * np.cos(np.radians(pos)), 0.225 * np.sin(np.radians(pos)),
             width=0.04, head_width=0.09, head_length=0.1, fc='k', ec='k')
    
    ax.add_patch(Circle((0, 0), radius=0.02, facecolor='k'))
    ax.add_patch(Circle((0, 0), radius=0.01, facecolor='w', zorder=11))

    ax.set_frame_on(False)
    ax.axes.set_xticks([])
    ax.axes.set_yticks([])
    ax.axis('equal')
    
    if fname:
        fig.savefig(fname, dpi=200)
    return fig

# Define the quiz function
def quiz():
    st.title("Find out if you will graduate with brainrot🎓")
    st.image("gallery/brain_rot_quiz.png")

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
            "answer": "obsessive mom",
            "options": ["obsessive mom", "a mom who loves almonds", "a mom from Almond, USA"]
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
        "What is the TikTok national anthem?": {
            "answer": "Carnival",
            "options": ["Carnival", "TikTok Song", "National Anthem of TikTokia"]
        }
    }

    scenarios = list(fill_in_the_blank_questions.items()) + list(questions_and_answers.items())

    if 'start_quiz' not in st.session_state:
        st.session_state.start_quiz = False

    if not st.session_state.start_quiz:
        if st.button("Start Quiz"):
            st.session_state.start_quiz = True
            st.session_state.score = 0
            st.session_state.current_scenario_index = 0
            st.experimental_rerun()
    else:
        progress = st.session_state.current_scenario_index / len(scenarios)
        st.progress(progress)

        if st.session_state.current_scenario_index < len(scenarios):
            current_scenario = scenarios[st.session_state.current_scenario_index]
            st.markdown(f'<p style="color: white; font-weight: bold;">Scenario {st.session_state.current_scenario_index + 1}:</p>', unsafe_allow_html=True)
            st.markdown(f'<p style="color: white; font-weight: bold;">{current_scenario[0]}</p>', unsafe_allow_html=True)

            with st.form(key=f'scenario_{st.session_state.current_scenario_index}'):
                selected_option = st.radio("Options", options=current_scenario[1]["options"])

                submit_button = st.form_submit_button("Next")

                if submit_button:
                    st.session_state[f'answer_{st.session_state.current_scenario_index}'] = selected_option
                    st.session_state.current_scenario_index += 1
                    st.experimental_rerun()
        else:
            for i, s in enumerate(scenarios):
                if st.session_state[f'answer_{i}'] == s[1]["answer"]:
                    st.session_state.score += 1
            
            max_score = len(scenarios)
            score_labels = ['Terrible', 'Bad', 'Okay', 'Good', 'Great']
            score_colors = ['red', 'orangered', 'orange', 'skyblue', 'blue']
            arrow_pos = int((st.session_state.score / max_score) * (len(score_labels) - 1))
            fig = gauge(score_labels, score_colors, arrow_pos, "Your BrainRot Score")
            st.pyplot(fig)

            with st.form(key='result_form'):
                if st.session_state.score <= 3:
                    st.markdown("<b>You're <span style='color: red;'>cooked😳</span> you're <span style='color: red;'>aura debt</span> cooked you suffer from brainrot</b>", unsafe_allow_html=True)
                else:
                    st.markdown("<b>😮‍💨Your <span style='color: green;'>aura is bountiful</span> you're boring and need to live a little aura</b>", unsafe_allow_html=True)

                if st.form_submit_button("Repeat Quiz"):
                    st.session_state.start_quiz = False
                    st.experimental_rerun()

            share_link = "https://aura-points-quiz.streamlit.app/"
            st.markdown(f"Share the quiz: [Share]({share_link})")

            st.markdown(
                """
                ---
                Follow us on:

                TikTok → [@cr8ing](https://tiktok.com/@fiatluxlabs)
                
                🔮📈Gain aura each time you send us scenarios on TikTok (real)
                
                🧙🏼‍♂️You've been granted +100 points for completing this quiz. Share on TikTok for an extra +100,000 points
                """
            )

    st.divider()
    footer = """<div style="text-align: center;">
                    <p>A <a href="http://fiat-lux-labs-tmp.vercel.app/" target="_blank">Fiat Lux Labs</a> Project</p>
                    <a href="https://visitorbadge.io/status?path=https%3A%2F%2Fbrainrottest.streamlit.app%2F">
                        <img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fbrainrottest.streamlit.app%2F&label=brainrot-visitors&labelColor=%23ffffff&countColor=%23000000&style=plastic" />
                    </a>
                </div>"""
    st.markdown(footer, unsafe_allow_html=True)

quiz()

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
            "answer": "obsessive mom",
            "options": ["obsessive mom", "a mom who loves almonds", "a mom from Almond, USA"]
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
        "What is the TikTok national anthem?": {
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
            
            max_score = len(scenarios)
            fig = create_gauge_chart(st.session_state.score, max_score)
            st.pyplot(fig)

            # Display result message
            with st.form(key='result_form'):
                if st.session_state.score <= 3:
                    st.markdown("<b>You're <span style='color: red;'>cooked😳</span> you're <span style='color: red;'>aura debt</span> cooked you suffer from brainrot</b>", unsafe_allow_html=True)
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

                TikTok → [@cr8ing](https://tiktok.com/@fiatluxlabs)
                
                🔮📈Gain aura each time you send us scenarios on TikTok (real)
                
                🧙🏼‍♂️You've been granted +100 points for completing this quiz. Share on TikTok for an extra +100,000 points
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
