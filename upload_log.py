import streamlit as st
import webbrowser

st.markdown("# FREEPAY LOG UPLOAD")

if st.button("로그 전송") :
#  st.html("<a href=""intent://freepaylink?trantype=upload_log&catid=1111111111#Intent;scheme=smartroapp;package=com.smartro.secapps.freepay>테스트</a>")
    st.html('<a href="smartroapp://freepaylink?trantype=upload_log&catid=1111111111">테스트</a>')

if st.button("웹 브라우저") :
    webbrowser.open("https://www.naver.com")
