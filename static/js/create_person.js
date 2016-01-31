var overlay_repo_category = ['processing']
var categories = [];
var cities = {};

var ws = new WebSocket('ws://127.0.0.1:8888/realtime/mygroup');

$( document ).ready(function() {
	var ws = new WebSocket('ws://127.0.0.1:8888/realtime/mygroup');
	ws.onopen = function(){
          $("#success_span").html("Conexão Aberta!");
          $("#success_div").show();
   };
   ws.onclose = function(){
<<<<<<< HEAD
   	  //location.href =  location.origin+'/TG/default/downloads';
      $("#error_span").html("Conexão fechada!");
=======
      $("#error_span").html("Não foi possível estabelecer uma conexão!");
>>>>>>> c9d12f6ffaaf671181260c9e7192f5fafd865297
      $("#error_div").show();
      $('#add_person').attr('disabled', 'disabled');
      $('#amostra1').attr('disabled', 'disabled');
      $('#amostra2').attr('disabled', 'disabled');

   };
});



function websocket(wButton){
    ws.onmessage = function(evt){
        x = document.createElement("p");
        var retorno = evt.data;
        if (retorno == '@1'){
        	//location.href =  location.origin+'/TG/default/downloads';
        	$('#error_div').show();
        	$('#error_span').html('Conecte o Leitor Biometrico!');

        }
        else if (retorno == '@2'){
        	$('#error_div').show();
        	$('#error_span').html('Cannot get image size from device!');
        }
        else if (retorno == '@3'){
        	$('#error_div').show();
        	$('#error_span').html('Coloque o dedo no leitor!');
        }
        else if (retorno == '@4'){
        	$('#error_div').show();
        	$('#error_span').html('Ocorreu um erro! Tente Novamnte!');
        }
        else{
        	if(wButton == 1){
          		$('#key1').css("background-color", "#008000" );
          		$('#keypoints1').val(retorno);
				console.log(retorno);
          	}else{
          		$('#key2').css("background-color", "#008000" );
          		$('#keypoints2').val(retorno);
				console.log(retorno);
          	}
        }
    }
}

function get_fingerprint(wValue){
	var userInput = '@0'
	if(wValue == '1'){
		//$('#key1').val(userInput);
		//ws.send(userInput);
		websocket(1);
	}
	else{
		//$('#key2').val(userInput);
		
		websocket(2);
	}
	ws.send(userInput);	
	
}


function submit_person(){
	var keypoints1 = $("#keypoints1").val();
	var keypoints2 = $("#keypoints2").val();
	if(keypoints1 == ''){
		$('#error_div').show();
        $('#error_span').html('Colete a amostra 1;');
	}
	else if(keypoints2 == ''){
		$('#error_div').show();
        $('#error_span').html('Colete a amostra 2;');
    }else{
		document.getElementById('submit_form').submit();	
	}
}

function checkPerson(){
	var ws = new WebSocket('ws://127.0.0.1:8888/realtime/mygroup');
	ws.onmessage = function(evt){
		x = document.createElement("p");
        var retorno = evt.data;
        if (retorno == '@1'){
        	$("#error_div").html('Conecte o Leitor Biometrico!');
        	return false;
        }
        else{
          console.log(retorno);
          var cbox = document.getElementById("retorno");
          //cbox.innerHTML = keypoints;
          $('#keypoints1').css( "background-color", "#008000" );
          //$('#key').val(retorno);
          return true;
        }
    }
    return true;
	
}


function init_insert_person(wCities,wData){
	$("#cpf").inputmask("999.999.999-99");
	$('#birth_date').inputmask("99/99/9999");
	$('#zipcode').inputmask('99.999-999');
	$('#street_number').inputmask('99999');
	var selectCities = $('#city_person');
	for(y=0;y<wCities.length;y++){
		selectCities.append("<option value='"+wCities[y]['id']+"'>"+ wCities[y]['name'] +"</option>");
		cities[wCities[y]['id']] = wCities[y]['name'];
	}
	for(var item in MARITAL_STATUS){
      $('#marital_status').append("<option value='"+item+"'>"+MARITAL_STATUS[item]+"</option>");
    }
	if(Object.keys(wData).length>0) fillPerson(wData);
 }

function fillPerson(wData){
	$('#full_name').val(wData[0]['full_name']);
	$('#birth_date').val(dateAndTime(wData[0]['birth_date']));
	$('#cpf').val(wData[0]['cpf']);
	$('#rg').val(wData[0]['rg']);
	if($('#sex').val(wData[0]['sex']) == 0)
		$('#sex').val(0);
	else
		$('#sex').val(1);
	$('#last_update').val(dateOnly(wData[0]['last_update']));
	$('#keypoints1').val(wData[0]['keypoints1']);
	$('#keypoints2').val(wData[0]['keypoints2']);
  	$('#marital_status').val(wData[0]['marital_status']);
	$('#street').val(wData[0]['street']);
	$('#neigh').val(wData[0]['neigh']);
	$('#street_number').val(wData[0]['street_number']);
	$('#comp_person').val(wData[0]['comp_person']);
	$('#zipcode').val(wData[0]['zipcode']);
	$('#email').val(wData[0]['email']);
	$('#cellphone').val(wData[0]['cellphone']);
	$('#city_person').val(wData[0]['city_person']);
	$('#id').val(wData[0]['id']);
}

function dateOnly(wDate){
  if ((wDate != null) && (wDate!='')){
    wDate = wDate.split('T')[0];
    if (wDate.indexOf('-')!=-1)
      var date = wDate.split(" ")[0].split("-");
    else
      var date = wDate.split(" ")[0].split("/");
    if (date.length!=3) return '';
    if (date[0].length==4)
      return date[2]+"/"+date[1]+"/"+date[0];
    else
      return date[0]+"/"+date[1]+"/"+date[2];
  }
  return '';
}


function dateAndTime(wDate){
	if ((wDate != null) && (wDate!='')){
		var date = wDate.split(" ")[0].split("-");
		if (date.length!=3) return '';
		return date[2]+"/"+date[1]+"/"+date[0];
	}
	return '';
}


function manage_overlay(wStatus,wId){
	if (wId!='')
		for (var i=0;i<overlay_repo_category.length;i++)
			if (overlay_repo_category[i]==wId) $('#'+wId).show();
			else                               $('#'+wId).hide();

	if (wStatus=='show') $('#overlay').css("visibility", "visible");
	else                 $('#overlay').css("visibility", "hidden");
}
