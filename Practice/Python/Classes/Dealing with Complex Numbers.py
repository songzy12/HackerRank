def print_complex(s):
    if s.real:
        if s.imag > 0:
            print '%.2f + %.2fi' % (s.real, s.imag)
        elif s.imag < 0:
            print '%.2f - %.2fi' % (s.real, -s.imag)
        else:
            print '%.2f' % (s.real)
    else:
        if s.imag > 0:
            print '%.2fi' % (s.imag)
        elif s.imag < 0:
            print '-%.2fi' % (-s.imag)
        else:
            print '0.00' #format
        
r1, i1 = map(float, raw_input().split())
r2, i2 = map(float, raw_input().split())
C = complex(r1, i1)
D = complex(r2, i2)
print_complex(C.__add__(D))
print_complex(C.__sub__(D))
print_complex(C.__mul__(D))
print_complex(C.__div__(D))
print '%.2f' %((C.real**2 + C.imag**2)**0.5)
print '%.2f' %((D.real**2 + D.imag**2)**0.5)
