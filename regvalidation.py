<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- bootstrap cdn link for css  -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <!-- bootstarp cdn link for js  -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    <title>Registration form validation </title>

    <style>

        #form-div{
            width: 60%;
            margin: 0px auto;
        }
    </style>

</head>
<body>
    

    <div class="container my-3">

        <!-- heading div  -->

        <div class="container text-center bg-info text-light p-2 rounded-1 shadow">
            <h1 class="display-6">Registration Form</h1>
        </div>

        <!-- form div  -->

        <div class="container my-4 shadow p-5" id="form-div">
            <form action="" onsubmit="return FormValidation()">

                <!-- name div  -->

                <div class="mb-3">
                    <label for="name">Enter your Name :</label>
                    <input type="text" name="name" id="name" class="form-control">
                    <p id="namemsg"></p>
                </div>

                <!-- user div  -->

                <div class="mb-3">
                    <label for="username">Enter your UserName :</label>
                    <input type="text" name="username" id="username" class="form-control">
                    <p id="usermsg"></p>
                </div>

                <!-- contact div  -->

                <div class="mb-3">
                    <label for="contact">Contact Number :</label>
                    <input type="text" name="contact" id="contact" class="form-control">
                    <p id="contactmsg"></p>
                </div>

                <!-- email div  -->
                <div class="mb-3">
                    <label for="email">Enter Email-id :</label>
                    <input type="text" name="email" id="email" class="form-control">
                    <p id="emailmsg"></p>
                </div>

                <!-- password div  -->
                <div class="mb-3">
                    <label for="pass1">Enter Password :</label>
                    <input type="password" name="pass1" id="pass1" class="form-control">
                    <p id="passmsg1"></p>
                </div>

                <!-- confirm password  div -->
                <div class="mb-3">
                    <label for="pass2">Confirm Password :</label>
                    <input type="password" name="pass2" id="pass2" class="form-control">
                    <p id="passmsg2"></p>
                </div>

                <!-- check box show password div -->
                <div class="mb-3">
                    <input type="checkbox" name="showpass" id="showpass">
                    <label for="showpass">Show Password</label>
                    
                </div>

                <!-- registration button div  -->
                <div class="mb-3">
                    <input type="submit" value="Register" class="btn btn-success ">
                </div>

            </form>

        </div>
    </div>




    <script>

// **************************** for show password ******************************** 

        var showpass = document.getElementById("showpass");
        var pass1 = document.getElementById("pass1");
        var pass2 = document.getElementById("pass2");

        showpass.addEventListener("click" , showpassfunc);

        function showpassfunc(){
            // console.log("working");
            if (pass1.type == "password" || pass2.type == "password"){
                pass1.type = "text";
                pass2.type = "text"
            }
            else{
                pass1.type = "password"
                pass2.type = "password"
            }
        }


// ************************* form validation *********************************
        function FormValidation(){

            var name = document.getElementById("name").value;
            var username = document.getElementById("username").value;
            var contact = document.getElementById("contact").value;
            var email = document.getElementById("email").value;
            var pass1 = document.getElementById("pass1").value;
            var pass2 = document.getElementById("pass2").value;

            console.log(name);
            console.log(username);
            console.log(contact);
            console.log(email);
            console.log(pass1);
            console.log(pass2);

            return false
    }



    </script>

</body>
</html>





























final code...20 feb 2023..
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- bootstrap cdn link for css  -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <!-- bootstarp cdn link for js  -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    <title>Registration form validation </title>

    <style>

        #form-div{
            width: 60%;
            margin: 0px auto;
        }
    </style>

</head>
<body>
    

    <div class="container my-3">

        <!-- heading div  -->

        <div class="container text-center bg-info text-light p-2 rounded-1 shadow">
            <h1 class="display-6">Registration Form</h1>
        </div>

        <!-- form div  -->

        <div class="container my-4 shadow p-5" id="form-div">
            <form action="" onsubmit="return FormValidation()">

                <!-- name div  -->

                <div class="mb-3">
                    <label for="name">Enter your Name :</label>
                    <input type="text" name="name" id="name" class="form-control">
                    <p id="namemsg"></p>
                </div>

                <!-- user div  -->

                <div class="mb-3">
                    <label for="username">Enter your UserName :</label>
                    <input type="text" name="username" id="username" class="form-control">
                    <p id="usermsg"></p>
                </div>

                <!-- contact div  -->

                <div class="mb-3">
                    <label for="contact">Contact Number :</label>
                    <input type="text" name="contact" id="contact" class="form-control">
                    <p id="contactmsg"></p>
                </div>

                <!-- email div  -->
                <div class="mb-3">
                    <label for="email">Enter Email-id :</label>
                    <input type="text" name="email" id="email" class="form-control">
                    <p id="emailmsg"></p>
                </div>

                <!-- password div  -->
                <div class="mb-3">
                    <label for="pass1">Enter Password :</label>
                    <input type="password" name="pass1" id="pass1" class="form-control">
                    <p id="passmsg1"></p>
                </div>

                <!-- confirm password  div -->
                <div class="mb-3">
                    <label for="pass2">Confirm Password :</label>
                    <input type="password" name="pass2" id="pass2" class="form-control">
                    <p id="passmsg2"></p>
                </div>

                <!-- check box show password div -->
                <div class="mb-3">
                    <input type="checkbox" name="showpass" id="showpass">
                    <label for="showpass">Show Password</label>
                    
                </div>

                <!-- registration button div  -->
                <div class="mb-3">
                    <input type="submit" value="Register" class="btn btn-success ">
                </div>

            </form>

        </div>
    </div>




    <script>

