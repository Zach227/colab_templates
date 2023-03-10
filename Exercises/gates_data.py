class Question:
    def __init__(self, title, code):
        self.title = title
        self.code = []


data = {
    "main_file_name": "gates",
    "frq_file_name": "frq_gates",
    "tt_file_name": "tt_gates",
    "intro_title": "Logic Gates",
    "intro_body": [
        "After learning about boolean algebra, it's time to see how we can actually use it in computers.",
        "You can use logic gates to implement boolean logic in hardware to help computers make decisions.",
        "A simple logic gate will have 2 inputs, and 1 output.",
        "These inputs and outputs represent digital signals.",
        "The signals can either be high or low.",
        "High means that the signal has a positive voltage.",
        "This is represented as a 1, and is the same as 'true' when using boolean logic.",
        "Low means that the signal has not voltage.",
        "This can be represented as a 0, or 'false' when using bolean logic.",
        "When you put a bunch of these gates together is strategic ways, you can create complex systems that make up computers.",
    ],
    "section1_title": "AND, OR, NOT",
    "section1_body": [
        "These gates should be a review of the ideas you learned about with boolean algebrea in the previes section.",
        "Here you will learn the symbols we use to represent each type of gate in diagrams.",
        "<p align='left'>",
        "<img src='https://raw.githubusercontent.com/byuccl/digital_design_colab2/master/Exercises/gates/media/andgate.png'",
        "width='250' height=' style='display: block; margin: 0 auto' />",
        "</p>",
        " ",
        "AND: The output is high when both inbuts a, and b are high.",
        "Otherwise, the output is low.",
        " ",
        "<p align='left'>",
        "<img src='https://raw.githubusercontent.com/byuccl/digital_design_colab2/master/Exercises/gates/media/orgate.png'",
        "width='250' height=' style='display: block; margin: 0 auto' />",
        "</p>",
        "OR: The output is high when either one of the inputs is high.",
        "If both inputs are low, the output is low.",
        "<p align='left'>",
        "<img src='https://raw.githubusercontent.com/byuccl/digital_design_colab2/master/Exercises/gates/media/notgate.png'",
        "width='250' height=' style='display: block; margin: 0 auto' />",
        "</p>",
        "NOT: The output is alwasys the oposite of the input.",
    ],
    "section1_quiz_title": "Fill out the truth tables below",
    "section1_questions": [
        Question("Truth Tables", ["print_tt_grid(1)", "print_tt_grid(2)", "print_tt_grid(3)"])
    ],
    "section2_exists": True,
    "section2_title": "NAND, NOR, XOR, XNOR",
    "section2_body": [
        "Array of strings, one for each sentence",
    ],
    "section2_quiz_title": "Try filling out the truth tables for these new gates",
    "section2_questions": [
        Question("Put question title here", ["Put code to create widget here"])
    ],
    "section3_exists": True,
    "section3_title": "Complex Diagrams",
    "section3_body": [
        "Array of strings, one for each sentence",
    ],
    "section3_quiz_title": "Questions",
    "section3_questions": [
        Question("Put question title here", ["Put code to create widget here"])
    ],
}


def get_data():
    return data



q = Question("Truth Tables", ["print_tt_grid(1)", "print_tt_grid(2)", "print_tt_grid(3)"])
print(q.title)
print(q.code)