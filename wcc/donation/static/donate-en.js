// Scripts for the online donation page - English
function getSelectedButton(buttonGroup) {
	for (var i=0; i< buttonGroup.length; i++) {
		if (buttonGroup[i].checked)
			{ return i }
	}
	return -1
}
function resetAmount() {
	if (document.donation.normalAmount.value != "") {
		if (getSelectedButton(document.donation.amountslist) != -1 ) {
			document.donation.amountslist[getSelectedButton(document.donation.amountslist)].checked = false
		}
	}
}
function resetOtherAmount() {
	document.donation.normalAmount.value = ""
}
function checkNumeric(e)  {
	var charCode = (navigator.appName == "Netscape") ? e.which : e.keyCode
	status = charCode
	if (charCode != 46 && (charCode < 48 || charCode > 57)) {
		return false
	}
}
function validate(){

var msg;
var msgflag;
var pswdflag;
var i;

msgflag = "false";
var pswdflag = "false";

 msg="The following fields require values:\n";


if(getSelectedButton(document.donation.MC_frequency)  == -1) {
	msg+="\nIs your gift monthly or unique?";
    	msgflag="true";
	}
 if(document.donation.MC_firstname.value == ""){
	msg+="\nFirst Name";
	msgflag="true";
	}
 if(document.donation.MC_lastname.value == ""){
	msg+="\nLast Name";
	 msgflag="true";
	}
if(document.donation.email.value  == ""){
	msg+="\nE-Mail Address";
    	msgflag="true";
	}
if(document.donation.email.value  != ""){
     var estr = new String(document.donation.email.value);
    var atindex = estr.indexOf("@");
     if(atindex ==-1){
         alert("You must enter a valid E-Mail Address!")
         document.donation.email.focus();
          return;
         }
	}
	
if(getSelectedButton(document.donation.amountslist)  == -1 && document.donation.normalAmount.value  == "" ){
	msg+="\nAmount you want to give";
    	msgflag="true";
	}

 if(msgflag == "true"){
	msg+="\n\nPress OK button below to return the form";
     	alert(msg);
}


if(msgflag == "false") {
		if(document.donation.normalAmount.value  == "") {
			document.donation.normalAmount.value = document.donation.amountslist[getSelectedButton(document.donation.amountslist)].value
		};
		document.donation.name.value = document.donation.MC_firstname.value + " " + document.donation.MC_lastname.value;
		document.donation.cartId.value=document.donation.MC_firstname.value+" "+document.donation.MC_lastname.value+"?"+document.donation.email.value;
		if(document.donation.MC_frequency[getSelectedButton(document.donation.MC_frequency)].value == "single" ) {
			document.donation.noOfPayments.value =""
			document.donation.intervalUnit.value =""
			document.donation.futurePayType.value = ""
			document.donation.amount.value = document.donation.normalAmount.value;
			document.donation.normalAmount.value = ""
			document.donation.MC_normalAmount.value = "0"
			document.donation.desc.value = "Single donation for the WCC";
		} else {
			document.donation.noOfPayments.value ="0"
			document.donation.intervalUnit.value ="3"
			document.donation.futurePayType.value = "regular"
			document.donation.amount.value = "0"
			document.donation.MC_normalAmount.value = document.donation.normalAmount.value
			document.donation.desc.value = "Monthly donation for the WCC"
		}
		document.donation.submit()
	}
}
