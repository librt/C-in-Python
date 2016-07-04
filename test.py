from ctypes import cdll

basics = cdll.LoadLibrary('ConsoleApplication1.dll')
mul=basics.mul

test=mul(4, 3)

print test
