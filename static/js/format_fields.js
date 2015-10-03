

function formatCPF(wCpf){
	if ((wCpf != '') && (wCpf != null))
		return 	wCpf.substring(0,3)+"."+wCpf.substring(3,6)+"."+wCpf.substring(6,9)+"-"+wCpf.substring(9,11);
	return '';
}

function formatRG(wRg){
	if ((wRg != '') && (wRg!=null) && (wRg.length>=8)) {
	    return wRg.substring(0,2)+"."+wRg.substring(2,5)+"."+wRg.substring(5,8)+"-"+wRg.substring(8);
	}
	if (wRg==null) return '';
	return wRg;
}

function formatPhone(wPhone){
    if (wPhone==null) return '';
    wPhone = wPhone.replace('(','').replace(')','');
    if ((wPhone != '') && (wPhone != null)){
        if ((wPhone != '') && (wPhone != null) && (wPhone.length>=11)){
            return "("+wPhone.substring(0,2)+") "+wPhone.substring(2,7)+"-"+wPhone.substring(7,11);
        }
    	if  (wPhone.length>=10){
    		return "("+wPhone.substring(0,2)+") "+wPhone.substring(2,6)+"-"+wPhone.substring(6,10);
		}
    	if  (wPhone.length>=8){
    		return wPhone.substring(0,4)+"-"+wPhone.substring(4,8);
		}
    }
	
}

function formatCelPhone(wPhone){
	if (wPhone==null) return '';
    if ((wPhone != '') && (wPhone != null) && (wPhone.length>=11)){
        return "("+wPhone.substring(0,2)+") "+wPhone.substring(2,7)+"-"+wPhone.substring(7,11);
    }
	if  (wPhone.length>=10){
		return "("+wPhone.substring(0,2)+") "+wPhone.substring(2,6)+"-"+wPhone.substring(6,10);
	}
	if  (wPhone.length>=8){
		return wPhone.substring(0,4)+"-"+wPhone.substring(4,8);
	}
	// return wPhone;
}

function formatCEP(wCep){
    if ((wCep != '') && (wCep != null) && (wCep.length>=8)){
        return wCep.substring(0,2)+"."+wCep.substring(2,5)+"-"+wCep.substring(5,8);
    }
	if (wCep==null) return '';
	return wCep;
}

function dateOnly(wDate){
	if ((wDate != null) && (wDate!='')){
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

/*!
 * Get date from database and get it as JAVASCRIPT Date type
 * @param wDate full 
 * @return The date as JAVASCRIPT object
 */
function parseDate(wDate) {
	if ((wDate == null) || (wDate=='')) return new Date();
	var full_date = wDate.split(" ");
	if (full_date.length!=2) return null;
	if (wDate.indexOf('-')!=-1)  var date = full_date[0].split("-");
	else                         var date = full_date[0].split("/");
	
	var hours = full_date[1].split(':');
	if (hours.length!=3) return null;
	
	if (date[0].length==4)
		return new Date(date[0],date[1]-1,date[2],hours[0],hours[1],hours[2]);
	else
		return new Date(date[0],date[1]-1,date[2],hours[0],hours[1],hours[2]);
}

/*!
 * Run the difference between two JAVASCRIPT date
 * @param wFirst The first date
 * @param wSecond The second date
 * @return The number of days in between the two dates
 */
function dayDiff(wFirst, wSecond) {
    return (wSecond-wFirst)/(1000*60*60*24);
}

/*!
 * Return the item background and font color based on 
 * @param wCreated The created date
 * @param wStatus The requisition status
 * @param wNormal The number of days to be normal
 * @param wMax the maximum number of days to solve
 * @return A vector with background, font color and text
 */
function getReqColorByStatus(wCreated, wStatus, wNormal, wMax){
	var created = parseDate(wCreated);
	if (created==null) return ['#fff','#555', STATUS_REQ[wStatus],-1];
	var diff = dayDiff(created,new Date());
	if (wStatus=='0') return ['#fff','#555', STATUS_REQ[wStatus],diff];
	if (wStatus=='2') return ['#2B65EC','#fff', STATUS_REQ[wStatus],diff];
	if (diff<wNormal) return ['#008b45','#fff', STATUS_REQ[wStatus],diff];
	if (diff<wMax) return ['#ffd700','#000', STATUS_REQ[wStatus],diff];
	
	return ['#cd0000','#fff', STATUS_REQ[wStatus],diff];
}

function dateAndTime(wDate){
	if ((wDate != null) && (wDate!='')){
		var date = wDate.split(" ")[0].split("-");
		var time = wDate.split(" ")[1].split(':');
		if (date.length!=3) return '';
		return date[2]+"/"+date[1]+"/"+date[0]+" "+time[0]+":"+time[1]+":"+time[2];
	}
	return '';
}

function formatStatus(wField){
	if ((wField == '1') || (wField == 1)) return 'Enviando';
	if ((wField == '0') || (wField == 0)) return 'Aguardando Envio';
	if ((wField == '2') || (wField == -1)) return 'Terminado';
	if ((wField == '3') || (wField == -1)) return 'Cancelado';
	else return '';
}

function formatStatusRequisition(wField){
	if ((wField == '1') || (wField == 1)) return 'Enviando';
	if ((wField == '0') || (wField == 0)) return 'Aguardando Envio';
	if ((wField == '2') || (wField == -1)) return 'Terminado';
	if ((wField == '3') || (wField == -1)) return 'Cancelado';
	else return '';
}

function checkNull(wField){
	if ((wField == null) || (wField == 'null')) return '0';
	else return wField;
}


/*!
 * Show the file size as text
 * @param wSize the enter size
 * @return The size converted, the measured value and the combining of those
 */

function formatFileSize(wSize){
    if (wSize<1024)
        return [wSize,"Bytes", wSize+" Bytes"];
    if (wSize<102400){
        wSize = wSize/1024;
        return [wSize,"KB", wSize+" KB"];
    }
    else{
        wSize = (wSize/1024)/1000;
        return [wSize,"MB", wSize+" MB"];
    }
}
 