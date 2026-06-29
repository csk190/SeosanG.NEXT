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
    # 현재 파일(app.py)의 위치를 기준으로 이미지의 절대 경로를 생성합니다.
    current_dir = Path(__file__).parent
    image_path = current_dir / "Gemini_Generated_Image_qc0uqsqc0uqsqc0u.jpg"
    
    # 이미지가 실제로 존재하는지 확인 후 렌더링 (앱 크래시 방지)
    if image_path.exists():
        st.image(str(image_path), use_container_width=True)
    else:
        st.error(f"⚠️ 배너 이미지를 찾을 수 없습니다: {image_path.name}")
        st.info("GitHub 저장소에 이미지 파일이 정상적으로 업로드되었는지, 대소문자가 정확한지 확인해 주세요.")
    
    # 배너 아래에 추가적인 환영 문구 등을 넣고 싶다면 아래 주석을 해제하고 활용하세요.
    # st.title("경남 최초 구글 레퍼런스 스쿨, 서상고등학교")
    # st.markdown("미래형 인재 양성 **G-NEXT** 프로젝트에 오신 것을 환영합니다.")

# 2. 메인 홈을 st.Page로 지정 (default=True로 설정해 접속 시 가장 먼저 렌더링)
home = st.Page(home_page, title="메인 홈", icon="🏠", default=True)

pages_dir = Path("pages")

# 3. 페이지 리스트의 맨 처음에 '메인 홈' 페이지 삽입
pages_list = [home]

# 기존 pages 폴더 내의 페이지들 불러오기 (폴더 존재 여부 확인 추가)
if pages_dir.exists() and pages_dir.is_dir():
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
