def votaciones():
    num_universidades = int(input("Ingrese el numero de universidades: "))
    class universidad:
        nombre = ""
        blanco = 0
        nulo = 0
        aceptan = 0
        rechazan = 0

        def __init__(self, blanco, aceptan, rechazan, nulo, nombre):
            self.blanco = blanco,
            self.aceptan = aceptan,
            self.rechazan = rechazan,
            self.nulo = nulo,
            self.nombre = nombre

        def empate(self):
            if self.aceptan == self.rechazan:
                return True
            else: 
                return False

        #def __str__(self):
            return f"Universidad: {self.nombre}\nAceptan: {self.aceptan}\nRechazan: {self.rechazan}\nBlanco: {self.blanco}\nNulo: {self.nulo}\nEmpate?: {self.empate}"

    universidades = []

    for i in range(num_universidades):
        nombre = input("Ingrese el nombre de la universidad: ")
        nulo = 0
        blanco = 0
        aceptan = 0 
        rechazan = 0
        menu = True

        while menu == True:

            opcion = input(f" \n\tMenu Votaciones - Universidad {nombre} \n\t(A). Aceptar\n\t(R). Rechazar\n\t(N). Nulo\n\t(B). Blanco\n\t(X). Guardar resultados\n\n\tOpcion: ").upper()

            if opcion == "A":
                aceptan += 1
            elif opcion == "R":
                rechazan += 1
            elif opcion == "N": 
                nulo += 1
            elif opcion == "B":
                blanco += 1
            elif opcion == "X":
                uni = universidad(blanco, aceptan, rechazan, nulo, nombre)
                universidades.append(uni)
                print("\nVotacion finalizada, resultados guardados satisfactoriamente\n")
                menu = False
            else: 
                print("Digite una opcion valida")

    aceptaron = 0
    rechazaron = 0
    empataron = 0

    print(f"Numero de universidades: {num_universidades}\n")

    for uni in universidades:
        print(f"Universidad: {uni.nombre}\nAceptan: {uni.aceptan}\nRechazan: {uni.rechazan}\nBlanco: {uni.blanco}\nNulo: {uni.nulo}\n")
        if uni.aceptan > uni.rechazan:
            aceptaron += 1
        elif uni.aceptan < uni.rechazan:
            rechazaron += 1
        elif uni.aceptan == uni.rechazan: 
            empataron += 1
        print("")

    print(f"Universidades que aceptan: {aceptaron}")
    print(f"Universidades que rechazaron: {rechazaron}")
    print(f"Universidades con empate: {empataron}")

#Reto 5: Question Description
def dias(kellyDiario, samDiario, diferencia):
    if kellyDiario <= samDiario:
        return print("-1")
    samResolvio = diferencia
    kellyResolvio = 0
    dias = 0

    while kellyResolvio <= samResolvio:
        samResolvio += samDiario
        kellyResolvio += kellyDiario
        dias += 1

    print(f"Kelly puede alcanzar a Sam en {dias} dias.")

votaciones()