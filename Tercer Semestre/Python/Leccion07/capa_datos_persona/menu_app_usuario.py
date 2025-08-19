opcion = None
while opcion != 5:
    print('''
    Opciones:
    1. Listar usuarios
    2. Agregar un usuario
    3. Modificar un usuario
    4. Eliminar un usuario
    5. Salir
    ''')

    opcion = input('Seleccione una opción (1-5): ')

    if opcion == 1:
        usuario = UsuarioDAO.seleccionar()
        for usuario in usuario:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('Ingrese el nombre de usuario: ')
        password_var = input('Ingrese la contraseña: ')
        usuario = Usuario(username=username_var, password=password_var)
        usuarios_insertado = UsuarioDAO.insertar(usuario)
        log.info(f'Usuario insertado: {usuarios_insertado}')
    elif opcion == 3:
        id_usuario_var = int(input('Ingrese el ID del usuario a modificar: '))
        username_var = input('Ingrese el nuevo nombre de usuario: ')
        password_var = input('Ingrese la nueva contraseña: ')
        usuario = Usuario(id_usuario=id_usuario_var, username=username_var, password=password_var)
        usuarios_actualizado = UsuarioDAO.actualizar(usuario)
        log.info(f'Usuario actualizado: {usuarios_actualizado}')
    elif opcion == 4:
        id_usuario_var = int(input('Ingrese el ID del usuario a eliminar: '))
        usuario = Usuario(id_usuario=id_usuario_var)
        usuarios_eliminado = UsuarioDAO.eliminar(usuario)
        log.info(f'Usuario eliminado: {usuarios_eliminado}')
else:
    log.info('Salimos de la aplicación. Hata pronto!!!')