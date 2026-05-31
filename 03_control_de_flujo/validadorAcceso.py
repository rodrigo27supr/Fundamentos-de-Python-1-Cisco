usuarioNombre = "admin"
usuarioClave = "1234"

nombreIngresado = input("Usuario: ")
claveIngresada = input("Contrasena: ")

if nombreIngresado == usuarioNombre and claveIngresada == usuarioClave:
    print("Acceso concedido")
else:
    print("Acceso denegado")