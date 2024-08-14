'''
문제 링크:https://www.acmicpc.net/problem/28702
카테고리: 수학, 문자열
문제해설: FizzBuzz
i=3배수->fizz
i=5배수->buzz
i=3과5의배수->fizzbuzz
i=3의 배수도 5의 배수도 아님->i

입력된 연속된 세 수 다음의 i를 조건에 맞게 출력하기
입력된 수가 모두 문자열일 경우는 없다고 가정
'''
arr=[]

result_1=0
result_2=0

for _ in range(3):
  i=input()
  arr.append(i)

#입력된 세개 중 숫자인걸 찾아서 정수변환
for i in arr:

  if i!='Fizz'and i!='FizzBuzz'and i!='Buzz':
    n=int(i)


#정수가 arr 인덱스 몇번째에 있는지 보고 4번째 수 추청
    if i==arr[0]:
      result_1=n+3
    if i==arr[1]:
      result_1=n+2
    if i==arr[2]:
      result_1=n+1


#4번째 수 가 3,5,3과5의 배수인지 확인 후 출력
  if result_1%3==0 and result_1%5==0:
    result_2='FizzBuzz'
  elif result_1%3==0 and result_1%5!=0:
    result_2='Fizz'
  elif result_1%3!=0 and result_1%5==0:
    result_2='Buzz'
  elif result_1%3!=0 and result_1%5!=0:
    result_2=result_1

print(result_2)