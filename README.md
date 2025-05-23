# 알고리즘 스터디

Since 24.06.08

## 디렉토리 구조

```bash
Baekjoon/
  /username
    문제번호.확장자
  /99mini
    1000.js
  /cakejin
    1000.py
이테코/
  CH1/
    01테스트_문제.py
Study/
  BFS/
    README.md
```

- Baekjoon
  - 백준사이트의 문제를 해결합니다.
  - 파일명은 `<문제번호>.<확장자>`로 합니다.
- 이테코
  - `CH<number>/`: 챕터 번호를 하위 폴더로 합니다.
  - `<number><문제이름>`: 문제 번호와 이름을 띄워쓰기 없이 적습니다.
- Study
  - 알고리즘 개념을 정리합니다.
  - 알고리즘 이름을 폴더로 하여 마크다운을 이용하여 내용을 정리합니다.

## 파일 템플릿

### 주석

각 언어별 블록 주석을 이용합니다.

**필수 항목**

- 작성자
- 문제 링크
- 카테고리
- 문제 해설: 간략하게 문제 해설을 작성합니다.

**선택 항목**

- 참조 링크
- 그 외 부가적 설명

### 예시

1. `python`

```python
'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/1000
카테고리: 수학
문제 해설: A + B를 계산합니다.

(옵션)참조링크:
'''
print(sum(map(int, input().split())))
```

## Issue

질문이 필요한 경우 이슈를 생성합니다.

- 이슈 이름: `[사이트] 문제번호`
- 라벨: 언어, 카테고리

## Pull Request

해결한 문제에 대해 PR을 작성합니다.

- PR 이름: `[사이트 문제번호]<카테고리>: 요약`
- 본문

1. 개요
   `관련 이슈`, `문제 링크`, `문제 요약` 등을 작성합니다.
2. 카테고리
   알고리즘 문제 사이트에서 제공하는 카테고리를 작성합니다.
3. 문제해설
   구체적인 문제해설을 작성합니다.

### Merge

`squash merge`하기 때문에 branch, commit 컨벤션을 따로 정하지 않습니다.

## 구성원

- [99mini](https://github.com/99mini)
- [cakejin](https://github.com/cakejin)
- [l-lyun](https://github.com/l-lyun)
