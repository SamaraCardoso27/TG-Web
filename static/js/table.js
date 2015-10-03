
var button_disable = 'rgb(231, 231, 231)'; //when button is disable
var button_enable = 'rgb(0, 0, 0)'; //when button is enable

var old_style = 'font-size: 15px; background-color: black; color: white;';

var qnt_pag_view = 7; // hold the number of jump that can be done into the page


function changeStatus(wPage,wLastPage, wParent, wHide){
	wParent = '#'+wParent
	var operate;

	if (wPage==0) operate = button_disable;
	else          operate = button_enable;

	$(wParent+"_page_first").css("background-color",operate);
	$(wParent+"_page_prev").css("background-color",operate);

	if (wPage==wLastPage) operate = button_disable;
	else                 operate = button_enable;

	$(wParent+"_page_last").css("background-color",operate);
	$(wParent+"_page_next").css("background-color",operate);

	if (wHide) operate = button_disable;
	else       operate = button_enable;
	
	if (wHide){
		item = 
		$(wParent+'_page_'+wPage).hide();
		$(wParent+'_page_'+wPage).css('background','black');
		if (wPage>0) $(wParent+'_page_'+(wPage-1)).hide();
		if (wPage<wLastPage) $(wParent+'_page_'+(wPage+1)).hide();
	}
	else{
		$(wParent+'_page_'+wPage).show();
		$(wParent+'_page_'+wPage).css('background','rgb(114, 114, 114)');
		if (wPage>0) $(wParent+'_page_'+(wPage-1)).show();
		if (wPage<wLastPage) $(wParent+'_page_'+(wPage+1)).show();
	}
}


function jumpToPage(wItem,wParent){
	var cur_page = Number($('#'+wParent).attr('data-page_number'));
	var last_page = Number($('#'+wParent+'_page_last').attr('data-page_number'));
	var new_page = $('#'+wParent+'_page_'+wItem).attr('data-page_number');
	if (wItem=='first') new_page='0';
	if (wItem=='prev') new_page=(cur_page-1);
	if (wItem=='last') new_page=last_page.toString();
	if (wItem=='next') new_page=(cur_page+1).toString();
	$('#'+wParent+'_table_page_'+cur_page).hide();
	changeStatus(cur_page,last_page,wParent,true);
	$('#'+wParent).attr('data-page_number',new_page);
	changeStatus(Number(new_page),last_page,wParent,false);
	$('#'+wParent+'_table_page_'+new_page).show();
}


function fillTableData(wClassTable, wDivTable, wData, wTitle, wField, wPerPage){
	if (wPerPage==undefined) wPerPage= 15;
	var quant_table = Math.round(Math.ceil(wData.length.toFixed(2)/wPerPage));
    var pag = '<center><nav><ul class="pagination">\
    	<li><a href="#" id="'+wDivTable+'_page_first" onclick="jumpToPage(\'first\',\''+wDivTable+'\');" data-page_number="0" style = "'+old_style+'"><i class="glyphicon glyphicon-fast-backward "></i></a></li>\
    	<li><a href="#" id="'+wDivTable+'_page_prev"  onclick="jumpToPage(\'prev\',\''+wDivTable+'\');" data-page_number=""  style = "'+old_style+'"> <i class="glyphicon glyphicon-step-backward"></i> </a></li>';
    var page = 0;
    var page_s = page.toString();
    var ret = "";
    var count = wPerPage;
    var i_pg, i_head;
    for (i_pg=0;i_pg<wData.length;i_pg++){
    	// add head to page
    	if (count==wPerPage){
    		if (i_pg!=0)  ret+='</table>';
            ret+= '<table id="'+wDivTable+'_table_page_'+page_s+'" class="'+wClassTable+'" style="display:none;border-collapse: collapse;"><tr>';
            // add the head to the table
            for (i_head=0;i_head<wTitle.length;i_head++)
            	ret+='<th '+wTitle[i_head][0]+'>'+wTitle[i_head][1]+'</th>';
            ret+='</tr><tr>';
            pag+='<li><a href="#" onclick="jumpToPage(\''+page_s+'\',\''+wDivTable+'\');"  id="'+wDivTable+'_page_'+page_s+'" data-page_number="'+page+'" style = "'+old_style+' display:none;"> '+(page+1)+' </a></li>';
            count = 0;
            page++;
            page_s = page.toString();
    	}
    	// add line to table
    	for (i_head=0;i_head<wField.length;i_head++){
    		if (wField[i_head][1]==undefined)
    			ret+='<td '+wField[i_head][2]+'>'+wData[i_pg][wField[i_head][0]]+'</td>';
    		else
    			ret+='<td '+wField[i_head][2]+'>'+wField[i_head][1](wData[i_pg],i_pg)+'</td>';
    	}
    	ret+='</tr>';
    	count++;
    }
    var items='';
    for (i_head=0;i_head<wField.length;i_head++)
		if (wField[i_head][1]==undefined)
			items+='<td '+wField[i_head][2]+'>'+wData[0][wField[i_head][0]]+'</td>';
		else
			items+='<td '+wField[i_head][2]+'>'+wField[i_head][1](wData[0],0)+'</td>';
    // fill the rest of the table
    for (;count<wPerPage;count++)
    	ret+='<tr style="visibility:hidden;">'+items+'</tr>';
    
	pag += '\
		<li><a href="#" id="'+wDivTable+'_page_next"  onclick="jumpToPage(\'next\',\''+wDivTable+'\');" data-page_number=""               style = "'+old_style+'"> <i class="glyphicon glyphicon-step-forward"></i> </a></li>\
    	<li><a href="#" id="'+wDivTable+'_page_last" onclick="jumpToPage(\'last\',\''+wDivTable+'\');" data-page_number="'+(quant_table-1)+'" style = "'+old_style+'"><i class="glyphicon glyphicon-fast-forward "></i></a></li>\
    	</ul></nav></center>';
	
	ret+='</table>';
	$('#'+wDivTable).attr('data-page_number','0');
	$('#'+wDivTable).html(ret+'<br>'+pag);
	jumpToPage('0',wDivTable);
}