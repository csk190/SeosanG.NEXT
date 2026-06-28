import streamlit as st
from pathlib import Path
import ast

st.set_page_config(
    page_title="서상고등학교",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

pages_dir = Path("pages")
pages_list = []

for f in sorted(pages_dir.glob("*.py")):
    try:
        # 문법 오류 있는 파일은 건너뜀
        ast.parse(f.read_text(encoding="utf-8"))
        pages_list.append(st.Page(str(f), title=f.stem.split("_", 1)[-1]))
    except SyntaxError as e:
        st.sidebar.error(f"⚠️ {f.name} 오류: {e}")

if pages_list:
    pg = st.navigation({"서상고등학교 메뉴": pages_list})
    with st.sidebar:
        st.divider()
        st.caption("2027학년도 신입생 모집 중")
    pg.run()
