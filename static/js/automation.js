
// Hold all overlay forms
var overlay_repo_city = ['processing','add_custom_window','remove_custom_window','confirm_deletion_window'];

// hold the commemoration
var commem_dates = [];

// hold the means of communication
var means_comm = [];

// which event is in use
var event_in_use = {};

// which field is selected
var field_in_use = [];

// which interface shall be processed
var interface_active = '2';

/*!
 * start the interface
 * @param wData All the actions created by the company
 * @param wInterface The current interface running
 * @param wMeans The means of communication
 * @param wList The list 
 */
function fill_search(wData,wInterface,wMeans,wList){
	manage_overlay('show','processing');
    interface_active = wInterface;
    
    if (wInterface==AUTO_AUTOMATION){
    	$('#calendar_button').hide();
    	$('#not_found').text(htmlJs('Nenhuma a&ccedil;&atilde;o autom&aacute;tica foi encontrada!'));
    	$('#action_date').prop('disabled',true);
    	var select = document.getElementById("action_filter");
    	for (var i in AUTO_EVENT_INFO)
    		if (i!=0)
    			select.options[i] = new Option(AUTO_EVENT_INFO[i], i);
    }
    else{
    	var d = new Date();
    	buildCalendar(d.getFullYear(),'calendar','getDateCalendar','addNewDate','removeNewDate',
    			'/legislator/backcall/load_holidays/','/legislator/backcall/load_mydates/','900px');
    	$('#calendar_button').show();
    	$('#not_found').text(htmlJs('Nenhuma a&ccedil;&atilde;o no calend&aacute;rio foi encontrada!'));

    	var select = document.getElementById("action_filter");
    	select.options[1] = new Option(AUTO_EVENT_INFO[0], 0);
    }

    if (wList.length>0) fillSearchList(wList,wInterface);
    
	$('#my_new_date').inputmask('99/99/9999');
	$('#action_date').inputmask('99/99/9999');
    
	means_comm = wMeans;
	var select = document.getElementById("action_channel");
	for (var i=0;i<wMeans.length;i++)
		select.options[i] = new Option(wMeans[i]['comm_title'], wMeans[i]['id']);
	
	changeTypeEvent(document.getElementById("action_filter"));
	$('#value').prop('disabled', true);

	if (Object.keys(wData).length!=0){
		fillForm(wData);
	}
	else{
		addRichText();
	}

	manage_overlay('hide','');
}

/*!
 * Fill form fields with a JSON result
 * @param wData The date itself
 */
function fillForm(wData){
	$('#action_title').val(wData['action_title']);
	$('#action_date').val(wData['action_date']);
	$('#action_channel').val(wData['action_channel']);
	changeChannelEvent(document.getElementById('action_channel'));
	$('#action_filter').val(wData['action_filter']);
	changeTypeEvent(document.getElementById('action_filter'));
	$('#action_field').val(wData['action_field']);
	changeFieldEvent(document.getElementById('action_field'));
	$('#action_operation').val(wData['action_operation']);
	changeOperationEvent(document.getElementById('action_operation'));
	if (wData['action_value']!='NULL')
		$('#action_value').val(wData['action_value']);
	else
		$('#action_value').val('');
	addRichText(wData['action_msg']);
}

/*!
 * Run the validation and submit for each interface
 */
