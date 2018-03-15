#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from Tkinter import *
import os
import tkFileDialog
import tkMessageBox
import functions as fnt

def compara():
	finestra_cmp=Tk()
	finestra_cmp.title("Compara arxius")
	finestra_cmp.geometry("800x800+250+100")
	finestra_cmp.minsize(800,800)
	
	#Frames
	frame_cmp_top=Frame(finestra_cmp, width=800, height=150)
	frame_cmp_top.pack(side=TOP, anchor=W, fill=X)
	
	frame_cmp_bot=Frame(finestra_cmp)
	frame_cmp_bot.pack(side=BOTTOM, anchor=S, fill=X)
	
	frame_cmp_left=Frame(finestra_cmp)
	frame_cmp_left.pack(side=LEFT, anchor=W, fill=BOTH, expand=True)
	
	frame_cmp_right=Frame(finestra_cmp)
	frame_cmp_right.pack(side=LEFT, anchor=W, fill=BOTH, expand=True)
	
	frame_cmp_top_l=Frame(frame_cmp_top, bg='red', width=400, height=150)
	frame_cmp_top_l.pack(side=LEFT, anchor=W)
	
	frame_cmp_top_r=Frame(frame_cmp_top, bg='blue', width=400, height=150)
	frame_cmp_top_r.pack(side=LEFT, anchor=E)
	
	#Widgets Frame TOP
	#lab_top=Label(frame_cmp_top_l, text="Inode i path relatiu font")
	#lab_top.pack(side=TOP, anchor=W)
	'''	
	text_cmp_top=Text(frame_cmp_top_l, height=50)
	text_cmp_top.pack(fill=BOTH, expand=True)
	
	lab_top=Label(frame_cmp_top_r, text="Inode i path relatiu desti")
	lab_top.pack(side=TOP, anchor=W)
	
	text_cmp_top_r=Text(frame_cmp_top_r, height=50)
	text_cmp_top_r.pack(fill=BOTH, expand=True)
	'''
	#Widgets Frame MID
	lab_left=Label(frame_cmp_left, text="Arxiu Font")
	lab_left.pack(side=TOP, anchor=W)
	
	text_cmp_left=Text(frame_cmp_left, width=50)
	text_cmp_left.pack(fill=BOTH, expand=True)
	
	lab_right=Label(frame_cmp_right, text="Arxiu Destí")
	lab_right.pack(side=TOP, anchor=W)
	
	text_cmp_right=Text(frame_cmp_right, width=50)
	text_cmp_right.pack(fill=BOTH, expand=True)
	
	#Widgets Frame BOTTOM
	but_compara = Button(frame_cmp_bot, text = "Compara", width = 6)
	but_compara.pack(side=TOP, anchor=W)
	
	sortir = Button(frame_cmp_bot, text = "Sortir", width = 6)
	sortir.pack(side=BOTTOM, anchor=W)
	'''
	fnt.text_cmp_top=text_cmp_top
	fnt.text_cmp_left=text_cmp_left
	fnt.text_cmp_right=text_cmp_right
	'''
	fnt.inode()
	fnt.obre_arxiu_font()
	fnt.obre_arxiu_desti()
	finestra_cmp.mainloop()
	
#MAIN
finestra= Tk()
finestra.title("Cerca fitxers Redundants")
finestra.minsize(700,450)
finestra.geometry('700x450+250+250')

#Frame TOP(font)
frame_top = Frame(finestra)
frame_top.pack(side=TOP, fill=X)

#Frame TOP_BELOW(desti)
frame_top_below = Frame(finestra)
frame_top_below.pack(side=TOP, fill=X)

#Frame BOTTOM_ABSOLUT
frame_bot_abs = Frame(finestra)
frame_bot_abs.pack(side=BOTTOM, anchor=SW)

#Frame MIDDLE_LEFT (Fitxers originals)
frame_mid_L = Frame(finestra)
frame_mid_L.pack(side=LEFT, anchor=N, fill=Y)

#Frame MIDDLE_TOP (Fitxers iguals)
frame_mid_T = Frame(finestra, padx=5)
frame_mid_T.pack(side=TOP, anchor=N, fill=BOTH, expand=True)

#Frame MIDDLE_BELOW (Fitxers Semblants)
frame_mid_below = Frame(finestra, padx=5)
frame_mid_below.pack(side=BOTTOM, anchor=S, fill=BOTH, expand=True)
	
#Objetos Frame TOP (Font)
dir_fon = Button(frame_top, text = "Escolliu directori font", height=1, width=19, command=fnt.arxiu_fon)
dir_fon.pack(side=LEFT)

lab_dir_fon = Label(frame_top, text=" ", relief=SUNKEN, height=1, anchor=W)
lab_dir_fon.pack(expand=True, fill=X)
		
