# 메인 페이지 — 허브 역할. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

# 실제 오프라인 사업장 주소가 없는 방문형 사이트이므로 LocalBusiness 대신
# Organization + WebPage + FAQPage 스키마만 사용한다.
_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "telephone": "{PHONE}",
  "url": "{BASE_URL}/",
  "logo": "{BASE_URL}/assets/og-image.png",
  "image": "{BASE_URL}/assets/og-image.png",
  "description": "중랑구 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "서울특별시 중랑구"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "중랑구 출장마사지 · 중랑구 홈타이 지역별 예약 안내",
  "url": "{BASE_URL}/",
  "primaryImageOfPage": {{
    "@type": "ImageObject",
    "url": "{BASE_URL}/assets/og-image.png",
    "width": 1200,
    "height": 630
  }},
  "breadcrumb": {{
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "홈", "item": "{BASE_URL}/" }}
    ]
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "중랑구 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 면목동, 상봉동, 중화동, 묵동, 망우동, 신내동 대표동 안내 페이지에서 생활권별로 확인할 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "상봉역이나 면목역 근처도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "면목역, 사가정역, 상봉역, 망우역, 신내역 등 주요 역세권은 역 상세 페이지에서 인접 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "면목2동, 상봉1동처럼 번호 동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "면목본동·면목2~7동은 면목동, 상봉1·2동은 상봉동처럼 번호 행정동은 대표동 페이지에서 통합 안내하여 중복 페이지 위험을 줄입니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "출장마사지와 홈타이는 어떻게 다른가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "두 가지 모두 자택·숙소·사무실 인근으로 방문하는 관리 방식입니다. 차이와 이용 기준은 홈타이 이용 가이드에서 확인할 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "당일 예약도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "가능할 수 있지만 저녁 시간대와 주말은 문의가 많을 수 있어 사전 예약을 권장합니다. 신내동, 망우동 등 차량 이동 기준이 중요한 지역은 여유를 두고 연락 주세요."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 중랑구 전지역</p>
    <h1>중랑구 출장마사지 · 홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 프리미엄 방문 관리.<br>면목·상봉·중화·묵·망우·신내동 어디든 전화 한 통이면 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/seoul/jungnang-gu/">지역별 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>6개</strong><span>대표 지역</span></li>
      <li><strong>11개</strong><span>역세권 안내</span></li>
      <li><strong>10개</strong><span>생활권 안내</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="standard">
<h2>중랑구에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
<p>중랑구 출장마사지를 찾는 분들은 보통 현재 위치에서 가까운 방문 가능 지역을 먼저 확인합니다. {BRAND}는 단순히 “중랑 전지역 가능”이라고만 안내하지 않고, 대표동과 역세권, 생활권을 나누어 방문 가능 여부와 예약 전 확인사항을 정리합니다. 예약 전에는 방문 가능 지역, 예약 가능 시간, 추가 이동비 여부, 결제 방식, 취소 기준, 개인정보 처리 기준을 먼저 확인하시는 것이 좋습니다. 이 페이지는 중랑구 전체 구조를 설명하는 허브 역할을 하며, 더 자세한 내용은 <a href="/seoul/jungnang-gu/">중랑구 지역별 안내</a>, <a href="/seoul/jungnang-gu/station/">역세권 안내</a>, <a href="/seoul/jungnang-gu/area/">생활권 안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="lifezone">
<h2>면목·상봉·망우·신내 생활권 차이</h2>
<p>중랑구는 서울 동북권에 있는 자치구로, 면목동을 중심으로 한 주거 생활권, 상봉역과 망우역을 중심으로 한 교통 생활권, 중화동과 묵동의 지하철 7호선 생활권, 신내동과 망우동의 북동쪽 주거 생활권이 함께 있는 지역입니다. 같은 중랑구라도 생활권마다 주거 형태와 이동 동선이 달라, 방문 시간대나 공간 준비, 추가 이동비 기준이 조금씩 다릅니다. 면목동은 면목역·사가정역·용마산역 생활권, 상봉동은 상봉터미널·상봉역 교통 생활권, 묵동은 먹골역·봉화산 생활권, 신내동은 신내역·봉화산역 주거 생활권으로 이해하면 본인에게 맞는 페이지를 빠르게 찾을 수 있습니다. 생활권 단위 안내는 <a href="/seoul/jungnang-gu/area/">중랑구 생활권별 방문 관리 안내</a>에서 이동 동선 기준으로 정리했습니다.</p>
</section>

