
var aceito ={
    texto: /[a-zA-ZàáâãäåÀÁÂÃÄÅéëèêÈÉÊËîìïíÏÎÍÌôòõöóÖÔÓÒÕûùüúÜÛÚÙÑñçÇ. ]+/,
    numero:/[0-9]+/,
    textoNumero: /[a-zA-Z0-9àáâãäåÀÁÂÃÄÅéëèêÈÉÊËîìïíÏÎÍÌôòõöóÖÔÓÒÕûùüúÜÛÚÙÑñçÇ. ]+/,
    telefone: /[-0-9\(\)+ ]+/,
    cep : /[-0-9 ]+/,
    cpfrg : /[-0-9\.]+/,
    cnpj : /[-0-9\.\/ ]+/,
    textoSemAcento: /[a-zA-Z. ]+/,
    textoNumeroSemAcento: /[a-zA-Z0-9. ]+/,
    textoVarios: /[-a-zA-Z0-9àáâãäåÀÁÂÃÄÅéëèêÈÉÊËîìïíÏÎÍÌôòõöóÖÔÓÒÕûùüúÜÛÚÙÑñçÇ!\n@$%*()\\+=\[\].\/{}<>:?\'°ºª ]+/,
    comAspa : /[\"\']+/,
    site : /[-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?/gi,
    phone: /[\s ()-]/g,
    search: /[\"\'%]+/,
};
var invalido = "";


/*!
 * Run the validation over the basic searchs information, it means, avoid ', " and %
 * @param wValue The input to be evaluated
 * @return True for OK or the problem
 */
function validateBasicSearch(wValue){
    if(wValue == "") return true;
    if(wValue.match(aceito['search']) == null) return true;
    else return false;
    if(Value.length != wValue.match(aceito['search'])[0].length){
        return false;
    }
    return true;
}

/*!
 * Check if the search contains a valid date, it may be
 * a day, a day and a month or a day and a month and a year
 * @param wValue The text to be evaluated
 * @return  0 - OK, 1 - Empty, 2 - Day wrong, 3 - Day wrong or 4 Year wrong, 5 - Invalid date
 */
function validateDataSearch(wValue){
	if ((wValue=="")||(wValue==undefined)) return 1;
	var parts = wValue.split('/');
	switch (parts.length){
		case 1:
			if (validateNumber(parts[0])){
				if ((Number(parts[0])>0) && (Number(parts[0])<32)) return 0;
				else return 2;
			}
			return 2;
			break;
		case 2: 
			if (validateNumber(parts[0])){
				if ((Number(parts[0])<1) || (Number(parts[0])>31)) return 2;
			}
			else return 2;
			if (validateNumber(parts[1])){
				if ((Number(parts[1])<1) || (Number(parts[1])>12)) return 3;
			}
			else return 3;
			return 0;
			break;
		case 3: 
			if (validateNumber(parts[0])){
				if ((Number(parts[0])<1) || (Number(parts[0])>31)) return 2;
			}
			else return 2;
			if (validateNumber(parts[1])){
				if ((Number(parts[1])<1) || (Number(parts[1])>12)) return 3;
			}
			else return 3;
			if (validateNumber(parts[2])){
				if ((Number(parts[2])<2015) || (Number(parts[2])>2100)) return 4;
			}
			else return 4;
			return 0;
			break;
		default:
			return 5;
			break;
	}
}

function validaTexto(valor){
    if(valor == "") return true;
    if(valor.match(aceito['texto']) == null){invalido = valor[0]; return false;}
    if(valor.length != valor.match(aceito['texto'])[0].length){
        invalido = valor[valor.match(aceito['texto'])[0].length];
        return false;
    }
    return true;
}

function validateNoQuotation(valor){
    if(valor == ""){return true;}
    if(valor.match(aceito['comAspa']) == null) return true;
    else return false;
    if(valor.length != valor.match(aceito['comAspa'])[0].length){
        return false;
    }
    return true;
}


function validateNumber(valor){
    if(valor == "") return true;
    if(valor.match(aceito['numero']) == null)  return false;
    if(valor.length != valor.match(aceito['numero'])[0].length){
        return false;
    }
    return true;
}

function validaTextoNumero(valor){
    if(valor == ""){return true;}
    if(valor.match(aceito['textoNumero']) == null){invalido = valor[0]; return false;}
    if(valor.length != valor.match(aceito['textoNumero'])[0].length){
        invalido = valor[valor.match(aceito['textoNumero'])[0].length];
        return false;
    }
    return true;
}

function validaTelefone(valor){
    if(valor == ""){return true;}
    if(valor.match(aceito['telefone']) == null){invalido = valor[0]; return false;}
    if(valor.length != valor.match(aceito['telefone'])[0].length){
        invalido = valor[valor.match(aceito['telefone'])[0].length];
        return false;
    }
    return true;
}

function validaCpfRg(valor){
    if(valor == ""){return true;}
    if(valor.match(aceito['cpfrg']) == null){invalido = valor[0]; return false;}
    if(valor.length != valor.match(aceito['cpfrg'])[0].length){
        invalido = valor[valor.match(aceito['cpfrg'])[0].length];
        return false;
    }
    return true;
}

function validaCnpj(valor){
    if(valor == ""){return true;}
    if(valor.match(aceito['cnpj']) == null){invalido = valor[0]; return false;}
    if(valor.length != valor.match(aceito['cnpj'])[0].length){
        invalido = valor[valor.match(aceito['cnpj'])[0].length];
        return false;
    }
    return true;
}

function validaTextoSemAcento(valor){
    if(valor == ""){return true;}
    if(valor.match(aceito['textoSemAcento']) == null){invalido = valor[0]; return false;}
    if(valor.length != valor.match(aceito['textoSemAcento'])[0].length){
        invalido = valor[valor.match(aceito['textoSemAcento'])[0].length];
        return false;
    }
    return true;
}

function validaTextoNumeroSemAcento(valor){
    if(valor == ""){return true;}
    if(valor.match(aceito['textoNumeroSemAcento']) == null){invalido = valor[0]; return false;}
    if(valor.length != valor.match(aceito['textoNumeroSemAcento'])[0].length){
        invalido = valor[valor.match(aceito['textoNumeroSemAcento'])[0].length];
        return false;
    }
    return true;
}

function validaTextoVarios(valor){
    if(valor == ""){return true;}
    if(valor.match(aceito['textoVarios']) == null){invalido = valor[0]; return false;}
    if(valor.length != valor.match(aceito['textoVarios'])[0].length){
        invalido = valor[valor.match(aceito['textoVarios'])[0].length];
        return false;
    }
    return true;
}

function validateEmail(wEmail) {
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (wEmail == '' || wEmail == null) return true;
    if (re.test(wEmail) == true && wEmail.length <= 50) return true;
    else return false;
}

function validateCPF(wcpf){
    var Soma;
    var Resto;
    Soma = 0;
    var strCPF;
    strCPF = wcpf.replace(/[.-]/g, '');
    //strCPF = strcpf1.replace("-",'');
    if (strCPF == "00000000000") return false;
    for (i=1; i<=9; i++) Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (11 - i);
    Resto = (Soma * 10) % 11;
    if ((Resto == 10) || (Resto == 11)) Resto = 0;
    if (Resto != parseInt(strCPF.substring(9, 10)) ) return false;
    Soma = 0;
    for (i = 1; i <= 10; i++) Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (12 - i);
    Resto = (Soma * 10) % 11;
    if ((Resto == 10) || (Resto == 11)) Resto = 0;
    if (Resto != parseInt(strCPF.substring(10, 11) ) ) return false;
    return true;
}

function validateCEP(wCep){
    if ((wCep == '') || (wCep==null)) return false;
    wCep = wCep.replace(/[.-]/g, '');
    if (wCep.length != 8) return false;
    if (isNaN(wCep)) return false;
    return true;
}

var numbers_string="0123456789";
var not_char = /[!?#$%'"()*]/g;

function haveNumbers(wText){
   for(i=0; i<wText.length; i++)
      if (numbers_string.indexOf(wText.charAt(i),0)!=-1)
         return false;
   return true;
} 

function validateName(wName, wAllowNumber){
    if ((wName != '') && (wName != null)){
        if  ((haveNumbers(wName) == true)|| (wAllowNumber =='undefined')){
            var vect = wName.split(' ').filter(function(n){ return ((n != undefined) && (n.length>=2))});
            if (vect.length>1){
                var x = wName.match(not_char);
                if (x == null) return true;
                else return false;   
            }
            else return false;
        }
        else return false;
    }
    return true;
}

function validateAddress(wItem){
	if (wItem == '' || wItem == null) return true;
	else{
		var x = wItem.match(not_char);
		if (x == null) return true;
		else return false;
	}
}

function validateStreet(wItem){
    var street = validateAddress(wItem);
    var notCaracter = validateCaracter(wItem);
    if (street == true && notCaracter == true && wItem.length <= 100){
        var res = wItem.split(" ");
        if (res[1] == undefined)
            return false;
        else
            return true;
    }
   
}

var caracter="!@#$%()_+/?°;·,{}[]§:<'>*";
function validateCaracter(wItem){
   wItem = wItem.replace(/\s/g, '');
   for(i=0; i<wItem.length; i++)
      if (caracter.indexOf(wItem.charAt(i),0)!=-1)
         return false;
   return true;
}

function validatePassword(wPassword){
	if (wPassword.length >= 10 && validateCaracter(wPassword) == false)
		return true;
	else
		return false;
}



var acentos = "àáâãäåÀÁÂÃÄÅéëèêÈÉÊËîìïíÏÎÍÌôòõöóÖÔÓÒÕûùüúÜÛÚÙÑñçÇ"

function validateAcento(wText){
    wText = wText.replace(/\s/g, '');
   for(i=0; i<wText.length; i++)
      if (acentos.indexOf(wText.charAt(i),0)!=-1)
         return false;
   return true;
} 

function validateCNPJ(wCNPJ){
	wCNPJ = wCNPJ.replace('.','');
	wCNPJ = wCNPJ.replace('.','');
	wCNPJ = wCNPJ.replace('.','');
	wCNPJ = wCNPJ.replace('-','');
	wCNPJ = wCNPJ.replace('/','');
    cnpj = wCNPJ;
    var numeros, digitos, soma, i, resultado, pos, tamanho, digitos_iguais;
    digitos_iguais = 1;
    if (cnpj.length < 14 && cnpj.length < 15)
        return false;
    for (i = 0; i < cnpj.length - 1; i++)
        if (cnpj.charAt(i) != cnpj.charAt(i + 1)){
        digitos_iguais = 0;
        break;
    }
    if (!digitos_iguais){
        tamanho = cnpj.length - 2
        numeros = cnpj.substring(0,tamanho);
        digitos = cnpj.substring(tamanho);
        soma = 0;
        pos = tamanho - 7;
        for (i = tamanho; i >= 1; i--){
            soma += numeros.charAt(tamanho - i) * pos--;
            if (pos < 2)
                pos = 9;
        }
        resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
        if (resultado != digitos.charAt(0))
            return false;
        tamanho = tamanho + 1;
        numeros = cnpj.substring(0,tamanho);
        soma = 0;
        pos = tamanho - 7;
        for (i = tamanho; i >= 1; i--){
            soma += numeros.charAt(tamanho - i) * pos--;
            if (pos < 2)
                pos = 9;
        }
        resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
        if (resultado != digitos.charAt(1))
            return false;
        return true;
    }
    else
        return false;
}

var caracterLess="\' @ \" ";
function validateFieldMenageNumber(wItem){
	wItem = wItem.replace(/\s/g, '');
   for(i=0; i< wItem.length; i++)
      if (caracterLess.indexOf(wItem.charAt(i),0)!=-1)
         return false;
   return true;
}

function checkDate(data_nasc, not_birth){
    var data = data_nasc;
    date = new Date();
    if (data.length != 3) return false;
    if ((data[0].length) != 2 || (data[1].length) != 2 || (data[2].length) != 4) return false;
    if ((data[1] <= 12) && (data[1]>= 1)){
        if((data[1] == 1) || (data[1] == 3) || (data[1] == 5) || (data[1] == 7) || (data[1] == 8) || (data[1] == 10) || (data[1] == 12)){
            if ((data[0] <= 31) && (data[0]>= 1)){
                if ((not_birth) || (data[2] <= date.getFullYear())) return true;
            }
        }
        else if ((data[1] == 4) || (data[1] == 6) || (data[1] == 9) || (data[1] == 11)){
            if ((data[0] <= 30) && (data[0]>= 1)){
                if ((not_birth) || (data[2] <= date.getFullYear())) return true;
            }
        }
        else if(data[1] == 2){
            if((data[2] % 4 == 0) && (data[2] % 100 != 0) || (data[2] % 400 == 0)){
                if ((data[0] <= 29) && (data[0]>= 1)){
                    if ((not_birth) || (data[2] <= date.getFullYear())) return true;
                }
            }
            else{
                if ((data[0] <= 28) && (data[0]>= 1)){
                    if ((not_birth) || (data[2] <= date.getFullYear())) return true;
                }
            }
        }
    }
    return false;
}

function checkFile(wFile){
	var type = wFile.split('.');
	type = type[type.length-1];
	for (i=0;i<TYPE_INFORMATION_FILE.length;i++){
		if (TYPE_INFORMATION_FILE[i] == type) return true;
	}
	return false;
}

/*!
 * Check if the phone number is valid, it remove the non number itens,
 * check if the rest is a number and validate the lenght throgh size of 
 * at least 10 and not more than 15
 * @param wNumber the number enter
 * @return 1 if ok, 0 if not number -1 if to sort and -2 if to long
 */
function validatePhoneNumber(wNumber){
	var clean_number = wNumber.replace(aceito['phone'], '');
	if (validateNumber(clean_number)==false) return 0;
	if (clean_number.lenght>15)               return -1;
	if (clean_number.lenght<10)               return -2;
	return 1;
}

/*!
 * Validate a website based on regular expression
 */
function validateWebSite(wURL){
	 if (wURL.match(aceito['site'])) return true;
	 return false;
}

/*!
 *  Validate the image
 * @param wFile The file input
 * @param wSizeVector The vector with minimum and maximum size
 * @param wTypeVector The vector of the allowed type
 * @param wField The field in the form for error message
 * @param wPreview If the image must be showed
 * @return The success or not
 */
function validateImage(wFile,wSizeVector,wTypeVector,wField, wPreview,wResolution) {

    if (!window.File || !window.FileReader || !window.FileList || !window.Blob)
      return exporeError('browser_file_api');;
    
    if (!wFile.files)
        return exporeError('browser_file_files');;
    if (!wFile.files[0])
      return false;
   
    full_path = wFile.value;
    if (full_path) {
    	var start_index = (full_path.indexOf('\\') >= 0 ? full_path.lastIndexOf('\\') : full_path.lastIndexOf('/'));
    	var file_name = full_path.substring(start_index);
    	if (file_name.indexOf('\\') === 0 || file_name.indexOf('/') === 0) {
    		var file_name_length = (file_name.substring(1)).length;
    		if (file_name_length>75) return exporeError([wField,75],'invalid_file_name_size');
    	}
    	else return exporeError(wField,'invalid_file_name');
    }
    else return exporeError(wField,'invalid_file_name');
    
    var reader = new FileReader();
    var error = false, contain = false;

    reader.readAsDataURL(wFile.files[0]);
    for (var i=0;i<wTypeVector.length;i++){
        if (wFile.files[0].type.indexOf(wTypeVector[i])!=-1){
            if ((wFile.files[0].size<wSizeVector[i][0]) || (wFile.files[0].size>wSizeVector[i][1])){
                wFile.value = "";
                $('#'+wPreview).attr("src","/legislator/static/images/man_photo.png");
                return exporeError([wField,formatFileSize(wSizeVector[i][0])[2],formatFileSize(wSizeVector[i][1])[2]],'file_size');
            }
            contain = true;
            break;
        }
    }
    if (!contain){
        wFile.value = "";
        $('#'+wPreview).attr("src","/legislator/static/images/man_photo.png");
        return exporeError(wField,'invalid_file');
    }
    else{
        if ((wPreview != undefined)&&(wPreview != 'undefined')){
            var image  = new Image();
            return reader.onload = function(_file) {
                image.src    = _file.target.result;              // url.createObjectURL(file);
                
                image.onload = function() {
                    if (((image.naturalWidth < wResolution[wPreview][0]) || (image.naturalHeight < wResolution[wPreview][1])) || 
                        ((image.naturalWidth > wResolution[wPreview][2]) || (image.naturalHeight > wResolution[wPreview][3]))){
                        if (wResolution[wPreview][0]!=wResolution[wPreview][2]){
                            wFile.value = "";
                            $('#'+wPreview).attr("src","/legislator/static/images/man_photo.png");
                            return exporeError('<b>A resolução da imagem no campo '+wField+' deve estar entre '+wResolution[wPreview][0]+
                                               'x'+wResolution[wPreview][1]+' e '+wResolution[wPreview][2]+
                                               'x'+wResolution[wPreview][3]+'!</b>','custom');
                        }
                        else{
                            wFile.value = "";
                            $('#'+wPreview).attr("src","/legislator/static/images/man_photo.png");
                            return exporeError('<b>A resolução da imagem no campo '+wField+' deve ser de '+wResolution[wPreview][0]+
                                    'x'+wResolution[wPreview][1]+'!</b>','custom');
                        }
                    }
                    else{
                        if (wPreview!='undefined')
                           $('#'+wPreview).attr("src",this.src);
                    }
                };
                image.onerror= function() {
                    wFile.value = "";
                    $('#'+wPreview).attr("src","/legislator/static/images/man_photo.png");
                    return exporeError(wField,'invalid_file');
                };
            }; 
        }
    }
}