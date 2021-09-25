import os
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette	# For Colorschemes
import sqlite3 as db

''' 
Classes
'''
class TestBench():
	"""
	My TestBench for testing concepts and ideas
	"""
	def __init__(self):
		print("TestBench")

class PracticeGround():
	"""
	My PracticeGround for practicing ideas/concepts and learning points
	"""
	def __init__(self):
		print("PracticeGround")

class LearningRoom():
	"""
	My LearningRoom for applying tutorials, guides and learning stuff in general
	"""
	def __init__(self):
		print("LearningRoom")
	
	class Qt5():
		def __init__(self, qapp_params=None):
			"""
			Initialize Application

			:: Params
				qapp_params
					Data Type: List
					Description: Parameters for Application object
			"""
			global designers, widget_creator, app_ctrl
			# Initialize classes
			designers = self.Designers()
			widget_creator = designers.Create()
			app_ctrl = designers.App()

			# Initialize other variables
			self.app = self.create_app()

		def create_app(self, qapp_params=None):
			"""
			Create Application

			:: Params
				qapp_params
					Type: List
					Description: The Application parameters
			"""

			# Default
			if qapp_params == None:
				qapp_params = []

			# Create App
			app = QApplication(qapp_params)
			return app

		def show_widget(self, widget=None):
			"""
			Display Widget/Window in Application
			"""
			if not (widget == None):
				widget.show()

		def addwidgets(self, layout=None, widgets=None):
			"""
			Add multiple widgets at once
			:: Params
				widgets
					[1]
						Data Type: Dictionary
						Description: The Widget you wish to add to the layout and its parameters
						Syntax:
							widget-type: String; Your Widget's type {Label|Button}
							widget-n-id: String; Your Widget's Name
							widget-params: List; Your Widget's Parameters

							{
								"<widget-type>" : {
									"widget-n-id" : [<widget-params>],
								}
							}
						Examples:
							{
								"Button" : {
									"btn-1" : ["Top"],
									"btn-2" : ["Bottom"],
								}
							}
			:: Returns
				Type: List
					[0] : The Layout object itself
					[1] : A dictionary containing the widget_id mapped to the created widget according to its provided parameters
				Syntax:
					[
						<layout-object>,
						{
							"<widget-id>" : <widget-object>
						}
					]
			"""

			# --- Input
			widgets_added = {}

			# --- Processing
			for k,v in widgets.items():
				curr_widget_type = k
				curr_widget_object = v
				
				for curr_widget_id, curr_widget_param in curr_widget_object.items():
					checkstr = curr_widget_type.lower()
					if checkstr == "button":
						tmp_widget = QPushButton(*curr_widget_param)
						layout.addWidget(tmp_widget)
					elif checkstr == "label":
						tmp_widget = QLabel(*curr_widget_param)
						layout.addWidget(tmp_widget)

					# Archive added widgets and their ID
					widgets_added[curr_widget_id] = tmp_widget

			# --- Output
			return [layout, widgets_added]

		def set_layout(self, win=None, layout=None):
			"""
			Wrapper for window.setLayout()

			To set the designed QVBoxLayout() into the window (QWidget)
			"""
			if win == None:
				# Default Value
				win = QWidget()

			if not (layout == None):
				win.setLayout(layout)

			return win

		def exec_app(self, appl=None):
			"""
			Wrapper to execute application with just 1 function
			"""
			if not (appl == None):
				appl.exec()

		class Designers():
			"""
			Self-wrapped designer classes
			"""
			class Create():
				"""
				Create Widgets
				"""
				def labels(self, params=None):
					"""
					Design Labels
					"""
					lb_res = None
					if type(params) == type(list):
						lb_res = QLabel(*params)
					elif type(params) == type(dict):
						lb_res = QLabel(**params)
					else:
						lb_res = QLabel(params)
					return lb_res

				def buttons(self, params=None):
					"""
					Design Buttons
					"""
					btn_res = None
					if type(params) == type(list):
						btn_res = QPushButton(*params)
					elif type(params) == type(dict):
						btn_res = QPushButton(**params)
					else:
						btn_res = QPushButton(params)
					return btn_res
				
				def personal(self, widget_type=None, params=None):
					"""
					Design a Widget of your choice with a single function

					:: Params
						widget_type
							Type: String
							Description: The Widget you wish to use
								Window: QWidget()
								Button: QPushButton()
								Label: QLabel()

						params
							Type: Dictionary|List
							Description: Your Widget Parameters
					"""
					res = None

					# Default
					if params == None:
						params = {}

					target_widget_type = widget_type.lower()
					if target_widget_type == "window":
						if type(params) == type(dict):
							res = QWidget(**params)
						elif type(params) == type(list):
							res = QWidget(*params)
						else:
							res = QWidget(params)
					elif target_widget_type == "layout":
						if type(params) == type(dict):
							res = QVBoxLayout(**params)
						elif type(params) == type(list):
							res = QVBoxLayout(*params)
						else:
							res = QVBoxLayout(params)
					elif target_widget_type == "button":
						if type(params) == type(dict):
							res = QPushButton(**params)
						elif type(params) == type(list):
							res = QPushButton(*params)
						else:
							res = QPushButton(params)
					elif target_widget_type == "label":
						if type(params) == type(dict):
							res = QLabel(**params)
						elif type(params) == type(list):
							res = QLabel(*params)
						else:
							res = QLabel(params)
					return res

			class App():
				"""
				Design Application
				"""
				def style(self, app, style_params=None):
					"""
					Design application styles

					:: Params
						app
							Type: QApplication([])
							Description: Your Application object

						style_params
							Type: String
							Description: The application style
							Options: 'Fusion', 'Windows', 'WindowsVista', 'Macintosh'
					"""
					app.setStyle(style_params)

				def color(self, app, palette=None, color=None):
					"""
					Set application palette colorscheme
					:: Params
						palette
							Type: QPalette()
							Description: The palette widget to hold colours

						color
							Types: {List|Dictionary}
							Description: The parameters for setColor()
							[1] Dictionary
								keys: acg, acr, acolor, GlobalColor

							[2] List
								Syntax:
									Area to change color, Color
								Options: 
									QPalette.ButtonText --> Font color

					:: Returns
						Type: List
						Index
							[0]: Application Object after setting color
							[1]: Palette Widget
					"""
					if palette == None:
						palette = QPalette()

					if not(color == None):
						if type(color) == type(dict):
							palette.setColor(**color)
						elif type(color) == type(list):
							palette.setColor(*color)
					else:
						palette.setColor()
					
					app.setPalette(palette)
					return [app, palette]

			
		def test1_helloworld(self):	
			# Design Label
			lb_helloworld = widget_creator.labels("Hello World")
			# self.show_widget(lb_helloworld)
			self.show_widget(lb_helloworld)

			# Start Application
			self.exec_app(self.app)

		def test2_btnlayout(self):
			# Create a Window
			window = widget_creator.personal("window")

			# Create a Layout (Container)
			layout = widget_creator.personal("layout")

			# Design Widgets and place into Layout (container)
			widgets = {
				"button":
					{
						"btn-1" : ["Top"], 
						"btn-2" : ["Middle"],
						"btn-3" : ["Bottom"]
					}
			}
			layout = self.addwidgets(layout, widgets)

			# Place Container into Window
			window = self.set_layout(window, layout[0])

			# Show the Window when application executes
			self.show_widget(window)

			# Execute the application
			self.exec_app(self.app)

		def test3_palette(self):
			app_ctrl.style(self.app, "Fusion")
			app_styleset = app_ctrl.color(self.app, None, [QPalette.ButtonText, Qt.red])
			palette = app_styleset[1]
			btn_helloworld = widget_creator.personal("Button", "Hello World")
			self.show_widget(btn_helloworld)
			self.exec_app(self.app)

'''
Body
'''
def init():
	"""
	Initialize variables / settings / configs on startup
	"""
	global tb, pg, lr, qt5
	tb = TestBench()
	pg = PracticeGround()
	lr = LearningRoom()
	qt5 = lr.Qt5()

def setup():
	"""
	Do basic setups - i.e. setup, populating data etc.
	"""
	init()


def main():
	print("Hello World")
	qt5.test3_palette()
	

if __name__ == "__main__":
	setup()
	main()