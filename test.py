from ctypes import windll, c_int
from ctypes import cdll
from ctypes import WINFUNCTYPE

windll.kernel32.GetModuleHandleW(0)

lib = cdll.LoadLibrary('ConsoleApplication1.dll')
mul=lib.mul

test=mul(2, 3)

print test
