◉ Distinctiveness and Complexity:

    ⦿ I have created a human resource Agency fully responsive web application specialized in IT solutions. I utilised Django on the backend and JavaScript on the frontend.

    ⦿ The candidate 
        ▶︎ can make a spontaneous application or respond to a job announcements.
        ▶︎ can fill a form and send automatically an email with the candidate's resume as an attachment to the agengy email address specified in the code:
            ▻ I imported the "loader" module from django.template to load a text template that will be used to generate the email message.
            ▻ An EmailMultiAlternatives object is created with a subject line, the rendered message as its body, and the sender and recipient email addresses.
            ▻ The content subtype of the email is set to "html", indicating that the message body contains HTML markup.

    ⦿ The user can contact the support, if there is a specific request.Users who did not apply, cannot contact the support because the email is not registered. 
    
    ⦿ The agency employees or administrator can log in, but applicants cannot 

    ⦿ Users can also send a simple message to the admnistrator.
    
    ⦿ Users can to see the number of available vacancies  and the time remaining to apply in opportunities page.

    ⦿ The Agency employee who is logged in will have direct access to the backend page that allows him/her to manage new job announcements.
    The Backend allows to see the number of applicants, to manage the number of available vacancies, to create vacancies as well, to create a countdown to define the deadline for application and leave some notes.
        ► If the number of vacancies is equal to 0, the offer button is disabled, and the job offers of the same category disappear 

    ⦿ After logging in the employee can contact the support (the email of the employee is directly displayed in the form for the support ) and the superuser can directly access the site administration page without having to contact support.
        ► When the employee is logged in, the e-mail field is filled in automatically when he/she contacts the support.

    ⦿ A timer has been created to define the application deadline:
        ► All job offers are deactivated when the time is over, But there is a modal alert notifying applicants that they can register in the waiting list.
    
    ⦿ Each field of the application form  must be validated:
        ▶︎ Setting the Maximum upload file size.
        ▶︎ Allow only letters in Name.
        ▶︎ Prevent more than 2 white spaces inside the input Name.
        ▶︎ Prevent to start with a space character in an <input> or a <textarea>.
        ▶︎ In Age field only Numbers accepted, Auto clear, prevent the age greater than 50 and prevent starting by zero .
        ▶︎ Using Inputmask for the phone validation.

    ⦿ After closing the modal, ensuring that any input data is cleared and the form is ready for the next use.

    ⦿ Show a spinner animation while an AJAX request is being made, and alert the user with data returned from the server once the request is successful.

    ⦿ Checking if the email submitted by the user already exists.If it does, it displays a message 
        ▶︎ request for support
        ▶︎ resume 
        ▶︎ waiting list 

    ⦿ SECURITY
        ▶︎ The @login_required decorator is used to restrict access to a view to authenticated users only(only Employees or Super user).
        ▶︎ CACHE AND STORE  @cache_control, no_cache=True, must_revalidate=True, no_store=True:
            ▻ these decorators are used to add security measures to a view function, ensuring that only authenticated users can access it and that the response is not cached or stored in any cache.
        ▶︎ DDOS vulnerability: Put [onunload=''] inside "body" and Cache control in all views functions (protect against ddos clearing history without refresh the page).

    ⦿ MEDIA FILES setting : handling the serving and storage of user-uploaded media files by setting MEDIA_URL, Django knows where to look for media files when they are requested by a user. By setting MEDIA_ROOT, Django knows where to store media files when they are uploaded by a user.

    ⦿ ADMIN PAGE SETTING :
        ► Secure data manipulation in Django admin:
            ▻ Created a function to allow only one record or one ID (table: Countdown, Notepad, Openings) in Django admin page to control whether the "Add" button is displayed or not, based on certain conditions.
            ▻ Disabling the possibility to modify data in admin.py by adding  "readonly_fields".
        ► Define a custom admin interface for models
            ▻ Administrator can change the status in Support, Waiting list or message table.(Read or Unread - Pending or Done)
        ► Remove extra 'S' in Django admin and change name in models.py by including "verbose_name_plural".

