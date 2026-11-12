# 원작자 삭제 요청 처리

창구: founder@yeoksam836.com · GitHub 이슈(템플릿 `takedown`). 받으면 그날 처리한다.

1. 맥북에서 `git pull` 후 `python3 scripts/remove_person.py "<핸들>" --dry`로 대상 확인
2. `python3 scripts/remove_person.py "<핸들>"` → `build_plugin.py` → `build_site.py`
3. `git grep -i "<핸들>"` 0건 확인 → 커밋·push (커밋 메시지·변경 이력에 이름을 쓰지 않는다: "remove: 원작자 요청 1건")
4. 맥미니도 같은 명령 실행(inbox·state는 맥미니에만 있음): `ssh macmini 'cd ~/gh/n7business/botong-saram && git pull && /opt/homebrew/bin/python3 scripts/remove_person.py "<핸들>"'`
5. 요청자에게 처리 완료 회신. 이슈로 왔으면 닫는다.

기록까지 지워 달라는 요청이면(이전 커밋에 남음) 저장소를 새 커밋 1개로 다시 만든다 — 11/4에 쓴 방식. 저장소 삭제는 민서 승인 후.

공개 저장소 규칙: 실명 인물에 대한 평가·비판 문구는 쓰지 않는다. 신뢰도는 weight 숫자로만.

이름 재등장 방지: `remove_person.py`가 이름을 `state/removed.txt`(공개 안 됨)에 남긴다. 맥북·맥미니 양쪽에 같은 파일이 있어야 한다. 빌드가 공개 파일에서 그 이름을 찾으면 멈추고, 그날 push도 하지 않는다. 문서·커밋 메시지에도 이름을 쓰지 않는다.
