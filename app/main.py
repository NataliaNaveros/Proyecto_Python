from flask import Flask, render_template, request, session, make_response, escape
from flask_sqlalchemy import SQLAlchemy
import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
import sys
import os
import sqlite3
import csv
#import mysql.connector

#Presentado Por:
#Natalia Hernandez
#Leidy Quintero
#Maurico Lopez

#Base de Datos
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/barrios_cali.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)

con = sqlite3.connect('database/barrios_cali.db')
db = pd.read_sql('SELECT Nombre, Estrato_moda FROM barrios_cali',con)
datos_BD = db.iloc[20:50]

#CSV
datos = pd.read_csv('database/Barrios_Cali.csv')
newdata = datos.iloc[20:50]
Nombre = 0
Estrato = 0
#clear = lambda: os.system('cls')

#WS

#url = https://www.datos.gov.co/Ordenamiento-Territorial/-rea-barrios-de-Cali-2015/g76f-wss7

#class barrios_cali(db.Model):
#	Id_barrio = db.Column(db.Integer, primary_key = True)
#	Cod_barrio = db.Column(db.Integer)
#	Cod_comuna = db.Column(db.Integer)
#	Nombre = db.Column(db.String(50))
#	Area = db.Column(db.Float)
#	Perimetro = db.Column(db.Float)
#	Estrato_moda = db.Column(db.Integer)


	
@app.route('/')
def index():
	return render_template('index.html')

#CSV

#--------------------------------------------------------------
#Graficas

@app.route('/csv')
def csv():
	return render_template('csv.html')

@app.route('/bd')
def bd():
	#barrios_cali.query.filter_by(name='Leonidas').first()
	return render_template('bd.html')

@app.route('/ws')
def ws():
	return render_template('ws.html')

@app.route('/lineal')
def lineal():
	Nombre = newdata['Nombre']
	Estrato = newdata['Estrato_moda']
	plt.plot(Nombre,Estrato)
	plt.xticks(rotation=90)
	plt.xlabel('Nombre del Barrio')
	plt.ylabel('Estrato')
	plt.suptitle('Barrios de la ciudad de Cali Valle (CSV)')
	plt.savefig('static/img/lineal.png', pad_inches=0, bbox_inches='tight')
	return render_template('lineal.html', url='/static/img/lineal.png')

@app.route('/columnas')
def columnas():
	Nombre = newdata['Nombre']
	Estrato = newdata['Estrato_moda']
	plt.bar(Nombre, Estrato, align='center', alpha=1)
	plt.xticks(rotation=90)
	plt.xlabel('Nombre del Barrio')
	plt.ylabel('Estrato')
	plt.suptitle('Barrios de la ciudad de Cali Valle (CSV)')
	plt.savefig('static/img/columnas.png',pad_inches=0, bbox_inches='tight')
	return render_template('columnas.html', url='/static/img/columnas.png')

@app.route('/puntos')
def puntos():
	Nombre = newdata['Nombre']
	Estrato = newdata['Estrato_moda']
	plt.scatter(Nombre,Estrato)
	plt.plot(Nombre,Estrato,'b--')
	plt.xticks(rotation=90)
	plt.xlabel('Nombre del Barrio')
	plt.ylabel('Estrato')
	plt.suptitle('Barrios de la ciudad de Cali Valle (CSV)')
	plt.savefig('static/img/puntos.png',pad_inches=0, bbox_inches='tight')
	return render_template('puntos.html', url='/static/img/puntos.png')

@app.route('/circular')
def circular():
	datos1 = pd.read_csv('database/Barrios_Cali.csv')
	newdata1 = datos1.iloc[0:10]
	Nombre = newdata1['Nombre']
	Estrato = newdata1['Estrato_moda']
	plt.suptitle('Barrios de la ciudad de Cali Valle (CSV)')
	plt.pie(Estrato, labels=Nombre, autopct='%1.0f%%',shadow=True,startangle=190)
	plt.savefig('static/img/circular.png',pad_inches=0, bbox_inches='tight')
	return render_template('circular.html', url='/static/img/circular.png')

@app.route('/barras')
def barras():
	Nombre = newdata['Nombre']
	Estrato = newdata['Estrato_moda']
	plt.barh(Nombre,Estrato)
	plt.ylabel('Nombre del Barrio')
	plt.xlabel('Estrato')
	plt.suptitle('Barrios de la ciudad de Cali Valle (CSV)')
	plt.savefig('static/img/barras.png',pad_inches=0, bbox_inches='tight')
	return render_template('barras.html', url='/static/img/barras.png')

#------------------------------------------------------------------
#Limpieza

@app.route('/limpieza_uno')
def limpieza_uno():

	pass


#------------------------------------------------------------------
#Consultas
@app.route('/consulta_uno')
def consulta_uno():
	#datos.iloc[0:20]
	var = newdata
	return render_template('consulta_uno.html',datos = var)


@app.route('/consulta_dos')
def consulta_dos():
	var = pd.read_csv('database/Barrios_Cali.csv', delimiter = ",")
	#for Id_barrio, Cod_barrio, Cod_comuna, Nombre, Area (ha), Perimetro (m), Estrato_moda in var:
	return render_template('consulta_dos.html',datos = var.describe())
    #print date

	#datos.iloc[0:20]
	#var = datos.loc[datos['Estrato_moda']=='2',['Nombre']]
	#		return render_template('consulta_dos.html',datos = var.describe())

