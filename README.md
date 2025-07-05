# T02.03-Reserva-de-hotel-API

![image](https://github.com/user-attachments/assets/c2dd14a1-e12d-49a6-b010-0ee663dd9afd)


Este proyecto es una API REST construida con **FastAPI**, que permite gestionar:
- Registro de usuarios.
- Inicio de sesión seguro con JWT.

## ¿Qué hace esta API?

- Los **usuarios** pueden registrarse y autenticarse.
- El **login** devuelve un token JWT para acceder a rutas protegidas.
- Se valida que los correos electrónicos sean únicos y correctos.
- Los datos se guardan en una base de datos SQLite para pruebas.
- La API se documenta sola con Swagger (`/docs`).

## Tecnologías usadas

- **FastAPI**: framework para crear APIs rápidas y modernas.
- **Uvicorn**: servidor ASGI para correr la aplicación.
- **SQLAlchemy**: ORM para manejar la base de datos.
- **Pydantic**: para validar los datos de entrada y salida.
- **Passlib**: para encriptar contraseñas.

![image](https://github.com/user-attachments/assets/57dc490b-8e42-4245-9435-079e52293369)
![image](https://github.com/user-attachments/assets/373a0a65-31f9-4b3a-8ae7-cfac31868f97)
![image](https://github.com/user-attachments/assets/f3672157-9e64-4e04-bdde-a649db39ae8c)
![image](https://github.com/user-attachments/assets/eeae5229-95c8-49a2-89f0-ff71d7373d42)



