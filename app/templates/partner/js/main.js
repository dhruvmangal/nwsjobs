$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();   
});

function bigButton()
{
	document.getElementById('employ').style.fontSize= "22px";
}
function smallButton()
{
	document.getElementById('employ').style.fontSize="18px";
}
function bigButton1()
{
	document.getElementById('employ1').style.fontSize= "22px";
}
function smallButton1()
{
	document.getElementById('employ1').style.fontSize="18px";
}
function close_popup()
{
	document.getElementById("popup").style.display= "none";
}
function icon_hover(x)
{
	x.style.color="#fc1e1e";
	x.style.backgroundColor= "white";
}
function icon_hover_remove(x)
{
	x.style.color="white";
	x.style.backgroundColor= "#fc1e1e";
}
function category_large(x)
{
	x.style.width= "110%";
	x.style.height= "auto";
}
reverse_color()
{
	document.getElementById("gender").style.backgroundColor="red";
}