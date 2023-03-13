class Question:
    def __init__(self, title, code):
        self.title = title
        self.code = code


data = {
    "main_file_name": "",
    "frq_file_name": "",
    "tt_file_name": "",
    "intro_title": "",
    "intro_body": """
text goes here
    """,
    "section1_title": "",
    "section1_body": """
text goes here
    """,
    "section1_quiz_title": "",
    "section1_questions": [
        Question(["title"], ["code"])
    ],
    "section2_exists": True,
    "section2_title": "",
    "section2_body": """
text goes here
        """,
    "section2_quiz_title": "",
    "section2_questions": [
        Question(["title"], ["code"])
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

