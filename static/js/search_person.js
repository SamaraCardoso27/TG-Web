

var overlay_user = ['processing','confirm_delete_div'];

var person_id = 0;

function fill_search(wData, wOption, wValue){
	if ((wData!=null) && (wData.length>0)){
		fillTableData(wData);
	}
}


function formatDateTable(wData,wId){
	return dateAndTime(wData['last_update']);
}


function blockValue(wSelect){
	var value = $("#value").val("");
	if (wSelect.value == 0){
		//value.readOnly = true;
		
		value.prop('disabled', true);
		value.val("");

	}		
	else{
		value.readOnly = false;
		value.focus();
		//value.prop('disabled', false);
	}
}


function insertButtonTable(wData){
	return '<button type="button" class="btn btn-info" aria-label="Left Align"\
    		onclick="editPerson('+wData['id']+');"><span class="glyphicon glyphicon-pencil" aria-hidden="true">\
    		</span></button><button type="button" class="btn btn-danger" aria-label="Left Align"\
    		onclick="confirmDelete('+wData["id"]+',\''+wData["full_name"]+'\');"><span class="glyphicon glyphicon-remove" aria-hidden="true">\
    		</span></button>';
}

function confirmDelete(wId, wName){
	person_id = wId;
	document.getElementById('message').innerHTML = '<h4>Tem certeza que deseja excluir o Cliente <br>'+wName+'?</h4>';
	manage_overlay('show','confirm_delete_div');
	deletePerson(person_id);
}

function deletePerson(){
	manage_overlay('hide','confirm_delete_div');
	window.location.href = window.location.href.replace('#','')+'?id='+person_id+'&action=delete';
	manage_overlay('show','processing');
}

function editPerson(wId){
	manage_overlay('show','processing');
	window.location.href = window.location.origin+'/TG/default/create_person'+'/update?id='+wId;
}


function search_person(){
	manage_overlay('show','processing');
	if (!validateBasicSearch($('#value').val())){
		manage_overlay('hide','processing');
		return exporeError(['de cliente','\'," e %'],'search_field');
	}
	document.getElementById('submit_form').submit();
}


function manage_overlay(wStatus,wId){
    if (wId!='')
        for (var i=0;i<overlay_user.length;i++)
            if (overlay_user[i]==wId){
                if (wStatus=='show')$('#'+wId).show();
                else $('#'+wId).hide();
            }
            else  $('#'+overlay_user[i]).hide();

    if (wStatus=='show') $('#overlay').css("visibility", "visible");
    else                 $('#overlay').css("visibility", "hidden");
}


function fillTableData(wData){
	var table = '<table id="example" class="table table-striped table-bordered" cellspacing="0" width="100%">'+
				'<thead>'+
	            	'<tr>'+
	                	'<th>Nome</th>'+
	                	'<th>CPF</th>'+
	                	'<th>RG</th>'+
	                	'<th>Última Alteração</th>'+
	                	'<th>Ações</th>'+
	            	'</tr>'+
        		'</thead>';
	
	for (var i = 0; i < wData.length; i++) {
		table = table + '<tr>'+
                '<td>'+wData[i]["full_name"]+'</td>'+
                '<td>'+wData[i]["cpf"]+'</td>'+
                '<td>'+wData[i]["rg"]+'</td>'+
                '<td>'+wData[i]["last_update"]+'</td>'+
                '<td><button type="button" class="btn btn-info" aria-label="Left Align"\
    		     onclick="editPerson('+wData[i]['id']+');"><span class="glyphicon glyphicon-pencil" aria-hidden="true">\
    		     </span></button><button type="button" class="btn btn-danger" aria-label="Left Align"\
    		     onclick="confirmDelete('+wData[i]["id"]+',\''+wData[i]["full_name"]+'\');"><span class="glyphicon glyphicon-remove" aria-hidden="true">\
    		    </span></button></td>'+
                '</tr>';
	}
	table = table  + '</table>'
	$("#table_div").html(table);
}