function submitAutomation(){
	manage_overlay('show','processing');
    var content = $('#action_title').val();
    if (content=='')                       return exporeError('"Título"','empty_field');
    if (!validateNoQuotation(content))     return exporeError('"Título"','quotation_field');
    if (content.length>127)                return exporeError(['"Título"',127],'larger_field');

	content = CKEDITOR.instances.action_msg.getData().length;
	if (content.length==0)		            return exporeError('"Mensagem"', 'empty_field');
	if (content>3000)				        return exporeError('"Mensagem"','larger_field_tag');
	content = CKEDITOR.instances.action_msg.document.getBody().getText().length;
	if (content>1000)				        return exporeError(['"Mensagem"',1000],'larger_field');

	// check for SMS channel type
	select = document.getElementById('action_channel');
	var id = select.options[select.selectedIndex].value;
	for (var i=0;i<means_comm.length;i++)
		if (means_comm[i]['id']==id){
			if (COMM_TYPES[means_comm[i]['comm_type']]=='SMS')
				if (content>140)	    	
					return exporeError(['"Mensagem" para envio por SMS',140],'larger_field');
			break;
		}
	

	if (interface_active!=AUTO_AUTOMATION){
		content = $('#action_date').val();
		if(content=='')			            	return exporeError('"Data"','empty_field');
		if (!checkDate(content.split('/')))		return exporeError('"Data"','invalid_field');

		var date = parseDate(content+" 23:59:59.999");
		if (date.getTime()>=(new Date()).getTime())
			return exporeError(['"Data"','"data de hoje"'],'date_equal_and_greater');
	}
	
	if ($('#action_filter').val()=='')      return exporeError('"Tipo de Evento"','empty_field');
	if ($('#action_channel').val()=='')     return exporeError('"Enviar Via"','empty_field');
	if ($('#action_field').val()=='')       return exporeError('"Campo"','empty_field');
	if ($('#action_operation').val()=='')   return exporeError('"Operador"','empty_field');
	
	if ($('#action_operation option:selected').text()!='Todos'){
		content = $('#action_value').val();
		if (content=='')                    return exporeError('"Valor"','empty_field');
	    if (!validateNoQuotation(content))  return exporeError('"Valor"','quotation_field');
	    if (content.length>127)             return exporeError(['"Valor"',127],'larger_field');

	}
	
	document.getElementById('form_category').submit();
}

/*!
 * Called when the channel type is changed
 * @param wSelect The select component
 */
function changeChannelEvent(wSelect){
	var id = wSelect.options[wSelect.selectedIndex].value;
	for (var i=0;i<means_comm.length;i++)
		if (means_comm[i]['id']==id){
			if (COMM_TYPES[means_comm[i]['comm_type']]=='SMS'){
				// save the text before remove the instance
				var text = CKEDITOR.instances.action_msg.document.getBody().getText();
				CKEDITOR.instances['action_msg'].destroy(true);
				$('#action_msg').val(text);
			}
			else
				addRichText();
			break;
		}
}

/*!
 * When the type of event is changed, the field items is changed
 * @param wSelect The select that generates the event
 */
function changeTypeEvent(wSelect){
	$('#action_field').find('option').remove();
	if (wSelect.selectedIndex==0) return ;
	event_in_use = VARIABLES_AUTO[wSelect.options[wSelect.selectedIndex].value];
	var field = document.getElementById("action_field");
	var index = 1;
	for (var key in event_in_use) field[index++] = new Option(event_in_use[key][0],key);

	$('#action_operation').find('option').remove();
}

/*!
 * When the field is selected, the operator must be filled
 * @param wSelect The select that generates the event
 */
function changeFieldEvent(wSelect){
	if (wSelect.selectedIndex==0) return ;
	field_in_use = event_in_use[wSelect.options[wSelect.selectedIndex].value];
	var operation = document.getElementById("action_operation");
	for (var i=0;i<field_in_use[2].length;i++) operation[i+1] = new Option(field_in_use[2][i],i);

	$('#action_value').prop('disabled', true);
}

/*!
 * When the operation is selected, 
 */
function changeOperationEvent(wSelect){
	if (wSelect.selectedIndex==0) return ;
	$('#action_value').prop('disabled', wSelect.options[wSelect.selectedIndex].text=='Todos');
}

/*!
 * Process the rich text content or the CKEDITOR
 * @param wContent the content itself or an undefined or null item
 */
