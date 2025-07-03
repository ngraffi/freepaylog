import streamlit as st

st.subheader("FREEPAY 로그")

catID = st.text_input("단말기번호", max_chars=10, icon="💳")
    
st.link_button(url="smartroapp://freepaylink?trantype=upload_log&catid=" + catID, label="실행하기", icon='🐶', disabled=len(catID)!=10)

