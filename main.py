import streamlit as st

from PIL import Image
import time





st.title('Streamlit 入門')

st.write('プログレスバーの表示')
'start'
latest_iteration=st.empty()
bar=st.progress(0)


for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.05)
'Done'


left_column, right_column=st.columns(2)
button=left_column.button('右カラむに文字表示')
if button:
    right_column.write('ここは右カラむです')





img=Image.open(r"C:\Users\amori\Programing\StreamlitPractice\IMG_2057.jpg")
expander1=st.expander('問い合わせ1')
expander1.write('問い合わせ回答1')
expander2=st.expander('問い合わせ2')
expander2.write('問い合わせ回答2')
expander2.image(img, caption='aoki masahiro', use_column_width=True)

expander3=st.expander('問い合わせ3')
expander3.write('問い合わせ回答3')
