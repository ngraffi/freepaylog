import streamlit as st
# from plyer import intent
# from plyer.facades import Intent
# from plyer import notification

st.subheader("FREEPAY 로그")

# if st.button("로그 전송") :
    # my_intent = Intent(
    #     action=Intent.ACTION_VIEw,
    #     data="smartroapp://freepaylink?trantype=upload_log&catid=111111111"
    # )

    # my_intent.send()
    # notification.notify(title = "Greeting!", messgae = "message~~", app_icon = None, timeout = 10, toast = False)
    

st.link_button(url="smartroapp://freepaylink?trantype=upload_log&catid=111111111", label="로그 올리기", icon='🐶')


