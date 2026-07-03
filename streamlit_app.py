import streamlit as st
from random import randint

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
table_name = ["red","orange","yellow","green","blue","purple"]

table_dict = {
    "red" : red,
    "orange" : orange,
    "yellow" : yellow,
    "green" : green,
    "blue" : blue,
    "purple" : purple,
}

def num_pick(num):
    result = []
    even = []
    odd = []
    c_table = table_name[randint(0,5)]
    for k,v in table_dict.items():
        if num in v :
            select_n = num
        else:
            select_n = v[randint(0,len(v)-1)]
        
        if select_n in result:
            select_n += 2
        
        result.append(select_n)
        if c_table == k:
            if select_n == 37:
                result.append(select_n-1)
            else:
                result.append(select_n+1)
        
    for i,v in enumerate(result):
        if v % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
        
        
    if len(even) > 4:
        while len(even) != 4:
            select_i = even[randint(0,len(even)-1)]
            mem_n_p = result[select_i]+1
            mem_n_m = result[select_i]-1
        
            if mem_n_p in result and mem_n_m not in result:
                result[select_i] = mem_n_m
            elif mem_n_p not in result and mem_n_m in result:
                result[select_i] = mem_n_p
            else:
                flip = randint(0,1)
                if flip == 0:
                    result[select_i] = mem_n_p
                else:
                    result[select_i] = mem_n_m
            even = []
            odd = []
            for i,v in enumerate(result):
                if v % 2 == 0:
                    even.append(i)
                else:
                    odd.append(i)
        
                
    if len(odd) > 4:
        while len(odd) != 4:
            select_i = odd[randint(0,len(odd)-1)]
            mem_n_p = result[select_i]+1
            mem_n_m = result[select_i]-1
        
            if mem_n_m == 0:
                mem_n_m = 4
            
            if mem_n_p == 38:
                mem_n_p = 34
            
        
            if mem_n_p in result and mem_n_m not in result:
                result[select_i] = mem_n_m
            elif mem_n_p not in result and mem_n_m in result:
                result[select_i] = mem_n_p
            else:
                flip = randint(0,1)
                if flip == 0:
                    result[select_i] = mem_n_p
                else:
                    result[select_i] = mem_n_m
            even = []
            odd = []
            for i,v in enumerate(result):
                if v % 2 == 0:
                    even.append(i)
                else:
                    odd.append(i)

    st.write(result)

with st.form("my_form_1"):
    st.write("まんべんなくピック")
    pick_ini_num = st.selectbox("引っ張り数字",[n for n in range(1,38)])
    #pick_ini_range = st.radio("引っ張り数字をズラす",["ズラす","ズラさない"])

    submitted = st.form_submit_button("Submit")
    if submitted:
        num_pick(int(pick_ini_num))
