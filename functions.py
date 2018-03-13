#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from Tkinter import *
import tkFileDialog
import tkMessageBox
import commands
import os

global lab_dir_fon, directoris, path_comu
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

def arxius_path(path):
	llista=[]
	num_separadors = path.count(os.sep)
	for dirpath,dirnames,filesname in os.walk(path):
		num_separadors_act = dirpath.count(os.sep)
		if num_separadors == num_separadors_act: 			#	Si nombre de separadors es igual (estem al mateix nivell), imprimim els fitxers
			llista.append(filesname)
	return llista

def cercar():
	if(directoris[0] and directoris[1]):
		#Arxius font
		arxius_font=arxius_path(directoris[0])				#	Arxius font
		arxius_desti=arxius_path(directoris[1])				#	Arxius desti
		if ()
		
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

