import secrets
class Question:
    def __init__(self, title, code):
        self.title = title
        self.code = code

hash = secrets.token_hex(32)

data = {
    "hash": hash,
    "main_file_name": "gates",
    "frq_file_name": "frq_gates",
    "tt_file_name": "tt_gates",
    "intro_title": "Logic Gates",
    "intro_body": """
After learning about boolean algebra, it's time to see how we can actually use it in computers.
You can use logic gates to implement boolean logic in hardware to help computers make decisions.
A simple logic gate will have 2 inputs, and 1 output. These inputs and outputs represent digital signals.
The signals can either be high or low. High means that the signal has a positive voltage.
This is represented as a 1, and is the same as "true" when using boolean logic.
Low means that the signal has not voltage. This can be represented as a 0, or "false" when using bolean logic.
When you put a bunch of these gates together is strategic ways, you can create complex systems that make up computers.
    """,
    "section1_title": "AND, OR, NOT",
    "section1_body": """
These gates should be a review of the ideas you learned about with boolean algebrea in the previes section.
Here you will learn the symbols we use to represent each type of gate in diagrams.

<p align="left">
<img src="https://raw.githubusercontent.com/byuccl/digital_design_colab2/master/Exercises/gates/media/andgate.png"
width="250" height="" style="display: block; margin: 0 auto" />
</p>

AND: The output is high when both inbuts a, and b are high.
Otherwise, the output is low.

<p align="left">
<img src="https://raw.githubusercontent.com/byuccl/digital_design_colab2/master/Exercises/gates/media/orgate.png"
width="250" height="" style="display: block; margin: 0 auto" />
</p>

OR: The output is high when either one of the inputs is high.
If both inputs are low, the output is low.

<p align="left">
<img src="https://raw.githubusercontent.com/byuccl/digital_design_colab2/master/Exercises/gates/media/notgate.png"
width="250" height="" style="display: block; margin: 0 auto" />
</p>


NOT: The output is alwasys the oposite of the input. 
    """,
    "section1_quiz_title": "Fill out the truth tables below",
    "section1_questions": [
        Question(["Fill out the truth tables below"], ["print_tt_grid(1)", "print()", "print_tt_grid(2)", "print()", "print_tt_grid(3)"])
    ],
    "section2_exists": True,
    "section2_title": "NAND, NOR, XOR, XNOR",
    "section2_body": """
Bubbles are used to represent inverting a wire or signal.
Just think of them as a NOT gate. 

<p align="left">
<img src="https://raw.githubusercontent.com/byuccl/digital_design_colab2/master/Exercises/gates/media/norgate.png"
width="250" height="" style="display: block; margin: 0 auto" />
</p>

NOR Gates are OR gates, but the output is inverted.
The dot is used to represent an invert or NOT gate.

<p align="left">
<img src="https://raw.githubusercontent.com/byuccl/digital_design_colab2/master/Exercises/gates/media/nandgate.png"
width="250" height="" style="display: block; margin: 0 auto" />
</p>

NAND gates are AND gates but the output is inverted

<p align="left">
<img src= "https://raw.githubusercontent.com/byuccl/digital_design_colab2/master/Exercises/gates/media/xorgate.png"
width="250" height="" style="display: block; margin: 0 auto" />
</p>


XOR gates are exclusive OR gates.
The output is only 1 if an odd number of the inputs are 1.
In this example, if the two inputs are both 0 or they are both 1, the output is 0.

<p align="left">
<img src="https://raw.githubusercontent.com/byuccl/digital_design_colab2/master/Exercises/gates/media/xnorgate.png"
width="250" height="" style="display: block; margin: 0 auto" />
</p>


XNOR gates are XOR gates but the ouput is inverted. The oupt is 1 if an even number of inputs are the same. 

        """,
    "section2_quiz_title": "Try filling out the truth tables for these new gates",
    "section2_questions": [
        Question(["Fill out the truth tables below"], ["print_tt_grid(4)", "print()", "print_tt_grid(5)", "print()", "print_tt_grid(6)", "print()", "print_tt_grid(7)"])
    ],
    "section3_exists": True,
    "section3_title": "Complex Diagrams",
    "section3_body": """
You can combine these logic gates to implement a function with multiple inputs and a single output. 
Here is an example:

<p align="left"> 
<img src="https://raw.githubusercontent.com/byuccl/digital_design_colab2/master/Exercises/gates/media/example_circuit.png" 
width="250" height="" style="display: block; margin: 0 auto" /> </p>

This circuit implement boolean logic that takes inputs A, B, and C, and outputs Y. 
The output of the top NAND gate is (AB)', the output of the middile NOR gate is (A+C)', and the output of the botton AND gate is BC.
These three signals go into the final OR gate to produce the output Y = (AB)'+(A+C)'+BC.
This is really cool when you think about what is going on here!
You can can design a system that does somthing based on a complex set of conditions.
You could use this strategey to implement if-else statements, and as you put more and more of them together this is how computers run!
Also notice from this circuit that logic gates can have more than 2 inputs. 
In these cases, they still work in exactly the same way.
An AND gate will need all of its inputs to be high for its output to be high. 
An or gate will only need at least of its inputs to be high for its output to be high.
    """,
    "section3_quiz_title": "Questions",
    "section3_questions": [
        Question(["#@markdown Use this diagram for the following questions", "#@markdown <p align=\"left\"> <img src=\"https://raw.githubusercontent.com/byuccl/digital_design_colab2/master/Exercises/gates/media/circuit_1.png\" width=\"250\" height=\"\" style=\"display: block; margin: 0 auto\" /> </p>"], ["print_frq_grid(1)", "print()", "print_frq_grid(2)"]),
        Question(["#@markdown Use this diagram for the following questions", "#@markdown <p align=\"left\"> <img src=\"https://raw.githubusercontent.com/byuccl/digital_design_colab2/master/Exercises/gates/media/circuit_2.png\" width=\"250\" height=\"\" style=\"display: block; margin: 0 auto\" /> </p>"], ["print_frq_grid(3)", "print()", "print_frq_grid(4)"]),
        Question(["#@markdown Use this diagram for the following questions", "#@markdown <p align=\"left\"> <img src=\"https://raw.githubusercontent.com/byuccl/digital_design_colab2/master/Exercises/gates/media/circuit_3.png\" width=\"250\" height=\"\" style=\"display: block; margin: 0 auto\" /> </p>"], ["print_frq_grid(5)", "print()", "print_frq_grid(6)"])
    ],
}

def get_data():
    for key in data:
        if "body" in key:
            data[key]=data[key].replace('"', '\\"')
            data[key]=data[key].splitlines() # Remove extra indentation
        if "questions" in key:
            for question in data[key]:
                i = 0
                for line in question.title:
                    line=line.replace('"', '\\"')
                    question.title[i] = line
                    i+=1
    return data