<section id="areas">
<h2>대표동별 방문 가능 지역 안내</h2>
<p>중랑구 지역 안내는 면목동, 상봉동, 중화동, 묵동, 망우동, 신내동 여섯 개 대표동을 중심으로 구성합니다. 면목본동·면목2·3·8·4·5·7동, 상봉1·2동, 중화1·2동, 묵1·2동, 망우본동·망우3동, 신내1·2동처럼 번호로 나뉜 행정동은 별도 페이지를 만들지 않고 각 대표동 페이지에서 통합해 세부 생활권으로 설명합니다. 같은 생활권을 잘게 쪼개 비슷한 내용을 반복하기보다, 동 단위로 묶어 방문 조건을 한 번에 안내하는 편이 이용자에게도 정확하기 때문입니다.</p>
<ul class="card-grid">
<li><a href="/seoul/jungnang-gu/myeonmok-dong/">면목동</a></li>
<li><a href="/seoul/jungnang-gu/sangbong-dong/">상봉동</a></li>
<li><a href="/seoul/jungnang-gu/junghwa-dong/">중화동</a></li>
<li><a href="/seoul/jungnang-gu/muk-dong/">묵동</a></li>
<li><a href="/seoul/jungnang-gu/mangu-dong/">망우동</a></li>
<li><a href="/seoul/jungnang-gu/sinnae-dong/">신내동</a></li>
</ul>
<p>면목동은 중랑구 안에서도 검색 의도가 가장 넓은 대표 페이지로, <a href="/seoul/jungnang-gu/myeonmok-dong/">면목역·사가정역 인근 방문 관리 안내</a>를 한눈에 확인할 수 있습니다. 행정 구역 정보가 더 궁금하시면 <a href="https://www.jungnang.go.kr" target="_blank" rel="noopener nofollow">중랑구청 공식 홈페이지</a>도 참고하실 수 있습니다.</p>
</section>

<section id="stations">
<h2>상봉역·망우역·면목역·신내역 역세권 안내</h2>
<p>역세권 안내는 중랑구를 지나는 7호선·6호선·경의중앙선·경춘선 주요 역을 기준으로 구성합니다. 각 역 페이지에서는 인근 생활권, 주변 대표동, 예약 가능 시간, 방문 전 준비사항을 설명하며, 출구별 페이지나 노선별 페이지는 만들지 않습니다. 상봉역, 망우역, 신내역처럼 환승·광역철도 성격이 있는 역도 역명 기준 1개 페이지로만 운영합니다.</p>
<ul class="card-grid">
<li><a href="/seoul/jungnang-gu/station/myeonmok-station/">면목역</a></li>
<li><a href="/seoul/jungnang-gu/station/sagajeong-station/">사가정역</a></li>
<li><a href="/seoul/jungnang-gu/station/yongmasan-station/">용마산역</a></li>
<li><a href="/seoul/jungnang-gu/station/sangbong-station/">상봉역</a></li>
<li><a href="/seoul/jungnang-gu/station/mangu-station/">망우역</a></li>
<li><a href="/seoul/jungnang-gu/station/jungnang-station/">중랑역</a></li>
<li><a href="/seoul/jungnang-gu/station/junghwa-station/">중화역</a></li>
<li><a href="/seoul/jungnang-gu/station/meokgol-station/">먹골역</a></li>
<li><a href="/seoul/jungnang-gu/station/bonghwasan-station/">봉화산역</a></li>
<li><a href="/seoul/jungnang-gu/station/sinnae-station/">신내역</a></li>
<li><a href="/seoul/jungnang-gu/station/yangwon-nearby-area/">양원역 인접 생활권</a></li>
</ul>
</section>

