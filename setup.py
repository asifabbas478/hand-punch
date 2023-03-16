from cx_Freeze import setup, Executable

setup(
    name="MyApplication",
    version="1.0",
    description="My tkinter application",
    executables=[Executable("myapp.py", base="Win32GUI")],
)
