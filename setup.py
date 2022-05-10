from cx_Freeze import setup, Executable

base = None    

executables = [Executable("demo.py", base=base)]

packages = ["sklearn","xgboost","pickle","scipy"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "zerotwo",
    options = options,
    version = "0.1",
    description = 'hello',
    executables = executables
)