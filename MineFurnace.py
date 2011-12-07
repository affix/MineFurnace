#!/usr/bin/env python
#
#  Title  : MineFurnace
#  Author : Keiran "Affix" Smith
#  Date   : 7/12/2011
#  Description :
# 	Calculates how many items are required to smelt in minecraft
#	Based on http://minecraftforum.net/topic/824008-furnacecalc-tool
#
#  Requires : 
#	PyGTK
#	GTK+ >= 2
#

import sys
try:
	import pygtk
	pygtk.require("2.0")
except:
	pass

try:
	import gtk
	import gtk.glade
except:
	print("GTK Not Available on this system!")
	sys.exit(1)

class MineFurnace:
	builder = None
	
	def __init__( self ):
		self.builder = gtk.Builder()
		self.builder.add_from_file("./ui/ui.glade")
		self.window = self.builder.get_object("window")
		self.builder.connect_signals(self)

	def on_btnCalc_clicked(self, widget):
		amount = self.builder.get_object("txtHowMany").get_text()
		bucketCount = float(amount) * 0.005
		self.builder.get_object("lblBucket").set_text(str(bucketCount))
		coalCount = float(amount) * 0.125
		self.builder.get_object("lblCoal").set_text(str(coalCount))
		woodCount = float(amount) * 0.67
		self.builder.get_object("lblWood").set_text(str(woodCount))
		stickCount = float(amount) * 2
		self.builder.get_object("lblStick").set_text(str(stickCount))
		rodCount = float(amount) * 0.083
		self.builder.get_object("lblRod").set_text(str(rodCount))
		
	def on_window_destroy(self, widget):
		sys.exit(1)

if __name__ == "__main__":	
	MineFurnace = MineFurnace()
	MineFurnace.window.show()
	gtk.main()
	sys.exit(1)
