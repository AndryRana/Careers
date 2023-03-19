/* ---------------------------- 
# FULL VALIDATION FORM
---------------------------- */
// 1) Inputmask (PHONE)
$(document).ready(function() {
    $(".phone").inputmask("(999) 999-9999", {"onincomplete": function() {
        $(".phone").val("");
        swal("Oh noez!", "Incomplete phone!", "info");
        return false;
    }});
});

// 2) INPUT VALIDATION
// 2.1) Frontend form
function validateEmailFrontend(email_frontend) {
    const regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email_frontend);
}
function frontend_form_valid() {
    const name_frontend = document.getElementById("name_frontend").value;
    const age_frontend = document.getElementById("age_frontend").value;
    const email_frontend = document.getElementById("email_frontend").value;
    const phone_frontend = document.getElementById("phone_frontend").value;
    const address_frontend = document.getElementById("address_frontend").value;
    const experience_frontend = document.getElementById("experience_frontend").value;
    const skills_frontend = document.getElementById("skills_frontend").value;
    const file_frontend = document.getElementById("file_frontend").value;

    if (name_frontend == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Name field cannot be empty.", "error");
        return false;
    }
    else if (name_frontend == name_frontend.toUpperCase()) {
        document.getElementById("spinner_screen").style.display = "none";
        document.getElementById("name_frontend").value = '';
        swal("Oh noez! !", "Name field cannot be Uppercase.", "info");
        return false;
    }
    else if (name_frontend.split(' ').length < 2) {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Full Name requiered.", "info");
        return false;
    }
    else if (age_frontend == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Age field cannot be empty.", "error");
        return false;
    }
    else if ((age_frontend < 18) || (age_frontend > 50)) {
        document.getElementById("spinner_screen").style.display = "none";
        document.getElementById('age_frontend').value='';
        swal("Oh noez! !", "Your Age must be between 18 & 50 years old.", "info");
        return false;
    }
    else if (email_frontend == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Email field cannot be empty.", "error");
        return false;
    }
    else if (!(validateEmailFrontend(email_frontend))) {
        document.getElementById("spinner_screen").style.display = "none";
        document.getElementById('email_frontend').value='';
        swal("Oh noez! !", "Put a valid email address.", "error");
        return false;
    }
    else if (phone_frontend == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Phone field cannot be empty.", "error");
        return false;
    }
    else if (address_frontend == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Address field cannot be empty.", "error");
        return false;
    }
    else if (experience_frontend == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Experience cannot be empty.", "error");
        return false;
    }
    else if (skills_frontend == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Skills cannot be empty.", "error");
        return false;
    }
    else if (file_frontend == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "File field cannot be empty.", "error");
        return false;
    }
    else {
        return true;
    }
}
// 2.2) backend form
function validateEmailBackend(email_backend) {
    const regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email_backend);
}
function backend_form_valid() {
    const name_backend = document.getElementById("name_backend").value;
    const age_backend = document.getElementById("age_backend").value;
    const email_backend = document.getElementById("email_backend").value;
    const phone_backend = document.getElementById("phone_backend").value;
    const address_backend = document.getElementById("address_backend").value;
    const experience_backend =document.getElementById("experience_backend").value;
    const skills_backend = document.getElementById("skills_backend").value;
    const file_backend = document.getElementById("file_backend").value;

    if (name_backend == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Name field cannot be empty.", "error");
        return false;
    }
    else if (name_backend == name_backend.toUpperCase()) {
        document.getElementById("spinner_screen").style.display = "none";
        document.getElementById("name_backend").value = '';
        swal("Oh noez! !", "Name field cannot be Uppercase.", "info");
        return false;
    }
    else if (name_backend.split(' ').length < 2) {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Full Name requiered.", "info");
        return false;
    }
    else if (age_backend == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Age field cannot be empty.", "error");
        return false;
    }
    else if ((age_backend < 18) || (age_backend > 50)) {
        document.getElementById("spinner_screen").style.display = "none";
        document.getElementById('age_backend').value='';
        swal("Oh noez! !", "Your Age must be between 18 & 50 years old.", "info");
        return false;
    }
    else if (email_backend == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Email field cannot be empty.", "error");
        return false;
    }
    else if (!(validateEmailBackend(email_backend))) {
        document.getElementById("spinner_screen").style.display = "none";
        document.getElementById('email_backend').value='';
        swal("Oh noez! !", "Put a valid email address.", "error");
        return false;
    }
    else if (phone_backend == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Phone field cannot be empty.", "error");
        return false;
    }
    else if (address_backend == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Address field cannot be empty.", "error");
        return false;
    }
    else if (experience_backend == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Experience cannot be empty.", "error");
        return false;
    }
    else if (skills_backend == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Skills cannot be empty.", "error");
        return false;
    }
    else if (file_backend == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "File field cannot be empty.", "error");
        return false;
    }
    else {
        return true;
    }
}
// 2.3) fullstack form
function validateEmailFullstack(email_fullstack) {
    const regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email_fullstack);
}
function fullstack_form_valid() {
    const name_fullstack = document.getElementById("name_fullstack").value;
    const age_fullstack = document.getElementById("age_fullstack").value;
    const email_fullstack = document.getElementById("email_fullstack").value;
    const phone_fullstack = document.getElementById("phone_fullstack").value;
    const address_fullstack = document.getElementById("address_fullstack").value;
    const experience_fullstack =document.getElementById("experience_fullstack").value;
    const skills_fullstack = document.getElementById("skills_fullstack").value;
    const file_fullstack = document.getElementById("file_fullstack").value;

    if (name_fullstack == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Name field cannot be empty.", "error");
        return false;
    }
    else if (name_fullstack == name_fullstack.toUpperCase()) {
        document.getElementById("spinner_screen").style.display = "none";
        document.getElementById("name_fullstack").value = '';
        swal("Oh noez! !", "Name field cannot be Uppercase.", "info");
        return false;
    }
    else if (name_fullstack.split(' ').length < 2) {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Full Name requiered.", "info");
        return false;
    }
    else if (age_fullstack == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Age field cannot be empty.", "error");
        return false;
    }
    else if ((age_fullstack < 18) || (age_fullstack > 50)) {
        document.getElementById("spinner_screen").style.display = "none";
        document.getElementById('age_fullstack').value='';
        swal("Oh noez! !", "Your Age must be between 18 & 50 years old.", "info");
        return false;
    }
    else if (email_fullstack == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Email field cannot be empty.", "error");
        return false;
    }
    else if (!(validateEmailFullstack(email_fullstack))) {
        document.getElementById("spinner_screen").style.display = "none";
        document.getElementById('email_fullstack').value='';
        swal("Oh noez! !", "Put a valid email address.", "error");
        return false;
    }
    else if (phone_fullstack == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Phone field cannot be empty.", "error");
        return false;
    }
    else if (address_fullstack == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Address field cannot be empty.", "error");
        return false;
    }
    else if (experience_fullstack == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Experience cannot be empty.", "error");
        return false;
    }
    else if (skills_fullstack == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Skills cannot be empty.", "error");
        return false;
    }
    else if (file_fullstack == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "File field cannot be empty.", "error");
        return false;
    }
    else {
        return true;
    }
}

