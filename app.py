import streamlit as st
import os
from pathlib import Path

st.set_page_config(
    page_title="서상고등학교",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# pages/ 폴더 안의 파일을 자동으로 읽어서 등록
pages_dir = Path("pages")
page_files = sorted(pages_dir.glob("*.py"))  # 이름순 정렬

pages_list = [st.Page(str(f), title=f.stem.split("_", 1)[-1]) for f in page_files]

pg = st.navigation({"서상고등학교 메뉴": pages_list})

with st.sidebar:
    st.divider()
    st.caption("2026학년도 신입생 모집 중")

pg.run()
