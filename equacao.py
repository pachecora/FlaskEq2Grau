def equacao2grau(a, b, c) -> 'list':

    """Recebe 3 inteiros a, b e c e de uma equaçao do 2grau
    e calcula suas raízes"""

    delta = (b * b) - (4 * a * c)
    raizDelta = delta**(0.5)
    x1 = (-b + raizDelta) / (2*a)
    x2 = (-b - raizDelta) / (2 * a)
    lista = [x1, x2]
    return lista
