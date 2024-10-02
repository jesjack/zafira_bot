import subprocess
import sys
import traceback


def install_and_exec(missing_module, code):
    print(f"¿Instalar el módulo {missing_module}? [s]: ", end="")
    install = input().strip().lower().replace("s", "")
    if len(install) > 0:
        print("Oki Doki")
        return
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", missing_module])
        globals()[missing_module] = __import__(missing_module)
        exec(code)
    except ImportError as e:
        missing_module = str(e).split("'")[1]  # Obtiene el nombre del módulo entre comillas
        install_and_exec(missing_module, code)
    except Exception as e:
        print("Ha ocurrido un error:")
        print(code)
        traceback.print_exc()  # Mostrar el traceback del error
    finally:
        subprocess.check_call([sys.executable, "-m", "pip", "uninstall", missing_module, "-y"])
        globals().pop(missing_module, None)