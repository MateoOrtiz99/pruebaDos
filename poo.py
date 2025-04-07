#punto 1:
empleados = ["Marcos","Ana","Luis","Maria"]
sueldo = [
    [540, 540, 760]
    [200, 220, 250]
    [760, 799, 810]
]

#punto 2:
def calculadora_sueldos_totales(sueldos):
    sueldos_totales = []
    
    for fila in sueldos:
        total = 0
        for sueldo in fila:
            total = total + sueldo
        sueldos_totales.append(total)    
    
    return sueldos_totales