#Objetos Frame TOP_BELOW(desti)
dir_desti = Button(frame_top_below, text = "Escolliu directori destí", height=1, width=19, command=fnt.arxiu_des)
dir_desti.pack(side=LEFT)

lab_dir_des = Label(frame_top_below, text=" ", relief=SUNKEN, height=1, anchor=W)
lab_dir_des.pack(side=LEFT, expand=True, fill=X)
	
cerca = Button(frame_top_below, text = "Cerca", height=1, width = 6, command=fnt.cercar)
cerca.pack(side=LEFT)

#Objetos Frame MIDDLE_LEFT
fit_ori = Label(frame_mid_L, text="Fitxers Originals:")
fit_ori.pack(side=TOP, anchor=W)

scroll = Scrollbar(frame_mid_L)
scroll.pack(side=RIGHT, fill=Y)
editArea = Listbox(frame_mid_L, width=40, yscrollcommand=scroll.set)
editArea.pack(side=LEFT, anchor=W, fill=BOTH)    
scroll.config(command=editArea.yview)

#Objetos Frame MIDDLE_TOP
fit_ori = Label(frame_mid_T, text="    Fitxers Iguals: ")
fit_ori.pack(side=TOP, anchor=W)
scroll_rig_top = Scrollbar(frame_mid_T)
scroll_rig_top.pack(side=LEFT, fill=Y)
editArea_rig_top = Listbox(frame_mid_T, width=30, height=10, yscrollcommand=scroll_rig_top.set)
editArea_rig_top.pack(side=LEFT, anchor=E, fill=BOTH, expand=True)  
scroll_rig_top.config(command=editArea_rig_top.yview)

esborra = Button(frame_mid_T, text = "Esborra", width = 13, command=fnt.esborra_iguals)
esborra.pack(side=TOP, anchor=E, pady=1)
hdl = Button(frame_mid_T, text = "Hard Link", width = 13, command=fnt.hardlink)
hdl.pack(pady=1)
stl = Button(frame_mid_T, text = "Soft Link", width = 13, command=fnt.softlink)
stl.pack(pady=1)
selt = Button(frame_mid_T, text = "Selec Tots", width = 13, command=fnt.seleccionar_tots_iguals)
selt.pack(pady=1)
selc = Button(frame_mid_T, text = "Selec Cap", width = 13, command=fnt.desseleccionar_tots_iguals)
selc.pack(pady=1)

#Objetos Frame MIDDLE_BELOW
fit_sem = Label(frame_mid_below, text="    Fitxers Semblants: ")
fit_sem.pack(side=TOP, anchor=W)

scroll_rig_bot = Scrollbar(frame_mid_below)
scroll_rig_bot.pack(side=LEFT, fill=Y)
editArea_rig_bot = Listbox(frame_mid_below, width=30, height=10, yscrollcommand=scroll_rig_bot.set)
editArea_rig_bot.pack(side=LEFT, anchor=E, fill=BOTH, expand=True) 
scroll_rig_bot.config(command=editArea_rig_bot.yview)

compara = Button(frame_mid_below, text = "Compara", width = 13, command=compara)
compara.pack(pady=1)
renom = Button(frame_mid_below, text = "Renombra", width = 13, command=fnt.renombra)
renom.pack(pady=1)
esborra = Button(frame_mid_below, text = "Esborra", width = 13, command=fnt.esborra_semblants)
esborra.pack(pady=1)
selectots = Button(frame_mid_below, text = "Selec Tots", width = 13, command=fnt.seleccionar_tots_sem)
selectots.pack(pady=1)
seleccap = Button(frame_mid_below, text = "Selec Cap", width = 13, command=fnt.desseleccionar_tots_sem)
seleccap.pack(pady=1)
	
#Objetos Frame BOTTOM_ABSOLUT
sortir = Button(frame_bot_abs, text = "Sortir", width = 6, command=fnt.salir, activebackground='red')
sortir.pack(side=BOTTOM, anchor=W)
sel_tots = Button(frame_bot_abs, text = "Selecciona Tots", width = 13, command=fnt.seleccionar_tots)
sel_tots.pack(side=LEFT, anchor=W)
sel_cap = Button(frame_bot_abs, text = "Selecciona Cap", width = 13, command=fnt.desseleccionar_tots)
sel_cap.pack(side=LEFT, anchor=E)

'''Asignacion de variables'''
fnt.directoris[0:1]=False, False
(fnt.lab_dir_fon,fnt.lab_dir_des) = (lab_dir_fon,lab_dir_des)
fnt.editArea, fnt.editArea_rig_top, fnt.editArea_rig_bot = editArea, editArea_rig_top, editArea_rig_bot
fnt.finestra= finestra
finestra.mainloop()
