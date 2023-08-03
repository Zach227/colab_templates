import jinja2
import dataflow_data
import seven_segment_data
import gates_data
import stopwatch_data

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "lab_template.txt"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(dataflow_data.get_data())

text_file = open("dataflow_lab.ipynb", "w")
text_file.write(outputText)
text_file.close()

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "lab_template.txt"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(seven_segment_data.get_data())

text_file = open("seven_segment_lab.ipynb", "w")
text_file.write(outputText)
text_file.close()

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "lab_template.txt"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(gates_data.get_data())

text_file = open("gates_lab.ipynb", "w")
text_file.write(outputText)
text_file.close()

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "lab_template.txt"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(stopwatch_data.get_data())

text_file = open("stopwatch_lab.ipynb", "w")
text_file.write(outputText)
text_file.close()