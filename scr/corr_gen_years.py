import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import awesome_streamlit as ast

def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading About ..."):


        df_1 = pd.read_csv("life-expectancy.csv")
        df_2 = pd.read_csv('human-right-scores.csv')
        df_3 = pd.read_csv('gdp-data.csv')
        df_4 = pd.read_csv('coal-consumption.csv')
        df_5 = pd.read_csv('co2-emmisions.csv')


        CHOICE = {'Life-Expectancy': df_1, 'Human-Right-Scores': df_2, 'GDP': df_3, 'Coal-Consump': df_4,
                               'CO2-Emiss': df_5}

        CHOICE_2 = {'Life-Expectancy': df_1, 'Human-Right-Scores': df_2, 'GDP': df_3, 'Coal-Consump': df_4,
                               'CO2-Emiss': df_5}

        YEAR = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,
                2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

        st.title('Correlation-Generator(Year)')

        opt = st.selectbox("Select Dataset-1:", options=list(CHOICE.keys()))
        opt_2 = st.selectbox("Select Dataset-2:", options=list(CHOICE_2.keys()))
        opt_3 = st.selectbox("Select Countries:", options=YEAR)

        dataset_1 = CHOICE[opt]
        dataset_2 = CHOICE_2[opt_2]
        year = opt_3

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
            plot.set(xlabel=opt_2, ylabel=opt, title='Plot')
            st.pyplot()

        if st.button('Submit:'):
            my_func()
            # print("....")
