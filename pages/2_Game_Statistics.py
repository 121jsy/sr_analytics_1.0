from Dashboard import *

import plotly.express as px 
import streamlit as st
import pandas as pd
from PIL import Image


# list of indicators to display in each excel sheets "User Traffic" and "Game Statistics"
USER_TRAFFIC_INDIC = ['날짜', 'DAU(login)', 'DAU(chat)', 'DAU(quiz)', 'WAU(login)', 'MAU(login)',
                      'D+1 retention\n(login)', 'D+1 retention\n(nru login)', 'W+1 retention\n(login)',
                      'W+1 retention\n(new users login)', 'NRU (일일 신규 사용자 수)', 'CRU (누적 사용자 수)']
GAME_STATISTICS_INDIC = ['날짜', '스퀴즈볼 총 획득량\n(순수 획득)', '스퀴즈볼 총 사용량\n(소모성아이템 한정)', 'QAR\n퀴즈 정답률', '총 퀴즈 참여자 수', 'NQPP\n인당 퀴즈 참여',
                        'NCPP\n인당 채팅 참여', 'IUPP\n인당 아이템 사용']


def display_table(df, indicator):
    show_table = st.checkbox("Display Table")
    if show_table:
        # display '날짜' and chosen indicator in a table
        # .iloc[::1] to reverse the order of DataFrame        
        st.dataframe((df.iloc[::-1])[['날짜', indicator]], height=700)

def game_statistics_draw(df, indicator):
    with col2_1:
        draw(df, indicator)
    with col2_2:
        display_table(df, indicator)

im = Image.open("squizrun_png.png")
st.set_page_config(page_title="Squizrun Analytics", page_icon=im, layout="wide")
st.title("GAME STATISTICS")

df_ut, df_gs = load_from_file()

# Four columns for dynamic dropdown menu and date range (col1_4 and col1_5 are placeholders for indentation)
col1_1, col1_2, col1_3, col1_4 = st.columns([0.3, 0.45, 0.17, 0.08])

# First column in the first row for indicator dropdown menu
with col1_1:
    option = st.selectbox(
        '지표 선택',
        ('-', '인당 스퀴즈볼 총 획득량', '인당 스퀴즈볼 사용량', '총 퀴즈 참여자 수', '인당 퀴즈 참여 (NQPP)', '인당 채팅 참여 (NCPP)', '인당 아이템 사용 (IUPP)'))

with col1_3:
    filtered_df = date_range(df_gs)

# Two columns in the second row for the graph and table
data_container = st.container()
with data_container:
    col2_1, col2_2 = st.columns((3,1))

# Display DAU, MAU, WAU as default
if option == '-':
    game_statistics_draw(filtered_df, '총 퀴즈 참여자 수')

if option == '인당 스퀴즈볼 총 획득량':
    game_statistics_draw(filtered_df, '스퀴즈볼 총 획득량\n(순수 획득)')

elif option == '인당 스퀴즈볼 사용량':
    game_statistics_draw(filtered_df, '스퀴즈볼 총 사용량\n(소모성아이템 한정)')

elif option == '총 퀴즈 참여자 수':
    game_statistics_draw(filtered_df, '총 퀴즈 참여자 수')

elif option == '인당 퀴즈 참여 (NQPP)':
    game_statistics_draw(filtered_df, 'NQPP\n인당 퀴즈 참여')

elif option == '인당 채팅 참여 (NCPP)':
    game_statistics_draw(filtered_df, 'NCPP\n인당 채팅 참여')

elif option == '인당 아이템 사용 (IUPP)':
    game_statistics_draw(filtered_df, 'IUPP\n인당 아이템 사용')
