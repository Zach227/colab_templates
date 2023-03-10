import jinja2


class Question:
    def __init__(self, title, code):
        self.title = title
        self.code = code


section1_questions = [
    Question("Q1", "print_frq_grid(1)"),
    Question("Q2", "print_frq_grid(2)"),
    Question("Q3", "print_frq_grid(3)"),
    Question("Q4", "print_frq_grid(4)"),
    Question("Q5", "print_frq_grid(5)"),
    Question("Q6", "print_frq_grid(6)"),
]


str = """
{% for question in section1_questions %}
    {% raw %}
      {
        "cell_type": "code",
        "execution_count": null,
        "metadata": {
          "cellView": "form",
          "id": "47QYQDmyJ03H"
        },
        "outputs": [],
        "source": [
          "#@title {{ question.title }}",
          "{{ question.code }}"
        ]
      },    
    {% endraw %}
    {% endfor %}
"""

env = jinja2.Environment()
template = env.from_string(str)
output = template.render(
    section1_questions=[
        Question("Q1", "print_frq_grid(1)"),
        Question("Q2", "print_frq_grid(2)"),
    ]
)

print(output)
