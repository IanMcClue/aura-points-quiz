import streamlit as st
from st_copy_to_clipboard import st_copy_to_clipboard
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge, Rectangle, Circle

# This must be the first Streamlit command in your script
st.set_page_config(page_title="Official BrainRot Quiz",
                   page_icon=":brain:",
                   layout="wide")

st.markdown("# :rainbow[Official BrainRot Quiz]🧠💣")

# Define the function to create the degree range for the gauge
def degree_range(n): 
    start = np.linspace(0, 180, n + 1, endpoint=True)[0:-1]
    end = np.linspace(0, 180, n + 1, endpoint=True)[1::]
    mid_points = start + ((end - start) / 2.)
    return np.c_[start, end], mid_points

# Define the function to rotate text for the gauge
def rot_text(ang): 
    rotation = np.degrees(np.radians(ang) * np.pi / np.pi - np.radians(90))
    return rotation

# Define the gauge chart function
def gauge(labels, colors, arrow, title, fname=False):     
    N = len(labels)
    if arrow >= N: 
        raise Exception("\n\nThe category ({}) is greater than the length of the labels ({})".format(arrow, N)) 

    fig, ax = plt.subplots(figsize=(7, 5))
    fig.subplots_adjust(0, 0, 2, 1)

    ang_range, mid_points = degree_range(N)
    labels = labels[::-1]
    
    patches = []
    for ang, c in zip(ang_range, colors): 
        patches.append(Wedge((0., 0.), .4, *ang, facecolor='w', lw=2))
        patches.append(Wedge((0., 0.), .4, *ang, width=0.2, facecolor=c, lw=2, alpha=0.5))
    
    for p in patches:
        ax.add_patch(p)

    for mid, lab in zip(mid_points, labels): 
        ax.text(0.42 * np.cos(np.radians(mid)), 0.42 * np.sin(np.radians(mid)), lab,
                horizontalalignment='center', verticalalignment='center', fontsize=12,
                fontweight='bold', rotation=rot_text(mid))

    r = Rectangle((-0.4, -0.1), 0.8, 0.1, facecolor='w', lw=2)
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
        "Fill in the blank: '💃Skibbidi dop, dop, dop ______'": {
            "answer": "'yes, yes'",
            "options": ["'yes, yes'", "'no, no'", "'maybe, maybe'"],
            "image": "begging.png"
        },
        "Fill in the blank: 'And she was a ______'": {
            "answer": "fairy",
            "options": ["witch🧙🏽‍♀️", "mermaid🧜🏽‍♀️","fairy🧚🏼‍♀️"]
        },
        "Finish the lyrics: '💎my girl got diamonds on her arm, diamonds on her ______'": {
            "answer": "ears",
            "options": ["ears👂", "hand👋🏼", "hair👩🏼‍🦰"]
        }
    }

    questions_and_answers = {
        "What is a big back😃?": {
            "answer": "someone who LOVES food",
            "options": ["someone who LOVES food", "someone Fanum Taxes", "someone with a big backbone"]
        },
        "What is an almond mom👩🏼?": {
            "answer": "an obsessive mom",
            "options": ["a gentle mom", "an understanding mom","an obsessive mom"]
        },
        "What is an 🤔?": {
            "answer": "when a boy does something that turns you off",
            "options": ["when a man breathes🌬️", "when a boy does something that turns you off🤮", "a sassy man💅"]
        },
        "What is girl hobbying👧🏻?": {
            "answer": "Going on wholistic activities",
            "options": ["Going on wholistic activities", "Hobbying only for girls", "Collecting girls as a hobby"]
        },
        "What is called when someone steals 20% of your food❌🍲?": {
            "answer": "Fanum Tax",
            "options": ["Fanum Tax", "Partial theft", "Nara smith tax"]
        },
        "What is the TikTok national anthem🎤?": {
            "answer": "Carnival",
            "options": ["Carnival🎠", "Munch🍽️", "Dunk Contest🏀"]
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
            score_labels = ['Burnt', 'Cooked', 'Okay', 'Boring', 'You live under a rock']
            score_colors = ['blue', 'skyblue', 'orange', 'orangered', 'red']


            arrow_pos = min(int((st.session_state.score / max_score) * len(score_labels)), len(score_labels) - 1)
            fig = gauge(score_labels, score_colors, arrow_pos, "Your BrainRot Score")
            st.pyplot(fig)

            with st.form(key='result_form'):
                if st.session_state.score <= 3:
                    st.markdown("<b>You're <span style='color: red;'>COOKED😳</span> you have brainrot from watching tiktok too much</b>", unsafe_allow_html=True)
                else:
                    st.markdown("<b>You're <span style='color: orange;'>😒boring...</span>you've been living under a rock</b>", unsafe_allow_html=True)

                if st.form_submit_button("Repeat Quiz"):
                    st.session_state.start_quiz = False
                    st.experimental_rerun()

                # Render copy to clipboard button
            st.markdown("""
            Click on the 📋 emoji below 👇🏼 to share 📤 with friends
            """)
            st_copy_to_clipboard("https://brainrottest.streamlit.app/")
            st.markdown(
                """
                ---
                Follow us on:

                Tiktok → [@curetique](https://tiktok.com/@curetique)
                
                🔮📈Gain aura when you follow us on tiktok Tiktok (real)
                
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
