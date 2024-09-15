while True:
    a = input('введіть повідомлення')
    if not a:
        print('ви нічого не ввели')
    else:
        print('ввели')
        break
while True:
    age = input('введіть вік')

    if not age:
        print('ви нічого не ввели')
    else:
        if int(age) < 18:
            print('неповнолітній')
        else:
            print('повнолітній')
        break

print('hello world')
