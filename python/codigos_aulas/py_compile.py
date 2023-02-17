import py_compile
import sys

def soma(*args):
    print(f"A soma é {sum(args)}")

print(soma(1,2))

if __name__ != '__main__':
    py_compile.compile(
    file="~/Download/soma.py",
    cfile="~/Download/soma.pyc"
)
