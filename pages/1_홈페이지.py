import streamlit as st

# 커스텀 CSS 적용 (Streamlit 기본 UI 숨기기 및 여백 조정)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    /* header {visibility: hidden;} <- 이 줄을 삭제하여 > 버튼이 있는 상단바가 보이게 합니다 */
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
    .highlight-text {
        color: #2563eb;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

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

st.header("✨ 서상고 선택 포인트 5가지")
st.markdown("한 눈으로 보는 서상고만의 특별한 혜택과 매력을 확인하세요.")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("**🏆 내신 1등급 확보 유리**\n\n수행평가 부담 없이 내신 1등급으로 교과 전형 지원 가능. 대입에 강한 학교!")
    st.success("**🎨 예체능 진로 맞춤 레슨**\n\n예체능 진로 희망 학생들을 위한 1대 1 개인 레슨 지원")

with col2:
    st.warning("**📚 학생부 종합 전형 대비**\n\n수준 높은 생활 기록부 기재를 통한 완벽한 학생부 종합 전형 대비")
    st.error("**🎁 교육비 ZERO, 혜택 PLUS**\n\n모든 교내외 교육 활동과 교재 무상 지원 및 장학금 제공")

with col3:
    st.info("**💻 과목 선택권 완벽 보장**\n\n온라인 공동 교육과정 및 소인수 과목 개설로 원하는 과목 수강")

st.divider()

st.header("🎯 5등급제 시대에 맞는 가장 현명한 선택")
col_adv1, col_adv2 = st.columns([1, 1])

with col_adv1:
    st.markdown("""
    **2025학년도 1학년부터 적용되는 내신 등급제의 변화.**
    <br><span class='highlight-text' style='font-size: 1.2rem;'>서상고라면, 대입에서 충분히 인(IN) 서울 할 수 있습니다!</span>
    
    * ✅ 소수 정예 운영으로 세심한 개별 맞춤 지도
    * ✅ 최저 등급 충족을 위한 야간 수능 중점반 무료 운영
    """, unsafe_allow_html=True)

with col_adv2:
    st.markdown("##### 📊 1년 후 내 위치는 어디일까요?")
    st.markdown("**타학교 (100명 기준) - 1등급: 1~10등**")
    st.progress(0.10)
    st.markdown("**서상고 (10명 기준) - 1등급: 1등**")
    st.progress(0.10)

st.divider()

st.header("💎 교육비 걱정 ZERO! 혜택 PLUS!")
st.success("**매년 약 1,500만원 장학금 제공 및 교재/급식/해외수학여행 무상 지원**")

st.divider()

st.header("🏫 서상고 시설안내")
facilities = ["VR 체험실", "개인 학습실", "교내 노래방", "교실내 탈의실", "공기청정기 완비", "온라인 학습실", "탁구실", "천체망원경", "학습카페", "교내 골프장"]
html_tags = "".join([f"<span style='display:inline-block; background:#f1f5f9; padding:0.4rem 0.8rem; margin:0.2rem; border-radius:1rem; font-size:0.9rem; color:#334155; border:1px solid #cbd5e1;'>{f}</span>" for f in facilities])
st.markdown(f"<div style='text-align:center;'>{html_tags}</div>", unsafe_allow_html=True)

st.divider()

st.markdown("""
<div style='text-align: center; color: #64748b; padding: 2rem 0;'>
    <h3>서상고등학교 (SEOSANG HIGH SCHOOL)</h3>
    <p>📍 경남 함양군 서상면 서상로 232-1 | 📞 055-963-0305</p>
</div>
""", unsafe_allow_html=True)
