frase=(input("Coloca una frase de tu preferencia : ").lower())#Una frase
print(frase)
vocales = "a,e,i,o,u".lower()
consonantes = "b,c,d,f,g,h,i,j,k,l,m,n,p,q,r,s,t,u,v,w,x,y,z".lower()
#Verdadero o falso
if vocales == consonantes:
    print("son vocales y consonantes")
else:
    print("no son vocales ni consonantes")
#Bucle
for vocal in vocales:
  if vocal in consonantes:
        print(vocal)
else:
    print("Error vuelve a intentarlo")