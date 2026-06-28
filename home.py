import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="서상고등학교 홍보 페이지",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 커스텀 CSS 적용 (Streamlit 기본 UI 숨기기 및 여백 조정)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .hero-section {
        background: linear-gradient(135deg, #1e3a8a 0%, #3730a3 100%);
        color: white;
        padding: 4rem 2rem;
        border-radius: 1rem;
        text-align: center;
        margin-bottom: 3rem;
    }
    .hero-tag {
        background-color: rgba(255,255,255,0.2);
        padding: 0.5rem 1rem;
        border-radius: 2rem;
        font-size: 0.9rem;
        display: inline-block;
        margin-bottom: 1.5rem;
    }
    .card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        height: 100%;
        border: 1px solid #e2e8f0;
    }
    .highlight-text {
        color: #2563eb;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 1. 히어로 섹션
st.markdown("""
<div class="hero-section">
    <div class="hero-tag">🌟 경남 최초 구글 레퍼런스 스쿨</div>
    <h1 style='font-size: 3rem; font-weight: 800; margin-bottom: 1rem; color: white;'>G-NEXT 미래형 인재 양성</h1>
    <p style='font-size: 1.2rem; color: #e0e7ff; max-width: 800px; margin: 0 auto; line-height: 1.6;'>
        1인 1기기 지원, 원어민 외국어 교육, 야간 수능 중점반 운영.<br>
        수행평가 부담 없이 내신 1등급으로 인(IN) 서울을 향해 나아갑니다.
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# 2. 선택 포인트 5가지
st.header("✨ 서상고 선택 포인트 5가지")
st.markdown("한 눈으로 보는 서상고만의 특별한 혜택과 매력을 확인하세요.")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("**🏆 내신 1등급 확보 유리**\n\n수행평가 부담 없이 내신 1등급으로 교과 전형 지원 가능. 대입에 강한 학교!")
    st.success("**🎨 예체능 진로 맞춤 레슨**\n\n예체능 진로 희망 학생들을 위한 1대 1 개인 레슨 지원 (바이올린, 골프 등)")

with col2:
    st.warning("**📚 학생부 종합 전형 대비**\n\n수준 높은 생활 기록부 기재를 통한 완벽한 학생부 종합 전형 대비 체계 구축")
    st.error("**🎁 교육비 ZERO, 혜택 PLUS**\n\n모든 교내외 교육 활동과 교재 무상 지원 및 매년 약 1,500만원 장학금 제공")

with col3:
    st.info("**💻 과목 선택권 완벽 보장**\n\n온라인 공동 교육과정 및 소인수 과목 개설을 통해 학생이 원하는 과목 수강 가능")
    

st.divider()

# 3. 내신 경쟁력 (5등급제 시대)
st.header("🎯 5등급제 시대에 맞는 가장 현명한 선택")
col_adv1, col_adv2 = st.columns([1, 1])

with col_adv1:
    st.markdown("""
    **2025학년도 1학년부터 적용되는 내신 등급제의 변화.**
    아무리 과목 선택이 훌륭해도 내신 1~2등급이 아니라면 인(IN) 서울은 힘듭니다.
    
    <span class='highlight-text' style='font-size: 1.2rem;'>서상고라면, 대입에서 충분히 인(IN) 서울 할 수 있습니다!</span>
    
    * ✅ 소수 정예 운영으로 세심한 개별 맞춤 지도
    * ✅ 최저 등급 충족을 위한 방과후, 야간 수능 중점반 무료 운영 (국/영/수/사/과)
    """, unsafe_allow_html=True)

with col_adv2:
    st.markdown("##### 📊 1년 후 내 위치는 어디일까요?")
    
    st.markdown("**타학교 (100명 기준) - 1등급: 1~10등**")
    st.progress(0.10) # 10%
    
    st.markdown("**서상고 (10명 기준) - 1등급: 1등**")
    st.progress(0.10)
    
    st.caption("집중적인 케어와 전략적인 내신 관리로 1등급 쟁취의 가능성을 높입니다. 치열한 경쟁을 탈피하세요.")

st.divider()

# 4. 장학 및 혜택
st.header("💎 교육비 걱정 ZERO! 혜택 PLUS!")
col_ben1, col_ben2 = st.columns(2)

with col_ben1:
    st.subheader("🎓 100% 무상 지원 항목")
    st.markdown("""
    * **교재/교구비 전액 지원**
      방과후학교, 멘토링 특기적성 수업료 및 3학년 수능특강/완성 등 (일반고 약 24만원 소요)
    * **급식비 전액 지원**
      야간 자기주도학습 석식비 및 방학 중 중식비 100% 지원 (일반고 연간 약 98만원 소요)
    * **체험학습 & 수학여행**
      교내외 진로 및 문화 체험학습 비용과 **해외 수학여행비** 전액 무상 지원
    """)

with col_ben2:
    st.subheader("💰 서상고만의 특별한 장학금")
    st.success("""
    **'성적 향상 지원금'**
    노력하는 만큼 보상을 받습니다! 전국연합학력평가 및 모의수능 등급이 오를 때마다 보상을 주어 자기 주도 학습 역량을 극대화합니다.
    
    **매년 약 1,500만원 장학금 제공**
    학생 한 명 한 명의 노력과 성장을 섬세하게 파악하여 공정하게 보상합니다.
    """)

st.divider()

# 5. 구글 레퍼런스 스쿨
st.header("🌐 Google for Education Reference School")
st.markdown("**AI 디지털 수업 혁신! 미래형 인재 양성**")

col_g1, col_g2, col_g3, col_g4 = st.columns(4)
with col_g1:
    st.info("**Google Workspace**\n\n학생과 교사가 적극 활용하며, Google Classroom 기반 활발한 디지털 학습 진행")
with col_g2:
    st.info("**Chromebooks 2:1**\n\n학교 전체에 크롬북이 최소 2:1 수준 배포되어 제약 없이 디지털 기기 활용")
with col_g3:
    st.info("**G-NEXT 프로그램**\n\n구글코리아 방문, 구글 직원 멘토링 등 미래 인재 육성을 위해 연간 2천만원 지원")
with col_g4:
    st.info("**외국어 교육 강화**\n\n원어민 회화 수업, 방학 영어 캠프, 토익/토플 시험 역량 강화, IB 교원 초청 강연")

st.divider()

# 6. 특화 프로그램 (Tabs)
st.header("🎭 창의·융합 역량 & 공동체 교육")
tab1, tab2 = st.tabs(["🎨 문화와 예술 (Arts & Sports)", "🌍 글로벌 & 공동체 (Global & Community)"])

with tab1:
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.markdown("""
        * 🎻 **1인 1바이올린 연주:** 음악 시간 활용 1:1 교육 및 단위 학교 지원 사업(1천만원) 개인 레슨
        * ⛳ **'미래의 박세리' 골프 레슨:** 교내 시설 및 인근 연습장 레슨, 필드 경기 경험 제공
        * 📖 **지혜의 숲 독서 탐방:** 고전 소설 문학관 방문 등 인문 소양 함양 프로젝트
        """)
    with col_t2:
        st.markdown("""
        * 🎶 **전문가 협연 예술 콘서트:** 문화예술교육 격차 해소를 위해 전문가와 학생이 함께 연주
        * 🎬 **공감과 소통의 연극/뮤지컬:** 4~5일간의 연극 캠프 및 뮤지컬 직접 관람
        * ⚾ **사제동행 스포츠 체험:** 야구, 농구 등 관람을 통해 감성을 키우고 즐거움을 나누는 활동
        """)

with tab2:
    col_t3, col_t4 = st.columns(2)
    with col_t3:
        st.markdown("#### ✈️ 글로벌 역량 강화")
        st.markdown("""
        * **일본 해외 수학여행 전액 지원:** 오사카, 교토, 나라 등 타문화 이해 및 국제적 소양 함양
        * **대학 탐방 프로그램:** 진로를 주도적으로 설계하고 학문적 동기를 고취하는 내일 그리기 발걸음
        """)
    with col_t4:
        st.markdown("#### 🤝 공동체 역량 강화")
        st.markdown("""
        * **마음을 버무리는 김장 나눔:** 학생들이 직접 김장을 담가 지역 사회에 전달
        * **지속가능한 내일을 가꾸는 텃밭:** 자연과 소통하며 생명의 순환을 체험
        * **사제동행 체육대회 & 송림제(축제):** 상호 이해와 존중, 협력의 가치를 실천
        """)

st.divider()

# 7. 시설 안내
st.header("🏫 최고의 교육 환경, 서상고 시설안내")
facilities = [
    "VR 체험실", "개인 학습실", "교내 노래방", "교실내 탈의실", "공기청정기 완비", 
    "온라인 학습실", "탁구실", "음악실", "약품샤워실", "천체망원경", 
    "도서실", "진로진학실", "체육관", "학습카페", "교내 골프장", 
    "솔숲 전경", "숲속 작은 도서관", "블루베리/텃밭/비닐하우스"
]

# 태그 스타일로 나열
html_tags = "".join([f"<span style='display:inline-block; background:#f1f5f9; padding:0.4rem 0.8rem; margin:0.2rem; border-radius:1rem; font-size:0.9rem; color:#334155; border:1px solid #cbd5e1;'>{f}</span>" for f in facilities])
st.markdown(f"<div style='text-align:center;'>{html_tags}</div>", unsafe_allow_html=True)

st.divider()

# 8. 푸터
st.markdown("""
<div style='text-align: center; color: #64748b; padding: 2rem 0;'>
    <h3>서상고등학교 (SEOSANG HIGH SCHOOL)</h3>
    <p>📍 50003 경남 함양군 서상면 서상로 232-1<br>
    📞 교무실: 055-963-0305 | 행정실: 055-962-8835<br>
    🌐 <a href="http://seosang-h.gne.go.kr" target="_blank">http://seosang-h.gne.go.kr</a></p>
    <p style='margin-top: 1rem; font-weight: bold; color: #2563eb;'>2026학년도 신입생 모집 - 당신의 성장이 더 빛날 기회, 서상고등학교와 함께하세요.</p>
</div>
""", unsafe_allow_html=True)
