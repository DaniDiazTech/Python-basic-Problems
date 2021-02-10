"""
Este programa recorre una palabra o una frase e imprime si cada caracter es una vocal o una consonante
"""


def recorrer(palabra):
    # Hacemos un "For loop" para recorrer la palabra o frase, por cada caracter
    
    # Convertimos toda la frase en minuscula

    palabra = palabra.lower()

    for caracter in palabra:

        # Si el caracter es un espacio o un signo de puntuacion
        if not caracter.isalpha():
            print("Este no es no una consonante ni una vocal")
            # Pasamos el for loop
            pass

        # Revisamos si la palabra es una vocal
        if caracter in "aeiou":
            print("Es vocal")

        # Finalmente decidimos que todo lo demas seria una consonante
        
        else:
            print("Es una consonante")

# Tomamos el input del usuario
nuestra_palabra = input("Tu palabra >> ")

# llamamos la funcion
recorrer(nuestra_palabra)
