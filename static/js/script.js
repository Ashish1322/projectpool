function openNav() {
  document.getElementById("filt").style.width = "40vh";
  document.getElementById("mySidebar").style.width = "30vh";
  document.getElementById("filterbtn").style.zIndex = "0";   
}

/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("filterbtn").style.zIndex = "1";
  setTimeout(()=>{
    document.getElementById("filt").style.width = "0";
  },500)
  // document.getElementById("main").style.marginLeft = "0";
}

function formclsbtn() {
let formel = document.getElementById("signupform");
formel.innerHTML = "";
formel.style.width = "0%";
formel.style.height = "0%";
}

function openForm(){
let formel = document.getElementById("signupform");
formel.style.width = "100%";
formel.style.height = "100%";
formel.innerHTML=`
<div class="cross">
      <button onclick="formclsbtn()">x</button>
    </div>
    <div class="formm">
      <form action="{% url 'signup' %}" method="POST" enctype="multipart/form-data" >
        {% csrf_token %}
      <label>Username :</label><br>
      <input type="text" id="username" name="username" placeholder="Example : Am_I_Tea?" required><br>
      <label>University Name :</label><br>
      <input type="text" id="name" name="name" placeholder="University" required><br>
      <label>Email :</label><br>
      <input type="text" id="email" name="email" placeholder="Email address" required><br>
      <label>Password :</label><br>
      <input type="password" id="pass" name="password" placeholder="Password" required><br>
      <label>Confirm :</label><br>
      <input type="password" id="cpass" name="confirmpassword" placeholder="Password" required><br>
      <label>Unique Id :</label><br>
      <input type="text" id="uid" name="uid" 
      placeholder="Id" required><br>
      <label>City :</label><br>
      <input type="text" id="city" name="city" placeholder="State" required><br>
      <label>State :</label><br>
      <input type="text" id="state" name="state" placeholder="State" required><br>
      <label>Country :</label><br>
      <input type="text" id="country" name="country" placeholder="Country" required><br>
      <label>Upload Logo :</label><br>
      <input type="file" id="file" name="logo" required><br>
      <input type="submit" value="Submit">
    </form>
    </div>
`;
}
function lformclsbtn(){
let formel = document.getElementById("loginform");
formel.innerHTML = "";
formel.style.width = "0%";
formel.style.height = "0%";
}

function login(){
let formel = document.getElementById("loginform");
formel.style.width = "100%";
formel.style.height = "100%";
formel.innerHTML = `
<div class="cross">
      <button onclick="lformclsbtn()">x</button>
    </div>
    <div class="formm">
      <form method="POST" action="{% url 'login' %}" >
        {% csrf_token %}
      <label>Username :</label><br>
      <input type="text" id="Uname" name="Uname" placeholder="Example : Am_I_Tea?" required><br>
      <label>Password :</label><br>
      <input type="text" id="Uname" name="Uname" placeholder="Password" required><br>
      <input type="submit" value="LogIn">
    </form>
    </div>
`
}