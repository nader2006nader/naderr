import ctypes
lib = ctypes.CDLL('./tool.so')
lib.function_you_exposed()
