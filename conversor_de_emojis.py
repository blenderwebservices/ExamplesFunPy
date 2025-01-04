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
        # Error: Falta cerrar el método join con un paréntesis
    mensaje_con_emojis = " ".join([diccionario_emojis.get(palabra, palabra) for palabra en palabras]
    print(f"Mensaje con emojis: {mensaje_con_emojis}\n")
    new_var = input("pulsa Enter para continuar ... \n")