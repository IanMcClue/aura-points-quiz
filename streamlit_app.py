import streamlit as st

# This must be the first Streamlit command in your script
st.set_page_config(page_title="Welcome to Curetique", page_icon=":woman:", layout="wide")


st.markdown("# :white[Curetique]👯‍♀️")

st.markdown("""
Click on the sidebar 👈 to get started with the [BrainRot Quiz](https://brainrottest.streamlit.app/) 🧠💣
"""
)


st.markdown(
     """
---
Follow us on:

Tiktok → [@curetique](https://tiktok.com/@curetique)

🔮📈Gain aura when you follow us on Tiktok (real)

🧙🏼‍♂️You've been granted +100 points for completing this quiz share on Tiktok for an extra +100,000 points
"""
)

# Footer
st.divider()
footer = """<div style="text-align: center;">
                <p>A <a href="http://fiat-lux-labs-tmp.vercel.app/" target="_blank">Fiat Lux Labs</a> Project</p>
                <a href="https://visitorbadge.io/status?path=https%3A%2F%2Fbrainrottest.streamlit.app%2F">
                    <img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fbrainrottest.streamlit.app%2F&label=visitors&labelColor=%23ffffff&countColor=%23000000&style=plastic" />
                </a>
            </div>"""
st.markdown(footer, unsafe_allow_html=True)
