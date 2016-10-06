import Censado from DataBase
import datetime

def alta_sensor(tipo_sensor,medicion,hora_sensado,id,id_LiSANDRA):
	sensor = Censado.Censado()
	sensor.set_Type(tipo)
	sensor.set_Value(medicion)
	sensor.set_Time(hora_sensado)
	sensor.set_ID(id)
	sensor.set_LiSANDRA(id_LiSANDRA)
	
def addID(id):
	"""Agrega un nuevo sensor utilizando su id"""
	return Censado.Censado().addID(id)
	
def addLiSANDRA(id_LiSANDRA)
	"""Agrega un nuevo LiSANDRA"""
	return Censado.Censado().addLiSANDRA(id_LiSANDRA)
	
def buscar_Por_Id(id):
	"""Busca un sensor por su id"""
	return Censado.Censado().find_By_Id(id)
	
def buscar_Por_Tipo(tipo_sensor):
	"""Busca un sensor por su tipo humedad,ilumiacion o temperatura"""
	return Censado.Censado().find_By_Id(tipo_sensor)
	
def mostrar_Todo():
	"""Muestra todo ALV"""
	return Censado.Censado().All() 