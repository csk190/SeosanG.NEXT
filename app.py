import streamlit as st

# 전체 페이지 기본 설정 (가장 먼저 선언되어야 함)
st.set_page_config(
    page_title="서상고등학교",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded" # 사이드바를 기본으로 열어둡니다.
)

# 사이드바 커스터마이징 (제목 및 설명 추가)
with st.sidebar:
    st.title("🏫 서상고등학교 메뉴")
    st.markdown("원하시는 메뉴를 선택해주세요.")
    st.divider()
    st.caption("2026학년도 신입생 모집 중")

# 이 파일은 메인 진입점 역할만 하며, 실제 내용은 pages/ 폴더 안의 파일들이 렌더링됩니다.
# 사용자가 사이드바에서 메뉴를 클릭하지 않았을 때 처음 보여줄 화면 안내 (또는 홈으로 자동 리다이렉트 효과)
st.markdown("### 👈 왼쪽 사이드바에서 '1_홈페이지' 메뉴를 선택해주세요.")
