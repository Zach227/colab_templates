
import secrets

class Question:
    def __init__(self, title, code):
        self.title = title
        self.code = code

hash = secrets.token_hex(32)

data = {
    "hash": hash,
    "main_file_name": "binary_hex",
    "frq_file_name": "frqBH",
    "intro_title": "Number Systems",
    "intro_body": """
One of the first things we learned as children was how to count.
We would from 0 to 9, and then put a 1 in front of each number and repeated the process to count from 10 to 19.
The thing that we don't often think about is that the decision to add a new digit at 10 was completely arbitrary.
For example, we could count from 0 to 4, and then add a digit and restart for the next number.
This means that to count to our version of 10, you would go:  
1,2,3,4,10,11,12,13,14,20  
In this case when you go from 4 to 10, the first digit represents the "fives place" and the second digit represents the "ones place" (10 = 5+0 and 11 = 5+1).
This would be a base 5 number system, as opposed to our standard base 10 number system.
You could use any number as a base.
You could have a really small base, like base 2, or you could have a base bigger that usual like 16.
Binary is simply to count using a base 2 number system.
    """,
    "section1_title": "Binary",
    "section1_body": """
*Why Binary?*   
Well unlike humans, who have analog sense (everything is on a scale), computers are digital.  
They can only see things as off or on. This means that if they want to represent something   
they must do it in a series of offs and ons. We use 0 to represent this off and 1 to represent on.  
*Using binary*  
Let's break down a decimal number (base 10), and a binary number (base 2).
We can denote the base of the number with a subscript.
1496<sub>10</sub> = 1000 + 400 + 90 + 9  
&emsp;&emsp;&emsp;&nbsp; = 1 * 10<sup>3</sup> + 4 * 10<sup>2</sup> + 9 * 10<sup>1</sup> + 9 * 10<sup>0</sup> = 1496<sub>10</sub>
11001<sub>2</sub> = 1 * 2<sup>4</sup> + 1 * 2<sup>3</sup> + 0 * 2<sup>2</sup> + 0 * 2<sup>1</sup> + 1 * 2<sup>0</sup>  
&emsp;&emsp;&emsp;&nbsp; = 16 + 8 + 0 + 0 + 1 = 25<sub>10</sub>
So each place in a binary number corresponds to a power of 2.
You add up the values corresponding to each 1 to turn a binary number into a decimal number.
Each 1 or zero is referred to as a bit (binary digit).
The bit on the far left is called the MSB (Most Significant Bit) and the bit on the far right is called the LSB (Least Significant Bit).
The MSB is the most significant bit becuase it represents the highest power in the nubmer therefore haveing the greatest impact on it's value.
For example, in the number 1496<sub>10</sub>, the most significant 'bit' or number is the 1, as 1000 is significantly larger and has more of an impact on the number than the 6 does.
Similarly, the LSB is called the least significant bit because it has the least impact on the number.
In the example above, 6 is the least significant 'bit' or number as 1490 isn't that different from 1496.
Now what if you want to represent a decimal number in binary? Let's try converting the number 53 into binary.
You first want to find the largest power of 2 that can fit into 53.
In this case it is 32 or 2<sup>5</sup>.
This will be the MSB.
Now we can start to lay out our binary number with this information.
<sub>${\scriptsize 32}$ ${\scriptsize 16}$ &nbsp;${\scriptsize 8}$ ${\scriptsize 4}$ &nbsp;${\scriptsize 2}$ &nbsp;${\scriptsize 1}$</sub>  
&nbsp;1&nbsp; _ &nbsp;_ _ &nbsp;_ _  
We can find the remaining value that is not yet represented by subtracting 32 from 53 so our new target is 53 - 32 = 21.
Now we can repeat the process, what is the biggest power of 2 that can fit into 21? The answer is 16 or 2<sup>4</sup>, so now we can fill it in.
<sub>${\scriptsize 32}$ ${\scriptsize 16}$ &nbsp;${\scriptsize 8}$ ${\scriptsize 4}$ &nbsp;${\scriptsize 2}$ &nbsp;${\scriptsize 1}$</sub>  
&nbsp;1&nbsp; 1 &nbsp;_ _ &nbsp;_ _  
We just keep repeating this process until we have fill out every bit.
&nbsp;21 - 16 = 5, so the biggest power of 2 is 4.
<sub>${\scriptsize 32}$ ${\scriptsize 16}$ &nbsp;${\scriptsize 8}$ ${\scriptsize 4}$ &nbsp;${\scriptsize 2}$ &nbsp;${\scriptsize 1}$</sub>  
&nbsp;1&nbsp; 1 0 1 &nbsp;_ _  
&nbsp;5 - 4 = 1, so the biggest power of 2 is 1.
<sub>${\scriptsize 32}$ ${\scriptsize 16}$ &nbsp;${\scriptsize 8}$ ${\scriptsize 4}$ &nbsp;${\scriptsize 2}$ &nbsp;${\scriptsize 1}$</sub>  
&nbsp;1 &nbsp;1 0 1 0 1  
So 53<sub>10</sub> is 110101 in binary. 
    """,
    "section1_quiz_title": "Binary Practice",
    "section1_questions": [
        Question(["#@markdown Q1"], ["print_frq_grid(1)"]),
        Question(["#@markdown Q2"], ["print_frq_grid(2)"]),
        Question(["#@markdown Q3"], ["print_frq_grid(3)"]),
        Question(["#@markdown Q4"], ["print_frq_grid(4)"]),
        Question(["#@markdown Q5"], ["print_frq_grid(5)"]),
        Question(["#@markdown Q6"], ["print_frq_grid(6)"])
    ],
    "section2_exists": True,
    "section2_title": "Hexadecimal",
    "section2_body": """
After working with binary numbers for a while, you start to get tired of writing all the 1's and 0's.
Or maybe you want to write a binary number is a smaller space.
You can use hexadecimal to make binary numbers more compact.
Hexadecimal (hex) is a base 16 number system.
That means we can count up to 16 before needing another digit.
But wait, we only have digits 0-9, how can we represent 10 or 11 with just one digit? The convention is to use the first 6 letters of the alphabet to reach 15.
This means that to count to 16<sub>10</sub> , you would go:
1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,10
The process for converting a hex number to decimal is exaclty the same as with binary.
2a7<sub>16</sub> = 2 * 16<sup>2</sup> + 10 * 16<sup>1</sup> + 7 * 16<sup>0</sup>  
&emsp;&emsp;&nbsp;&nbsp;&nbsp; = 2 * 256 + 10 * 16 + 7 * 1  
&emsp;&emsp;&nbsp;&nbsp;&nbsp; = 512 + 160 + 1 = 673<sub>10</sub>
However, hex is truly useful becuase of how easy it is to convert between binary and hex.
Since 16 is a power of 2 (2<sup>4</sup>), we can break up a long binary number into groups of 4 and convert each group to hex independantly.
For example, if we are given the binary number 00101101 we could convert it to hexadecimal quite easily.
First we break it up into groups of 4 and then we convert each set of 4 to hex.
0010<sub>2</sub> = 0 + 0 + 2 + 0 = 2<sub>16</sub>  
1101<sub>2</sub> = 8 + 4 + 0 + 1 = 13 = D<sub>16</sub>
So the 8 digit binary number 00101101 can be represented with a 2 digit hex number as 2D<sub>2</sub>.
Once you have practiced doing this conversion, it is very easy to convert a 4 bit binary number to hex.
All of the 4 bit conversions are summarized in this table.
![picture](https://raw.githubusercontent.com/westonMS/tempColab/master/Exercises/binary_hex/media/hex_table.png)
With this strategy even very long binary numbers can be converted easily.
For example, lets convert the 32 bit number 11111010011010110010110101101000.  
1111 1010 0110 1011 0010 1101 0110 1000
&emsp;F&emsp;&emsp;A &emsp;&nbsp; 6&emsp;&emsp;B&emsp;&emsp;2 &emsp;&nbsp; D&emsp;&emsp;6 &emsp;&nbsp; 8
        """,
    "section2_quiz_title": "Hexadecimal Practice",
    "section2_questions": [
        Question(["#@markdown Q1"], ["print_frq_grid(7)"]),
        Question(["#@markdown Q2"], ["print_frq_grid(8)"]),
        Question(["#@markdown Q3"], ["print_frq_grid(9)"]),
        Question(["#@markdown Q4"], ["print_frq_grid(10)"]),
        Question(["#@markdown Q5"], ["print_frq_grid(11)"]),
        Question(["#@markdown Q6"], ["print_frq_grid(12)"])
    ],
    "section3_exists": False,
    "section3_title": "",
    "section3_body": """
text goes here
    """,
    "section3_quiz_title": "",
    "section3_questions": [
        Question(["title"], ["code"])
    ],
}

def get_data():
    for key in data:
        if "body" in key:
            data[key]=data[key].replace('"', '\\"')
            data[key]=data[key].replace('\\s', '\\\\s')
            data[key]=data[key].splitlines()
        if "questions" in key:
            for question in data[key]:
                i = 0
                for line in question.title:
                    line=line.replace('"', '\\"')
                    question.title[i] = line
                    i+=1
    return data