import streamlit as st
from pathlib import Path
import ast

st.set_page_config(
    page_title="서상고등학교",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 1. 첫 페이지(메인 홈)를 구성할 함수 정의
def home_page():
    # 업로드해주신 배너 이미지 파일명 적용 (화면 너비에 맞춰 꽉 차게 설정)
    st.image("Gemini_Generated_Image_qc0uqsqc0uqsqc0u.jpg", use_container_width=True)
    
    # 배너 아래에 추가적인 환영 문구 등을 넣고 싶다면 아래 주석을 해제하고 활용하세요.
    # st.title("경남 최초 구글 레퍼런스 스쿨, 서상고등학교")
    # st.markdown("미래형 인재 양성 **G-NEXT** 프로젝트에 오신 것을 환영합니다.")

# 2. 메인 홈을 st.Page로 지정 (default=True로 설정해 접속 시 가장 먼저 렌더링)
home = st.Page(home_page, title="메인 홈", icon="🏠", default=True)

pages_dir = Path("pages")

# 3. 페이지 리스트의 맨 처음에 '메인 홈' 페이지 삽입
pages_list = [home]

# 기존 pages 폴더 내의 페이지들 불러오기
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
