import dis

def add(x, y):
  return x + y

>>> dis.dis(add)

2           0 LOAD_FAST                0 (x)
            2 LOAD_FAST                1 (y)
            4 BINARY_ADD
            6 RETURN_VALUE
