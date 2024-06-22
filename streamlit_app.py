import streamlit as st

# This must be the first Streamlit command in your script
st.set_page_config(page_title="Welcome to Curetique",
                   page_icon=":woman:",
                   layout="wide")

# Check query parameters to handle page navigation
query_params = st.experimental_get_query_params()
if "page" in query_params:
    page = query_params["page"][0]
    if page == "1_BrainRot_Quiz":
        with open("pages/1_BrainRot_Quiz.py") as f:
            code = compile(f.read(), "pages/1_BrainRot_Quiz.py", 'exec')
            exec(code)
        st.stop()

st.markdown("# :red[Cureqtique]👯‍♀️")

# Add a button to navigate to the quiz page
if st.button('Start the BrainRot Quiz'):
    st.experimental_set_query_params(page="1_BrainRot_Quiz")
    st.experimental_rerun()
    st.balloons()

# Render copy to clipboard button
st.markdown("""
Click on the 📋 emoji below 👇🏼 to copy the link🔗 share 👯‍♀️ with friends
""")

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
