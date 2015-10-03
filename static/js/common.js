/*! 
 *   This file holds all constants needed into the 
 *   application. The idea is to bring here all 
 *   data that shall be constants but without download
 *   it from the server every time
 */ 

 /*!
  * Convert every text into universal accent
  * @param wText The text itself
  * @return The new text right encoded
  */
function htmlJs(wText){
    var y=document.createElement('span');
    y.innerHTML=wText;
    return y.innerHTML;
}



// Type of user that may do simple things
var USER_WOR = "Trabalhador";

// Holds the type of email
var MAIL_TYPE = {'0' : '', '1' : 'Pessoal', '2' : 'Trabalho', '3' : 'Outro'};

//Holds the type of email
var PHONE_TYPE = {'0' : '', '1' : 'Celular Pessoal', '2' : 'Celular Trabalho', '3' : 'Fixo Pessoal',
		                    '4' : 'Fixo Trabalho'  , '5' : 'Fax Pessoal'     , '6' : 'Fax Trabalho',
		                    '8' : 'Outro Trabalho' , '9' : 'Desconhecido'}

// Type of requisition
var CATEGORY_REQ = {'0' : htmlJs('Solicita&ccedil;&atilde;o'), '1' : htmlJs('Sugest&atilde;o'), 
		            '2' : htmlJs('Reclama&ccedil;&atilde;o'),  '3' : htmlJs('Den&uacute;ncia'), 
		            '4' : 'Agendamento'}

//Hold the requisition status
var STATUS_REQ = {'0': 'Novo', '1': 'Em andamento', '2': htmlJs('Conclu&iacute;do')}

//Holds the type of questions
var QUESTION_TYPE = {'0' : 'Simples', '1' : 'Múltipla Escolha'};

//Holds the type of options for question
var QUESTION_OPTION = {'0' : '', '1': 'Único', '2' : 'Múltiplo'};

// hold the means of communication
var COMM_TYPES = {'0' :'Notificação', '1' : 'e-Mail', '2' : 'SMS'};

// hold the provider type for mail
var PROVIDER_MAIL = {'0' : 'Genérico', '1' : 'GMAIL'};

//hold the provider type for mail
var COMM_TYPE_MAIL = {'0' : 'SMTP'};

// hold the provider type for mail
var PROVIDER_SMS = {'0' : 'IndexSMS'};

// Hold the phone carriers
var PHONE_CARRIER = {'0' : '', '1' : 'Claro', '2' : 'Oi', '3' : 'Nextel', '4' : 'Tim', '5' : 'Vivo'}

// Hold the dependent type
var DEPENDENT_TYPE = {'0' : '', '1' : htmlJs('Irmão(a)'), '2' : 'Filho(a)', '3' : htmlJs('Cônjuge'), '4':'Pai', 
		                         '5': htmlJs('Mãe'), '6':'Primo(a)', '7':'Tio(a)', '8':'Entiado(a)','9':'Outro'};
// Hold the project status
var PROJ_STATUS_DIC = {'0' : 'Tramitação', '1' : 'Aprovado', '2' : 'Reprovado'};

// Max size photo
var UPLOAD_LIMIT_FILE = [[10240,2560000],[10240,2560000],[10240,2560000]];
var UPLOAD_LIMIT_PHOTO = [10240,1280000];
var UPLOAD_LIMIT_IMGAPP = [[0, 15360],[0, 15360],[0, 15360]];
var PHOTO_LIMIT_SIZE = {'image_chamber':[60,73,100,100],'image_alderman':[43,60,73,80],'image_curr':[120,120,200,200],
                        'image_president':[60,60,120,100],'image_vice1':[60,60,120,100],'image_vice2':[60,60,120,100],
                        'image_sec1':[60,60,120,100],'image_sec2':[60,60,120,100],'image_repo':[100,100,1000,1000]};

// Type of image supported
var TYPE_IMAGE_FILE = ['jpeg','jpg','png'];

