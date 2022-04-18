# Taxi-app
Las siguientes instrucciones se deben ejecutar en el directorio /src
## Instrucciones para instalar el entorno
1. Installar python > 3.7
2. Installar pipenv<br>
   ```pip install pipenv```
3. Ejecutar el comando pipenv install<br>
   ```pipenv install```
4. Ejecutar el subcomando shell<br>
   ```pipenv shell```

## Instrucciones para ejecutar frontend
1. Situarse en el directorio /front<br>
```cd front```
2. Ejecutar el main tantas veces como sea necesario (tantas como usuarios concurrentes) <br>
```python main.py```
## Instrucciones para ejecutar backend
1. La primera vez que se ejecuta se debe iniciar la base de datos<br>
```python init_db.py``` 
2. Ejecutar el servidor<br>
```uvicorn app.main:app --reload```

## Resetear la base de datos
Ejecutar la instruccion ```python init_db.py``` desde la carpeta /src 

## Visualizar los datos de SQLite
Hay un plugin llamado ```SQLite``` en VSCode para explorar los datos del fichero de forma visual e interactiva.

## Documentacion de los APIs
Despues de ejecutar el servidor acceder a la pagina http://127.0.0.1:8000/docs

## Configuracion
Crear un archivo llamado ```config.json``` en la carpeta /src del copiando el siguiente contenido cambiando el correo y la contraseña

```json
{
  "email": {
    "address": "tu-correo@gmail.com",
    "password": "password del correo"
  }
}
```

