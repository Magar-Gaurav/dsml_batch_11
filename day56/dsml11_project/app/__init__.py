import importlib
import pkgutil

for model in pkgutil.iter_modules(__path__):
    importlib.import_module(f'{__name__}.{model.name}')