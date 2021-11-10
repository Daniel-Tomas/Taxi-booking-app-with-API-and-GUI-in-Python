# Taxi-app
Este programa pertenece al backend de una aplicacion con funciones minimas similares al de Uber.

## Instrucciones para ejecutarlo
1. Installar python > 3.7
2. Installar pipenv
```pip install pipenv```
3. Ejecutar el comando pipenv install
```pipenv install```
4. Ejecutar el subcomando shell
```pipenv shell```
5. La primera vez que se ejecuta se debe iniciar la base de datos
```python init_db.py``` 
6. Ejecutar el servidor
```uvicorn app.main:app --reload```

## Resetear la base de datos
Ejecutar la instruccion ```python init_db.py``` desde la raiz del proyecto

## Visualizar los datos de SQLite
Hay un plugin llamado ```SQLite``` en VSCode para explorar los datos del fichero de forma visual e interactiva.

## Documentacion de los APIs
Despues de ejecutar el servidor acceder a la pagina http://127.0.0.1:8000/docs

## Configuracion
Crear un archivo llamado ```config.json``` en la raiz del programa copiando el siguiente contenido cambiando el correo y la contraseña

```json
{
  "email": {
    "address": "tu-correo@gmail.com",
    "password": "password del correo"
  }
}
```

