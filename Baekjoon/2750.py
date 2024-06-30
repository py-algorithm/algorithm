'''
문제 링크: https://www.acmicpc.net/problem/2750
카테고리: 정렬
문제 해설: 오름차순으로 정렬합니다.
'''

'입출력핵심'
n=int(input())
m=[input() for _ in range(n)]#n개한줄 씩 입력받기
l=sorted(m)

print(*l,sep='\n')#l의 요소들 한줄씩 출력