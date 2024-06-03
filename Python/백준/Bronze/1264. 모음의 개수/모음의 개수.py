while True:
    a = input()
    if a == "#":
        break
    print(a.count("a")+a.count("e")+a.count("i")+a.count("u")+a.count("o")+a.count("A")+a.count("E")+a.count("I")+a.count("U")+a.count("O"))