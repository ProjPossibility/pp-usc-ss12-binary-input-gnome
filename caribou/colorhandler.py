import gtk

class ColorOptions: #This is basically just an enum
	standard = 0
	morseLeftNode = 1
	morseRightNode = 2
	test = 3

class ColorHandler:
    	class __impl:
        	""" Implementation of the singleton interface within ColorHandler """

		e = gtk.Entry()
		map = e.get_colormap()

		buttonList = dict() #key = letter of the button, value = style of button (that style will use color colorOption)
		morseLeftNodeColor = map.alloc_color("#c1c1f0")
		morseRightNodeColor = map.alloc_color("#f07171")
		standardColor = map.alloc_color("#dddddd")
		testColor = map.alloc_color("#ff00ff")
		colorMap = {ColorOptions.standard: standardColor, ColorOptions.morseLeftNode: morseLeftNodeColor, ColorOptions.morseRightNode: morseRightNodeColor, ColorOptions.test: testColor}  

		def addButton(self, button, colorOption):
			label = button.get_label()
			self.buttonList[label] = button
			self.setColor(button, colorOption)

		def setColorFromEncodedChar(self, encodedchar, colorOption):
			char = unichr(encodedchar)
			self.setColor(self.buttonList.get(char), colorOption)

		def setColor(self, button, colorOption):
			button.modify_bg(gtk.STATE_NORMAL, self.colorMap.get(colorOption))
			button.modify_bg(gtk.STATE_ACTIVE, self.colorMap.get(colorOption))

		def colorAll(self, colorOption):
			for button in self.buttonList.values():
				button.modify_bg(gtk.STATE_NORMAL, self.colorMap.get(colorOption))
				button.modify_bg(gtk.STATE_ACTIVE, self.colorMap.get(colorOption))

    	# storage for the instance reference
    	__instance = None

	 


	def __init__(self):
	        """ Create singleton instance """
	        # Check whether we already have an instance
	        if ColorHandler.__instance is None:
	            # Create and remember instance
	            ColorHandler.__instance = ColorHandler.__impl()

	        # Store instance reference as the only member in the handle
	        self.__dict__['_ColorHandler__instance'] = ColorHandler.__instance
	
	def __getattr__(self, attr):
	        """ Delegate access to implementation """
	        return getattr(self.__instance, attr)

	def __setattr__(self, attr, value):
		""" Delegate access to implementation """
	        return setattr(self.__instance, attr, value)

