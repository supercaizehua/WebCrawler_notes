while True:
    print("用户:", end="")
    input_string = input()
    print(input_string)
    print("机器人:" + input_string.strip("吗?") + "!")
