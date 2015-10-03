
function exporeError(wParam,wType){
	
	window.scroll(0,0);
	text = htmlJs('Erro desconhecido ou n&atilde;o reportado!');
	// for all empty field items
	if (wType=='custom')
		text = htmlJs(wParam);
	else if (wType=='empty_field')
		text = htmlJs('<b>O campo '+wParam+' n&atilde;o pode ser vazio!</b>');
    else if (wType=='larger_field')
        text = htmlJs('<b>O campo '+wParam[0]+' n&atilde;o pode conter mais de '+wParam[1]+' caracteres!</b>');
    else if (wType=='search_field')
        text = htmlJs('<b>A Busca '+wParam[0]+' n&atilde;o suporta os caracteres <i>'+wParam[1]+'</i>.</b>');
    else if (wType=='search_field_date')
        text = htmlJs('<b>A Busca '+wParam[0]+' n&atilde;o suporta <i>'+wParam[1]+'</i>.</b>');
    else if (wType=='larger_field_tag')
        text = htmlJs('<b>O campo '+wParam+' est&aacute muito grande, remova algum conte&uacute;do!</b>');
    else if (wType=='short_field')
        text = htmlJs('<b>O campo '+wParam[0]+' n&atilde;o pode conter menos de '+wParam[1]+' caracteres!</b>');
    else if (wType=='quotation_field')
        text = htmlJs('<b>O campo '+wParam+' n&atilde;o aceita os caracteres \' ou \"!</b>');
    else if (wType=='number_field')
        text = htmlJs('<b>O campo '+wParam+' aceita somente n&uacute;meros!</b>');
    else if (wType=='invalid_field')
        text = htmlJs('<b>O campo '+wParam+' &eacute; inv&aacute;lido!</b>');
    else if (wType=='invalid_position')
    	text = htmlJs('N&atilde;o foi poss&iacute;vel editar a '+wParam[0]+', a posiç&atilde;o '+wParam[1]+' &eacute; inv&aacute;lida!')
    else if (wType=='invalid_selection')
        text = htmlJs('<b>Nenhuma op&ccedil;&atilde;o foi selecionado no campo '+wParam+'!</b>');
    else if (wType=='empty_file')
        text = htmlJs('<b>O anexo do bot&atilde;o '+wParam+' n&atilde;o pode ser vazio!</b>');
    else if (wType=='invalid_file')
        text = htmlJs('<b>O tipo de arquivo carregado n&atilde;o &eacute; v&aacute;lido para o campo '+wParam+'!</b>');
    else if (wType=='file_size')
        text = htmlJs('<b>No campo '+wParam[0]+', o tamanho do arquivo deve estar entre '+wParam[1]+' e '+wParam[2]+'!</b>');
    else if (wType=='browser_file_api')
        text = htmlJs('<b>O seu browser n&atilde;o suporta a API de arquivo. Tente utilizar outro browser!</b>');
    else if (wType=='browser_file_files')
        text = htmlJs('<b>O seu browser n&atilde;o suporta a propriedade "files" no arquivo de entrada. Tente utilizar outro browser!</b>');
    else if (wType=='invalid_file_name')
        text = htmlJs('<b>O nome do arquivo carregado n&atilde;o &eacute; v&aacute;lido para o campo '+wParam+'!</b>');
    else if (wType=='invalid_file_name_size')
        text = htmlJs('<b>No campo '+wParam[0]+', o tamanho do nome do arquivo deve ser menor que '+wParam[1]+' caracteres!</b>');
    else if (wType=='date_equal_and_greater')
        text = htmlJs('<b>No campo '+wParam[0]+', deve ser maior ou igual a '+wParam[1]+'!</b>');

    
    if (wType=='return_data'){
        var ret = wParam.split(' ');
        var part = ret[0];
        ret.shift();
        text = ret.join(' ');
        $('#error_div').hide();
        $('#warning_div').hide();
        $('#success_div').hide();
        if (part=='success'){
            $('#success_span').html(text);
            $("#success_div").show();
        } 
        else if (part=='warning'){
            $('#warning_span').html(text);
            $("#warning_div").show(); 
        }
        else if (part=='error'){
            $('#error_span').html(text);
            $("#error_div").show();
        }
        else if (part=='info'){
            $('#info_span').html(text);
            $("#info_div").show();
        }
    }
    else{
        $('#error_div').hide();
        $('#error_span').html(text);
        $("#error_div").show();
    }
    try {
    	$("#overlay").css('visibility','hidden');
    }
    catch(err){
    	console.log('No overlay applied')
    }
	return false;
}