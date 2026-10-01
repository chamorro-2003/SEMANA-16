from typing import Dict, Any


class Usuario:
    """Representa un usuario del sistema (Cliente o Administrador)."""

    def __init__(
        self,
        usuario_id: str,
        nombre: str,
        rol: str = "Cliente",
        username: str = "",
        contrasena: str = "",
    ) -> None:
        self.usuario_id: str = str(usuario_id).strip()
        self.nombre: str = nombre.strip()
        self.rol: str = rol.strip()
        self.username: str = username.strip()
        self.contrasena: str = contrasena.strip()

    def a_diccionario(self) -> Dict[str, Any]:
        return {
            "usuario_id": self.usuario_id,
            "nombre": self.nombre,
            "rol": self.rol,
            "username": self.username,
            "contrasena": self.contrasena,
        }

    @classmethod
    def desde_diccionario(cls, data: Dict[str, Any]) -> "Usuario":
        return cls(
            usuario_id=data.get("usuario_id", data.get("id_usuario", "")),
            nombre=data.get("nombre", ""),
            rol=data.get("rol", "Cliente"),
            username=data.get("username", ""),
            contrasena=data.get("contrasena", ""),
        )

    def __str__(self) -> str:
        return f"[{self.usuario_id}] {self.nombre} - Rol: {self.rol}"
