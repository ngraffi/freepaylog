import streamlit as st
import webbrowser

st.markdown("# FREEPAY LOG UPLOAD??")

if st.button("로그 전송") :
 webbrowser.open("smartro://freepaylink?trantype=upload_log&catid=1111111111")

if st.button("웹 브라우저") :
 webbrowser.open("https://www.naver.com")
