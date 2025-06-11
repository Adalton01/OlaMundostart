print("="*30)
n = int(input("--Sequencia de Fibonacci--\n"))
t1 = 0
t2 = 1
print("="*30)
print(" {}-{}".format(t1,t2),end='')
cont = 3
while cont <= n:
    t3= t1+t2
    print(f"-{t3}",end='')
    t1 =t2
    t2 =t3
    cont += 1

print("- Fim")
print("*"*30)