// **************************** for show password ******************************** 

        var showpass = document.getElementById("showpass");
        var pass1 = document.getElementById("pass1");
        var pass2 = document.getElementById("pass2");

        showpass.addEventListener("click" , showpassfunc);

        function showpassfunc(){
            // console.log("working");
            if (pass1.type == "password" || pass2.type == "password"){
                pass1.type = "text";
                pass2.type = "text"
            }
            else{
                pass1.type = "password"
                pass2.type = "password"
            }
        }


// ************************* form validation *********************************
        function FormValidation(){

            var name = document.getElementById("name").value;
            var username = document.getElementById("username").value;
            var contact = document.getElementById("contact").value;
            var email = document.getElementById("email").value;
            var pass1 = document.getElementById("pass1").value;
            var pass2 = document.getElementById("pass2").value;

            // console.log(name);
            // console.log(username);
            // console.log(contact);
            // console.log(email);
            // console.log(pass1);
            // console.log(pass2);

            // return false
            var nameRegEx = /^[a-zA-Z\ ]+$/;
            var usernameRegEx = /^[a-zA-Z0-9]+$/;



            // empty fields
            if(name == '' || username == '' || contact == '' || email == '' || pass1 == '' || pass2 == '' ){
                
                if (name == ''){
                    var namemsg = document.getElementById('namemsg');
                    namemsg.innerHTML = 'Name field should not be empty..';
                    namemsg.style.color = 'red';
                    return false;
                }
                else {
                    var namemsg = document.getElementById('namemsg');
                    namemsg.innerHTML = '';

                }

                if (username == ''){
                    var usermsg = document.getElementById('usermsg');
                    usermsg.innerHTML = 'Username field should not be empty..';
                    usermsg.style.color = 'red';
                    return false;
                }

                else{
                    var usermsg = document.getElementById('usermsg');
                    usermsg.innerHTML = '';
                }

                if (contact == ''){
                    var contactmsg = document.getElementById('contactmsg');
                    contactmsg.innerHTML = 'Contact field should not be empty';
                    contactmsg.style.color = 'red';
                    return false;
                }
                else{
                    var contactmsg = document.getElementById('contactmsg');
                    contactmsg.innerHTML = '';
                }

                if (email == ''){
                    var emailmsg = document.getElementById('emailmsg');
                    emailmsg.style.color = 'red';
                    emailmsg.innerHTML = 'email field should not be empty';
                    return false;
                }
                else{
                    var emailmsg = document.getElementById('emailmsg');
                    emailmsg.innerHTML = '';
                }

                if (pass1 == ''){
                    var passmsg1 = document.getElementById('passmsg1');
                    passmsg1.innerHTML = 'password field should not be empty.';
                    passmsg1.style.color = 'red';
                    return false;
                }
                else {
                    var passmsg1 = document.getElementById('passmsg1');
                    passmsg1.innerHTML = '';

                }

                if (pass2 == ''){
                    var passmsg2 = document.getElementById('passmsg2');
                    passmsg2.innerHTML = 'confirm password field should not be empty.';
                    passmsg2.style.color = 'red';
                    return false;
                }
                else {
                    var passmsg2 = document.getElementById('passmsg2');
                    passmsg2.innerHTML = '';

                }
            }

            // name validationn

            if (name != ''){
                if (name.length <= 2){
                var namemsg = document.getElementById('namemsg');
                namemsg.innerHTML = 'Name should be greater than 2 character.';
                namemsg.style.color = 'red';
                return false;
                }

                if (name.length >= 20  ){
                    var namemsg = document.getElementById('namemsg');
                    namemsg.innerHTML = 'Name should be less then 20 character.';
                    namemsg.style.color = 'red';
                    return false;                 
                }
                if (!nameRegEx.test(name)){
                    var namemsg = document.getElementById('namemsg');
                    namemsg.innerHTML = 'Invalid Name';
                    namemsg.style.color = 'red';
                    return false; 

                }
            }

            // USER NAME VALIDATION

            if (!usernameRegEx.test(username)){
                var usermsg = document.getElementById('usermsg');
                usermsg.innerHTML = 'Invalid userName';
                usermsg.style.color = 'red';
                return false; 
            }
            
    }



    </script>

</body>
</html>
