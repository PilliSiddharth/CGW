import streamlit as st
import awesome_streamlit as ast
import pandas as pd

def write():
    @st.cache(allow_output_mutation=True)
    def get_report():
        return []

    st.title("Report Bugs:")
    user_input = st.text_area("Any bugs? Report here:")

    if st.button("Submit"):
        get_report().append({"Report": user_input})

    st.write(pd.DataFrame(get_report()))
