

document.getElementById("submitcreds").addEventListener("submit", submitForm(e));


function submitForm(e){
    e.preventDefault();
    const username = document.getElementById("userName");
    const password = document.getElementById("userpass");
    if(!username.value.trim()  || !password.value.trim()){
        let errorbox = document.getElementById("errorbox");
        errorbox.innerText = "username and password is required";
        return false;
    } else{
            errorbox.innerText = "";
            document.getElementById("submitcreds").submit();
     }
    return true;
}