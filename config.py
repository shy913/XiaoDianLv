def read_file():
    path = r"Info.txt"
    file = {}
    try:
        with open(path, "r") as f:
            info = f.read()
        # print(info.split("\n"))
        for item in info.split("\n"):
            file[item.split(":")[0]] = item.split(":")[1]
        return file
    except():
        return -1
while 1:

    print(f"   叫声：\t{read_file()['jiao']}")
    print(f"刷新时间：\t{read_file()['sleeptime']}")
    jiao = input("请输入新的叫声 j ∈ [0,3] ∩ Z :")
    sleeptime = input("新的刷新时间 t ∈ [0,+∞) ∩ Z :")
    with open("Info.txt", "w") as f:
        f.write(f"jiao:{jiao}\nsleeptime:{sleeptime}")