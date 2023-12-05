import streamlit as st
import numpy as np
import pandas as pd
import os
os.system('cls')
import matplotlib.pyplot as plt

col1, col2 = st.columns([1, 2])
with col1:
    'tt'
    # st.image('순심이.jpg')
with col2:
    '놓치면 후회할 인재 (신수인, 시급 3만원, 대박 쩔어~~)'
    '전화번호(📞) : 010-xxxx-xxxx'
    '이메일(📧) : gktjdcjf97@naver.com'
    '주소(🏠) : 충남 논산시 대학로 121'

''
'-----------------------'
col = st.columns(4)
with col[0]:
    st.link_button("Google(🌐)", "https://google.com")
with col[1]:
    st.link_button("Naver(✅)", "https://naver.com")
with col[2]:
    st.link_button("Daum(🇩)", "https://daum.net")
with col[3]:
    st.link_button("Facebook(ⓕ)", "https://facebook.com")

fig, ax = plt.subplots()

x = [-10, -9, -8, -7, -6]
x

x = []
y = []
for i in range(-10, 11, 2):
    x.append(i)
    y.append(3*i**3 - 5*i**2 + 3*i - 7)

cc = st.radio('선의 색을 선택하시오.', ['red', 'green', 'blue', 'orange'])
ma = st.radio('마커의 형태를 선택하시오', ['o', '^', 's', 'p', 'h'])
ls = st.radio('선의 형태를 선택하시오', ['-', '-.', ':', '--'])
# plt.plot(x, y, '-.go')
plt. plot(x, y, color=cc, linestyle=ls, marker=ma)
st.pyplot(fig)

x[0]


x = []
y = []
for i in range (-100, 101, 5):
    x.append(i)
    y.append(2*i**3 - 5*i**2 + 3*i -7)

col1, col2, col3 = st.columns(3)
with col1:
    color = st.radio('색을 선택하시오.', ('red', 'green', 'blue'))
with col2:
    linestyle = st.radio('선의 스타일을 선택하시오.', ('-', '-.', ':'))
with col3:
    marker = st.radio('마커의 스타일을 선택하시오.', ('s', '^', 'o'))




# li = [1, 2, 3, 4]
# n = np.array(li)
# p = pd.Series(li, index=['addd', ''])
# import streamlit as st

# list1 = list([['한빛', '남자', '20', '180'],
#               ['한결', '남자', '21', '177'],
#               ['김한결', '중성', '51', '155'],
#               ['한라', '여자', '20', '160']])
# n = np.array(list1)
# col_name = ['이름', '성별', '나이', '키']
# df = pd.DataFrame(list1, columns=col_name, index=['1행', '2행', '3행', '4행'])
# df

# genre = st.radio("선택하시오.",
#                  ["오름차순","내림차순", "기타", "요약"],
#                  horizontal=True, index=2)
# number = st.number_input('Insert a number', value=20, step=1)
# df.iloc[3, 2] = number

# if '오름' in genre:
#     st.dataframe(df.sort_values(by=['키']))
# if '내림' in genre:
#     st.dataframe(df.sort_values(by=['키'], ascending=False))
# if '기타' in genre:
#     st.dataframe(df)
# if '요약' in genre:
#     st.dataframe(df)
    
# genre = st.radio(
#     "What's your favorite movie genre",
#     [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
#     index=None,
# )

# st.write("You selected:", genre)

# for i  in range(4):
#     li[i] = li[i] + 3
# li
li = np.array([7, 2, 5, 4])
li
li_sort = np.sort(li)[::-1]
li_sort

import sys
sys.exit()


import turtle
import random
t1 = turtle.Turtle()
t1.shape('turtle')

t1.width(5)
t1.color('red')
t1.penup()
t1.goto(-100, 100)
t1.pendown()
t1.forward(100)

t2 = turtle.Turtle()
t2.shape('turtle')
t2.width(5)
t2.color('bule')
t2.goto(-100, 100)
t2.pendown()
t2.forward(100)

for i in range(30):            
    d1 = random.randint(1, 60)
    t1.forward(d1)
    d2 = random.randint(1, 60)
    t2.forward(d2)

# n = np.full((4, 5 ), 10)
# n

# n1 = np.zeros((4, 5))
# n1
# for i in range(4):
#     for j in range(5):
#         n1[i, j] = 10
# n1

# n2 = []
# n2 .append(10)
# n2
# np.append(n2, 15)
# n2

# arr = np.array[1, 2, 3]
# s = arr.sum()
# s
# s1 = np.sum(arr)
# s1

# 
a = np.arange(8)
a
a.shape = (4, 2)
a
b = a.flatten()
b
b = b.resize((2,4))
b
c = np.resize(b, (2,4))
c

import os
os.system('cls')

a = np.array([1, 10, -5, 2])
print(np.abs(a))
print(np.sqrt(a))
print(a**0.5)
print(np.square(a))
print(a**2)









list1 = [[1, 2, 3, 4], [3,5,7,9]]
a = np.array(list1) 
a
a.shape
s = a.sum(axis=0)
s
mn = a.min(axis=1)
mn
a[1, 2] = 30

a = np.zeros(2)
a
b = np.zeros((2,2))
b
c = np.ones((2,3))
c
d = np.full((2,3), 5)
d
e = np.eye(3)
e

# a.ndim
# n = np.ndim()
# def user_eye(n):
#     arr = np.zeros((n,n))
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 arr[i, j] = 1
#                 return arr
