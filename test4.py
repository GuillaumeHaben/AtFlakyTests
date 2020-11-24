from flaky import flaky

def scope_test():
    @flaky
    def do_local():
        spam = "local spam"

    @flaky
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    @flaky
    def do_global():
        global spam
        spam = "global spam"

    @flaky
    def do_local2():
        spam = "local spam"

    @flaky
    def do_nonlocal2():
        nonlocal spam
        spam = "nonlocal spam"

    @flaky
    def do_global2():
        global spam
        spam = "global spam"
    @flaky
    def do_local3():
        spam = "local spam"

    @flaky
    def do_nonlocal3():
        nonlocal spam
        spam = "nonlocal spam"

    @flaky
    def do_global3():
        global spam
        spam = "global spam"
    @flaky
    def do_local1():
        spam = "local spam"

    @flaky
    def do_nonlocal1():
        nonlocal spam
        spam = "nonlocal spam"

    @flaky
    def do_global1():
        global spam
        spam = "global spam"

    @flaky
    def do_local12():
        spam = "local spam"

    @flaky
    def do_nonlocal12():
        nonlocal spam
        spam = "nonlocal spam"

    @flaky
    def do_global12():
        global spam
        spam = "global spam"
    @flaky
    def do_local13():
        spam = "local spam"

    @flaky
    def do_nonlocal13():
        nonlocal spam
        spam = "nonlocal spam"

    @flaky
    def do_global13():
        global spam
        spam = "global spam"


    @flaky
    def do_local5():
        spam = "local spam"

    @flaky
    def do_nonlocal5():
        nonlocal spam
        spam = "nonlocal spam"

    @flaky
    def do_global5():
        global spam
        spam = "global spam"

    @flaky
    def do_local25():
        spam = "local spam"

    @flaky
    def do_nonlocal25():
        nonlocal spam
        spam = "nonlocal spam"

    @flaky
    def do_global25():
        global spam
        spam = "global spam"
    @flaky
    def do_local35():
        spam = "local spam"

    @flaky
    def do_nonlocal35():
        nonlocal spam
        spam = "nonlocal spam"

    @flaky
    def do_global35():
        global spam
        spam = "global spam"
    @flaky
    def do_local15():
        spam = "local spam"

    @flaky
    def do_nonlocal15():
        nonlocal spam
        spam = "nonlocal spam"

    @flaky
    def do_global15():
        global spam
        spam = "global spam"

    @flaky
    def do_local125():
        spam = "local spam"

    @flaky
    def do_nonlocal125():
        nonlocal spam
        spam = "nonlocal spam"

    @flaky
    def do_global125():
        global spam
        spam = "global spam"
    @flaky
    def do_local135():
        spam = "local spam"

    @flaky
    def do_nonlocal135():
        nonlocal spam
        spam = "nonlocal spam"

    @flaky
    def do_global135():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)