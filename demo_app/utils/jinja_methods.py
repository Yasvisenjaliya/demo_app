def full_name(doc):
    """Returns the full name of the student"""
    return f"{doc.first_name} {doc.middle_name or ''} {doc.last_name}".strip()

def get_grade_message(grade):
    """Returns a message based on the student's grade"""
    messages = {
        "A": "Excellent! Keep it up!",
        "B": "Good job! Aim higher.",
        "C": "Needs Improvement.",
    }
    return messages.get(grade, "Grade not found")
