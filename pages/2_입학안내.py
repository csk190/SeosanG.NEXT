import streamlit as st

st.set_page_config(
    page_title="입학안내 | 서상고등학교",
    page_icon="🏫",
    layout="wide",
)

# ── 전역 스타일 ──────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Noto Sans KR', sans-serif;
    background-color: #020617;
    color: #f8fafc;
}
.block-container { padding-top: 2rem; padding-bottom: 4rem; max-width: 860px; }

/* 공통 */
.grad { background: linear-gradient(90deg,#22d3ee,#3b82f6,#a855f7);
        -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.badge {
    display:inline-block; padding:4px 14px; border-radius:999px;
    border:1px solid rgba(34,211,238,0.35); background:rgba(34,211,238,0.1);
    color:#22d3ee; font-size:12px; font-weight:700; letter-spacing:.1em;
    text-transform:uppercase; margin-bottom:14px;
}

/* 히어로 */
.hero { text-align:center; padding: 48px 0 32px; }
.hero h1 { font-size:clamp(28px,5vw,48px); font-weight:900;
            line-height:1.2; margin-bottom:16px; letter-spacing:-.03em; }
.hero p  { color:#94a3b8; font-size:16px; line-height:1.8;
            max-width:600px; margin:0 auto; }

/* 섹션 헤더 */
.sec-header { display:flex; align-items:center; gap:10px; margin-bottom:6px; }
.sec-header h2 { font-size:22px; font-weight:900; }
.sec-sub { color:#64748b; font-size:13px; margin-bottom:24px; }

/* 일정 타임라인 */
.timeline { position:relative; padding-left:28px; margin-top:8px; }
.timeline::before {
    content:""; position:absolute; left:8px; top:0; bottom:0;
    width:2px; background:linear-gradient(180deg,#22d3ee,#a855f7);
    border-radius:999px;
}
.tl-item { position:relative; margin-bottom:20px; }
.tl-dot {
    position:absolute; left:-24px; top:4px;
    width:12px; height:12px; border-radius:50%;
    background:#22d3ee; border:2px solid #020617;
    box-shadow:0 0 8px #22d3ee88;
}
.tl-card {
    background:#0f172a; border:1px solid #1e293b;
    border-radius:12px; padding:14px 18px;
}
.tl-date { color:#22d3ee; font-size:12px; font-weight:700;
            letter-spacing:.05em; margin-bottom:4px; }
.tl-title { font-size:15px; font-weight:700; color:#e2e8f0; margin-bottom:4px; }
.tl-desc  { color:#64748b; font-size:13px; line-height:1.6; }

/* 정보 카드 */
.info-grid { display:grid; grid-template-columns:1fr 1fr; gap:14px; }
.info-card {
    background:#0f172a; border:1px solid #1e293b;
    border-radius:14px; padding:18px 20px;
    transition: border-color .2s;
}
.info-card:hover { border-color:#334155; }
.info-label { color:#94a3b8; font-size:12px; font-weight:700;
               letter-spacing:.05em; text-transform:uppercase; margin-bottom:6px; }
.info-value { font-size:18px; font-weight:900; color:#f1f5f9; }
.info-sub   { color:#64748b; font-size:12px; margin-top:4px; }

/* 제출 서류 */
.doc-list { display:flex; flex-direction:column; gap:10px; }
.doc-item {
    display:flex; align-items:flex-start; gap:12px;
    background:#0f172a; border:1px solid #1e293b;
    border-radius:12px; padding:14px 16px;
}
.doc-num {
    min-width:26px; height:26px; border-radius:50%;
    background:rgba(34,211,238,.15); color:#22d3ee;
    font-size:12px; font-weight:900;
    display:flex; align-items:center; justify-content:center;
}
.doc-name  { font-size:14px; font-weight:700; color:#e2e8f0; }
.doc-note  { color:#64748b; font-size:12px; margin-top:3px; }

/* 전형 유형 탭 */
.type-grid { display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:20px; }
.type-card {
    border-radius:16px; border:2px solid #1e293b;
    background:#0f172a; padding:20px; cursor:pointer;
    transition: all .2s;
}
.type-card.active { border-color:#22d3ee; background:rgba(34,211,238,.07); }
.type-card h3 { font-size:16px; font-weight:900; margin-bottom:6px; }
.type-card p  { color:#64748b; font-size:13px; line-height:1.6; }

/* 특색 프로그램 */
.prog-grid { display:grid; grid-template-columns:1fr 1fr; gap:12px; }
.prog-card {
    background:#0f172a; border:1px solid #1e293b;
    border-radius:14px; padding:18px;
}
.prog-icon { font-size:28px; margin-bottom:10px; }
.prog-title { font-size:15px; font-weight:700; color:#e2e8f0; margin-bottom:6px; }
.prog-desc  { color:#64748b; font-size:13px; line-height:1.6; }

/* 문의 */
.contact-box {
    background:#0f172a; border:1px solid rgba(34,211,238,.2);
    border-radius:20px; padding:32px; text-align:center;
}
.contact-box h3 { font-size:20px; font-weight:900; margin-bottom:8px; }
.contact-box p  { color:#94a3b8; font-size:14px; margin-bottom:20px; }
.contact-grid { display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; }
.contact-item {
    background:#020617; border:1px solid #1e293b;
    border-radius:12px; padding:14px;
}
.contact-label { color:#64748b; font-size:11px; font-weight:700;
                  text-transform:uppercase; letter-spacing:.05em; margin-bottom:6px; }
.contact-value { font-size:14px; font-weight:700; color:#e2e8f0; }

/* divider */
.divider { border:none; border-top:1px solid #1e293b; margin:32px 0; }

/* CTA */
.cta-wrap {
    border:1px solid rgba(34,211,238,.2); background:rgba(8,47,73,.3);
    border-radius:24px; padding:40px 32px; text-align:center; position:relative;
    margin-top:16px;
}
.cta-pill {
    display:inline-block; background:#06b6d4; color:#020617;
    font-size:11px; font-weight:900; padding:4px 16px;
    border-radius:999px; text-transform:uppercase; letter-spacing:.05em;
    margin-bottom:20px;
}
.cta-wrap h2 { font-size:clamp(20px,3vw,28px); font-weight:900; margin-bottom:10px; }
.cta-wrap p  { color:#94a3b8; font-size:15px; margin-bottom:0; }
</style>
""", unsafe_allow_html=True)

# ── 히어로 ────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="badge">2027 Admission Guide</div>
  <h1>서상고등학교<br><span class="grad">입학안내</span></h1>
  <p>미래를 설계하는 첫 번째 선택.<br>
     지원 자격부터 전형 일정, 제출 서류까지 한눈에 확인하세요.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ── 모집 현황 ─────────────────────────────────────────────────
st.markdown("""
<div class="sec-header"><span style="color:#22d3ee">📊</span><h2>모집 현황</h2></div>
<p class="sec-sub">2027학년도 신입생 모집 인원</p>
<div class="info-grid">
  <div class="info-card">
    <div class="info-label">모집 학급</div>
    <div class="info-value">1 <span style="font-size:14px;color:#64748b">학급</span></div>
    <div class="info-sub">일반고 과정</div>
  </div>
  <div class="info-card">
    <div class="info-label">모집 인원</div>
    <div class="info-value">10명 이내</div>
    <div class="info-sub">소인수 맞춤형 교육</div>
  </div>
  <div class="info-card">
    <div class="info-label">지원 자격</div>
    <div class="info-value" style="font-size:15px">중학교 졸업(예정)자</div>
    <div class="info-sub">해당 학구 내 거주자 우선</div>
  </div>
  <div class="info-card">
    <div class="info-label">모집 지역</div>
    <div class="info-value" style="font-size:15px">경상남도 일원</div>
    <div class="info-sub">타 지역 지원 가능 (결원 시)</div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ── 전형 유형 ─────────────────────────────────────────────────
st.markdown("""
<div class="sec-header"><span style="color:#a855f7">🎯</span><h2>전형 유형</h2></div>
<p class="sec-sub">지원자의 상황에 맞는 전형을 선택하세요</p>
<div class="type-grid">
  <div class="type-card active">
    <h3 style="color:#22d3ee">일반 전형</h3>
    <p>중학교 내신 성적을 중심으로 선발하는 기본 전형입니다. 성적 우수 학생에게 유리합니다.</p>
  </div>
  <div class="type-card">
    <h3 style="color:#a855f7">특별 전형</h3>
    <p>사회통합대상자, 다문화가정, 특수교육 대상자 등을 위한 별도 전형입니다.</p>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ── 전형 일정 ─────────────────────────────────────────────────
st.markdown("""
<div class="sec-header"><span style="color:#22d3ee">📅</span><h2>전형 일정</h2></div>
<p class="sec-sub">2027학년도 신입생 전형 주요 일정</p>
<div class="timeline">
  <div class="tl-item">
    <div class="tl-dot"></div>
    <div class="tl-card">
      <div class="tl-date">2026. 12. 10 (목) ~ 12. 14 (월)</div>
      <div class="tl-title">원서 접수</div>
      <div class="tl-desc">학교 행정실 방문 또는 온라인 접수 — 마감일 17:00까지</div>
    </div>
  </div>
  <div class="tl-item">
    <div class="tl-dot" style="background:#3b82f6; box-shadow:0 0 8px #3b82f688;"></div>
    <div class="tl-card">
      <div class="tl-date" style="color:#3b82f6">2026. 12. 15 (화) ~ 12. 23 (수)</div>
      <div class="tl-title">전형 실시</div>
      <div class="tl-desc">서류 심사 및 학교별 전형 진행</div>
    </div>
  </div>
  <div class="tl-item">
    <div class="tl-dot" style="background:#a855f7; box-shadow:0 0 8px #a855f788;"></div>
    <div class="tl-card">
      <div class="tl-date" style="color:#a855f7">2026. 12. 30 (수)</div>
      <div class="tl-title">합격자 발표</div>
      <div class="tl-desc">학교 홈페이지 및 개별 통보</div>
    </div>
  </div>
  <div class="tl-item">
    <div class="tl-dot" style="background:#10b981; box-shadow:0 0 8px #10b98188;"></div>
    <div class="tl-card">
      <div class="tl-date" style="color:#10b981">2027. 02. 初</div>
      <div class="tl-title">입학 등록</div>
      <div class="tl-desc">합격자 등록금 납부 및 서류 제출</div>
    </div>
  </div>
  <div class="tl-item">
    <div class="tl-dot" style="background:#f59e0b; box-shadow:0 0 8px #f59e0b88;"></div>
    <div class="tl-card">
      <div class="tl-date" style="color:#f59e0b">2027. 03. 02 (월)</div>
      <div class="tl-title">입학식</div>
      <div class="tl-desc">서상고등학교 대강당 — 09:00</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ── 제출 서류 ─────────────────────────────────────────────────
st.markdown("""
<div class="sec-header"><span style="color:#22d3ee">📋</span><h2>제출 서류</h2></div>
<p class="sec-sub">원서 접수 시 아래 서류를 모두 제출하세요</p>
<div class="doc-list">
  <div class="doc-item">
    <div class="doc-num">1</div>
    <div>
      <div class="doc-name">입학원서</div>
      <div class="doc-note">소정 양식 (학교 행정실 또는 홈페이지 다운로드)</div>
    </div>
  </div>
  <div class="doc-item">
    <div class="doc-num">2</div>
    <div>
      <div class="doc-name">중학교 학교생활기록부 사본</div>
      <div class="doc-note">출신 중학교 발급 — 직인 날인 필수</div>
    </div>
  </div>
  <div class="doc-item">
    <div class="doc-num">3</div>
    <div>
      <div class="doc-name">졸업(예정)증명서</div>
      <div class="doc-note">졸업예정자는 재학증명서로 대체 가능</div>
    </div>
  </div>
  <div class="doc-item">
    <div class="doc-num">4</div>
    <div>
      <div class="doc-name">주민등록등본 (또는 가족관계증명서)</div>
      <div class="doc-note">발급 후 3개월 이내 서류 / 주소지 확인용</div>
    </div>
  </div>
  <div class="doc-item">
    <div class="doc-num">5</div>
    <div>
      <div class="doc-name">사진 2매</div>
      <div class="doc-note">최근 3개월 이내 촬영 (3×4cm)</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
> ⚠️ **특별전형 지원자**는 해당 자격을 증빙하는 서류를 추가 제출해야 합니다. 자세한 사항은 행정실로 문의하세요.
""")

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ── 특색 프로그램 ──────────────────────────────────────────────
st.markdown("""
<div class="sec-header"><span style="color:#a855f7">✨</span><h2>입학 후 특색 프로그램</h2></div>
<p class="sec-sub">서상고에서만 경험할 수 있는 미래형 교육</p>
<div class="prog-grid">
  <div class="prog-card">
    <div class="prog-icon">🤖</div>
    <div class="prog-title">G-NEXT AI 크리에이터 과정</div>
    <div class="prog-desc">프롬프트 엔지니어링부터 바이브 코딩까지 — AI 도구를 자유자재로 다루는 역량을 키웁니다.</div>
  </div>
  <div class="prog-card">
    <div class="prog-icon">🌐</div>
    <div class="prog-title">글로벌 영어 집중 교육</div>
    <div class="prog-desc">4-Strands 기반 영어 수업으로 실질적인 의사소통 능력을 기릅니다.</div>
  </div>
  <div class="prog-card">
    <div class="prog-icon">🔬</div>
    <div class="prog-title">IB 스타일 개념 탐구</div>
    <div class="prog-desc">정답을 외우는 대신, 스스로 질문하고 탐구하는 개념 중심 수업을 운영합니다.</div>
  </div>
  <div class="prog-card">
    <div class="prog-icon">🏭</div>
    <div class="prog-title">메이커 스페이스 운영</div>
    <div class="prog-desc">3D 프린터, 피지컬 컴퓨팅, AI 굿즈 디자인까지 아이디어를 실물로 만드는 공간입니다.</div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ── 문의처 ─────────────────────────────────────────────────────
st.markdown("""
<div class="contact-box">
  <h3>📞 입학 문의</h3>
  <p>궁금한 점은 언제든지 문의해주세요.</p>
  <div class="contact-grid">
    <div class="contact-item">
      <div class="contact-label">대표전화</div>
      <div class="contact-value">055-963-0305</div>
    </div>
    <div class="contact-item">
      <div class="contact-label">팩스</div>
      <div class="contact-value">055-963-5380</div>
    </div>
    <div class="contact-item">
      <div class="contact-label">운영 시간</div>
      <div class="contact-value">평일 09:00 ~ 17:00</div>
    </div>
  </div>
  <div style="margin-top:16px; display:flex; flex-direction:column; gap:10px;">
    <div class="contact-item" style="text-align:left; display:flex; align-items:flex-start; gap:10px;">
      <div style="color:#22d3ee; font-size:16px; margin-top:2px;">📍</div>
      <div>
        <div class="contact-label">주소</div>
        <div class="contact-value" style="font-size:13px;">경상남도 함양군 서상면 서상로 232-1</div>
      </div>
    </div>
    <div class="contact-item" style="text-align:left; display:flex; align-items:flex-start; gap:10px;">
      <div style="color:#22d3ee; font-size:16px; margin-top:2px;">🌐</div>
      <div>
        <div class="contact-label">홈페이지</div>
        <div class="contact-value" style="font-size:13px;">
          <a href="http://seosang-h.gne.go.kr/seosang-h/main.do" target="_blank"
             style="color:#22d3ee; text-decoration:none;">seosang-h.gne.go.kr</a>
        </div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ── CTA ────────────────────────────────────────────────────────
st.markdown("""
<div class="cta-wrap">
  <div class="cta-pill">2027 지금 바로 신청</div>
  <h2>미래를 가장 먼저 경험하는 학교,<br>서상고등학교에서 만나요.</h2>
  <p style="margin-top:12px; color:#94a3b8">원서 접수 마감까지 D-Day를 놓치지 마세요!</p>
</div>
""", unsafe_allow_html=True)
