#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from Tkinter import *
import tkFileDialog
import tkMessageBox
import commands
import os
import filecmp as comp

global lab_dir_fon, directoris, path_comu, arxius_comuns
arxius_comuns=[]
directoris=[]
									#	Directoris botons
									#	[0] font
									#	[1]	desti
									#	[2]	comú

		
		
def arxiu_fon():
	global lab_dir_fon, directoris
	directoris[0]= tkFileDialog.askdirectory()
	if directoris[0]:
		lab_dir_fon.configure(text='\t\t'+directoris[0])

def arxiu_des():
	global directoris
	directoris[1] = tkFileDialog.askdirectory()
	if directoris[1]:
		lab_dir_des.configure(text='\t\t'+directoris[1])

def arxius_path(pathf, pathd):	
	llista=[]																#Llista = Contindra els arxius que estan als dos paths
	num_separadors = pathf.count(os.sep)									#Cuento el número de "/" que tiene el path
	for dirpath,dirnames,filenames in os.walk(pathf):						#Hacemos un walk y nos devuelve 3 parametros
		num_separadors_act = dirpath.count(os.sep)							#Contamos el numero de separadores actuales
		if (num_separadors == num_separadors_act): 							#Si nombre de separadors "/" es igual (estem al mateix nivell), llavors afegirem els fitxers
			for i in range(0,len(filenames)):								#Filenames = vector d'arxius que estan en el directori font, comprobem un a un que estiguin en el desti
				if (os.path.isfile(pathd+"/"+filenames[i])):						#Si esta al path_desti, afegim a la llista, l'arxiu en comu
					llista.append(filenames[i])
	return llista

def cercar():
	if(directoris[0] and directoris[1]):
		editArea.delete(0,END)
		editArea_rig_top.delete(0,END)
		editArea_rig_bot.delete(0,END)
		
		#Arxius originals
		global arxius_comuns
		arxius_comuns = arxius_path(directoris[0], directoris[1])			
		for i in range(0,len(arxius_comuns)):
			editArea.insert(END, arxius_comuns[i])
			
		#Archius iguals i semblants
		
		os.chdir(directoris[1])
		#editArea_rig_top.insert(END, os.path.relpath(directoris[1])+"/"+arxius_comuns[i])
		for i in range(0,len(arxius_comuns)):
			if comp.cmp(directoris[0]+"/"+arxius_comuns[i], directoris[1]+"/"+arxius_comuns[i], shallow=False):		#Si son el mateix arxiu
				editArea_rig_top.insert(END, os.path.relpath(directoris[1])+"/"+arxius_comuns[i])
			else:
				editArea_rig_bot.insert(END, os.path.relpath(directoris[1])+"/"+arxius_comuns[i])
	else:
		if directoris[0]:
			msg='\nFalta el directori destí per afegir\n'
		else:
			if directoris[1]:
				msg='\nFalta el directori font per afegir\n'			
			else:
				msg='\nFalten els dos directoris per afegir\n'
		tkMessageBox.showwarning(title='Error', message=msg, icon='warning')	
		return None
def salir():
	msg = tkMessageBox.askquestion(title='Salir', message='\nSegur que vols sortir?\n', icon='warning')
	if msg=='yes':
		finestra.quit()
			
def seleccionar_tots():
	editArea.selection_set(0,END)

def seleccionar_tots_iguals():
	editArea_rig_top.selection_set(0,END)

def seleccionar_tots_sem():
	editArea_rig_bot.selection_set(0,END)

def desseleccionar_tots():
	editArea.selection_clear(0,END)
	
def desseleccionar_tots_iguals():
	editArea_rig_top.selection_clear(0,END)
	
def desseleccionar_tots_sem():
	editArea_rig_bot.selection_clear(0,END)
	
def esborrar_original(nom):
	listbox_original=[]
	listbox_original=editArea.get(0,END)
	for i in range(0,len(listbox_original)):
		if nom==("./"+listbox_original[i]):
			editArea.delete(i)	

def seleccionat(num):
	if num==1:
		if (len(editArea_rig_top.curselection()) != 0):
			return True
	else:
		if (len(editArea_rig_bot.curselection()) != 0):
			return True
	tkMessageBox.showwarning(title='Error', message="\nNo ha fet cap selecció\n", icon='warning')
	return False

def esborra_iguals():
	if seleccionat(1):
		ig_element=editArea_rig_top.selection_get()
		index_ig=editArea_rig_top.curselection()
		path_ig_element=os.path.join(directoris[1], ig_element)
		editArea_rig_top.delete(index_ig)
		esborrar_original(ig_element)
		os.system("rm "+path_ig_element)
	
def esborra_semblants():
	if seleccionat(2):
		sem_element=editArea_rig_bot.selection_get()
		index_sem=editArea_rig_bot.curselection()
		path_sem_element=os.path.join(directoris[1], sem_element)
		editArea_rig_bot.delete(index_sem)
		esborrar_original(sem_element)
		os.system("rm "+path_sem_element)

def renombra():
	os.chdir(directoris[1])
	print nom_nou.get()
	print "mv "+editArea_rig_bot.selection_get()+" "+nom_nou.get()
	os.system("mv "+editArea_rig_bot.selection_get()+" "+nom_nou.get())
		


