"""Main module for the streamlit app"""
import streamlit as st

import awesome_streamlit as ast
import scr.corr_gen_count
import scr.corr_gen_years
import scr.report_bugs

ast.core.services.other.set_logging_format()

PAGES = {
    "Correlation-Generator(Country)": scr.corr_gen_count ,
    "Correlation-Generator(Year)": scr.corr_gen_years,
    "Report Bugs":scr.report_bugs
}


def main():
    """Main function of the App"""
    st.sidebar.title("Correlation-Generator   Navigation:")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)
    # st.sidebar.title("Contribute")
    # st.sidebar.info(
    #     "This an open source project and you are very welcome to **contribute** your awesome "
    #     "comments, questions, resources and apps as "
    #     "[issues](https://github.com/MarcSkovMadsen/awesome-streamlit/issues) of or "
    #     "[pull requests](https://github.com/MarcSkovMadsen/awesome-streamlit/pulls) "
    #     "to the [source code](https://github.com/MarcSkovMadsen/awesome-streamlit). "
    # )
    # st.sidebar.title("About")
#     st.sidebar.info(
#         """
#         This app is maintained by Marc Skov Madsen. You can learn more about me at
#         [datamodelsanalytics.com](https://datamodelsanalytics.com).
# """
#         )


if __name__ == "__main__":
    main()
