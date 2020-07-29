import pandas as pd
import numpy as np
import streamlit as st
from streamlit.ReportThread import get_report_ctx
from streamlit.hashing import _CodeHasher
from streamlit.server.Server import Server

df_1 = pd.read_csv("life-expectancy.csv")
df_2 = pd.read_csv('human-right-scores.csv')
df_3 = pd.read_csv('gdp-data.csv')
df_4 = pd.read_csv('coal-consumption.csv')
df_5 = pd.read_csv('co2-emmisions.csv')

CHOICES = {'Life-Expectancy': df_1, 'Human-Right-Scores': df_2, 'GDP': df_3, 'Coal-Consump': df_4,
           'CO2-Emiss': df_5}

CHOICES_2 = {'Life-Expectancy': df_1, 'Human-Right-Scores': df_2, 'GDP': df_3, 'Coal-Consump': df_4,
             'CO2-Emiss': df_5}

COUNTRY = ['United States', 'Canada', 'Mexico', 'Argentina', 'Brazil', 'France',
           'Germany', 'Italy', 'United Kingdom', 'Spain', 'Sweden', 'Switzerland',
           'Norway', 'Belgium', 'Poland', 'Israel', 'India', 'China', 'Japan',
           'South Korea', 'Singapore', 'Australia', 'Vietnam', 'Philippines', 'Indonesia',
           'South Africa', 'Ghana', 'Chile']

YEAR = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,
        2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]


def main():
    state = _get_state()
    pages = {
        "Correlation-generator(Country)": corr_gen_count,
        "Correlation-generator(Year)": corr_gen_year,
    }

    st.sidebar.title("Correlation-Generator")
    page = st.sidebar.radio("Select your correlation page:", tuple(pages.keys()))

    # Display the selected page with the session state
    pages[page](state)

    # Mandatory to avoid rollbacks with widgets, must be called at the end of your app
    state.sync()


def corr_gen_count(state):

    st.title('Correlation-Generator(For Country)')

    option = st.selectbox("Select Dataset-1", options=list(CHOICES.keys()))
    option_2 = st.selectbox("Select Dataset-2", options=list(CHOICES_2.keys()))
    option_3 = st.selectbox("Select Countries", options=COUNTRY)

    dataset_1 = CHOICES[option]
    dataset_2 = CHOICES_2[option_2]
    country = option_3

    dataset_1 = dataset_1.loc[(dataset_1["Entity"] == country)]
    dataset_2 = dataset_2.loc[(dataset_2["Entity"] == country)]

    df_all = dataset_2.merge(dataset_1.drop_duplicates(), on=['Year'], how='left', indicator=False)

    df_all.rename(columns={df_all.columns[3]: "Data-1"}, inplace=True)
    df_all.rename(columns={df_all.columns[6]: "Data-2"}, inplace=True)

    df_all = df_all[df_all['Data-1'].notna()]
    df_all = df_all[df_all['Data-2'].notna()]

    X = df_all["Data-1"]
    Y = df_all["Data-2"]

    pearson_coef1 = np.corrcoef(X, Y)
    pearson_coef = pearson_coef1[1, 0]
    def my_func():
        dat = str(pearson_coef)
        if dat[0] == '-':
            if pearson_coef >= -0.4:
                pe_str = str(pearson_coef)
                my_str = "This is a Week Negative correlation: {}".format(pe_str)
                st.write(my_str)
            elif pearson_coef >= -0.7:
                pe_str = str(pearson_coef)
                my_str = "This is a Medium Negative correlation: {}".format(pe_str)
                st.write(my_str)
            elif pearson_coef < -0.7:
                pe_str = str(pearson_coef)
                my_str = "This is a strong Negative correlation: {}".format(pe_str)
                st.write(my_str)
        else:
            if pearson_coef <= 0.4:
                pe_str = str(pearson_coef)
                my_str = "This is a Week Positive correlation: {}".format(pe_str)
                st.write(my_str)
            elif pearson_coef <= 0.7:
                pe_str = str(pearson_coef)
                my_str = "This is a Medium Positive correlation: {}".format(pe_str)
                st.write(my_str)
            elif pearson_coef > 0.7:
                pe_str = str(pearson_coef)
                my_str = "This is a Strong Positive correlation: {}".format(pe_str)
                st.write(my_str)

    if st.button('Submit'):
        my_func()

