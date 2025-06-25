def read_file_to_dict(filename):
    diccionario = {}
    try:
        with (open(filename, "r")) as file:
            line = file.readline().strip() 
            prod_y_valor = line.split(";") 
            for element in prod_y_valor:
                if ":" in element: 
                    producto, valor = element.split(":") 
                    valor = float(valor) 
                    if producto not in diccionario:
                        diccionario[producto] = [valor] 
                    else:
                        diccionario[producto].append(valor)
    except FileNotFoundError: 
        print ("Archivo no encontrado")
        raise
    return diccionario

def process_dict(data):
    for key, value in data.items():
        ventas_totales = 0 
        for element in value:
            ventas_totales += element
        promedio = ventas_totales/len(value)
        print (f"{key}: ventas totales ${ventas_totales:.2f}, promedio ${promedio:.2f}")
    return None
