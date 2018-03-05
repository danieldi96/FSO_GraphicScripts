#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from Tkinter import *
import tkFileDialog
import tkMessageBox
import commands
import os

global font, desti, lab_dir_fon, nomdir_font

def arxiu_fon():
	global font, lab_dir_fon, nomdir_font
	font=True
	nomdir_font = tkFileDialog.askdirectory()
	lab_dir_fon.configure(text='\t\t'+nomdir_font)

def arxiu_des():
	global desti
	desti=True
	lab_dir_des.configure(text='\t\t'+tkFileDialog.askdirectory())

def cercar():
	if(font and desti):
		os.chdir(nomdir_font)
		#print os.walk('.', topdown=False)
		#Aqui hay que utilizar un os.walk() 
		#recorre el arbol del path de arriba-abajo
		#o de abajo-arriba por cada subdirectorio
		fitxers_originals = commands.getoutput('find . -type f -exec md5sum {} + | sort | uniq -w32 -dD | tr -s " " | cut -d " " -f 2')
		if fitxers_originals:
			editArea.delete(0,END)						
			for i in fitxers_originals.split():
				editArea.insert(END, i)
	else:
		if font:
			msg='\nFalta el directori destí per afegir\n'
		else:
			if desti:
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

