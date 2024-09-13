from django.utils import timezone


def generate_student_id():
    return f'STD{int(timezone.now().timestamp())}'

def generate_teacher_id():
    return f'TCR{int(timezone.now().timestamp())}'

def generate_college_id():
    return f'CLG{int(timezone.now().timestamp())}'