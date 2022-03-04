import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

# st.write('DataFrame')
# st.write('Interactive Widgets')

# st.sidebar.write('Interactive Widgets')
# text = st.sidebar.text_input('あなたの趣味を教えて下さい。')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!!'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問合せ')
expander.write('問合せ内容を書く')

# text = st.text_input('あなたの趣味を教えて下さい。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味：', text, 'です。'
# 'コンディション：', condition

option = st.selectbox(
    'あなたが好きな数字を教えて下さい。',
    list(range(1, 11))
)

'あなたの好きな数字は、', option, 'です。'
#'あなたの好きな数字は、' + str(option) + 'です。'

st.write('Display Image')
if st.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img, caption='かやふぇしゅ', use_column_width=True)

# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })

#st.write(df)
# Streamlitで列幅を指定しても変わらない！自動幅調整機能がない！
#st.dataframe(df, width=100, height=100)
#st.dataframe(df.style.highlight_max(axis=0), width=500, height=200)

# st.dataframeと違ってソートができない。静的な表を使用する場合
# st.table(df.style.highlight_max(axis=0))

# df = pd.DataFrame(
#     np.random.rand(20, 3),  # np.random.rand()は[0.0, 1.0)（0.0以上、1.0未満）の乱数を返す。
#     columns=['a', 'b', 'c']
# )

# df = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)


"""
# 章
## 節
### 
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""