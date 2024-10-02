import os
from datetime import datetime


def save_code(code):
    # create folder if not exists
    os.makedirs("codes", exist_ok=True)
    # datetime as name
    name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # save code
    with open(f"codes/{name}.py", "w") as file:
        file.write(code)