fizzbuzz=[]
fizz=[]
buzz=[]
neither=[]
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizzbuzz")
        fizzbuzz.append(i)
    elif i % 3 == 0:
        print("Fizz")
        fizz.append(i)
    elif i % 5 == 0:
        print("Buzz")
        buzz.append(i)
    else:
        print(i)
        neither.append(i)
print("Fizzed on: ")
print(fizz)
print("Buzzed on: ")
print(buzz)
print("Fizzbuzzed on: ")
print(fizzbuzz)
print("Neithered on: ")
print(neither)