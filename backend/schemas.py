from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class EjercicioBase(BaseModel):
    nombre: str
    grupo_muscular: str
    imagen_url: str

class EjercicioResponse(EjercicioBase):
    id: int
    class Config: raise_errors = False; from_attributes = True

class AlumnoBase(BaseModel):
    nombre: str
    email: EmailStr
    telefono: str
    fecha_nacimiento: str
    objetivo: str
    notas: Optional[str] = None
    activo: bool = True

class AlumnoResponse(AlumnoBase):
    id: int
    created_at: datetime
    class Config: from_attributes = True

class DetallePlanillaBase(BaseModel):
    dia_semana: str
    ejercicio_id: int
    series: int
    repeticiones: int
    peso_kg: float
    descanso_segundos: int

class DetallePlanillaResponse(DetallePlanillaBase):
    id: int
    ejercicio: EjercicioResponse
    class Config: from_attributes = True

class PlanillaMensualBase(BaseModel):
    alumno_id: int
    mes_ano: str

class PlanillaMensualResponse(PlanillaMensualBase):
    id: int
    progresion_aplicada: bool
    detalles: List[DetallePlanillaResponse] = []
    class Config: from_attributes = True