var TYPE_INFORMATION_FILE = ['jpeg','jpg','png', 'mp4', '3gp', 'avi', 'mp3', 'wav', 'pdf'];

var UPLOAD_LIMIT_FILE = [[2048,1048576],[2048,1048576],[2048,1048576],[102400, 3145728],[102400, 3145728],[102400, 3145728], [10240, 1048576], [10240, 1048576], [10240, 1048576]];

// Hold the social media information
var SOCIAL_MEDIA_NAME = {'0' : 'E-mail', '1' : 'Facebook', '2' : 'G+', '3' : 'Instagram', '4' : 'Linkedin',
		                  '5' : 'Twitter', '6' : 'Whatsapp', '7' : 'Youtube'}
var SOCIAL_MEDIA_ICON = {'0' : 'email.jpg', '1' : 'facebook.jpg', '2' : 'gplus.jpg', '3' : 'instagram.jpg', '4' : 'linkedin.jpg',
        '5' : 'twitter.jpg', '6' : 'whatsapp.jpg', '7' : 'youtube.jpg'}

// Google chars default list of colors to be used when the things colors are null
var GOOGLE_COLORS = ['#3366CC','#DC3912','#FF9900','#109618','#990099','#3B3EAC','#0099C6','#DD4477',
                     '#66AA00','#B82E2E','#316395','#994499','#22AA99','#AAAA11','#6633CC','#E67300',
                     '#8B0707','#329262','#5574A6','#3B3EAC']

// Hold the extensive month names
var MONTH_LONG = {'01':'Janeiro','02':'Fevereiro','03':'Março','04':'Abril','05':'Maio','06':'Junho',
                    '07':'Julho','08':'Agosto','09':'Setembro','10':'Outubro','11':'Novembro','12':'Dezembro'};

// Hold the person marital status
var MARITAL_STATUS = {'0':'Solteiro','1':'Casado','2':'Viúvo','3':'Separado','4':'Divorciado'};

// Hold the person literacy
var LITERACY = {'0':'Analfabeto','1':'Lê e Escreve','2':'1º Incompleto','3':'1º Completo','4':'2º Incompleto','5':'2º Completo',
                '6':'Técnico','7':'Superior Incompleto','8':'Superior Completo','9':'Pós Incompleto','10':'Pós Completo'};

//Hold the type of interface for automation UI
var AUTO_AUTOMATION = '1';
var AUTO_CALENDAR = '2';

//Hold the automation event info
var AUTO_EVENT_INFO = {0 : 'Data Customizada', 
		               1 : htmlJs('Anivers&aacute;rio de Mun&iacute;cipe'), 
		               2 : htmlJs('Anivers&aacute;rio de Parente de Mun&iacute;cipe'),
					   3 : htmlJs('Anivers&aacute;rio de Usu&aacute;rio do Sistema'), 
					   4 : htmlJs('Requisi&ccedil;&atilde;o - Nova'), 
					   5 : htmlJs('Requisi&ccedil;&atilde;o - Atualiza&ccedil;&atilde;o'),
	                   6 : htmlJs('Requisi&ccedil;&atilde;o - Fora do prazo normal'),
	                   7 : htmlJs('Requisi&ccedil;&atilde;o - Fora do prazo m&aacute;ximo'),
					   8 : htmlJs('Requisi&ccedil;&atilde;o - Conclu&iacute;da'),
					   9 : htmlJs('Requisi&ccedil;&atilde;o - Dele&ccedil;&atilde;o')}

// Hold the automation operation between the fields and the value
var AUTO_OPERATIONS = ['Todos','Igual a','Diferente de'];

// Hold the tags for person
var AUTO_TAG_CITIZEN = ['@PROFISSAO','@RELIGIAO','@CIDADE','@BAIRRO','@NOME','@SEXO','@DATA','@HOJE'];

// Hold the tags for parent
var AUTO_TAG_PARENT = ['@NOME','@DATA','@RELACAO','@HOJE'];

