#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 스크립트.

빌드 후 한 번 실행하면 sitemap.xml 의 모든 URL 을 IndexNow 로 통보합니다.
IndexNow 참여 검색엔진(Bing, Yandex, Seznam, **Naver**)에 한 번에 전달됩니다.
(Google 은 IndexNow 미참여 — google_indexing.py 또는 Search Console 사용)

사용법:
    python3 build.py          # 먼저 빌드 (sitemap·키파일 생성)
    python3 tools/indexnow.py # 전체 URL 일괄 통보

    # 글 하나만 통보:
    python3 tools/indexnow.py https://jungnang-massage1.pages.dev/magazine/새글/

키는 content/site.py 의 INDEXNOW_KEY 를 사용하며,
루트의 <KEY>.txt 가 배포 사이트에서 접근 가능해야 검증됩니다.
"""
import json
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENDPOINT = "https://api.indexnow.org/indexnow"
HOST = re.sub(r"^https?://", "", BASE_URL).strip("/")


def sitemap_urls():
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python3 build.py` 를 실행하세요.")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def submit(urls):
    if not urls:
        print("통보할 URL 이 없습니다.")
        return
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE_URL.rstrip('/')}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            code = resp.status
    except urllib.error.HTTPError as e:
        code = e.code
    # 200 OK / 202 Accepted 는 정상 접수
    status = {200: "OK", 202: "Accepted(접수됨)"}.get(code, f"HTTP {code}")
    print(f"IndexNow 통보 완료: {len(urls)}개 URL → {status}")
    print(f"  host={HOST}  key=...{INDEXNOW_KEY[-8:]}")
    if code not in (200, 202):
        print("  ⚠ 키 파일이 배포 사이트에서 200으로 응답하는지 확인하세요:")
        print(f"    {BASE_URL.rstrip('/')}/{INDEXNOW_KEY}.txt")


if __name__ == "__main__":
    urls = sys.argv[1:] or sitemap_urls()
    submit(urls)