function addRichText(wContent){
	if (CKEDITOR.instances['action_msg']==undefined){
		CKEDITOR.replace( 'action_msg', {
			language: 'pt-br',
			skin : 'moonocolor'
		});
	}
	if ((wContent!=undefined) && (wContent!=null)){
		CKEDITOR.instances.action_msg.on("instanceReady",function() {
           // this is current editor instance
  		 this.insertHtml(wContent.replace(/\'/g,"'"));
		});
	}
}

/*!
 * Fill the list of actions based on the interface
 * @param wList The list with all items to be draw
 * @param wInterface the type of interface
 */
function fillSearchList(wList, wInterface){
	var table = '<center style="margin-top:25px;padding-top:25px;" ><table id="table_automation" style="width:100%;"'+
	'class="table table-striped table-bordered" cellspacing="0" ><thead><tr>'+
	'<th style="text-align:center;width:150px;">Criado</th><th style="text-align:center;">T&iacute;tulo</th>';
	if (wInterface!=AUTO_AUTOMATION)
		table+='<th style="text-align:center;">Execu&ccedil;&atilde;o</th>';
	table+='<th style="text-align:center;width:150px;">Atualizado</th><th style="text-align:center;width:150px;">Alterado Por</th>'+
	'<th style="text-align:center;width:100px;">Ações</th></tr></thead><tbody>';
	for (i=0;i<wList.length;i++){
		table+='<tr ><td style="min-width:120px;vertical-align:middle;">'+dateAndTime(wList[i]['created'])+'</td><td style="text-align:center;vertical-align:middle;">'+
	 		wList[i]['action_title']+'</td>';
		if (wInterface!=AUTO_AUTOMATION)
			table+='<td style="vertical-align:middle;text-align:center;">'+dateOnly(wList[i]['action_date'])+'</td>';
		table+='<td>'+dateAndTime(wList[i]['last_update'])+'</td>'+
		    '</td><td style="text-align:center;vertical-align:middle;">'+wList[i]['first_name']+'</td>'+
		    '<td style="text-align:center;">'+
		    '<a href="javascript:void(0);" onclick="editAutomation('+wList[i]['id']+')"><button type="button" style="margin-left: 2px;" class="btn btn-default ">'+
		    '<span class="glyphicon glyphicon-pencil" aria-hidden="true"></span></button></a>'+
		    '<a href="javascript:void(0);" onclick="removeAutomation(\''+wList[i]['id']+'\',\''+wList[i]['action_title']+'\',true)"><button type="button" style="margin-left: 2px;" class="btn btn-default ">'+
		    '<span class="glyphicon glyphicon-remove" aria-hidden="true"></span></button></a></td>';
	}
	table+='</tbody></table></center>';
	$('#table_search_automation').html(table);
	$('#table_automation').DataTable({
	"language" : {"sEmptyTable": "Nenhum registro encontrado",
	    "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
	    "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
	    "sInfoFiltered": "(Filtrados de _MAX_ registros)",
	    "sInfoPostFix": "",
	    "sInfoThousands": ".",
	    "sLengthMenu": "_MENU_ resultados por página",
	    "sLoadingRecords": "Carregando...",
	    "sProcessing": "Processando...",
	    "sZeroRecords": "Nenhum registro encontrado",
	    "sSearch": "Pesquisar",
	    "oPaginate": {
	        "sNext": "Próximo",
	        "sPrevious": "Anterior",
	        "sFirst": "Primeiro",
	        "sLast": "Último"
	    },
	    "oAria": {
	        "sSortAscending": ": Ordenar colunas de forma ascendente",
	        "sSortDescending": ": Ordenar colunas de forma descendente"
	    }
	}
	});
}

/*!
 * Prepare interface for edition
 * @param wId The Id that shall be removed
 */
function editAutomation(wId){
	manage_overlay('show','processing');
    $.ajax({
        url: '/legislator/backcall/edit_automation/',
        type: "POST",
        data: {'id' : wId, 'session_id' : $('#session_id').val()},
        enctype: 'multipart/form-data',
        success:function(wData){
        	if (wData==''){
	        	manage_overlay('hide','');
	        	exporeError('Erro ao tentar editar a a&ccedil;&atilde;o!','custom');;
	        	return true;
        	}
        	if ((wData['info']!=undefined) && (wData['info']!=null)){ 
        		exporeError(wData['info'],'custom');
        		return true;
        	}
        	$('#id').val(wData['id']);
        	// avoid date invert problem
        	if (wData['action_date']!='NULL')
        		wData['action_date'] = dateOnly(wData['action_date']);
        	$('#btn_cancel_edition').show();
        	$('#btn_add_action').val(htmlJs('Atualizar A&ccedil;&atilde;o'));
        	fillForm(wData);
        	// because the instance ready will never be called
    		CKEDITOR.instances.action_msg.insertHtml(wData['action_msg'].replace(/\'/g,"'"));
        	manage_overlay('hide','processing');
        	return true;
	    },
	    error: function (error) {
	    	exporeError(error,'custom');
	    	return true;
	    }
    });
}

/*!
 * Clean the fields if edition is not needed
 */
function cancelEdition(){
	$('#btn_cancel_edition').hide();
	$('#btn_add_action').val(htmlJs('Adicionar A&ccedil;&atilde;o'));
	$('#id').val('');
	$('#action_title').val('');
	$('#action_date').val('');
	$('#action_filter').val('');
	$('#action_field').val('');
	$('#action_operation').val('');
	$('#action_value').val('');
	CKEDITOR.instances.action_msg.setData('');
}

/*!
 * Show the warning if required and if not, request the item deletion
 * @param wId The Id that shall be removed
 * @param wTitle The title that shall be viewed at the deletion confirmation
 * @param wWarning If it shall request the confirmation or not
 */
function removeAutomation(wId,wTitle,wWarning){
	if (wWarning==true){
		$('#title_for_removal').text(wTitle);
		manage_overlay('show','confirm_deletion_window');
		$('#remove_action').click(function(){removeAutomation(wId,wTitle,false);});
		return false;
	}
	manage_overlay('show','processing');
    $.ajax({
        url: '/legislator/backcall/remove_automation/',
        type: "POST",
        data: {'id' : wId, 'session_id' : $('#session_id').val()},
        enctype: 'multipart/form-data',
        success:function(wData){
        	if (wData==''){
	        	manage_overlay('hide','');
	        	location.reload();
        	}
        	else
        		exporeError(wData,'return_data');
            
	    },
	    error: function (error) {
	    	exporeError(error,'custom');
	    }
    });
}

//-----------------------------   CALENDAR STUFF -------------------------------

/*!
 * Fill date with calendar date
 * @param wDate The clicked date
 */
function getDateCalendar(wDate){
	$('#action_date').val(fixDateExibition(wDate[2])+'/'+fixDateExibition(wDate[1])+'/'+wDate[0]);
}

/*!
 * Call the decision window from the custom date
 */
function removeNewDate(wDate){
	if ((wDate.length==0) || (wDate==''))    return exporeError('Nenhuma data selecionada para remoção!','return_data');
	$('#my_remove_date').val(wDate[2]+'/'+wDate[1]+'/'+wDate[0]);
	manage_overlay('show','remove_custom_window');
    $('#remove_custom_window_loader').hide();
    $('#remove_custom_window_table').show();
}

/*!
 * remove the customized date to table
 */
function removeNewCustomDate(){
    $('#remove_custom_window_table').hide();
    $('#remove_custom_window_loader').show();
    $.ajax({
        url: '/legislator/backcall/remove_new_custom_date/',
        type: "POST",
        data: {'date' : $('#my_remove_date').val(), 'session_id' : $('#session_id').val()},
        enctype: 'multipart/form-data',
        success:function(wData){
        	if (wData==''){
	        	manage_overlay('hide','');
	        	exporeError('success A data foi removida com sucesso!','return_data');
	        	loadMyDates('getDateCalendar',(new Date()).getFullYear(),'calendar','/legislator/backcall/load_mydates/');
        	}
        	else{
                $('#remove_custom_window_span').html(wData);
                $("#remove_custom_window_error").show();
                $('#remove_custom_window_loader').hide();
                $('#remove_custom_window_table').show();
        	}
        },
        error: function (error) {
            $('#remove_custom_window_span').html(error);
            $("#remove_custom_window_error").show();
            $('#remove_custom_window_loader').hide();
            $('#remove_custom_window_table').show();
        }
    });
}

/*!
 * Change the calendar status
 */
function changeStatusMap(){
	if ($('#calendar').is(':visible')) $('#calendar').hide();
	else                               $('#calendar').show();
}

/*!
 * Called every time the user wants to put a date as its 
 */
function addNewDate(wDate){
	manage_overlay('show','add_custom_window');
	$('.selectpicker').selectpicker('render');
    var item= $('.bootstrap-select');
    $('.bootstrap-select').css('margin','0px 0px 0px 0px ');
    item.css('border','0px solid black');
    item.find('div').css('margin','0px 0px 0px 0px')
    item.find('div').css('border','1px solid gray');
    item.find('div').find('div').css('border','0px solid gray');
    $('#add_custom_window_table').hide();
    $('#add_custom_window_loader').show();
    if (commem_dates.length==0)
    	loadCommemorationDateFromServer(wDate);
    else
    	fillAddCustomWindow(commem_dates,wDate);
}

/*!
 * Load all the commemoration date for adding a customized date
 * @param wDate The date selected.
 */
function loadCommemorationDateFromServer(wDate){
    $.ajax({
        url: '/legislator/backcall/load_commemorations/',
        type: "POST",
        data: {'year' : (new Date()).getFullYear()},
        enctype: 'multipart/form-data',
        success:function(wData){
            // ups, error returned
            if ((wData['info']!=undefined)&& (wData['info']!=null)){
            	exporeError(wData,'return_data');
            	fillAddCustomWindow([],wDate)
            }
            else
            	commem_dates = wData;
            	fillAddCustomWindow(wData,wDate)
        },
        error: function (error) {
        	exporeError('error '+error,'return_data');
            $('#add_custom_window_loader').hide();
            $('#add_custom_window_table').show();
        }
    });
}

/*!
 * Get the selected item and put that on the fields
 * @param wItem The option selected
 */
function copyDateMeaningToForm(wItem){
	var text = wItem.options[wItem.selectedIndex].text;
	var state = 0
	var index = 0;
	// remove the part before the reason
	while ((state<2) && (text.length>0)){
		if (state==0)
			if (text[0]!=' ') text=text.slice(1,text.length);
			else    		   state=1;
		if (state==1) 
			if (text[0]==' ') text=text.slice(1,text.length);
			else              state=2;
	}
	$('#my_new_date').val(wItem.options[wItem.selectedIndex].value);
	$('#my_new_meaning_date').val(text);
}

/*!
 * Add the date into the item and search into the select
 * @param The date to be set
 */
function fillAddCustomWindow(wData,wDate){
	if ((wData.length!=0)){
		$('#my_new_date_selector').find('option').remove().end();
		var select = document.getElementById("my_new_date_selector");
		select.options[0] = new Option(' ','');
		for (var i=0;i<wData.length;i++)
			select.options[i+1] = new Option(fixDateExibition(wData[i]['cal_day'])+'/'+month_of_year[wData[i]['cal_month']]+
			    ' '+wData[i]['cal_occasion'],fixDateExibition(wData[i]['cal_day'])+'/'+fixDateExibition(wData[i]['cal_month']+1)+'/'+wData[i]['cal_year']);
		$('.selectpicker').selectpicker('refresh');
		$('.selectpicker').selectpicker('render');
	    var item= $('.bootstrap-select');
	    $('.bootstrap-select').css('margin','0px 0px 0px 0px ');
	    item.css('border','0px solid black');
	    item.find('div').css('margin','0px 0px 0px 0px')
	    item.find('div').css('border','1px solid gray');
	    item.find('div').find('div').css('border','0px solid gray');
	    $('#add_custom_window_table').hide();
	    $('#add_custom_window_loader').show();
	}
    $('#add_custom_window_loader').hide();
    $('#add_custom_window_table').show();
    // set the clicked date into the date field
    if (wDate!='')
    	$('#my_new_date').val(fixDateExibition(wDate[2])+'/'+fixDateExibition(wDate[1])+'/'+wDate[0]);
}

/*!
 * Add the new customized date to table
 */
function addNewCustomDate(){
	var date = $('#my_new_date').val();
	var text = $('#my_new_meaning_date').val();
    if (text==''){
        $('#add_custom_window_span').html(htmlJs('<b>O campo "Significado" n&atilde;o pode ser vazio!</b>'));
        $("#add_custom_window_error").show();
        return ;
    }
    if (text.length>300){
        $('#add_custom_window_span').html(htmlJs('<b>O campo "Significado" n&atilde;o ter mais de 300 letras!</b>'));
        $("#add_custom_window_error").show();
        return ;
    }
    if (!validateNoQuotation(text)){
        $('#add_custom_window_span').html(htmlJs('<b>O campo "Significado" n&atilde;o pode conter aspas!</b>'));
        $("#add_custom_window_error").show();
        return ;
    }
    if (date==''){
        $('#add_custom_window_span').html(htmlJs('<b>O campo "Data" n&atilde;o pode ser vazio!</b>'));
        $("#add_custom_window_error").show();
        return ;
    }
    if (!checkDate(date.split('/'))){
        $('#add_custom_window_span').html(htmlJs('<b>O campo "Data" n&atilde;o &eacute; v&aacute;lido!</b>'));
        $("#add_custom_window_error").show();
        return ;
    }
	
    $('#add_custom_window_table').hide();
    $('#add_custom_window_loader').show();
    $.ajax({
        url: '/legislator/backcall/add_new_custom_date/',
        type: "POST",
        data: {'date' : date, 'meaning': text, 'session_id' : $('#session_id').val()},
        enctype: 'multipart/form-data',
        success:function(wData){
        	if (wData==''){
	        	manage_overlay('hide','');
	        	exporeError('success A nova data foi adicionada com sucesso!','return_data');
	        	loadMyDates('getDateCalendar',(new Date()).getFullYear(),'calendar','/legislator/backcall/load_mydates/');
        	}
        	else{
                $('#add_custom_window_span').html(wData);
                $("#add_custom_window_error").show();
                $('#add_custom_window_loader').hide();
                $('#add_custom_window_table').show();
        	}
        },
        error: function (error) {
            $('#add_custom_window_span').html(error);
            $("#add_custom_window_error").show();
            $('#add_custom_window_loader').hide();
            $('#add_custom_window_table').show();
        }
    });
}

//--------------------------------------- GENERIC STUFF ------------------------------

/*!
 * Show the tags available for each type of event
 */
function showTags(){
	var html = '';
	if (field_in_use.length==0)
		html='<center><b> Nenhum tipo de evento selecionado</b></center>';
	else{
		for (var i=0;i<field_in_use[1].length;i++)
			html += '<b>'+field_in_use[1][i]+'</b><br>';
	}
	$('#tags_items').html(html);
	$('#tags').show();
}

/*!
 * Apply the need for overlay over the interface
 * @param wStatus The general status
 * @param wId The item that shall be executed visible
 */
function manage_overlay(wStatus,wId){
    if (wId!='')
        for (var i=0;i<overlay_repo_city.length;i++)
            if (overlay_repo_city[i]==wId){
                if (wStatus=='show')$('#'+wId).show();
                else $('#'+wId).hide();
            }
            else  $('#'+overlay_repo_city[i]).hide();

    if (wStatus=='show') $('#overlay').css("visibility", "visible");
    else                 $('#overlay').css("visibility", "hidden");
    window.scrollTo(0,0);
}

