var objPeople = [
	{ 
		username: "prasad",
		password: "prasad123"
	},
	{ 
		username: "eswar",
		password: "eswar123"
	},
	{ 
		username: "saiprasad",
		password: "saiprasad123"
	}

]

function getInfo() {
	var username = document.getElementById('username').value
	var password = document.getElementById('password').value

	if(username== "" || password== "") {
		window.alert("Please fill the required fields");

	}
	else{
     
	for(var i = 0; i < objPeople.length; i++) {
		
		if(username == objPeople[i].username && password == objPeople[i].password) {
			window.alert(username + " is logged in!!!");
            
			return
		}

	}
	window.alert("incorrect username or password");
	}
}

function getInfo1() {
	var username = document.getElementById('username').value
	var password = document.getElementById('password').value
	var Cpassword = document.getElementById('password1').value

if(username== "" || password== "" || Cpassword== "") {
		window.alert("Please fill the required fields");

	}
	if(password==Cpassword && password!= ""){
	window.alert(username + " You are successfuly registerd");
     setTimeout('Redirect', 3000);
     Redirect();
}
else{
window.alert(" Not Registerd successfuly \ncheck the fields Please ");}
}

function Redirect() {
               window.open("store1.html");

            }            
           
           