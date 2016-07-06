from ctypes import c_int
from ctypes import cdll

basics = cdll.LoadLibrary('dllForPython')

first = (c_int * 3)(1, 2, 3)

vector3D = c_int * 3
second = vector3D(4, 5, 6)

c_result = basics.dot(first, second, 3)
python_result = sum(a * b for a, b in zip([1, 2, 3], [4, 5, 6]))
print('C returned', c_result, 'and Python returned', python_result)


basics.dot((c_int*1)(2), (c_int*1)(*[3]), 1)

try:
    vector3D([1, 2, 3])
except:
    print('You cannot pass lists')
try:
    vector3D(0, 1, 2, 3)
except:
    print('Forbidden to provide more elements than it should accept')   