// 2.4) Intern form
function validateEmailIntern(email_intern) {
    const regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email_intern);
}
function intern_form_valid() {
    const name_intern = document.getElementById("name_intern").value;
    const age_intern = document.getElementById("age_intern").value;
    const email_intern = document.getElementById("email_intern").value;
    const phone_intern = document.getElementById("phone_intern").value;
    const address_intern = document.getElementById("address_intern").value;
    const experience_intern =document.getElementById("experience_intern").value;
    const skills_intern = document.getElementById("skills_intern").value;
    const file_intern = document.getElementById("file_intern").value;

    if (name_intern == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Name field cannot be empty.", "error");
        return false;
    }
    else if (name_intern == name_intern.toUpperCase()) {
        document.getElementById("spinner_screen").style.display = "none";
        document.getElementById("name_intern").value = '';
        swal("Oh noez! !", "Name field cannot be Uppercase.", "info");
        return false;
    }
    else if (name_intern.split(' ').length < 2) {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Full Name requiered.", "info");
        return false;
    }
    else if (age_intern == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Age field cannot be empty.", "error");
        return false;
    }
    else if ((age_intern < 18) || (age_intern > 50)) {
        document.getElementById("spinner_screen").style.display = "none";
        document.getElementById('age_intern').value='';
        swal("Oh noez! !", "Your Age must be between 18 & 50 years old.", "info");
        return false;
    }
    else if (email_intern == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Email field cannot be empty.", "error");
        return false;
    }
    else if (!(validateEmailIntern(email_intern))) {
        document.getElementById("spinner_screen").style.display = "none";
        document.getElementById('email_intern').value='';
        swal("Oh noez! !", "Put a valid email address.", "error");
        return false;
    }
    else if (phone_intern == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Phone field cannot be empty.", "error");
        return false;
    }
    else if (address_intern == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Address field cannot be empty.", "error");
        return false;
    }
    else if (experience_intern == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Experience cannot be empty.", "error");
        return false;
    }
    else if (skills_intern == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "Skills cannot be empty.", "error");
        return false;
    }
    else if (file_intern == "") {
        document.getElementById("spinner_screen").style.display = "none";
        swal("Oh noez! !", "File field cannot be empty.", "error");
        return false;
    }
    else {
        return true;
    }
}

// 3) Maximum upload file size
$(document).ready(function() {
    $('#file_frontend, #file_backend, #file_fullstack, #file_intern, #file_waiting').bind('change', function() {
        var a = (this.files[0].size);

        if(a > 2 * 1048576) {
            swal("Oh noez !", "File maximum size is 2MB", 'info');
            this.value="";
        };
    });
});


//  4) Allow only letters in Name
$('.name').keyup(function() {
    if (!/^[a-zA-Z _]*$/.test(this.value)) {
        this.value = this.value.split(/[^a-zA-Z _]/).join('');
    }
});

// 5) Prevent more than 2 white spaces inside the input Name
$(".name").on('keydown', function() {
    var $this = $(this);
    $(this).val($this.val().replace(/(\s{2,})|[^a-zA-Z0-9_']/g, ' ').replace(/^\s*/, ''));
});

// 6) Prevent starting with space in all inputs and textarea
$("input[type=text], textarea").on("keypress", function(e){
    if (e.which === 32 && ! this.value.length) {
        e.preventDefault();
    }
});

// 7) Only Numbers accepted in Age field
$(".age, .openings_job").keyup(function(){
    if (!/^[0-9]*$/.test(this.value)) {
        this.value = this.value.split(/[^0-9]/).join('');
    }
});

// 8) Auto clear and prevent Age field greater than 50
$('.age').keyup(function (){
    if (((this.value) > 50)) {
        this.value = '';
    }
});

// 9) Prevent starting by zero in Age field
$('.age').on("input", function (){
    if(/^0/.test(this.value)) {
        this.value = this.value.replace(/^0/, "")
    }
});

// 10) Script to lowercase email field
$(document).ready(function (){
    $(".email").keyup(function(){
        this.value = this.value.toLowerCase();
    });
});

/* ---------------------------- ---------
     Hide || show password on login page
    ------------------------------------ */
function checking(){
    var pass = document.querySelector("#password");
    if (pass.type === "password") {
        pass.type = "text";
    }
    else {
        pass.type = "password";
    }
}

