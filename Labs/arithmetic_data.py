import random
import string

class Question:
    def __init__(self, title, code):
        self.title = title
        self.code = code


data = {
    "notebook_dir": "arithmetic_lab",
    "intro_title": "The Lab",
    "intro_body": "",
    "part1_title": "Full Adder",
    "part1_body": """
The first building block of your Circuit will be the full adder.  

![picture](https://raw.githubusercontent.com/byuccl/digital_design_colab/master/Labs/arithmetic_lab/media/adder.png)

| Module Name: |Full_Add|||
| ----------- | ----------- |--|--|
| Port Name      | Direction       |Width|Function|
|a 	|Input 	|1| 	‘a’ operand input|
|b 	|Input 	|1 |	‘b’ operand input|
|cin |	Input| 	1| 	Carry in|
|s 	|Output 	|1| 	Sum output|
|co| 	Output 	|1| 	Carry out output|

It will add together `a` and `b` and a carry over from another module. (If it is the first bit the `Cin` will be `0`)   
It will then give `s` is the sum of the inputs. If there is a carry out, `co` should be `1`.
        """,
    "part1_wavedrom": True,
    "part1_testbench": True,
    "part1_sim_file": "full_add",

    "part2_exists": True,
    "part2_title": "8-bit Adder",
    "part2_body": """
**What is a module?**  

Instead of copying and pasting a Full-Adder over and over, we can instantiate it again as a module.  
This is the same concept as making a function call in python or C++. We are just reusing code we have already written.  
It follows the following format:  
`module_name module_title (.first_signal(first_connection), .second_signal(second_connection));`  
The first line will be whatever you have called your module. In this case it will be `Full_Add`.  
Then you must give each full adder a name. This part isn't important, but if its name has meaning it will be easier to understand your code. So, label each adder depending on its position.
Now you must define which internal signals go to which external signals.  
For example, if we want to add 8 bits together, for the first full adder, a should be the first bit of an a bit input. The `Cin` should be `0`. `s` should be the first bit of an output and `co` should be neither an input nor an output, but should instead be an intermediate signal that is used for the second bit.

**Creating an 8 bit adder**

To create an 8-bit adder, you will need 8 one bit adders all linked together.

![picture](https://raw.githubusercontent.com/byuccl/digital_design_colab/master/Labs/arithmetic_lab/media/add8.png)

| Module Name: |8Add|||
| ----------- | ----------- |--|--|
| Port Name      | Direction       |Width|Function|
|a 	|Input 	|8| 	‘a’ operand input|
|b 	|Input 	|8 |	‘b’ operand input|
|cin |	Input| 1	| 	Carry in|
|s 	|Output 	|8| 	Sum output|
|co| 	Output 	|1| 	Carry out output of the last bit|


You can use various internal signals for `Cin` and `Cout`.  
This module should have 8 instances of your Full_Add module.
        """,
    "part2_wavedrom": False,
    "part2_testbench": True,
    "part2_sim_file": "add_8",

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

    "top_module_title": "Top Level Module",
    "top_module_body": """
![picture](https://raw.githubusercontent.com/byuccl/digital_design_colab/master/Labs/arithmetic_lab/media/lab_top.png)

You probably noticed that there is no `led` or `sw` signal yet. This will be contained in a top level module. You will instantiate 8Add and feed into it all the necessary signals.

| Module Name: |arithemtic_top|||
| ----------- | ----------- |--|--|
| Port Name      | Direction       |Width|Function|
|sw 	|Input 	|16| Switches (`sw[15:8]` = `b`, `sw[7:0]` = `a` operand)	|
|btnc |	Input| 1	| Subtract when pressed|
|led	|Output 	|9| 	LEDs (`led[8]`= overflow, `led[7:0]` = sum)|  

While `btnc` is high, `b` should be inverted to subtract `b` from `a`.  
Led[8] should be high if overflow occurs.

**Overflow Detection**

While using two's complement we can easily check for overflow. 
If the MSB's are the same, but the output is different then overflow has occurred. For example, `1111`+`1000`, both MSB are `1`. The output would be `0111`. Since `0`, the MSB, is different than `1`, we can tell that overflow has occurred.  
In other words, if you add two negative numbers and get a positive number, overflow has occurred. If you add two negative numbers and the output is positive, overflow has occurred.

**How does subtraction work?**

As we explained earlier, there are two ways to do subtraction with two's complement, either using borrows like in elementary school, or inverting the second operator.  
Unfortunately, our computers never went to elementary school, so they will have to do the second option.  
Luckily, inverting `b` is quite simple.  
But you must also add `1` when inverting. Also, we have a carry in signal for our first bit, which acts exactly like adding `1`.    
This means that we can write our code such that if that carry in is high, then subtraction should occur.
        """,
    "top_module_wavedrom": False,
    "top_module_testbench": False,
    "top_module_sim_file": "arithmetic_top",

    "xdc_exists": True,
    "xdc_title": "XDC File",
    "xdc_body":
    """
In the xdc file below, uncomment the lines corresponding to the FPGA I/O that you are using. Then run the code block to create your xdc file.
        """,

    "f4pga_exists": True,
    "download_exists": True,
    "download_body": 
    """
You can use this configuration file and the program openOCD to download the bitstream to your board. You will need to download this file and the bitstream to your local machine.
        """,

    "top": "arithmetic_top",
    "folder": "Arithmetic",
    "files": "Makefile xdc.xdc arithmetic_top.sv full_add.sv add_8.sv",

    "next_lesson": "seven_segment_lab",
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

