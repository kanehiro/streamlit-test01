import streamlit as st
import pandas as pd

# ダミーデータの作成
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'joe'],
    'age': [25, 30, 34],
})

# DataFrameを表示
st.write(df)
# st.dataframe()でも表示可能
st.dataframe(df)
st.bar_chart(df.set_index('name'))