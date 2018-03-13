def conditions(num1, num2):
    thing = 0
    for i in range(num1, num2):
        if i % 2 == 1:
            thing += i
    print thing

conditions(4586, 9546)
