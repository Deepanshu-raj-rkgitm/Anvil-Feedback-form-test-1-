from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    name = self.name_box.text
    email = self.email_box.text
    feedback = self.feedback_box.text
    
    anvil.server.call('add_feedback', name, email, feedback)
    Notification("Feedback Submitted!").show()
    self.clear_inputs()

  def clear_inputs(self):
    self.name_box.text=""
    self.email_box.text=""
    self.feedback_box.text=""

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