def corr_gen_year(state):

    st.title('Correlation-Generator(For Years)')

    option = st.selectbox("Select Dataset-1", options=list(CHOICES.keys()))
    option_2 = st.selectbox("Select Dataset-2", options=list(CHOICES_2.keys()))
    option_3 = st.selectbox("Select Year", options=YEAR)

    dataset_1 = CHOICES[option]
    dataset_2 = CHOICES_2[option_2]
    year = option_3

    dataset_1 = dataset_1.loc[(dataset_1["Year"] == year)]
    dataset_2 = dataset_2.loc[(dataset_2["Year"] == year)]

    df_all = dataset_2.merge(dataset_1.drop_duplicates(), on=['Entity'], how='left', indicator=False)

    df_all.rename(columns={df_all.columns[3]: "Data-1"}, inplace=True)
    df_all.rename(columns={df_all.columns[6]: "Data-2"}, inplace=True)

    df_all = df_all[df_all['Data-1'].notna()]
    df_all = df_all[df_all['Data-2'].notna()]

    X = df_all["Data-1"]
    Y = df_all["Data-2"]

    pearson_coef1 = np.corrcoef(X, Y)
    pearson_coef = pearson_coef1[1, 0]
    def my_func():
        dat = str(pearson_coef)
        if dat[0] == '-':
            if pearson_coef >= -0.4:
                pe_str = str(pearson_coef)
                my_str = "This is a Week Negative correlation: {}".format(pe_str)
                st.write(my_str)
            elif pearson_coef >= -0.7:
                pe_str = str(pearson_coef)
                my_str = "This is a Medium Negative correlation: {}".format(pe_str)
                st.write(my_str)
            elif pearson_coef < -0.7:
                pe_str = str(pearson_coef)
                my_str = "This is a strong Negative correlation: {}".format(pe_str)
                st.write(my_str)
        else:
            if pearson_coef <= 0.4:
                pe_str = str(pearson_coef)
                my_str = "This is a Week Positive correlation: {}".format(pe_str)
                st.write(my_str)
            elif pearson_coef <= 0.7:
                pe_str = str(pearson_coef)
                my_str = "This is a Medium Positive correlation: {}".format(pe_str)
                st.write(my_str)
            elif pearson_coef > 0.7:
                pe_str = str(pearson_coef)
                my_str = "This is a Strong Positive correlation: {}".format(pe_str)
                st.write(my_str)

    if st.button('Submit'):
        my_func()

class _SessionState:

    def __init__(self, session, hash_funcs):
        """Initialize SessionState instance."""
        self.__dict__["_state"] = {
            "data": {},
            "hash": None,
            "hasher": _CodeHasher(hash_funcs),
            "is_rerun": False,
            "session": session,
        }

    def __call__(self, **kwargs):
        """Initialize state data once."""
        for item, value in kwargs.items():
            if item not in self._state["data"]:
                self._state["data"][item] = value

    def __getitem__(self, item):
        """Return a saved state value, None if item is undefined."""
        return self._state["data"].get(item, None)

    def __getattr__(self, item):
        """Return a saved state value, None if item is undefined."""
        return self._state["data"].get(item, None)

    def __setitem__(self, item, value):
        """Set state value."""
        self._state["data"][item] = value

    def __setattr__(self, item, value):
        """Set state value."""
        self._state["data"][item] = value

    def clear(self):
        """Clear session state and request a rerun."""
        self._state["data"].clear()
        self._state["session"].request_rerun()

    def sync(self):
        """Rerun the app with all state values up to date from the beginning to fix rollbacks."""

        # Ensure to rerun only once to avoid infinite loops
        # caused by a constantly changing state value at each run.
        #
        # Example: state.value += 1
        if self._state["is_rerun"]:
            self._state["is_rerun"] = False

        elif self._state["hash"] is not None:
            if self._state["hash"] != self._state["hasher"].to_bytes(self._state["data"], None):
                self._state["is_rerun"] = True
                self._state["session"].request_rerun()

        self._state["hash"] = self._state["hasher"].to_bytes(self._state["data"], None)


def _get_session():
    session_id = get_report_ctx().session_id
    session_info = Server.get_current()._get_session_info(session_id)

    if session_info is None:
        raise RuntimeError("Couldn't get your Streamlit Session object.")

    return session_info.session


def _get_state(hash_funcs=None):
    session = _get_session()

    if not hasattr(session, "_custom_session_state"):
        session._custom_session_state = _SessionState(session, hash_funcs)

    return session._custom_session_state


if __name__ == "__main__":
    main()
