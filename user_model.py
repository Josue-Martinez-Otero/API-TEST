"""
Modelos y enumeraciones para la gestión de usuarios.

Define los esquemas de datos utilizados por la API.
"""

from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Genero(str, Enum):
    """
    Enumeración que representa el género del usuario.
    """

    MASCULINO = "Masculino"
    FEMENINO = "Femenino"
    NO_BINARIO = "NoBinario"


class Role(str, Enum):
    """
    Enumeración que representa los roles de un usuario.
    """

    ADMIN = "Admin"
    USER = "User"
    INVITADO = "Invitado"


class Usuario(BaseModel):
    """
    Modelo que representa un usuario del sistema.
    """

    id: Optional[UUID] = Field(default_factory=uuid4)
    nombre: str
    apellidos: str
    genero: Genero
    roles: List[Role]
