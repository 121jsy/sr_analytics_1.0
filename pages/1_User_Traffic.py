from Dashboard import *

import plotly.express as px 
import streamlit as st
import pandas as pd
import datetime


# list of indicators to display in each excel sheets "User Traffic" and "Game Statistics"
USER_TRAFFIC_INDIC = ['날짜', 'DAU(login)', 'DAU(chat)', 'DAU(quiz)', 'WAU(login)', 'MAU(login)',
                      'D+1 retention\n(login)', 'D+1 retention\n(nru login)', 'W+1 retention\n(login)',
                      'W+1 retention\n(new users login)', 'NRU (일일 신규 사용자 수)', 'CRU (누적 사용자 수)']
GAME_STATISTICS_INDIC = ['날짜', '스퀴즈볼 총 획득량', '스퀴즈볼 총 사용량\n(소모성아이템 한정)', 'QAR\n퀴즈 정답률', '총 퀴즈 참여자 수', 'NQPP\n인당 퀴즈 참여',
                        'NCPP\n인당 채팅 참여', 'IUPP\n인당 아이템 사용']


st.set_page_config(layout="wide")
st.title("USER TRAFFIC")

df_ut, df_gs = load_from_file()

def display_table(df, indicator):
    show_table = st.checkbox("Display Table")
    if show_table:
        st.dataframe(df[['날짜', indicator]], height=700)

def user_traffic_draw(df, indicator):
    with col2_1:
        draw(df, indicator)
    with col2_2:
        display_table(df, indicator)


# Four columns for dynamic dropdown menu and date range (col1_4 and col1_5 are placeholders for indentation)
col1_1, col1_2, col1_3, col1_4, col1_5, col1_6 = st.columns([0.15, 0.15, 0.15, 0.3, 0.17, 0.08])


with col1_5:
    filtered_df = date_range(df_ut)

# First column in the first row for indicator dropdown menu
with col1_1:
    option = st.selectbox(
        '지표 선택',
        ('-', 'DAU', 'WAU', 'MAU', 'Retention', 'NRU', 'CRU'))
    

# Two columns in the second row for the graph and table
data_container = st.container()
with data_container:
    col2_1, col2_2 = st.columns((3,1))


if option == 'DAU':
    with col1_2:
        option_1 = st.selectbox('',('-','login', 'chat', 'quiz'))
    if option_1 == 'login':
        indicator = 'DAU(login)'
        user_traffic_draw(filtered_df, indicator)
    elif option_1 == 'chat':
        indicator = 'DAU(chat)'
        user_traffic_draw(filtered_df, indicator)
    elif option_1 == 'quiz':
        indicator = 'DAU(quiz)'
        user_traffic_draw(filtered_df, indicator)

elif option == 'WAU':
    indicator = 'WAU(login)'
    # filtered_df = date_range(df_ut)
    user_traffic_draw(filtered_df, indicator)

elif option == 'MAU':
    indicator = 'MAU(login)'
    user_traffic_draw(filtered_df, indicator)

elif option == 'Retention':
    with col1_2:
        option_1 = st.selectbox('Retention 타입 선택',('-', 'D+1', 'W+1'))
    with col1_3:
        option_2 = st.selectbox('전체 또는 신규 유저 선택',('-', 'Total Users', 'New Users'))
    if option_1 == 'D+1' and option_2 == 'Total Users':
        indicator = 'D+1 retention\n(login)'
        user_traffic_draw(filtered_df, indicator)

    elif option_1 == 'D+1' and option_2 == 'New Users':
        indicator = 'D+1 retention\n(nru login)'
        user_traffic_draw(filtered_df, indicator)

    elif option_1 == 'W+1' and option_2 == 'Total Users':
        indicator = 'W+1 retention\n(login)'
        user_traffic_draw(filtered_df, indicator)

    elif option_1 == 'W+1' and option_2 == 'New Users':
        indicator = 'W+1 retention\n(new users login)'
        user_traffic_draw(filtered_df, indicator)

elif option == 'NRU':
    indicator = 'NRU (일일 신규 사용자 수)'
    user_traffic_draw(filtered_df, indicator)

elif option == 'CRU':
    indicator = 'CRU (누적 사용자 수)'
    user_traffic_draw(filtered_df, indicator)

