#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from Tkinter import *
import tkFileDialog
import tkMessageBox
import commands
import os
import filecmp as comp

global lab_dir_fon, directoris, path_comu, arxius_comuns, string_ln, index_ln, trash, slink, path
path=[]
string_ln=[]
arxius_comuns=[]
directoris=[]
									#	Directoris botons
									#	[0] font
									#	[1]	desti
									#	[2]	comú

def errores(path):
	global trash, slink
	trash,slink=False, False	
	if os.path.islink(path):
		slink=True	
		
def arxiu_fon():
	global lab_dir_fon, directoris
	directoris[0]= tkFileDialog.askdirectory()
	if directoris[0]:
		lab_dir_fon.configure(text='\t\t'+directoris[0])
	errores(directoris[0])
	path[0]=directoris[0].replace(" ", "\ ")

def arxiu_des():
	global directoris
	directoris[1] = tkFileDialog.askdirectory()
	if directoris[1]:
		lab_dir_des.configure(text='\t\t'+directoris[1])
	errores(directoris[1])
	if directoris[1]==".local/share/Trash/files":	
		tkMessageBox.showwarning(title="Warning",message="\nAquest path correspon a la paperera\n")	
		trash=True		
	path[1]=directoris[1].replace(" ", "\ ")

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
		if not trash and not slink:
			if os.path.isdir(directoris[0]) and os.path.isdir(directoris[1]):
				editArea.delete(0,END)
				editArea_rig_top.delete(0,END)
				editArea_rig_bot.delete(0,END)
				
				#Arxius originals
				global arxius_comuns
				arxius_comuns = arxius_path(directoris[0], directoris[1])			
				for i in range(0,len(arxius_comuns)):
					editArea.insert(END, arxius_comuns[i])
					
				#Archius iguals i semblants
				if not trash:
					os.chdir(directoris[1])
					for i in range(0,len(arxius_comuns)):
						if comp.cmp(directoris[0]+"/"+arxius_comuns[i], directoris[1]+"/"+arxius_comuns[i], shallow=False):		#Si son el mateix arxiu
							editArea_rig_top.insert(END, os.path.relpath(directoris[1])+"/"+arxius_comuns[i])
						else:
							editArea_rig_bot.insert(END, os.path.relpath(directoris[1])+"/"+arxius_comuns[i])
			else:
				if os.path.isdir(directoris[0]):
					msg="\nEl directori desti no existeix\n"
				elif os.path.isdir(directoris[1]):
					msg="\nEl directori font no existeix\n"
				else:
					msg="\nNo exiteixen cap dels dos directoris\n"
				tkMessageBox.showerror(title="ERROR",message=msg)
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
	if tkMessageBox.askquestion(title='Salir', message='\nSegur que vols sortir?\n', icon='warning')=='yes':
		finestra.quit()

def seleccionat(num):
	if num==0:
		if (len(editArea.curselection()) != 0):
			return True
	if num==1:
		if (len(editArea_rig_top.curselection()) != 0):
			return True
	else:
		if (len(editArea_rig_bot.curselection()) != 0):
			return True
	tkMessageBox.showwarning(title='Error', message="\nNo ha fet cap selecció\n", icon='warning')
	return False
					
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

def esborra_iguals():
	if seleccionat(1):
		index_ig=editArea_rig_top.curselection()								#Conseguimos el rango de items seleccionados
		for i in index_ig:
			ig_element=editArea_rig_top.get(index_ig[0])						#Apuntamos siempre a la posición 0 del indice, porque al eliminar una posición de una listbox, todos los elementos de abajo suben 1 posición
			string=ig_element[2:]												#Eliminamos el ./
			path_ig_element=os.path.join(directoris[1], string)					#Concatenem path_treball+path_relatiu=path_abolut_fitxer
			editArea_rig_top.delete(index_ig[0])
			esborrar_original(ig_element)
			os.system("rm "+path_ig_element)
	
def esborra_semblants():
	if seleccionat(2):
		index_sem=editArea_rig_bot.curselection()
		for i in index_sem:
			sem_element=editArea_rig_bot.get(index_sem[0])
			string=sem_element[2:]
			path_sem_element=os.path.join(directoris[1], string)
			editArea_rig_bot.delete(index_sem[0])
			esborrar_original(sem_element)
			os.system("rm "+path_sem_element)
					

