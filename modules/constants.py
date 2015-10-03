# -*- coding: utf-8 -*-


###################################
#
#   Hold all the constants used through the system
#
###################################

from re import compile

# Hold the emails of the support team
SUPPORT = ['diego.palharini@urbemobile.com.br','samara.cardoso@urbemobile.com.br']


global REP_REG_CLEARPOINTS
REP_REG_CLEARPOINTS = compile(r"[\.\s\_-]")

global REP_REG_PHONE
REP_REG_PHONE = compile(r"[\.\s\_\(\)-]")

global REP_REG_CLEARALL
REP_REG_CLEARALL = compile(r"[\.\s\_\(\)\:/-]")

# type of companies accepted into de system
TYPE_CMP_ADMIN     = 'Administrador'
TYPE_CMP_CHAMBER   = 'Câmara'
TYPE_CMP_ALDERMAN  = 'Vereador'
TYPE_CMP_SUPPORT   = 'Suporte'

# Type of users
USER_ANO = "Anonimo"
USER_VIZ = "Visualizador"
USER_THI = "Terceiros"
USER_WOR = "Trabalhador"
USER_MAN = "Gerente"
USER_ADM = "Administrador"
USER_NEW = "Noticia"
USER_BACK = "Background"
USER_GOD = "God"

# define the automation vector, used for definition
AUTO_CALENDAR = '2'
AUTO_AUTMOATION = '1'
AUTO_VECTOR = [AUTO_CALENDAR,AUTO_AUTMOATION]

# define the limit of uploaded file
UPLOAD_LIMIT_FILE = [[1024,2560000],[1024,2560000],[1024,2560000]]
UPLOAD_LIMIT_PHOTO = [[1024,1280000],[1024,1280000],[1024,1280000]]
UPLOAD_LIMIT_IMGAPP = [[0, 15360],[0, 15360],[0, 15360]]

# Type of image supported
TYPE_IMAGE_FILE = ['jpeg','jpg','png']

TYPE_INFORMATION_FILE = ['jpeg','jpg','png', 'mp4', '3gp', 'avi', 'mp3', 'wav', 'pdf']

UPLOAD_LIMIT_FILE = [[2048,1048576],[2048,1048576],[2048,1048576],[102400, 3145728],[102400, 3145728],[102400, 3145728], [10240, 1048576], [10240, 1048576], [10240, 1048576]]

# All workers can see
USER_WORKERS = [USER_WOR , USER_MAN, USER_ADM, USER_GOD]
# All managers can see
USER_MANAGERS = [USER_MAN, USER_ADM, USER_GOD]

# All companies that can access the admin pages
ADM_COMPANY = [TYPE_CMP_ADMIN, TYPE_CMP_SUPPORT]

#All client company that can access application pages
CLI_COMPANY = [TYPE_CMP_CHAMBER, TYPE_CMP_ALDERMAN, TYPE_CMP_SUPPORT]

# Map permission in the front-end to database
PERMISSION_MAP = {'0' : USER_WOR, '1' : USER_MAN}

# hold the means of communication
COMM_TYPES = {'0' :'Notificação', '1' : 'e-Mail', '2' : 'SMS'}

# hold the provider type for mail
PROVIDER_MAIL = {'0' : 'Genérico', '1' : 'GMAIL'}

#hold the provider type for mail
COMM_TYPE_MAIL = {'0' : 'SMTP'};

# hold the provider type for mail
PROVIDER_SMS = {'0' : 'IndexSMS'}

# Type of project status
PROJ_STATUS_DIC = {'0' : 'Tramitação', '1' : 'Aprovado', '2' : 'Reprovado'}
# Type of project status
PROJ_STATUS_REV = {'tramitação' : 0, 'aprovado' : 1, 'reprovado' : 2}

# Constants for keys
CREATE_KEY   = 0   # create a new key
RETRIAVE_KEY = -1  # get the key content
REVOKE_KEY   = -2  # remove the key if it is not for use 
SEARCH_USER  = 1
INSERT_USER  = 2
INSERT_RAW = 3 # to insert raw data without concern of contents

IMAGEM_LOGO = '<img src= "http://www.epasse.com/static/images/favicon.png" style="widht:100px; height:50px;">'

EMAIL_RECOVERY_PART_I = "<html>"+\
    "<h4 style='font-size:18px;'><b>Informações para redefinir sua senha</b></h4>"+\
    "<span style='font-size:14px;'> Clique no botão abaixo para redefinir sua senha.</span><br>"+\
    "<a href='https://"
    
