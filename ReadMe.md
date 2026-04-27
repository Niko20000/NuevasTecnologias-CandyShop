**Integrantes**
Nikolas Martinez Morales
Mariana Bedoya
Samuel Galvis
Matias Naranjo

**Como Ejecutar El Proyecto Desde La Terminal**
1.activa el entorno virtual
2.descarga requeriments.txt
3. escribe esto en la terminal 
python main.py


*ENTORNO VIRTUAL*
Paso a paso 

1. Crea el entorno
python -m venv venv
2. Activar entorno virtual
.\.venv\Scripts\Activate.ps1

Si tenemos restricciones en powerShell con Script:
Set-ExecutionPolicy Unrestricted -Scope Process           //   solo en la terminal actual

Para desactivar…
desactivate

SI TIENES FALLAS INTENTA ESTO
rm -r venv
python -m venv venv
.\venv\Scripts\Activate

*Instalar las dependencias*
pip install -r requirements.txt