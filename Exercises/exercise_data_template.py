class Question:
    def __init__(self, title, code):
        self.title = title
        self.code = code


data = {
    "main_file_name": "",
    "frq_file_name": "",
    "tt_file_name": "",
    "intro_title": "",
    "intro_body": [
        "Array of strings, one for each sentence",
    ],
    "section1_title": "",
    "section1_body": [
        "Array of strings, one for each sentence",
    ],
    "section1_quiz_title": "Binary Practice",
    "section1_questions": [
        Question("Put question title here", "Put code to create widget here")
    ],
    "section2_exists": True,
    "section2_title": "",
    "section2_body": [
        "Array of strings, one for each sentence",
    ],
    "section2_quiz_title": "",
    "section2_questions": [
        Question("Put question title here", "Put code to create widget here")
    ],
    "section3_exists": False,
    "section3_title": "",
    "section3_body": [
        "Array of strings, one for each sentence",
    ],
    "section3_quiz_title": "",
    "section3_questions": [
        Question("Put question title here", "Put code to create widget here")
    ],
}