<section id="check">
<h2>중랑구 홈타이 예약 전 확인사항</h2>
<p>중랑구 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 확인한 뒤 이용하는 방문형 관리 서비스입니다. 상봉역과 면목역처럼 접근성이 좋은 지역도 있지만, 신내동, 망우동, 용마산 인접 지역은 시간대에 따라 차량 이동 기준이 달라질 수 있습니다. 그래서 예약 전에는 정확한 도로명 주소, 공동현관 출입 방법, 조용한 공간 확보 여부, 예약 가능 시간대를 함께 확인해 주시면 좋습니다. 출장마사지와 홈타이의 차이, 처음 이용하는 분을 위한 기준은 <a href="/guide/#hometai">중랑구 홈타이 이용 가이드</a>에서, 예약 절차와 추가 이동비 안내는 <a href="/reservation/">예약안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="dedupe">
<h2>중랑구 페이지 중복 방지 운영 기준</h2>
<p>{BRAND}는 검색 순위를 위해 비슷한 페이지를 양산하지 않습니다. 면목역 페이지와 면목동 페이지는 역할을 다르게 작성하고, 상봉역 페이지와 상봉동 페이지는 동일한 본문을 쓰지 않습니다. 역세권 페이지는 이동 동선과 환승 특징을, 대표동 페이지는 주거 생활권과 방문 조건을 중심으로 설명합니다. 또한 태릉입구역은 노원구 성격이 강해, 아차산역은 광진구 성격이 강해 중랑구 핵심 역세권으로 만들지 않으며, 양원역은 망우동·신내동 인접 생활권으로만 안내합니다. 행정동 경계가 아니라 실제 주소와 예약 시간으로 방문 가능 여부를 판단하므로, 어느 페이지로 들어오셔도 예약 기준은 동일합니다.</p>
</section>

<section id="how">
<h2>중랑구 출장마사지 사이트 이용 방법</h2>
<p>이용 방법은 간단합니다. 먼저 거주하시거나 머무시는 <a href="/seoul/jungnang-gu/">대표동</a> 또는 <a href="/seoul/jungnang-gu/station/">가까운 역</a>을 확인하고, 원하시는 관리 유형은 <a href="/themes/">테마별 안내</a>와 <a href="/courses/">코스안내</a>에서 고른 뒤, 예약 전화로 위치와 희망 시간을 알려주시면 됩니다. 처음 이용하시는 분은 <a href="/guide/">이용가이드</a>의 준비사항을, 위생·안전 기준과 금지행위 안내는 <a href="/guide/#hygiene">위생·안전 기준</a>을 함께 확인해 주세요. 사이트 전체는 정보형 안내 톤을 유지하며, 불법·선정적 표현이나 허위 후기는 사용하지 않습니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>중랑구 전지역 방문이 가능한가요?</h3>
<p>예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 면목동, 상봉동, 중화동, 묵동, 망우동, 신내동 대표동 안내에서 생활권별로 확인할 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>상봉역이나 면목역 근처도 가능한가요?</h3>
<p>면목역, 사가정역, 상봉역, 망우역, 신내역 등 주요 역세권은 역 상세 페이지에서 인접 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다.</p>
</div>
<div class="faq-item">
<h3>면목2동, 상봉1동처럼 번호 동은 왜 따로 없나요?</h3>
<p>면목본동·면목2~7동은 면목동, 상봉1·2동은 상봉동처럼 번호 행정동은 대표동 페이지에서 통합 안내하여 중복 페이지 위험을 줄입니다.</p>
</div>
<div class="faq-item">
<h3>출장마사지와 홈타이는 어떻게 다른가요?</h3>
<p>두 가지 모두 자택·숙소·사무실 인근으로 방문하는 관리 방식입니다. 차이와 이용 기준은 <a href="/guide/#hometai">홈타이 이용 가이드</a>에서 확인할 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>당일 예약도 가능한가요?</h3>
<p>가능할 수 있지만 저녁 시간대와 주말은 문의가 많을 수 있어 사전 예약을 권장합니다. 신내동, 망우동처럼 차량 이동 기준이 중요한 지역은 여유를 두고 연락 주세요.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>중랑구 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "중랑구 출장마사지｜면목·상봉·망우·신내 홈타이 지역 안내",
    "desc": "중랑구 출장마사지·홈타이 예약 전 면목동, 상봉동, 망우동, 신내동, 중화동 생활권을 확인하세요.",
    "h1": "중랑구 출장마사지 · 중랑구 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
