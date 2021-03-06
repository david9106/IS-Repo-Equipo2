import logging
import LimitHandler
from Handlers import PhoneHandler
import json
import webapp2
import sms

#function receives a dictionary
def compararLimites(data):
	#It represents the type of sensor unit
	unit =""
	#adjust values from data
	data['Tipo']=str(data['Tipo'])
	data['Valor']=float(data['Valor'])
	data['Ubicacion']=int(data['Ubicacion'])
	#get a phone list from bd
	phoneList=PhoneHandler.get_allEnable_Phones()
	#get max and min values from a type of sensor from bd
	limitMax=LimitHandler.get_Max_Value(data['Tipo'])
	limitMin=LimitHandler.get_min_Value(data['Tipo'])
	
	#adjust the unit based on the type of sensor
	if data['Tipo'] == 'temperatura':
		unit = "grados Centigrados"
	if data['Tipo'] == 'humedad':
		unit = "% humedad relativa"
	if data['Tipo'] == 'luz':
		unit = "luxes"
	if data['Tipo'] == 'co2':
		unit = "ppm"
	logging.info("Telefonos: ")
	for phone in phoneList:
		logging.info(phone.user_phone)
	logging.info("diccionario:")
	logging.info(data)
	logging.info("Limites- Tipo:"+str(type(limitMax))+" "+str(limitMax)+" ,Tipo: "+str(type(limitMin))+" "+str(limitMin))

	#compare whether the values are not within the established limits

	if data['Valor'] > limitMax and limitMax != None and limitMax != False:
		#build a message
		info= "La "+data["Tipo"] +" sobrepaso del limite establecido de "+ str(limitMax)+" "+unit+" Valor actual: "+str(data['Valor'])
		#send message to every phone on phone list
		for phone in phoneList:
			sms.sendMsg(str(phone.user_phone),info)


	if data['Valor'] < limitMin and limitMin != None and limitMin != False:
		#build a message
		info= "La "+data["Tipo"] +" esta por debajo del limite establecido de"+ str(limitMin)+" "+unit+" Valor actual: "+str(data['Valor'])
		#send message to every phone on phone list
		for phone in phoneList:
			sms.sendMsg(str(phone.user_phone),info)

	
