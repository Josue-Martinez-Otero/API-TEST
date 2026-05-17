"""
Módulo principal de la API de usuarios.

Define la aplicación FastAPI y los endpoints
para la gestión de usuarios.
"""

from typing import List
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException

from user_model import Genero, Role, Usuario


app = FastAPI()

USERS_DB: List[Usuario] = [
    Usuario(
        id=uuid4(),
        nombre="Josue",
        apellidos="Martinez Otero",
        genero=Genero.MASCULINO,
        roles=[Role.ADMIN],
    ),
    Usuario(
        id=uuid4(),
        nombre="Jonathan",
        apellidos="Balderma Ramirez",
        genero=Genero.MASCULINO,
        roles=[Role.USER],
    ),
    Usuario(
        id=uuid4(),
        nombre="Carlos",
        apellidos="Cabrera Tecorralco",
        genero=Genero.MASCULINO,
        roles=[Role.ADMIN],
    ),
    Usuario(
        id=uuid4(),
        nombre="Abril",
        apellidos="Guzman Pazas",
        genero=Genero.FEMENINO,
        roles=[Role.INVITADO],
    ),
]


@app.get("/")
async def root():
    """
    Endpoint raíz de la API.

    Returns:
        dict: Mensaje de bienvenidas.
    """
    return {"saludo": "Hola 8B IDGS hijos de Randolfo"}


@app.get("/api/v1/users")
async def get_users():
    """
    Obtiene la lista de usuarios.

    Returns:
        list: Lista de usuarios registrados.
    """
    return USERS_DB


@app.get("/api/v1/users/{usuario_id}", response_model=Usuario)
async def obtener_usuario(usuario_id: UUID):
    """
    Obtiene un usuario por su ID.

    Args:
        usuario_id (UUID): Identificador único del usuario.

    Returns:
        Usuario: Usuario encontrado.

    Raises:
        HTTPException: Si el usuario no existe.
    """
    for usuario in USERS_DB:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.post("/api/v1/users", response_model=Usuario)
async def create_user(user: Usuario):
    """
    Crea un nuevo usuario.

    Args:
        user (Usuario): Datos del usuario a crear.

    Returns:
        Usuario: Usuario creado.
    """
    user.id = uuid4()
    USERS_DB.append(user)
    return user


@app.put("/api/v1/users/{user_id}", response_model=Usuario)
async def update_user(user_id: UUID, updated_user: Usuario):
    """
    Actualiza un usuario existente.

    Args:
        user_id (UUID): ID del usuario a actualizar.
        updated_user (Usuario): Datos actualizados.

    Returns:
        Usuario: Usuario actualizado.

    Raises:
        HTTPException: Si el usuario no existe.
    """
    for index, user in enumerate(USERS_DB):
        if user.id == user_id:
            updated_user.id = user_id
            USERS_DB[index] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    """
    Elimina un usuario por su ID.

    Args:
        user_id (UUID): ID del usuario a eliminar.

    Returns:
        dict: Mensaje de confirmación.

    Raises:
        HTTPException: Si el usuario no existe.
    """
    for index, user in enumerate(USERS_DB):
        if user.id == user_id:
            del USERS_DB[index]
            return {"detail": "Usuario eliminado"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
