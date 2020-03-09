
def function_a():
    print('function_a() starts')
    function_b()
    function_d()
    print('function_a() ends() and returns')


def function_c():
    print('function_c() starts')
    print('function_c() ends and returns')


def function_b():
    print('function_b() starts')
    function_c()
    print('function_b() ends and returns')


def function_d():
    print('function_d() starts')
    print('function_d() ends and returns')


function_a()

