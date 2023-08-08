import random
import string

class Question:
    def __init__(self, title, code):
        self.title = title
        self.code = code


data = {
    "notebook_dir": "gates_lab",
    "intro_title": "System Verilog",
    "intro_body": """
In this lab you will be implementing 2 different logic fuctions using structural system verilog.
SystemVerilog is a Hardware Description Language (HDL).
Unlike other languages, which are compiled and executed on a processor, SystemVerilog is transformed into physical hardware.
This means that, for the most part, SystemVerilog isn't run line by line, but is describing the circuit design that you want.
You can often switch the order of 2 lines and it won't make a difference.
In this lab, you will only be using the logic gates that are built into the SystemVerilog language.
You will also practice simulating your design and getting information from the waveform.
To do this, you will need to know a few things about SystemVerilog.\n
<h3>

<summary><b>Creating a Module</b></summary>
 
</h3>

The fundamental coding blocks of SystemVerilog are called Modules.   

Think of modules as what you would call functions in other programming languages. You can call other modules and assign different signals to their inputs and outputs.
To Define a module, first use the keyword `module` then give the module a name. 
Then inside `();` define all of the inputs and outputs separated by `,`.  

After that, write any code you want in this module.  
Finally, use the keyword `endmodule` to finish it.   
Example: 
```
module moduleName( 
  input logic a,
  output logic b
  );

  // Write code here

endmodule
```


<h3>

<summary><b>Logic Gates</b></summary>
 
</h3>

System verilog has build in support for logic gates. 
You can instantiate a gate by using the format gateType(output, input1, input2).
For example we can use the code `and(out, A, B)` to represent the following AND gate.

<p align="left">
<img src="https://raw.githubusercontent.com/byuccl/digital_design_colab2/master/Labs/gates_lab/media/and_gate.png"
width="150" height="" style="display: block; margin: 0 auto" />
</p>

You can use this same format for NOT, OR, NOR, and NAND gates.

<h3>

<summary><b>Internal Signals</b></summary>
 
</h3>

While you list all your module inputs and outputs at the beginning of a module, you will always need more signals to connect different parts of your circuit.
These are called internal signals.
For example look at the circuit below. 

<p align="left">
<img src="https://raw.githubusercontent.com/byuccl/digital_design_colab2/master/Labs/gates_lab/media/example_circuit.png"
width="250" height="" style="display: block; margin: 0 auto" />
</p>

You will need intermediate signals to represent the outputs of the AND gates that become the inputs of the OR gate.
You can declare an internal signal in sytem verilog by simply using `logic signalName`.
So maybe for the example above you can write:
```
logic output1;
logic output2;
```
And then you can use these signals as outputs in the AND gates, and inputs in the OR gate. 

        """,

    "part1_exists": True,
    "part1_title": "Task 1",
    "part1_body": """
The first thing you will do is implement the following circuit in system verilog.

<p align="left">
<img src="https://raw.githubusercontent.com/byuccl/digital_design_colab2/master/Labs/gates_lab/media/assignment_circuit.png"
width="350" height="" style="display: block; margin: 0 auto" />
</p>

Start out by creating a module as shown above with 4 inputs and 1 output.
Name your inputs A, B, C, D, and name your output Q.
Name your module circuit.
The next thing you may want to do is create all the internal signals that you will need to connect the gates. 
If you forget how to use the simulation workspace review the [tutorial notebook](https://colab.research.google.com/github/byuccl/digital_design_colab2/blob/master/Tutorials/using_simulation_tools/using_simulation_tools.ipynb) on the subject. 
        """,
    "part1_wavedrom": True,
    "part1_testbench": True,
    "part1_sim_file": "circuit",

    "part2_exists": False,
    "part2_title": "",
    "part2_body": """
text goes here
        """,
    "part2_wavedrom": True,
    "part2_testbench": True,
    "part2_sim_file": "function4",


    "part3_exists": False,
    "part3_title": "",
    "part3_body": """
text goes here
    """,
    "part3_wavedrom": True,
    "part3_testbench": True,
    "part3_sim_file": "",

    "part4_exists": False,
    "part4_title": "",
    "part4_body": """
text goes here
        """,
    "part4_wavedrom": True,
    "part4_testbench": True,
    "part4_sim_file": "",

    "top_module_title": "Task 2",
    "top_module_body": """
Follow the same procedure from task 1 to implement the following boolean expression.

F = AB+AC'D+(BD)'

Name the module expression.
        """,
    "top_module_wavedrom": True,
    "top_module_testbench": True,
    "top_module_sim_file": "expression",

    "xdc_exists": False,
    "xdc_title": "",
    "xdc_body":
    """
text goes here
        """,

    "f4pga_exists": False,
    "download_exists": False,
    "download_body": 
    """
text goes here
        """,

    "top": "",
    "folder": "",
    "file": "",

    "top_file_exists": True,
    "top_file": "",

    "next_lesson": "karnaugh_maps",
}

def get_data():
    for key in data:
        if "body" in key:
            data[key]=data[key].replace('"', '\\"')
            data[key]=data[key].replace('\\s', '\\\\s')
            data[key]=data[key].replace('\n', '\\n')
            data[key]=data[key].replace('\t', '\\t')
            data[key]=data[key].replace('\frac', '\\\\frac')
            data[key]=data[key].splitlines()
    return data