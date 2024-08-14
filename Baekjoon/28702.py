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

result=0

for _ in range(3):
  i=input()
  arr.append(i)

#입력된 세개 중 숫자인걸 찾아서 정수변환
for index, element in enumerate(arr):

  if element != 'Fizz' and element != 'FizzBuzz' and element != 'Buzz':
    #정수가 arr 인덱스 몇번째에 있는지 보고 4번째 수 추청
    n = 3 - index + int(element)

    is_multiple_3 = n % 3 == 0
    is_multiple_5 = n % 5 == 0
    
    #4번째 수 가 3,5,3과5의 배수인지 확인 후 출력
    if is_multiple_3 and is_multiple_5:
      result='FizzBuzz'
    elif is_multiple_3 and not is_multiple_5:
      result='Fizz'
    elif not is_multiple_3 and is_multiple_5:
      result='Buzz'
    else:
      result=n
    
    print(result)
    break