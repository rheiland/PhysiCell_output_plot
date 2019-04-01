 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}

        param_name1 = Button(description='tumor_radius', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.tumor_radius = FloatText(
          value=250.0,
          step=10,
          style=style, layout=widget_layout)

        param_name2 = Button(description='oncoprotein_mean', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.oncoprotein_mean = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name3 = Button(description='oncoprotein_sd', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.oncoprotein_sd = FloatText(
          value=0.25,
          step=0.01,
          style=style, layout=widget_layout)

        param_name4 = Button(description='oncoprotein_min', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.oncoprotein_min = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name5 = Button(description='oncoprotein_max', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.oncoprotein_max = FloatText(
          value=2,
          step=0.1,
          style=style, layout=widget_layout)

        param_name6 = Button(description='random_seed', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.random_seed = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name7 = Button(description='cancerous_astrocyte_non_motile_speed', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.cancerous_astrocyte_non_motile_speed = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name8 = Button(description='cancerous_astrocyte_apoptosis_rate', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.cancerous_astrocyte_apoptosis_rate = FloatText(
          value=4.065e-5,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name9 = Button(description='cancerous_astrocyte_cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.cancerous_astrocyte_cell_cell_adhesion_strength = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name10 = Button(description='microglia_motile_speed', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.microglia_motile_speed = FloatText(
          value=2,
          step=0.1,
          style=style, layout=widget_layout)

        param_name11 = Button(description='microglia_macrophage_biasing_detection_threshold', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.microglia_macrophage_biasing_detection_threshold = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name12 = Button(description='transfer_to_cancerous_threshold', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.transfer_to_cancerous_threshold = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        units_button1 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'

        desc_button1 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'

        row1 = [param_name1, self.tumor_radius, units_button1, desc_button1] 
        row2 = [param_name2, self.oncoprotein_mean, units_button2, desc_button2] 
        row3 = [param_name3, self.oncoprotein_sd, units_button3, desc_button3] 
        row4 = [param_name4, self.oncoprotein_min, units_button4, desc_button4] 
        row5 = [param_name5, self.oncoprotein_max, units_button5, desc_button5] 
        row6 = [param_name6, self.random_seed, units_button6, desc_button6] 
        row7 = [param_name7, self.cancerous_astrocyte_non_motile_speed, units_button7, desc_button7] 
        row8 = [param_name8, self.cancerous_astrocyte_apoptosis_rate, units_button8, desc_button8] 
        row9 = [param_name9, self.cancerous_astrocyte_cell_cell_adhesion_strength, units_button9, desc_button9] 
        row10 = [param_name10, self.microglia_motile_speed, units_button10, desc_button10] 
        row11 = [param_name11, self.microglia_macrophage_biasing_detection_threshold, units_button11, desc_button11] 
        row12 = [param_name12, self.transfer_to_cancerous_threshold, units_button12, desc_button12] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML
        self.tumor_radius.value = float(uep.find('.//tumor_radius').text)
        self.oncoprotein_mean.value = float(uep.find('.//oncoprotein_mean').text)
        self.oncoprotein_sd.value = float(uep.find('.//oncoprotein_sd').text)
        self.oncoprotein_min.value = float(uep.find('.//oncoprotein_min').text)
        self.oncoprotein_max.value = float(uep.find('.//oncoprotein_max').text)
        self.random_seed.value = int(uep.find('.//random_seed').text)
        self.cancerous_astrocyte_non_motile_speed.value = float(uep.find('.//cancerous_astrocyte_non_motile_speed').text)
        self.cancerous_astrocyte_apoptosis_rate.value = float(uep.find('.//cancerous_astrocyte_apoptosis_rate').text)
        self.cancerous_astrocyte_cell_cell_adhesion_strength.value = float(uep.find('.//cancerous_astrocyte_cell_cell_adhesion_strength').text)
        self.microglia_motile_speed.value = float(uep.find('.//microglia_motile_speed').text)
        self.microglia_macrophage_biasing_detection_threshold.value = float(uep.find('.//microglia_macrophage_biasing_detection_threshold').text)
        self.transfer_to_cancerous_threshold.value = float(uep.find('.//transfer_to_cancerous_threshold').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML 
        uep.find('.//tumor_radius').text = str(self.tumor_radius.value)
        uep.find('.//oncoprotein_mean').text = str(self.oncoprotein_mean.value)
        uep.find('.//oncoprotein_sd').text = str(self.oncoprotein_sd.value)
        uep.find('.//oncoprotein_min').text = str(self.oncoprotein_min.value)
        uep.find('.//oncoprotein_max').text = str(self.oncoprotein_max.value)
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//cancerous_astrocyte_non_motile_speed').text = str(self.cancerous_astrocyte_non_motile_speed.value)
        uep.find('.//cancerous_astrocyte_apoptosis_rate').text = str(self.cancerous_astrocyte_apoptosis_rate.value)
        uep.find('.//cancerous_astrocyte_cell_cell_adhesion_strength').text = str(self.cancerous_astrocyte_cell_cell_adhesion_strength.value)
        uep.find('.//microglia_motile_speed').text = str(self.microglia_motile_speed.value)
        uep.find('.//microglia_macrophage_biasing_detection_threshold').text = str(self.microglia_macrophage_biasing_detection_threshold.value)
        uep.find('.//transfer_to_cancerous_threshold').text = str(self.transfer_to_cancerous_threshold.value)
