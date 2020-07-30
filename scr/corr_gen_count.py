import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import awesome_streamlit as ast


def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading Page ..."):
        # ast.shared.components.title_awesome(" - About")
        # st.markdown(
        #     """## Contributions""")


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

        st.title('Correlation-Generator(Country)')

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
        int(pearson_coef)
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
        
         plot = sns.regplot(X,Y)
         plot.set(xlabel=option_2, ylabel=option, title='Plot')
         st.pyplot()
        
        if st.button('Submit'):
         my_func()
         # print("....")
