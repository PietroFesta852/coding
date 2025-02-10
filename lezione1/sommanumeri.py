n=int(input('Numero'))
totale=0
# i=1
# while i<=n:
#     totale=totale+i
#     i=i+1
# print(f'La somma dei numeri fino a {n} è {totale}')
for i in range(1,n+1):
    totale=totale+i
print(f'La somma dei numeri fino a {n} è {totale}')