{
'name': "My library",
'summary': "Manage books easily",
'description': """
Manage Library
==============
Description related to library.
""",
'author': "Andrei Daryin",
'website': "http://www.example.com",
'category': 'Uncategorized',
'version': '13.0.1',
'depends': ['base'],
'data': [
    'security/groups.xml',
    'security/ir.model.access.csv',
    'views/library_book.xml',
    'views/library_book_categ.xml'
    ],
'demo': ['demo.xml'],
}