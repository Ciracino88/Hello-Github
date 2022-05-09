# map 함수는 반환값이 오브젝트 타입이므로 list를 씌워 형변환을 시켜야 계산이 가능하다.
a = list(map(int, input().split()))
print(a[0] - a[1])