// Hold the tags for system users
var AUTO_TAG_USER = ['@NOME', '@DATA','@CIDADE','@BAIRRO','@HOJE'];

// Hold the tags for requisition
var AUTO_TAG_REQ = ['@LOCAL','@DESCRICAO','@CRIACAO','@ATUALIZADO','@USUARIO','@CATEGORIA','@TIPO',
                    '@SITUACAO','@PROTOCOLO','@SECRETARIA','@TIPODOCUMENTO','@PRAZONORMAL','@PRAZOMAXIMO',
                    '@HOJE'];
/*!
 * For each event there is a Field and operation, the tag that may be inside, the operations allowed 
 * and the type of validation that shall be applied
 */
var VARIABLES_AUTO = {0 : {0 : [htmlJs('Profiss&atilde;o'),          AUTO_TAG_CITIZEN,AUTO_OPERATIONS,['text']],
					       1 : [htmlJs('Religi&atilde;o'),           AUTO_TAG_CITIZEN,AUTO_OPERATIONS,['text']],
						   2 : [htmlJs('Cidade'),                    AUTO_TAG_CITIZEN,AUTO_OPERATIONS,['text']],
						   3 : [htmlJs('Bairro'),                    AUTO_TAG_CITIZEN,AUTO_OPERATIONS,['text']],
						   4 : [htmlJs('Nome'),                      AUTO_TAG_CITIZEN,AUTO_OPERATIONS,['text']],
						   5 : [htmlJs('Sexo'),                      AUTO_TAG_CITIZEN,AUTO_OPERATIONS,['text']],
						   6 : [htmlJs('Data'),                      AUTO_TAG_CITIZEN,AUTO_OPERATIONS,['text']]},
					  1 : {0 : [htmlJs('Data de Anivers&aacute;rio'),AUTO_TAG_CITIZEN,['Todos'],[]]},
					  2 : {0 : [htmlJs('Data de Anivers&aacute;rio'),AUTO_TAG_PARENT,['Todos'],[]]},
					  3 : {0 : [htmlJs('Data de Anivers&aacute;rio'),AUTO_TAG_USER,['Todos'],[]]},
					  4 : {0 : [htmlJs('Situa&ccedil;&atilde;o for Nova'),AUTO_TAG_REQ,['Todos'],[]]},
					  5 : {0 : [htmlJs('Atualiza&ccedil;&atilde;o da Requisi&ccedil;&atilde;o'),AUTO_TAG_REQ,['Todos'],[]]},
	                  6 : {0 : [htmlJs('Requisi&ccedil;&atilde;o estiver fora do prazo normal'),AUTO_TAG_REQ,['Todos'],[]]},
	                  7 : {0 : [htmlJs('Requisi&ccedil;&atilde;o estiver fora do prazo m&aacute;ximo'),AUTO_TAG_REQ,['Todos'],[]]},
					  8 : {0 : [htmlJs('Requisi&ccedil;&atilde;o for Conclu&iacute;da'),AUTO_TAG_REQ,['Todos'],[]]},
					  9 : {0 : [htmlJs('Requisi&ccedil;&atilde;o for Dele&ccedil;&atilde;o'),AUTO_TAG_REQ,['Todos'],[]]},
}

/*!
 * Language for Data table in jquery
 */
LANG_FOR_TABLE = {
    processing: "Processando...",
    search: "Filtro :",
    lengthMenu: "_MENU_ elementos por página",
    info: "Mostrando de _START_ à _END_ no total de _TOTAL_ elemento(s)",
    infoEmpty: "Não há elementos",
    infoFiltered: "(filtrado _MAX_ elemento(s) de _TOTAL_)",
    infoPostFix: "",
    loadingRecords: "processando...",
    zeroRecords: "Nenhum elemento na tabela",
    emptyTable: "Nenhum elemento encontrado.",
    paginate: {
        first: "Primeiro",
        previous: "Anterior",
        next: "Próximo",
        last: "Último"
    }
};

function downloadFile(url){
    document.getElementById('download_target').src=url;
}
