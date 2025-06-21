function validate(e){
    e.preventDefault();
    const email = document.getElementById("email").Value;
    const pass = document.getElementById("password").Value;
    const age = document.getElementById("age").Value;
    const msgbox = document.getElementById("message");
    let message = '';

    if (email === '') {
        message ='Please enter an email.';
        msgbox.style.color = 'red';
    }
    else if (pass === '') {
        message ='Password must be atleast 8 characters long.';
        msgbox.style.color = 'red';
    }
    else if (age === '') {
        message ='Age must be between 12 - 50.';
        msgbox.style.color = 'red';
    }
    else {
        message = 'Login successful';
        msgbox.style.color = 'green';
    }
    msgbox.innerText = message;
}