import jinja2
import binary_hex_data
import gates_data

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "exercise_templateV2.ipynb"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(gates_data.get_data())

text_file = open("gates.ipynb", "w")
text_file.write(outputText)
text_file.close()
