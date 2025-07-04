import streamlit as st
from st_keyup import st_keyup

st.set_page_config(
    page_title = "Smartro",
    page_icon = "🚧"
)

st.subheader("FREEPAY 로그")

catID = st_keyup("단말기번호", max_chars=10)

st.link_button(
    url="smartroapp://freepaylink?trantype=upload_log&catid=" + catID, 
    label="실행하기", 
    icon='🐶', 
    disabled=len(catID)!=10, 
)

