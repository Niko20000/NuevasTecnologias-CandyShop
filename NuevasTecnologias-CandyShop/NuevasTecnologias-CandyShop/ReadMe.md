**Integrantes**
Nikolas Martinez Morales
Mariana Bedoya
Samuel Galvis
Matias Naranjo



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