import re
from functools32 import lru_cache
#from ctypes import c_uint16 as uint

values = {}

@lru_cache()
def process(line):
    print line,
    op = re.search('[A-Z]+', line).group() if re.search('[A-Z]+', line) else None
    sym = re.findall('[a-z0-9]+', line)

    if sym[0].isdigit():
        print 'confirm?'
        raw_input()
        if not op:
            return int(sym[0])
        elif op == 'NOT':
            return 2**16 + ~int(sym[0])
        elif op == 'AND':
            return int(sym[0]) & process(values[sym[1]])
        else:
            print 'error 1:', line
    else:
        if not op:
            return process(values[sym[0]])
        elif op == 'NOT':
            return 2**16 + ~process(values[sym[0]])
        elif op == 'AND':
            return process(values[sym[0]]) & process(values[sym[1]])
        elif op == 'OR':
            return process(values[sym[0]]) | process(values[sym[1]])
        elif op == 'LSHIFT':
            return (process(values[sym[0]]) << int(sym[1])) % 2**16
        elif op == 'RSHIFT':
            return (process(values[sym[0]]) >> int(sym[1])) % 2**16
        else:
            print 'error 2:', line


with open('07.txt') as f:
    for line in f.readlines():
        sym = re.findall('[a-z0-9]+', line)
        dest = sym[-1]
        values[dest] = line

        op = re.search('[A-Z]+', line).group() if re.search('[A-Z]+', line) else None
        print line.strip(), '    \t', op, sym

print
values['b'] = '956'
print process(values['a'])


