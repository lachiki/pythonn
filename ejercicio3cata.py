print("ingrese el numero de resdpuestas; correctas-incorrecta-en blanco")

correctas=int(input("respuestas correctas "))
incorrectas=int(input("respuestas incorrectas "))
blanco=int(input("respuestas en blanco "))


tc=correctas*3
ti=incorrectas*-1
tb=blanco*0

puntaje=tc+ti+tb

print("su puntaje final es ", puntaje)