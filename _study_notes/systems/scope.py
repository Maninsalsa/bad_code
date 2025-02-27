var = "global"

def non_local():
    # global var
    var = "nonlocal"
    print(var)

    def local_var():
        nonlocal var
        var = "local"

    local_var()
    print(var)

print(var)
non_local()