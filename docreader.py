import importlib

module_name = input("Please enter the module name to import:")
module = importlib.import_module(module_name)

print(module.__doc__)
