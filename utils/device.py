import random, numpy as np

def get_device(preference: str = "auto") -> str:
    # En este boilerplate devolvemos una etiqueta para la UI.
    # Los forks pueden implementar lógica real para CPU/GPU.
    return preference

def set_seed(seed: int = 42) -> None:
    random.seed(seed)
    np.random.seed(seed)
