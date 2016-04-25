while True:
    try:
        (x,) = (int(x) for x in raw_input().split())
        for i in range(x):
            (A, B, C) = (int(x) for x in raw_input().split())
            print "Case #{0}: {1}".format(i+1, ans[A+B > C])
    except EOFError:
        break
