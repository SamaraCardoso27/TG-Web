

var overlay_user = ['processing','confirm_delete_div'];

var person_id = 0;

function fill_search(wData, wOption, wValue){
	manage_overlay('show','processing');
	
	if ((wData!=null) && (wData.length>0))
		fillTableData('table','table_div',wData,[['style="text-align:center;min-width:250px;"','Nome'],['style="text-align:center;min-width:120px;"','CPF'],
                       ['style="text-align:center;min-width:80px%;"','RG'],['style="text-align:center;min-width:160px;"',htmlJs('Última Alteração')],
		               ['style="text-align:center;min-width:100px;"',htmlJs('A&ccedil;&otilde;es')]],
		               [['full_name',,''],['cpf',,''],['rg',,''],
		                ['last_update',formatDateTable,'style="text-align:center;"'],['',insertButtonTable,'style="text-align:center;"']],10);

	if (wOption!='None' && wOption!=''){
		$("#option").val(wOption);
		blockValue(document.getElementById('option'));
		$('#value').val(wValue);
		// nothing as found
		if (!((wData!=null) && (wData.length>0))){
			if (wValue!='None' && wValue!=''){
				$("#table_div").html('<center style="margin-top:150px;font-size:22px;">'+htmlJs('Nenhum cidad&atilde;o foi encontrado com o filtro ')+'<span style="color:red">'+
						$("#option option:selected").text()+'</span> <b>=</b> <span style="color:red">'+wValue+'</span>');
				$('#value').val(htmlJs(wValue));
			}
			else
				$("#table_div").html('<center style="margin-top:150px;font-size:22px;">'+htmlJs('Nenhum cidad&atilde;o foi encontrado com o filtro ')+'<span style="color:red">'+
						$("#option option:selected").text()+'</span>');
		}
	}
	manage_overlay('hide','processing');
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
	return '<button type="button" class="btn btn-default" aria-label="Left Align"\
    		onclick="editPerson('+wData['id']+');"><span class="glyphicon glyphicon-pencil" aria-hidden="true">\
    		</span></button><button type="button" class="btn btn-default" aria-label="Left Align"\
    		onclick="confirmDelete('+wData["id"]+',\''+wData["full_name"]+'\');"><span class="glyphicon glyphicon-remove" aria-hidden="true">\
    		</span></button>';
}

function confirmDelete(wId, wName){
	person_id = wId;
	document.getElementById('message').innerHTML = '<h4>Tem certeza que deseja excluir o Cliente <br>'+wName+'?</h4>';
	manage_overlay('show','confirm_delete_div');
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