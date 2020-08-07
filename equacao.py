from math import sqrt


def equacao2grau(a, b, c) -> 'list':

    """Recebe 3 inteiros a, b e c e de uma equaçao do 2grau
    e calcula suas raízes"""

    if a == None:
        return '  '

    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        x1 = 'Sem raiz Real'
        x2 = 'Sem raiz Real'
        lista = [x1, x2]
        return lista

    raizDelta = sqrt(delta)
    x1 = (-b + raizDelta) / (2 * a)
    x2 = (-b - raizDelta) / (2 * a)
    x1 = round(x1, 3)
    x2 = round(x2, 3)
    lista = [x1, x2]
    return lista
