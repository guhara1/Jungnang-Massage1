# 바로GO — 중랑 출장마사지·홈타이 안내 사이트

중랑구 전지역 방문 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
상호: **바로GO** / 예약전화: **0508-202-4719**

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함

```
build.py            # 빌드 스크립트 (레이아웃·글자수 검사·sitemap 생성)
content/
  site.py           # 상호·전화·BASE_URL·메뉴 구조
  main.py           # 메인 페이지 (+ Organization/WebPage/FAQPage JSON-LD)
  areas.py          # 지역별: 중랑구 허브 + 대표 동 6개 + 생활권 허브 + 생활권 10개
  stations.py       # 역세권: 허브 + 11개 역
  themes.py         # 테마별: 허브 + 14개 테마
  info.py           # 출장마사지 안내·코스·예약·가이드·후기·고객센터·약관
assets/             # CSS, 모바일 내비 JS
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다.

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 지역은 대표 동 6개만 (면목·상봉·중화·묵·망우·신내동) — 숫자 행정동 페이지 없음
- 역은 역 1개당 페이지 1개 — 환승역도 URL 하나, 출구별 페이지 없음
- **지역+역+테마 조합 페이지 없음** (도어웨이 방지) — 테마는 독립 페이지로만 운영
- 상단/하위 메뉴와 푸터에 키워드·지역명·역명 대량 나열 없음
- 모든 페이지 본문은 페이지별 고유 작성 (지역명만 바꾼 복붙 없음)

## 색인·인덱싱 (네이버·구글·빙)

빌드(`python3 build.py`) 시 자동 생성되는 색인 자산:

| 파일 | 용도 |
| --- | --- |
| `sitemap.xml` | XML 사이트맵 (`lastmod`·`changefreq` 포함) |
| `rss.xml` | RSS 사이트맵 — 검색엔진 발견용, `<head>`에 alternate 링크 |
| `robots.txt` | Yeti(네이버)·Daumoa(다음)·Bingbot·Googlebot 허용 + 두 사이트맵 노출 |
| `<INDEXNOW_KEY>.txt` | IndexNow 소유권 증명 키 파일 (루트) |
| 메인 `<meta name="naver-site-verification">` | 네이버 서치어드바이저 사이트 등록 |

### 즉시 색인 통보 (IndexNow → Bing·Yandex·Seznam·**Naver**)

```bash
python3 build.py            # 사이트맵·키파일 생성
# (배포 후) 키 파일이 https://도메인/<KEY>.txt 로 200 응답하는지 확인
python3 tools/indexnow.py   # 전체 URL 일괄 통보
python3 tools/indexnow.py https://도메인/magazine/새글/   # 글 1건 통보
```

글을 올릴 때마다 `tools/indexnow.py <URL>` 한 줄이면 빙·네이버에 즉시 색인 요청이 갑니다.

### 검색엔진별 등록

1. **네이버 서치어드바이저**: 사이트 등록 → 메인 메타 태그(이미 삽입됨)로 소유확인 → `sitemap.xml`·`rss.xml` 제출
2. **구글 Search Console**: 속성 등록 → `sitemap.xml` 제출 (구글은 IndexNow 미참여)
   - 선택: `tools/google_indexing.py` (서비스 계정 필요, 보조 수단)
3. **빙 웹마스터도구**: 사이트 등록 → IndexNow 자동 연동

> 참고: 구글·빙의 옛 `sitemap ping` 엔드포인트는 폐지되어, 즉시 통보는 IndexNow + Search Console/서치어드바이저 제출이 정석입니다.

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL` 확인 (현재 `https://jungnang-massage1.pages.dev`)
2. `python3 build.py` 재실행 (canonical·sitemap·rss·robots에 반영됨)
3. 네이버 서치어드바이저·구글 Search Console에 `sitemap.xml` 제출
4. 배포 후 `python3 tools/indexnow.py` 1회 실행 — 전체 URL 즉시 통보
