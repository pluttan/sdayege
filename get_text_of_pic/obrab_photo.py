import urllib.request
# Fetch the html file
response = open('view-source:http://ege.fipi.ru/os11/project/questions/question_view.php?qst=016972443309A69849315372D1015C5D&md=qprint')
html_doc = response.read()

print (html_doc)