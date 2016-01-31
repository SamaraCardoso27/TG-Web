# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

## app configuration made easy. Look inside private/appconfig.ini
from gluon.contrib.appconfig import AppConfig
from datetime import datetime
## once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)


global teste
if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    #db = DAL(myconf.take('db.uri'), pool_size=myconf.take('db.pool_size', cast=int), check_reserved=['all'],migrate = True)
    try:
        #db = DAL(myconf.take('db.uri'), pool_size=myconf.take('db.pool_size', cast=int), check_reserved=['all'],migrate = True)
        db = DAL('postgres://postgres:s4m4r4@localhost/TG',pool_size=1,check_reserved=['all'],migrate = True)
    except Exception as wE:
        print('Erro de Conexão');
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## choose a style for forms
response.formstyle = myconf.take('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.take('forms.separator')


## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
## (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()


## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.take('smtp.server')
mail.settings.sender = myconf.take('smtp.sender')
mail.settings.login = myconf.take('smtp.login')

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)



db.define_table('city',
    Field('created','datetime',writable=False,readable=False,label='Criado',default=datetime.now()),
    Field('last_update','datetime',writable=False,readable=False,label='Última Atualização',default=datetime.now()),
    Field('name',requires=IS_NOT_EMPTY(),length=50,label='Nome da Cidade'),
    Field('deleted','boolean',writable=False,readable=False,label='Deleção Lógica',default='F'),
    format='%(name)s')

auth.settings.extra_fields['auth_user'] = [
    Field('created','datetime',writable=False,readable=False,label='Criado',default=datetime.now()),
    Field('last_update','datetime',writable=False,readable=False,label='Última Atualização',default=datetime.now()),
    Field('birth_date',type='date',label='Data de Nascimento'),
    Field('cpf',length=50,label='CPF'),
    Field('cellphone',length=100,label='Celular'),
    Field('keypoints1',length=50000,label='keypoints 1'),
    Field('keypoints2',length=50000,label='keypoints 2'),
    Field('sex','boolean',label='Sexo'),
    Field('street_number',length=5,label='Numero'),
    Field('comp_person',length=50,label='Complemento'),
    Field('neigh',length=50,label='Bairro'),
    Field('street',length=100,label='Logradouro'),
    Field('zipcode',length=10,label='CEP'),
    Field('city_person',db.city,label='Cidade'),
    Field('marital_status',type='integer',label='Estado civil'),
    Field('deleted','boolean',writable=False,readable=False,label='Deleção Lógica',default='F')
]

auth.define_tables(username=False, signature=False)




auth._next = None
auth.settings.login_next=URL('default','update_session')
auth.settings.logout_next = URL('default','index')
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True
auth.settings.actions_disabled.append('register')
auth.settings.actions_disabled.append('profile')
auth.settings.login_captcha = False     #adicionar captcha
auth.settings.password_min_length = 8   #tamanho do password
auth.settings.expiration = 10800 #segundos  4 horas
auth.settings.remember_me_form = False
auth.settings.retrieve_password_captcha = False
db.auth_user.email.label=T('E-mail')
db.auth_user.password.label=T('Password')