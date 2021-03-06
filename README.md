# Ejercicio 2

Para el ejercicio 2, se construyo un API utilizando Flask (Python) y Sqlite, se
dejaron disponibles los siguientes endpoints.
  
| Método | Endpoint | Funcion |
| -------|-------------------------------------|---------------------------------------|
| GET    | api/v1.0/usuarios/                    | lista los usuarios                      |
| GET    | api/v1.0/usuarios/{correo@domain.tld} | revisa los datos de un usuario          |
| POST   | api/v1.0/usuarios/                    | agrega un usuario (email, nombre, clave)|
| DELETE | api/v1.0/usuarios/{correo@domain.tld} | elimina un usuario                      |
| PUT    | api/v1.0/usuarios/{correo@domain.tld} | modifica un usuario                     |

## Descarga e instalación del proyecto

Para descargar el proyecto se puede clonar el repositorio con el comando, ejecutamos lo siguiente

```console
git clone https://github.com/usach-devops-seccion1-grupo6/modulo2-ejercicio2/
```

### Con Docker

Construimos la imagen ejecutando:

```console
docker build -t ejercicio2-modulo2 .
```

Luego corremos la imagen ejecutando:
    
```console
docker run -it --name ejercicio2-modulo2 --env="APP_SETTINGS_MODULE=config.default" -d -p 5000:5000 ejercicio2-modulo2
```

### Con Python

Creamos un entorno de trabajo local e instalamos las dependencias.

```console
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Configuramos las variables de entorno para correr el servicio flask

#### Linux/Mac

```console
export FLASK_APP="entrypoint"
export FLASK_ENV="development"
export APP_SETTINGS_MODULE=config.default
```

#### Windows

```console
set "FLASK_APP=entrypoint"
set "FLASK_ENV=development"
set "APP_SETTINGS_MODULE=config.default"
```

### Ejecución con el servidor que trae Flask

Se puede iniciar el servicio del proyecto ejecutando:

```console
flask run
```

## Para interactuar con el API

### Agregar

Para agregar un usuario.

```console
curl -X POST -H "Content-Type: application/json" -d '{
     "nombre": "Nombre Apellido",
     "email": "nombre@test.cl",
     "clave": "111aA_"
 }' http://localhost:5000/api/v1.0/usuarios
```

Adicionalmente se puede ocupar el script_test/creacion.sh para crear usuarios aleatoriamente.

### Listar

Para listar todos los usuarios disponibles

```console
curl http://localhost:5000/api/v1.0/usuarios
```

### Mostrar

Para mostrar los datos de un usuario

```console
curl http://localhost:5000/api/v1.0/usuarios/${correo}
```

### Eliminar

Para mostrar los datos de un usuario

```console
curl -X DELETE  http://localhost:5000/api/v1.0/usuarios/${correo}
```

### Modificar

Para mostrar los datos de un usuario

```console
curl -X PUT -H "Content-Type: application/json" -d '{
     "nombre": "Nombre2 Apellido2",
     "clave": "111aA_2"
 }' http://localhost:5000/api/v1.0/usuarios/${correo}
```

# Integrantes Grupo 6
* Gonzalo Muñoz Boisier
* Flamel Jesod Canto Sanchez
* David Antonio Figueroa Mejias
* Eduardo Andres Cabrera Flores
* Alejandro Ignacio Carrasco Navarrete