@app.route('/consulta_tres')
def consulta_tres():
	#datos.iloc[0:20]
	var = pd.read_csv('database/Barrios_Cali.csv', delimiter = ",")
	variable =var.iloc[0:5]
	return render_template('consulta_tres.html',datos = variable)


@app.route('/consulta_cuatro')
def consulta_cuatro():
	#datos.iloc[0:20]
	var = pd.read_csv('database/Barrios_Cali.csv', delimiter = ",")
	variable =var.iloc[5:10]
	return render_template('consulta_cuatro.html',datos = variable)


@app.route('/consulta_cinco')
def consulta_cinco():
	#datos.iloc[0:20]
	var = pd.read_csv('database/Barrios_Cali.csv', delimiter = ",")
	variable =var.iloc[10:30]
	return render_template('consulta_cinco.html',datos = variable)
#------------------------------------------------------------------
#Exportar



#Base de Datos


@app.route('/lineal_BD')
def lineal_BD():
	Nombre = datos_BD['Nombre']
	Estrato = datos_BD['Estrato_moda']
	plt.plot(Nombre,Estrato)
	plt.xticks(rotation=90)
	plt.xlabel('Nombre del Barrio')
	plt.ylabel('Estrato')
	plt.suptitle('Barrios de la ciudad de Cali Valle (BD)')
	plt.savefig('static/img/lineal_BD.png', pad_inches=0, bbox_inches='tight')
	return render_template('lineal_BD.html', url='/static/img/lineal_BD.png')

@app.route('/columnas_BD')
def columnas_BD():
	Nombre = datos_BD['Nombre']
	Estrato = datos_BD['Estrato_moda']
	plt.bar(Nombre, Estrato, align='center', alpha=1)
	plt.xticks(rotation=90)
	plt.xlabel('Nombre del Barrio')
	plt.ylabel('Estrato')
	plt.suptitle('Barrios de la ciudad de Cali Valle (BD)')
	plt.savefig('static/img/columnas_BD.png',pad_inches=0, bbox_inches='tight')
	return render_template('columnas_BD.html', url='/static/img/columnas_BD.png')

@app.route('/puntos_BD')
def puntos_BD():
	Nombre = datos_BD['Nombre']
	Estrato = datos_BD['Estrato_moda']
	plt.scatter(Nombre,Estrato)
	plt.plot(Nombre,Estrato,'b--')
	plt.xticks(rotation=90)
	plt.xlabel('Nombre del Barrio')
	plt.ylabel('Estrato')
	plt.suptitle('Barrios de la ciudad de Cali Valle (BD)')
	plt.savefig('static/img/puntos_BD.png',pad_inches=0, bbox_inches='tight')
	return render_template('puntos_BD.html', url='/static/img/puntos_BD.png')

@app.route('/circular_BD')
def circular_BD():
	datos_BD1 = db.iloc[0:10]
	Nombre = datos_BD1['Nombre']
	Estrato = datos_BD1['Estrato_moda']
	plt.suptitle('Barrios de la ciudad de Cali Valle')
	plt.suptitle('Barrios de la ciudad de Cali Valle (BD)')
	plt.pie(Estrato, labels=Nombre, autopct='%1.0f%%',shadow=True,startangle=190)
	plt.savefig('static/img/circular_BD.png',pad_inches=0, bbox_inches='tight')
	return render_template('circular_BD.html', url='/static/img/circular_BD.png')

@app.route('/barras_BD')
def barras_BD():
	Nombre = datos_BD['Nombre']
	Estrato = datos_BD['Estrato_moda']
	plt.barh(Nombre,Estrato)
	plt.ylabel('Nombre del Barrio')
	plt.xlabel('Estrato')
	plt.suptitle('Barrios de la ciudad de Cali Valle (BD)')
	plt.savefig('static/img/barras_BD.png',pad_inches=0, bbox_inches='tight')
	return render_template('barras_BD.html', url='/static/img/barras_BD.png')


#Consultas
@app.route('/consulta_BD')
def consulta_BD():
	var = db
	return render_template('consulta_BD.html',datos = var)

@app.route('/consulta_BD_dos')
def consulta_BD_dos():
	conexion = sqlite3.connect('database/barrios_cali.db')
	var = pd.read_sql('SELECT Id_barrio, Nombre FROM barrios_cali',conexion)
	return render_template('consulta_BD_dos.html',datos = var)	

@app.route('/consulta_BD_tres')
def consulta_BD_tres():
	conexion = sqlite3.connect('database/barrios_cali.db')
	var = pd.read_sql('SELECT Cod_barrio, Nombre FROM barrios_cali',conexion)
	return render_template('consulta_BD_tres.html',datos = var)

@app.route('/consulta_BD_cuatro')
def consulta_BD_cuatro():
	conexion = sqlite3.connect('database/barrios_cali.db')
	var = pd.read_sql('SELECT Area, Nombre FROM barrios_cali',conexion)
	return render_template('consulta_BD_cuatro.html',datos = var)

@app.route('/consulta_BD_cinco')
def consulta_BD_cinco():
	conexion = sqlite3.connect('database/barrios_cali.db')
	var = pd.read_sql('SELECT Cod_comuna, Nombre FROM barrios_cali',conexion)
	return render_template('consulta_BD_cinco.html',datos = var)

#-----------------------------------------------------------------------------------
#WS

#Graficos




if __name__ == '__main__':
	#db.create_all()
	del Nombre
	del Estrato 
	app.run(debug=True)
	#clear('Nombre')
	#clear('Estrato')
	os.system('cls')
