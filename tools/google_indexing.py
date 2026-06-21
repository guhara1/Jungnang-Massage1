#!/usr/bin/env python3
"""Google Indexing API 일괄 통보 (선택).

Google 은 IndexNow 에 참여하지 않으므로, 즉시 색인 통보가 필요하면
Search Console 의 URL 검사 + 색인 요청을 쓰거나, 이 스크립트로
Indexing API(urlNotifications:publish) 를 호출합니다.

※ 주의: 구글 Indexing API 는 공식적으로 JobPosting·BroadcastEvent 용도이며
  일반 페이지 색인은 보장되지 않습니다. 가장 확실한 방법은
  Search Console 사이트 등록 + sitemap.xml 제출입니다.
  이 스크립트는 보조 수단으로 제공합니다.

사전 준비:
  1) Google Cloud 프로젝트에서 Indexing API 사용 설정
  2) 서비스 계정 생성 → JSON 키 다운로드
  3) Search Console 속성에 그 서비스 계정 이메일을 '소유자'로 추가
  4) pip install google-auth requests
  5) 환경변수: GOOGLE_APPLICATION_CREDENTIALS=서비스계정.json

사용법:
  python3 build.py
  python3 tools/google_indexing.py            # sitemap 전체
  python3 tools/google_indexing.py https://.../magazine/새글/
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"


def sitemap_urls():
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python3 build.py` 를 실행하세요.")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def main():
    try:
        import requests
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        sys.exit("의존성 필요: pip install google-auth requests")

    cred = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred or not os.path.exists(cred):
        sys.exit("GOOGLE_APPLICATION_CREDENTIALS 환경변수에 서비스계정 JSON 경로를 설정하세요.")

    creds = service_account.Credentials.from_service_account_file(cred, scopes=SCOPES)
    session = AuthorizedSession(creds)

    urls = sys.argv[1:] or sitemap_urls()
    ok = 0
    for u in urls:
        r = session.post(ENDPOINT, json={"url": u, "type": "URL_UPDATED"})
        if r.status_code == 200:
            ok += 1
        else:
            print(f"  ⚠ {u} → HTTP {r.status_code} {r.text[:120]}")
    print(f"Google Indexing API 통보: {ok}/{len(urls)} 성공")


if __name__ == "__main__":
    main()
