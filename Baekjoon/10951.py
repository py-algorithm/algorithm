'''
문제 링크: https://www.acmicpc.net/problem/10951
카테고리: 수학
문제 해설: A + B를 계산합니다.
'''
while True:
  try:#try에서 에러발생시 except로 가서 정상종료를 위함
    a,b=map(int,input().split())
    print(a+b)
  except:
    break