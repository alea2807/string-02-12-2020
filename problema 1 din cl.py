s=str(input('introduceti un nume si un prenume:'))
a,b=s.split()
print(a)
print(b)
if((a.title()==a)and(b.title()==b)):
    print('numele introdus este corect')
else:
    print('numele introdus este incorect')