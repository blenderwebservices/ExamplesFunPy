def conversor_de_emojis():
    diccionario_emojis = {
        "feliz": "😄",
        "triste": "😢",
        "corazón": "❤️",
        "fuego": "🔥",
    }

    print("\nConvierte palabras a emojis según el diccionario.")
    print(diccionario_emojis)
    mensaje = input("Escribe un mensaje: ")
    palabras = mensaje.split()
    mensaje_con_emojis = " ".join([diccionario_emojis.get(palabra, palabra) for palabra in palabras])
    print(f"Mensaje con emojis: {mensaje_con_emojis}\n")
    new_var = input("pulsa Enter para continuar ... \n")
