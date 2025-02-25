# import frappe
# from frappe import _, msgprint

# def execute(filters=None):
#     if not filters:
#         filters = {}

#     data, columns = [], []
#     columns = get_columns()
#     cs_data = get_cs_data(filters)
    
#     if not cs_data:
#         msgprint(_('No record found'))
#         return columns, cs_data

#     data = []
#     for d in cs_data:
#         row = {
#             'first_name': d.first_name,
#             'dob': d.dob,
#             'age': d.age
#         }       
#         data.append(row)
        
#         chart = get_chart_data(data)
#         # report_summary = get_report_summary(data)
    
#     return columns, data, None,chart

# def get_columns():
#     return [
#         {
#             'fieldname': 'first_name',
#             'label': _('Name'),
#             'fieldtype': 'Data', 
#             'width': '120'
#         },
#         {
#             'fieldname': 'dob',
#             'label': _('DOB'),
#             'fieldtype': 'Date', 
#             'width': '120' 
#         },
#         {
#             'fieldname': 'age',
#             'label': _('Age'),
#             'fieldtype': 'Int', 
#             'width': '120'
#         }
#     ]

# def get_cs_data(filters):
#     conditions = get_conditions(filters)
#     data = frappe.get_all(
#         doctype='Server Side Scripting',
#         fields=['first_name', 'dob', 'age'],
#         filters=conditions,
#         order_by='first_name desc'
#     )
#     return data

# def get_conditions(filters):
#     conditions = {}
#     for key, value in filters.items():
#         if filters.get(key):
#             conditions[key] = value
    
#     return conditions

# def get_chart_data(data):
#     if not data:
#         return None
    
#     labels = ['Age <= 45', 'Age > 45']
    
#     age_data = {
#         'Age > 45': 0,
#         'Age <= 45': 0,
#     }
#     datasets = []
    
#     for entry in data:
#         if entry['age'] <= 45:
#             age_data['Age <= 45'] += 1
#         else: 
#             age_data['Age > 45'] += 1
    
#     datasets.append({
#         'name': 'Age Status',
#         'Values': [age_data.get('Age <= 45'), age_data.get('Age > 45')]
#     })
    
#     chart = {
#         'data': {
#             'labels': labels,
#             'datasets': datasets
#         },
#         'type': 'pie',
#         'height': 300,
#     }
    
#     return chart


import frappe
from frappe import _, msgprint

def execute(filters=None):
    if not filters:
        filters = {}

    data, columns = [], []
    columns = get_columns()
    cs_data = get_cs_data(filters)
    
    if not cs_data:
        msgprint(_('No record found'))
        return columns, cs_data

    data = []
    for d in cs_data:
        row = {
            'first_name': d.first_name,
            'dob': d.dob,
            'age': d.age
        }    
        data.append(row)
        
        chart = get_chart_data(data)
        # report_summary = get_report_summary(data)
    
    return columns, data

def get_columns():
    return [
        {
            'fieldname': 'first_name',
            'label': _('Name'),
            'fieldtype': 'Data', 
            'width': '120'
        },
        {
            'fieldname': 'dob',
            'label': _('DOB'),
            'fieldtype': 'Date', 
            'width': '120' 
        },
        {
            'fieldname': 'age',
            'label': _('Age'),
            'fieldtype': 'Int', 
            'width': '120'
        }
    ]

def get_cs_data(filters):
    conditions = get_conditions(filters)
    data = frappe.get_all(
        doctype='Server Side Scripting',
        fields=['first_name', 'dob', 'age'],
        filters=conditions,
        order_by='first_name desc'
    )
    return data

def get_conditions(filters):
    conditions = {}
    for key, value in filters.items():
        if filters.get(key):
            conditions[key] = value
    
    return conditions

def get_chart_data(data):
    if not data:
        return None
    
    labels = ['Age <= 45', 'Age > 45']
    
    age_data = {
        'Age > 45': 0,
        'Age <= 45': 0,
    }
    datasets = []
    
    for entry in data:
        try:
            age = int(entry['age'])
        except ValueError:
            continue  
        
        if age <= 45:
            age_data['Age <= 45'] += 1
        else: 
            age_data['Age > 45'] += 1
    
    datasets.append({
        'name': 'Age Status',
        'Values': [age_data.get('Age <= 45'), age_data.get('Age > 45')]
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

# def get_report_summary(data):
#     total_records = len(data)
#     total_age = sum(entry['age'] for entry in data if isinstance(entry['age'], int))
#     avg_age = total_age / total_records if total_records else 0
    
#     summary = {
#         'Total Records': total_records,
#         'Total Age': total_age,
#         'Average Age': avg_age
#     }
    
#     return summary

