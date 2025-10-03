def asientos(seats, students):
    seats.sort()
    students.sort()
    suma = 0
    for i in range(len(seats)):
        valor = seats[i] - students[i]
        suma += abs(valor)
    return suma
    
print(asientos([3,1,5],[2,7,4]))