◉ FILES:

    ❖ requirements.txt : contains 2 packages
    
    ❖ STATIC
        ⦿ css :
            ► style.css : Setting the web application css
        ⦿ img :
            ► favicon and background image
        ⦿ js :
            ► job.js :
                ▻ Full validation form
                ▻ Hide or show password on login page

    ❖ TEMPLATES
        ⦿ layout.html :
            ► contain all link, script, include and Javascript ou jQuery to display message popup, spinner Ajax, close modal after clicking on send   button,     Clear the form (inside the modal) after closing the modal, disable or enable dependent option inside the support form, Countdown.
        ⦿ home.html : is the index. 
        ⦿ opportunities.html :
            ► contain the codes to display the vacant opportunities and to apply.
        ⦿ description.html :
            ► allow to view the job description and to apply.
        ⦿ job/templates/backend.html :
            ► allow to manage the job announcements by the employee.
        ⦿ support.html :
            ► contain Form to contact the support.
        ⦿ waiting_list.html:
            ► contain Form to register in the waiting list when job offers are deactivated.
        ⦿ resume_form.txt:
            ► contain text template that will be used to generate the email message.

    ❖ REGISTRATION
        ⦿ login.html :
            ► show the login page for the employees or superusers.

    ❖ MODALS/BACKEND
        ⦿ layout.html :
            ► Contain modal root template to manage number of vacant jobs, notepad, timer and job creation.
        ⦿ candidates.html :
            ► Allow to display the number of candidates.
        ⦿ jobOpenings.html :
            ► Allow to change the number of job vacancy.
        ⦿ notepad.html :
            ► Allow you to leave some notes.
        ⦿ show_countdown.html :
            ► Allow you to change the timer.
        ⦿ vacancy.html :
            ► Allow you to create new job announcements.

    ❖ MODALS/CLOSEDPOSITION
        ⦿ layout.html :
            ► Contain modal root template to manage all opportunities closed.
        ⦿ 1_position :
            ► backend_closed.html, frontend_closed.html, fullstack_closed.html,intern_closed.html :
                ▻ Show that 1 category the jobs are closed.
        ⦿ 2_positions :
            ► back_full_closed.html, back_intern_closed.html, front_back_closed.html, front_full_closed.html, front_intern_closed.html, full_Intern_closed.   html:
                ▻ Show that 2 categories of the job are closed.
        ⦿ 3_positions :
            ► back_full_intern_closed.html, front_back_full_closed.html, front_back_intern_closed.html, front_full_intern_closed.html :
                ▻ Show that 3 categories of the job are closed.
        ⦿ 4_positions :
            ► all_closed.html:
                ▻ Show a warning message that all categories of the job are closed.
            ► all_countdown_closed.html:
                ▻ Show link to register in the waiting list.

    ❖ MODALS/DUPLICATED_MSG
        ⦿ layout.html :
            ► Contain modal root template to display all error message related to duplicated request.
        ⦿ duplicate_request_modal.html :
            ► Show error message related to a pending request to support 
        ⦿ duplicate_resume_modal.html :
            ► Show error message related to an existing resume in database
        ⦿ duplicate_wait_list_modal.html :
            ► Show error message related to an existing waiting list request

    ❖ MODALS/FORMS
        ⦿ layout.html :
            ► Contain modal root template to display the fields of a form to apply a job.
        ⦿ backend.html, frontend.html, fullstack.html, intern.html :
            ► Contain the settings of the fields of each job in the modal.

    ❖ MODALS/VARIOUS
        ⦿ layout.html :
            ► Contain modal root template to display some notifications in logout, opportunities info, message, and support.
        ⦿ logout.html :
            ► Allow the employees or superusers to log out.
        ⦿ opportunities_info.html :
            ► Allow users to see the number of available vacancies and the time remaining to apply.
        ⦿ sendMessage.html :
            ► Allow users to send a simple message to the administrator.
        ⦿ supportModalPopup.html :
            ► Display a message informing about the availability of the support


◉ HOW TO RUN THE APPLICATION
    ⦿ Install the requirements.txt file packages 
    ⦿ Create a super user
    ⦿ Create user (employee) in Django Administration
    ⦿ In order to receive by e-mail the job applications:
        ► Setting your GMAIL account inside the "setting.py" by adding your email and password (line 137, 138)
            ▻ EMAIL_HOST_USER = 'Your email address here...'
            ▻ EMAIL_HOST_PASSWORD = 'Password'    
        ► If you use another e-mail server, enter all the necessary data in "setting.py"
    ⦿ In "views.py" enter your email in the following functions:
        ► frontend_email, backend_email, fullstack_email, Intern_email 
            ▻ On the line where this piece of code is placed:
                email = EmailMultiAlternatives(
                "Backend - Candidate",
                message,
                "Backend Opportunity",
                ["Your email address here.."],
            )
