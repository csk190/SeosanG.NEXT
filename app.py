import streamlit as st

st.set_page_config(
    page_title="서상고등학교",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 페이지 정의 (파일 경로는 실제 파일명에 맞게 수정)
pages = {
    "서상고등학교 메뉴": [
        st.Page("pages/1_홈페이지.py", title="🏠 홈페이지"),
        st.Page("pages/2_학교소개.py", title="🏫 학교소개"),
        st.Page("pages/3_입학안내.py", title="📋 입학안내"),
        # 나머지 페이지들 추가
    ]
}

pg = st.navigation(pages)

# 사이드바 추가 정보
with st.sidebar:
    st.divider()
    st.caption("2026학년도 신입생 모집 중")

pg.run()
