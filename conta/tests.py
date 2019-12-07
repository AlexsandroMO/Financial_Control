from django.test import TestCase


#https://www.geeksforgeeks.org/textfield-django-models/




#pip install django-crispy-forms

#Zerar senha do admin
#python manage.py shell
#from django.contrib.auth.models import User
#User.objects.filter(is_superuser=True)

#usr = User.objects.get(username='nome-do-administrador')
#usr.set_password('nova-senha')
#usr.save()



'''Upload documents on Github

git clone <nome>

<entra na pasta criada>

git add .

git commit -m "texto"

git push
'''


#Heroku
#https://github.com/Gpzim98/django-heroku

#git add .gitignore
#colocar no gitignore
'''.idea
.pyc
.DS_Store
*.sqlite3'''

'''
Publishing the app
git add .
git commit -m "Configuring the app"
git push heroku master --force
'''