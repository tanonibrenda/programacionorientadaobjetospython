import monitor

m = monitor.Monitor("LG", "27 pulgadas", "LED", "HDMI")
print(m.getInfo_marca())
print(m.getInfo_tamano())
print(m.getInfo_tipo_pant())    
print(m.getInfo_conexion())