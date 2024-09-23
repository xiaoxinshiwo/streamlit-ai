import streamlit as st

st.title('My first streamlit app')
st.logo('image/Rice.png')
table_markdown = '''
A Table:

| Feature     | Support              |
| ----------: | :------------------- |
| CommonMark  | 100%                 |
| GFM         | 100% w/ `remark-gfm` |
'''

st.write(table_markdown)
st.image('image/juice.svg')