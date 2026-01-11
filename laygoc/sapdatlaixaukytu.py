for x in range(int(input())):
    a = [i for i in input()]
    b = [i for i in input()]
    print(f'Test {x+1}: ' + ('YES' if sorted(a)==sorted(b) else 'NO'))