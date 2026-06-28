import streamlit as st

# 페이지 기본 설정 (가장 먼저 호출되어야 함)
st.set_page_config(
    page_title="서상고 G-NEXT 디지털 브로슈어",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 스트림릿의 기본 UI를 덮어쓰고 힙한 다크/네온 테마를 적용하기 위한 CSS
custom_css = """
<style>
    /* 전체 배경 및 폰트 설정 */
    .stApp {
        background-color: #020617; /* slate-950 */
        color: #f8fafc; /* slate-50 */
        font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
    }
    
    /* 상단 기본 헤더 숨기기 */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* 그라데이션 텍스트 (네온 효과) */
    .gradient-text {
        background: linear-gradient(to right, #22d3ee, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        display: inline;
    }
    
    /* 네비게이션 바 */
    .nav-bar {
        padding: 1rem 0;
        border-bottom: 1px solid #1e293b;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 3rem;
    }
    .nav-logo {
        font-size: 1.25rem;
        font-weight: 900;
        background: linear-gradient(to right, #22d3ee, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.05em;
    }
    
    /* 웰컴 뱃지 */
    .welcome-badge {
        display: inline-block;
        padding: 0.25rem 1rem;
        border-radius: 9999px;
        border: 1px solid rgba(6, 182, 212, 0.3);
        background-color: rgba(6, 182, 212, 0.1);
        color: #22d3ee;
        font-size: 0.875rem;
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-bottom: 1.5rem;
    }

    /* 스탯 바 카드 UI */
    .stat-card {
        background-color: #020617;
        border: 1px solid #1e293b;
        padding: 1.25rem;
        border-radius: 1rem;
        margin-bottom: 1rem;
        transition: border-color 0.3s ease;
    }
    .stat-card:hover {
        border-color: #475569;
    }
    .stat-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.75rem;
    }
    .stat-title {
        font-weight: 700;
        color: #e2e8f0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .stat-level {
        font-weight: 900;
        font-size: 0.875rem;
    }
    .progress-bg {
        height: 0.5rem;
        background-color: #1e293b;
        border-radius: 9999px;
        overflow: hidden;
    }
    .progress-fill {
        height: 100%;
        border-radius: 9999px;
    }

    /* CTA 섹션 */
    .cta-container {
        border: 1px solid rgba(6, 182, 212, 0.2);
        background-color: rgba(8, 51, 68, 0.3);
        padding: 3rem 2rem;
        border-radius: 1.5rem;
        text-align: center;
        margin-top: 4rem;
        margin-bottom: 4rem;
        position: relative;
    }
    .limited-badge {
        position: absolute;
        top: -12px;
        left: 50%;
        transform: translateX(-50%);
        background-color: #06b6d4;
        color: #020617;
        font-size: 0.75rem;
        font-weight: 900;
        padding: 0.25rem 1rem;
        border-radius: 9999px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* 링크 버튼 중앙 정렬용 */
    .center-btn {
        display: flex;
        justify-content: center;
        margin-top: 1.5rem;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 상단 네비게이션
st.markdown("""
<div class="nav-bar">
    <div class="nav-logo">SEOSANG.NEXT</div>
    <div style="font-size: 0.875rem; color: #94a3b8;">👨‍💻 G-NEXT AI Center</div>
</div>
""", unsafe_allow_html=True)

# 히어로(메인) 섹션
st.markdown("""
<div style="text-align: center; padding: 2rem 0 4rem 0;">
    <div class="welcome-badge">Welcome to the Future</div>
    <h1 style="font-size: 3.5rem; font-weight: 900; line-height: 1.2; margin-bottom: 1.5rem; color: #f8fafc;">
        교실? 아니, <br>
        여긴 내 <span class="gradient-text">크리에이티브 랩(Lab)</span>이야
    </h1>
    <p style="color: #94a3b8; font-size: 1.125rem; line-height: 1.6; max-width: 600px; margin: 0 auto 2.5rem auto; font-weight: 300;">
        아직도 분필 가루 마시며 수업 들어? 서상고에서는 프롬프트 하나로 세상을 디자인해. 너만의 AI, 여기서 직접 만들어봐.
    </p>
</div>
""", unsafe_allow_html=True)

# 버튼 영역 (Streamlit 기본 컬럼 사용)
col1, col2, col3, col4 = st.columns([1, 2, 2, 1])
with col2:
    st.link_button("🚀 G-NEXT AI 캠프 신청", "https://forms.google.com", use_container_width=True)
with col3:
    st.link_button("📺 POV 숏폼 영상 보기", "https://youtube.com", use_container_width=True)

st.divider()

st.markdown("""
<div style="margin-bottom: 2rem;">
    <h2 style="font-weight: 900; color: #f8fafc; font-size: 1.8rem; margin-bottom: 0.5rem;">💻 PLAYER STATS</h2>
    <p style="color: #94a3b8;">서상고 입학 후 자동 장착되는 너의 스탯. 평범한 고등학생과는 시작부터 다르지.</p>
</div>
""", unsafe_allow_html=True)

# 스탯 카드 생성을 위한 헬퍼 함수
def create_stat_card(title, level, percentage, color, icon):
    return f"""
    <div class="stat-card">
        <div class="stat-header">
            <div class="stat-title">{icon} {title}</div>
            <div class="stat-level" style="color: {color};">{level}</div>
        </div>
        <div class="progress-bg">
            <div class="progress-fill" style="width: {percentage}; background-color: {color};"></div>
        </div>
    </div>
    """

# 2단 구성으로 스탯 표시
stat_col1, stat_col2 = st.columns(2)

with stat_col1:
    st.markdown(create_stat_card("프롬프트 엔지니어링", "Lv.99", "95%", "#06b6d4", "🧠"), unsafe_allow_html=True)
    st.markdown(create_stat_card("바이브 코딩 (Vibe Coding)", "Lv.85", "85%", "#a855f7", "⌨️"), unsafe_allow_html=True)

with stat_col2:
    st.markdown(create_stat_card("글로벌 의사소통 (4-Strands)", "Lv.90", "90%", "#3b82f6", "💬"), unsafe_allow_html=True)
    st.markdown(create_stat_card("개념적 탐구력 (IB Style)", "Lv.88", "88%", "#10b981", "⚡"), unsafe_allow_html=True)

st.divider()

st.markdown("""
<div style="text-align: center; margin-bottom: 2rem;">
    <h2 style="font-weight: 900; font-size: 2.2rem; color: #f8fafc; margin-bottom: 0.5rem;">G-NEXT AI CENTER</h2>
    <p style="color: #94a3b8;">상상하는 모든 것이 현실이 되는 두 개의 심장</p>
</div>
""", unsafe_allow_html=True)

# Streamlit 내장 탭 기능 활용
tab1, tab2 = st.tabs(["🧠 아이데이션 존 (Ideation Zone)", "🛠️ 메이커 존 (Maker Zone)"])

with tab1:
    st.markdown("""
    <div style="background-color: #0f172a; padding: 2rem; border-radius: 1rem; border: 1px solid #1e293b;">
        <h3 style="color: #22d3ee; font-weight: 900; font-size: 1.5rem; margin-bottom: 1rem;">아이데이션 존</h3>
        <p style="color: #cbd5e1; font-size: 1.1rem; line-height: 1.6; margin-bottom: 1.5rem;">
            <strong>"생각의 한계를 깨부수는 곳."</strong><br>
            정해진 답을 외우는 대신, AI 튜터와 토론하며 나만의 세계관을 기획해. NotebookLM으로 수천 장의 자료를 1초 만에 분석하고, 거대한 개념(Concept)을 도출하는 진짜 탐구가 시작되는 공간이야.
        </p>
        <div style="color: #94a3b8; display: grid; grid-template-columns: 1fr 1fr; gap: 0.8rem;">
            <div>⚡ AI 기반 브레인스토밍</div>
            <div>⚡ 개념 기반 탐구 토론</div>
            <div>⚡ 스마트 프레젠테이션</div>
            <div>⚡ 데이터 분석 및 리서치</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div style="background-color: #0f172a; padding: 2rem; border-radius: 1rem; border: 1px solid #1e293b;">
        <h3 style="color: #c084fc; font-weight: 900; font-size: 1.5rem; margin-bottom: 1rem;">메이커 존</h3>
        <p style="color: #cbd5e1; font-size: 1.1rem; line-height: 1.6; margin-bottom: 1.5rem;">
            <strong>"머릿속 아이디어를 실물로 뽑아내는 곳."</strong><br>
            자연어로 코딩하는 '바이브 코딩'으로 나만의 앱을 만들고, 생성형 AI로 지브리 스타일의 캐릭터를 디자인해. 3D 프린터와 연동해서 실물 피규어까지! 네가 상상한 모든 것이 눈앞에 나타날 거야.
        </p>
        <div style="color: #94a3b8; display: grid; grid-template-columns: 1fr 1fr; gap: 0.8rem;">
            <div>⚡ Vibe Coding 앱 제작</div>
            <div>⚡ 3D 모델링 및 프린팅</div>
            <div>⚡ 생성형 AI 굿즈 디자인</div>
            <div>⚡ 피지컬 컴퓨팅</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="cta-container">
    <div class="limited-badge">Limited Invitation</div>
    <h2 style="font-size: 2.5rem; font-weight: 900; color: #f8fafc; margin-bottom: 1rem;">지금, 미래로 접속할 시간</h2>
    <p style="color: #94a3b8; font-size: 1.1rem; margin-bottom: 0;">
        단 하루, 서상고 G-NEXT AI 크리에이터 캠프에서 압도적인 에듀테크를 직접 경험해봐.
    </p>
</div>
""", unsafe_allow_html=True)

# 중앙 하단 버튼
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    st.link_button("🚀 캠프 사전예약 하러가기", "https://forms.google.com", use_container_width=True)

# 푸터 영역
st.markdown("""
<div style="text-align: center; color: #64748b; font-size: 0.875rem; margin-top: 4rem; padding-top: 2rem; border-top: 1px solid #1e293b;">
    <p style="font-weight: 700; letter-spacing: 0.1em; margin-bottom: 0.5rem; text-transform: uppercase;">Seosang High School</p>
    <p>미래를 가장 먼저 경험하는 학교. 우리는 결과가 아닌 창조하는 과정을 평가합니다.</p>
</div>
""", unsafe_allow_html=True)
