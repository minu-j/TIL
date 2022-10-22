# GIT

## Branch

```bash
# 깃 폴더 등록
$ git init


# 상태확인
$ git status
  On branch master
  nothing to commit, working tree clean


# 커밋 로그 확인
$ git log
  commit 2f8274ec12ed93599a64295904ce4184d7b23d71 (HEAD -> water)
  Author: minu-j <minu.j.dev@gmail.com>
  Date:   Fri Oct 7 16:48:06 2022 +0900

      collision

  commit 5d11e63101678e95b370816f72dac711d269fef4 (master)
  Author: minu-j <minu.j.dev@gmail.com>
  Date:   Fri Oct 7 16:40:30 2022 +0900

      water attraction


# 커밋 로그를 한줄로 확인
$ git log --oneline
  6714d5f (HEAD -> master) master collision
  5d11e63 water attraction
  ea8d8a9 ground 2
  0c5dddb ground attraction
  a735a5a 'commit'


# 브랜치를 그래픽으로 한눈에 확인
$ git log --oneline --graph

  - 328d5a8 (HEAD -> master, origin/master, origin/HEAD) Update .clabot
  - 4748f20 Update .clabot
  - 93b8860 Create .clabot
  - 2a5e45c Merge pull request #71 from flrngel/patch-1
    |\
    | * b104189 remove question mark
    |/
  - fa5fbd1 (tag: v0.4) Merge branch 'release/v0.4'
    |\
    | * 4d92033 새 버전의 모델에 맞게 readme 및 이미지 업데이트
    | * cbfe6d4 Merge pull request #68 from kakao/feature/59
    | |\
    | | * 4abd399 f-strings로 인해 python 3.6 버전 이하에서 오류가 나는 부분 수정 #59
    | |/
    | * 61bea08 Merge pull request #67 from kakao/feature/64
    | |\
    | | * 7629c1f pylint 오류 수정 #64


# 이전버전의 내용 확인
$ git checkout <commit hash>


# 브랜치 생성
$ git branch <branch name>


# branch 생성 후 이동
$ git switch -c <branch name>
  Switched to a new branch '<branch name>'


# 지금 어느 브랜치에 있는지, 어느 브랜치가 있는지?
$ git branch
  * master
    <branch name>


# 깃 브랜치 전환
$ git switch <branch name>
  Switched to branch '<branch name>'


# 다시 마스터로 돌아오기
$ git switch master


# 브랜치 삭제
$ git branch -d <branch name>
  Deleted branch <branch name> (<commit hash>).


# 브랜치 합치기
$ git merge <branch name>
  Updating ea8d8a9..5d11e63
  Fast-forward
  <file name> | 6 +++++-
  1 file changed, 5 insertions(+), 1 deletion(-)

  # collision 에러 메시지
  Auto-merging <file name>
  CONFLICT (content): Merge conflict in <file name>
  Automatic merge failed; fix conflicts and then commit the result.

```

## Pull request

```bash
# 허브에 push
$ git push origin <branch name>
  Enumerating objects: 5, done.
  Counting objects: 100% (5/5), done.
  Writing objects: 100% (3/3), 289 bytes | 289.00 KiB/s, done.
  Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
  remote: 
  remote: Create a pull request for '<branch name>' on GitHub by visiting:
  remote:      https://github.com/.../pull/new/<branch name>
  remote:
  To https://github.com/minu-j/test.git
  * [new branch]      <branch name> -> <branch name>

```

## Fork

```bash

```
업스트링 등록 > git pull upstring?