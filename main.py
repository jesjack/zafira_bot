import os
import traceback

from gen import gen_code
from imports_installer import install_and_exec
from saver import save_code

while True:
    request = input(">>> ").strip().lower()
    if request == "exit" or request == "salir":
        break
    if len(request) == 0:
        continue
    if request == "clear" or request == "limpiar" or request == "cls":
        os.system("cls" if os.name == "nt" else "clear")
        continue
    if request == "open":
        # open current dir in explorer
        os.system(f"start {'.' if os.name == 'nt' else '.'}")
        continue
    code = gen_code(request)
    save_code(code)
    try:
        exec(code)
    except ImportError as e:
        missing_module = str(e).split("'")[1]  # Obtiene el nombre del módulo entre comillas
        install_and_exec(missing_module, code)
    except Exception as e:
        traceback.print_exc()  # Mostrar el traceback del error