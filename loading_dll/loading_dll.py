import ctypes
 
MB_ICONEXCLAMATION = ctypes.c_uint(int("0x30",0));
NULL = None;
message = b'This is a MessageBox wrapping MessageBoxA()\nmy test\nhahahaha'
hDllUser32 = ctypes.WinDLL('user32.dll')
ret = hDllUser32.MessageBoxA(NULL,
                             message,
                             b'Message Box Test',
                             MB_ICONEXCLAMATION);
 
del hDllUser32;