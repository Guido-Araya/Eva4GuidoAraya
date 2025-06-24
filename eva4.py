compradores=[]
def comprar_entrada():
    nombre = input ("Ingrese nombre de comprador.")
    if nombre in compradores:
        print("El nombre del comprador ya existe.")

        return
    
    tipo = input ("Ingrese el tipo de entrada (G/V):").upper()
    if tipo not in {'G'/'V'}:
        print("Tipo de entrada invalido")

        return
     
    while true:



     