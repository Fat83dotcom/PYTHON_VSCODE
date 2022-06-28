# função decoradora direta:

# def master(f):
#     def slave():
#         f()
#     return slave


# def fala_oi():
#     print('Oi')


# var = master(fala_oi)
# var()  # praticamente essa função recebe a função slave.

# usando a sintaxe decorador

def master(f):
    def slave(*args, **kwargs):
        print('Estou decorada.')
        f(*args, **kwargs) 
    return slave


# @master
def fala_oi():
    print('Oi')


# var = master(fala_oi)
# var()

@master
def func(msg):
    print(msg)


fala_oi()
func('OI')
