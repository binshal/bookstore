function Loginalert(){

    var username = document.getElementById('username').value;
    var fname = document.getElementById('fname').value;
    var lname = document.getElementById('lname').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var cpassword = document.getElementById('cpassword').value;


    if (!username || !fname || !lname || !email || !password || !cpassword){
        alert("Please fill all the fields")
    }
    else{
        alert("User Registration Submitted Succesfullly")
    }
}