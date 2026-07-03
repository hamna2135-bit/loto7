import streamlit as st

st.title("🎱 ロト7番号ピックアップ")
st.write("どっかの攻略法を設計思想として、なんかありそうな番号をピックするよ")
st.write("クイックピック、ランダムピックではないからね")
#設計思想
#1.引っ張り数字は「1つ」必ず入れる
#2.連番は「1組」必ず入れる
#3.末尾（下一桁）を「1組」合わせる
#4.奇数・偶数のバランスは「3:4」か「4:3」
#5.低中高のテーブルで均一になるように ↓で1個ずつピックできればいけるのでOK
#6.6個ずつのテーブルでまんべんなく

red = [n for n in range(1,7)]
orange = [n+6 for n in red]
yellow = [n+6 for n in orange]
green = [n+6 for n in yellow]
blue = [n+6 for n in green]
purple = [n+6 for n in blue]
purple.append(37)

with st.form("my_form_1"):
    st.write("まんべんなくピック")
    pick_ini_num = st.selectbox("引っ張り数字",[n for n in range(1,38)])
    pick_ini_range = st.radio("引っ張り数字をズラす",["ズラす","ズラさない"])

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("引っ張り数字", pick_ini_num)
        st.write("引っ張り数字を", pick_ini_range)

st.write("outside form")
st.write(pick_ini_num)
st.write(pick_ini_range)