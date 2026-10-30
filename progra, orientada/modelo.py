



from abc import ABC, abstractmethod
from datetime import date
from typing import List

class Departamento:
    def __init__(self, id_departamento: int, nombre_dep: str, nombre_admin: str):
        self.__id_departamento = id_departamento
        self.__nombre_dep = nombre_dep
        self.__nombre_admin = nombre_admin

    @property
    def nombre_dep(self) -> str:
        return self.__nombre_dep

    @nombre_dep.setter
    def nombre_dep(self, nuevo_nombre: str):
        self.__nombre_dep = nuevo_nombre

    def create_dep(self) -> None:
        pass

    def eliminate_dep(self) -> None:
        pass

    def edit_dep(self) -> None:
        pass

class Persona(ABC):
    def __init__(self, id_persona: int, correo: str, nombre: str, telefono: int):
        self._id_persona = id_persona
        self._correo = correo
        self._nombre = nombre
        self._telefono = telefono
        self._departamento = None 

    @property
    def nombre(self) -> str:
        return self._nombre

    def editar_contacto(self, correo: str, nombre: str, telefono: int) -> None:
        self._correo = correo
        self._nombre = nombre
        self._telefono = telefono

    @abstractmethod
    def obtener_contacto(self) -> str:
        pass

    def asignar_departamento(self, departamento: Departamento) -> None:
        self._departamento = departamento

class Proyectos:
    def __init__(self, id_proyecto: int, inicio_proyecto: date, descripcion: str):
        self.__id_proyecto = id_proyecto
        self.__inicio_proyecto = inicio_proyecto
        self.__descripcion = descripcion

    def create_proyect(self) -> None:
        pass

    def edit_proyect(self) -> None:
        pass

    def eliminate_proyect(self) -> None:
        pass

class RegistroTiempo:
    def __init__(self, id_tiempo: int, fecha: date, horas_trabajadas: float, reporte: str):
        self.__id_tiempo = id_tiempo
        self.__fecha = fecha
        self.__horas_trabajadas = horas_trabajadas
        self.__reporte = reporte
        self.__proyecto_asociado = None 

    def imputar_proyecto(self, proyecto: Proyectos) -> None:
        self.__proyecto_asociado = proyecto

    def registrar_horas(self) -> None:
        pass

    def verificar_empleado(self) -> bool:
        return True

class Empleados(Persona):
    def __init__(self, id_persona: int, correo: str, nombre: str, telefono: int, id_empleado: int, inicio_contrato: date, salario: int):
        super().__init__(id_persona, correo, nombre, telefono)
        self.__id_empleado = id_empleado
        self.__inicio_contrato = inicio_contrato
        self.__salario = salario
        self.__registros_tiempo: List[RegistroTiempo] = []
        self.__proyectos_asignados: List[Proyectos] = []

    @property
    def salario(self) -> int:
        return self.__salario

    def obtener_contacto(self) -> str:
        return f"Empleado: {self._nombre} | Correo: {self._correo}"

    def agregar_registro(self, registro: RegistroTiempo) -> None:
        self.__registros_tiempo.append(registro)

    def asignar_proyecto(self, proyecto: Proyectos) -> None:
        self.__proyectos_asignados.append(proyecto)

    def fichar_llegada(self) -> None:
        pass

    def fichar_salida(self) -> None:
        pass

class Informe:
    def __init__(self, id_informe: int, empleados: str, proyecto: str, tiempo: date):
        self.__id_informe = id_informe
        self.__empleados = empleados
        self.__proyecto = proyecto
        self.__tiempo = tiempo

    def exportar_format(self) -> None:
        pass

    def editar_informe(self) -> None:
        pass

class Administradores(Persona):
    def __init__(self, id_persona: int, correo: str, nombre: str, telefono: int, id_admin: int, inicio_contrato: date, salario: int, contrasena: str):
        super().__init__(id_persona, correo, nombre, telefono)
        self.__id_admin = id_admin
        self.__inicio_contrato = inicio_contrato
        self.__salario = salario
        self.__contrasena = contrasena
        self.__informes_generados: List[Informe] = []

    def obtener_contacto(self) -> str:
        return f"Admin: {self._nombre} | Correo: {self._correo}"

    def agregar_informe(self, informe: Informe) -> None:
        self.__informes_generados.append(informe)

    def anadir_empleado(self) -> None:
        pass

    def modificar_empleado(self) -> None:
        pass

    def generar_informe(self) -> None:
        pass