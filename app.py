import streamlit as st


st.set_page_config(page_title="demo webpage", page_icon=":tada:", layout="wide")


with st.container():
st.subheader( "Hi,i am mohamed :wave:")
st.title("A very smart ten year old?")
st.write("new in coding and attempting to make a webpage hoping to become good at web developing")
st.write("inspiration from shift[learn more>](https://www.facebook.com/Shift.course?mibextid=ZbWKwL)")

#----WHAT I DO----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
      st.header("My story")
      st.write("##")
      st.write(
          """
          have you seen the link that sends you to this company named SHIFT? it is is my older brothers company, and i made this page to simulate how hard it is to make a website and my problems were:
          -it takes too much time, even when creating his own company my brother did not program it, he called his freind to program it
          -it is very tricky,this does not need explaining as forgeting a single letter makes every thing malfunction
          -not knowing how to type certain symbols,this is mostly why proggraming or making this was so time consuming

          while making this was thinking of making this costumer service, so if you have any problems with shifts courses you contact me by entering your name,emal, and problem
          """
         
      )
      
