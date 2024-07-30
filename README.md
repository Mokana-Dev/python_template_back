
# python_template_back
Arquitectura limpia, monolito python con fastapi implementa patron repository utilizando una moderna y rápida biblioteca para construir APIs con Python 3.9+ basada en estándares como OpenAPI y JSON Schema. La plantilla incluirá configuraciones y ejemplos para integrar las siguientes tecnologías:

## Uvicorn: 
Un servidor ASGI ultra rápido para ejecutar aplicaciones de FastAPI.
## SQLAlchemy: 
Un ORM (Object Relational Mapper) que facilita la interacción con bases de datos.
## python-dotenv: 
Para gestionar las variables de entorno de manera sencilla.
## sqlalchemy-utils: 
Proporciona diversas utilidades adicionales para trabajar con SQLAlchemy.
## Flake8: 
Una herramienta para asegurar la calidad del código siguiendo las convenciones de PEP8.
## PyJWT: 
Una biblioteca para trabajar con JSON Web Tokens (JWT) para autenticación.
## passlib[bcrypt]: Para la gestión de contraseñas, incluyendo el hashing seguro utilizando bcrypt.

## Run Locally
Los archivos [main.py, runtime.txt, vercel.json] son de configuracion para desplegar la aplicacion en VERCEL. Si desea desplegar la aplicacion en cualquier otro servicio puede modificar las actios en la carpeta .github/workflows/template-deploy.txt sino usar la configuracion que esta presente en la plantilla.

Clone the project
```bash
  git clone https://github.com/Mokana-Dev/python_template_back.git
```

Go to the project directory
```bash
  cd python_template_back
```

Create a virtual environment
```bash
  python -m venv venv
```

Activate the virtual environment
En Windows:
```bash
  venv\Scripts\activate
```

En macOS/Linux:
```bash
  source venv/bin/activate
```

Install dependencies
```bash
  pip install -r requirements.txt
```

Inicializar la base de datos a partir de los modelos
```bash
    python initialize_db.py
```

Ejecutar los seeds para crear los registros iniciales para las tablas de la base de datos
```bash
    python main_seeds.py
```

Start the server
```bash
  fastapi dev init.py
```

## Testing
Correr las pruebas con unittest
```bash
    python -m unittest discover tests
```

Correr linter flake8
```bash
    flake8 .
```
