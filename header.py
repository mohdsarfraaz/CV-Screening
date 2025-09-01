import streamlit as st

def render_header():
    st.markdown(
        """
        <style>
        .header-container {text-align:center;margin-bottom:30px;}
        .header-container img {width:85%;max-height:260px;object-fit:cover;
            border-radius:18px;margin-bottom:20px;
            box-shadow:0 12px 25px rgba(0,0,0,0.3);}
        .main-title {font-size:46px;font-weight:900;color:#2E86C1;
            text-shadow:3px 3px 0px #a5c9f7, 6px 6px 0px #d0e4ff;}
        .subtitle {font-size:22px;color:#333;margin-bottom:25px;font-style:italic;}
        .info-box {text-align:center;font-size:18px;padding:14px 22px;
            border-radius:14px;width:70%;margin:auto;
            background:linear-gradient(145deg,#e8f5e9,#c8efce);
            color:#1b5e20;font-weight:600;}
        </style>

        <div class="header-container">
            <h1 class="main-title">📄 Resume Ranker</h1>
            <div class="subtitle">Smart Resume Shortlisting System for HR Professionals</div>
            <img src="assets/banner.jpg" alt="HR Banner">
            <div class="info-box">
                💡 Great teams are built by hiring the right talent. Let’s make it faster & smarter!
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