def renombra():
	if seleccionat(2):
		finestra_renom=Toplevel()
		finestra_renom.title("Renombra el fitxer")
		finestra_renom.geometry("300x50+500+400")
		finestra_renom.resizable(0,0)
		frame_renom = Frame(finestra_renom)
		frame_renom.pack(fill=BOTH)
		nou_nom=StringVar()
		ent_renom=Entry(frame_renom, textvariable=nou_nom)
		ent_renom.pack(anchor=CENTER, fill=X,expand=True)
		
		def actual_nom():
			if len(editArea_rig_bot.get(0,END))!=0:
				os.chdir(directoris[1])
				vell_nom=editArea_rig_bot.selection_get()
				os.system("mv "+vell_nom+" "+nou_nom.get())
				esborrar_original(vell_nom)					
				sel_rem=editArea_rig_bot.curselection()
				editArea_rig_bot.delete(sel_rem)
			else:
				error_ent=StringVar()
				error_ent.set("ERROR. No hi ha items a la llista")
				ent_renom.config(background='red', textvariable=error_ent, justify=CENTER)
					
		but_renom_sortir=Button(frame_renom, text="Sortir", command=finestra_renom.destroy)
		but_renom_sortir.pack(side=RIGHT)	
		but_renom=Button(frame_renom, text="Aplicar", command=actual_nom)
		but_renom.pack(side=RIGHT)
		
		finestra_renom.mainloop()

def borrat_ln(numero):
	if seleccionat(1):
		global string_ln, index_ln														
		index_ln=editArea_rig_top.curselection()
		for i in index_ln:															
			ln_element=editArea_rig_top.get(index_ln[i])
			string_ln.append(ln_element[2:])
			path_element=os.path.join(directoris[1], string_ln[i])
			if os.path.isfile(path_element):
				os.system("rm "+path_element)
			if numero==1:
				os.system("ln "+directoris[0]+"/"+string_ln[i]+" "+string_ln[i])
			else:
				os.system("ln -s "+directoris[0]+"/"+string_ln[i]+" "+string_ln[i])			

def hardlink():
	if seleccionat(1):
		borrat_ln(1)
	
def softlink():
	if seleccionat(1):
		borrat_ln(2)

def inode(num):
	sel_inode=editArea_rig_bot.selection_get()
	os.chdir(directoris[num])
	print "diff -y --suppress-common-lines "+sel_inode+" "+path[1-num]+"/"+sel_inode[2:]+" | wc -l"
	num_lineas=commands.getoutput("diff -y --suppress-common-lines "+sel_inode+" "+path[1-num]+"/"+sel_inode[2:]+" | wc -l")
	if num==0:
		text_cmp_top.insert(INSERT, "Inode: "+commands.getoutput("stat -c '%i' "+path[num]+"/"+sel_inode[2:])+"\nPath relatiu: "+sel_inode+"\nNombre de línies diferents: "+num_lineas+"\n")
	else:
		text_cmp_top_r.insert(INSERT, "Inode: "+commands.getoutput("stat -c '%i' "+path[num]+"/"+sel_inode[2:])+"\nPath relatiu: "+sel_inode+"\nNombre de línies diferents: "+num_lineas+"\n")
		
def obre_arxiu_font():
	listbox_original=[]
	listbox_original=editArea.get(0,END)
	for i in range(0,len(listbox_original)):
		if editArea_rig_bot.selection_get()==("./"+listbox_original[i]):
			sel_cmp=listbox_original[i]
	with open(directoris[0]+"/"+sel_cmp, 'r') as f:
		text_cmp_left.insert(INSERT, f.read())
		
def obre_arxiu_desti():
	with open(directoris[1]+"/"+editArea_rig_bot.selection_get()[2:], 'r') as f:
		text_cmp_right.insert(INSERT, f.read())
		
def comparar_modificar():
	os.chdir(directoris[0])
	sel_inode=editArea_rig_bot.selection_get()
	os.system("vimdiff "+sel_inode+" "+path[1]+"/"+sel_inode[2:])
	#text_cmp_left.insert(INSERT, commands.getoutput("vimdiff "+sel_inode))
	
