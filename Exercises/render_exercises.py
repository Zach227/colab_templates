import jinja2
import binary_hex_data
import gates_data

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "notebook_template.txt"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(binary_hex_data.get_data())

text_file = open("binary_hex.ipynb", "w")
text_file.write(outputText)
text_file.close()

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "notebook_template.txt"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(gates_data.get_data())

text_file = open("gates.ipynb", "w")
text_file.write(outputText)
text_file.close()