EMAIL_RECOVERY_PART_II = "?key=%(key)s' style='font-size:15px;'><button>Redefinir Senha</button></a>"+\
    "<p style='font-size:14px;'>Para redefinir sua senha: </p>"+\
    "<p style='font-size:14px;margin-left:10px;'>1. Inserir a nova senha</p>"+\
    "<p style='font-size:14px;margin-left:10px;'>2. Confirmar a nova senha</p>"+\
    "<p style='font-size:14px;margin-left:10px;'>3. Clique no botão Requisitar renovação de senha </p>"+\
    "<p style='font-size:14px;'>Atenciosamente,<p>"+\
    "<p style='font-size:14px;'>Urbe Mobile<p>"+\
    "<p style='font-size:14px;'>Telefone: +55 12 3876-7748</p>"+\
    "<p style='font-size:14px;'>Email: urbemobile@urbemobile.com.br</p>"+\
    "<p style='color: red;font-size:14px;'><b>Caso o botão não funcione ou não apareça, copie esse link e cole na barra de endereço:</b></p>" +\
    "https://"

EMAIL_RECOVERY_PART_III = "/%(key)s" +\
    "<hr><br>"+IMAGEM_LOGO+\
    "</html>"

TYPE_ERROR = ['Erro Interno','Acesso Proibido/Não Autorizado','Erro não tratado no Handle_errors']

#Hold the automation event info
AUTO_EVENT_INFO = {'0' : 'Data Customizada', 
                   '1' : 'Aniversário de Munícipe', 
                   '2' : 'Aniversário de Parente de Munúcipe',
                   '3' : 'Aniversário de Usuário do Sistema', 
                   '4' : 'Requisição - Nova', 
                   '5' : 'Requisição - Atualização',
                   '6' : 'Requisição - Fora do prazo normal',
                   '7' : 'Requisição - Fora do prazo máximo',
                   '8' : 'Requisição - Concluída',
                   '9' : 'Requisição - Deleção;'}

# Hold the automation operation between the fields and the value
AUTO_OPERATIONS = ['Todos','Igual a','Diferente de']

# Hold the tags for person
AUTO_TAG_CITIZEN = ['@PROFISSAO','@RELIGIAO','@CIDADE','@BAIRRO','@NOME','@SEXO','@DATA']

#Hold the tags for parent
AUTO_TAG_PARENT = ['@NOME','@DATA','@RELACAO','@HOJE']

#Hold the tags for system users
AUTO_TAG_USER = ['@NOME', '@DATA','@CIDADE','@BAIRRO','@HOJE']

# Hold the tags for requisition
AUTO_TAG_REQ = ['@LOCAL','@DESCRICAO','@CRIACAO','@ATUALIZADO','@USUARIO','@CATEGORIA','@TIPO',
                '@SITUACAO','@PROTOCOLO','@SECRETARIA','@TIPODOCUMENTO','@PRAZONORMAL','@PRAZOMAXIMO',
                '@HOJE']



#For each event there is a Field and operation, the tag that may be inside, the operations allowed 
# and the type of validation that shall be applied
VARIABLES_AUTO = {'0' : {'0' : ['Profissão',          AUTO_TAG_CITIZEN,AUTO_OPERATIONS,['text']],
                       '1' : ['Religião',           AUTO_TAG_CITIZEN,AUTO_OPERATIONS,['text']],
                       '2' : ['Cidade',             AUTO_TAG_CITIZEN,AUTO_OPERATIONS,['text']],
                       '3' : ['Bairro',             AUTO_TAG_CITIZEN,AUTO_OPERATIONS,['text']],
                       '4' : ['Nome',               AUTO_TAG_CITIZEN,AUTO_OPERATIONS,['text']],
                       '5' : ['Sexo',               AUTO_TAG_CITIZEN,AUTO_OPERATIONS,['text']],
                       '6' : ['Data',               AUTO_TAG_CITIZEN,AUTO_OPERATIONS,['text']]},
                  '1' : {'0' : ['Data de Aniversário',AUTO_TAG_CITIZEN,['Todos'],[]]},
                  '2' : {'0' : ['Data de Aniversário',AUTO_TAG_PARENT,['Todos'],[]]},
                  '3' : {'0' : ['Data de Aniversário',AUTO_TAG_USER,['Todos'],[]]},
                  '4' : {'0' : ['Situação for Nova',AUTO_TAG_REQ,['Todos'],[]]},
                  '5' : {'0' : ['Atualização da Requisição',AUTO_TAG_REQ,['Todos'],[]]},
                  '6' : {'0' : ['Requisição estiver fora do prazo normal',AUTO_TAG_REQ,['Todos'],[]]},
                  '7' : {'0' : ['Requisição estiver fora do prazo máximo',AUTO_TAG_REQ,['Todos'],[]]},
                  '8' : {'0' : ['Requisição for Concluída',AUTO_TAG_REQ,['Todos'],[]]},
                  '9' : {"0" : ['Requisição for Deleção',AUTO_TAG_REQ,['Todos'],[]]},
}

