# Archivo relacionado con el video 13y14_autenticacion_proteccion_ruta
from jwt import encode, decode

# Funcion que generara el token pasando un dato (diccionario)
# algorithm='HS256'  Este es un tipo de codificacion (ver documentacion)
def dame_token(dato:dict)->str:
    token:str= encode(payload=dato,key='mi_clave',algorithm='HS256')
    return token

# Funcion que valida el token que se le pasa 
def valida_token(token:str)->dict:
    dato:dict = decode(token,key='mi_clave',algorithms=['HS256'])
    return dato 