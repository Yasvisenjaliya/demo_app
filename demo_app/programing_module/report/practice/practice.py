import frappe
from frappe import _, msgprint

def execute(filters=None):
    # Initialize data and columns
    if not filters:
        filters = {}

    data, columns = [], []
    columns = get_columns()  # Define the columns for the report
    student_data = get_student_data(filters)  # Fetch student data based on filters
    
    if not student_data:
        msgprint(_('No record found'))
        return columns, student_data

    # Prepare data for the report
    data = []
    for d in student_data:
        row = {
            'first_name': d.first_name,
            'last_name': d.last_name,
            'email': d.email,
            'grade': d.grade,
            'dob': d.dob,
            'subject': d.subject,  # Assuming subject is related to the student
        }
        data.append(row)
    
    chart = get_chart_data(data)  # Optional: Generate chart data if needed
    
    return columns, data, None, chart

def get_columns():
    # Define the columns for the report
    return [
        {
            'fieldname': 'first_name',
            'label': _('First Name'),
            'fieldtype': 'Data',
            'width': '150'
        },
        {
            'fieldname': 'last_name',
            'label': _('Last Name'),
            'fieldtype': 'Data',
            'width': '150'
        },
        {
            'fieldname': 'email',
            'label': _('Email'),
            'fieldtype': 'Data',
            'width': '200'
        },
        {
            'fieldname': 'grade',
            'label': _('Grade'),
            'fieldtype': 'Data',
            'width': '100'
        },
        {
            'fieldname': 'dob',
            'label': _('Date of Birth'),
            'fieldtype': 'Date',
            'width': '120'
        },
        {
            'fieldname': 'subject',
            'label': _('Subject'),
            'fieldtype': 'Data',
            'width': '150'
        }
    ]

def get_student_data(filters):
    # Fetch student data from the database based on the filters
    conditions = get_conditions(filters)
    data = frappe.get_all(
        doctype='Student',
        fields=['first_name', 'last_name', 'email', 'grade', 'dob', 'subject'],
        filters=conditions,
        order_by='first_name desc'
    )
    return data

def get_conditions(filters):
    # Build the conditions for the filters
    conditions = {}
    
    # Check if filters are provided for 'Subject' and 'Student'
    if filters.get('subject'):
        conditions['subject'] = filters.get('subject')
    
    if filters.get('student'):
        conditions['student'] = filters.get('student')

    return conditions

def get_chart_data(data):
    
    if not data:
        return None
    
    labels = ['Grade A', 'Grade B', 'Grade C', 'Grade D']
    grade_data = {
        'Grade A': 0,
        'Grade B': 0,
        'Grade C': 0,
        'Grade D': 0,
    }
    datasets = []

    for entry in data:
        grade = entry['grade']
        if grade in grade_data:
            grade_data[grade] += 1
    
    datasets.append({
        'name': 'Grade Distribution',
        'Values': [grade_data.get('Grade A'), grade_data.get('Grade B'), grade_data.get('Grade C'), grade_data.get('Grade D')]
    })
    
    chart = {
        'data': {
            'labels': labels,
            'datasets': datasets
        },
        'type': 'pie',
        'height': 300,
    }
    
    return chart
