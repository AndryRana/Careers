from django.db import models

# Create your models here.
# A)Prevent duplicate emails
class Registered_email(models.Model):
    email = models.CharField(max_length=40)
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name_plural = 'Registered'
    

# B)Send message
class Message(models.Model):
    
    SITUATION = {
        ('Read', 'Read'),
        ('Unread', 'Unread')
    }
    
    id = models.AutoField(primary_key=True)
    message = models.TextField()
    situation = models.CharField(max_length=50, null=True, choices=SITUATION, default='Unread')
    created_at = models.DateTimeField(auto_now_add=True)
    internal_note = models.TextField(blank=True)

#C) Support
class Support(models.Model):

    PERSON = {
        ('Employee', 'Employee'),
        ('Candidate', 'Candidate'),
    }

    OPTION = {
        ('I forgot my Password', 'I forgot my Password'),
        ('I forgot my account', 'I forgot my account'),
        ('Wanted to update my resume', 'Wanted to update my resume'),
        ('Others', 'Others'),
    }

    SITUATION = {
        ('Pending', 'Pending'),
        ('Done', 'Done'),
    }
    
    id = models.IntegerField(primary_key=True)
    terms = models.BooleanField("took responsability", default=False)
    message = models.TextField()
    person = models.CharField(max_length=50, choices=PERSON)
    option = models.CharField(max_length=50, choices=OPTION)
    email = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    situation = models.CharField(max_length=50, null=True, choices=SITUATION, default='Pending')
    internal_note = models.TextField(blank=True)

    def __str__(self):
        return self.person
    
    class Meta:
        verbose_name_plural = 'Support'

#D) Notepad
class Notepad(models.Model):
    
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=70)
    text = models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Notepad'
    
#E) Job openings
class Openings(models.Model):
    id = models.IntegerField(primary_key=True)
    backend = models.CharField(max_length=100)
    frontend = models.CharField(max_length=100)
    fullstack = models.CharField(max_length=100)
    intern = models.CharField(max_length=100)
    
    def __str__(self):
        return self.frontend
    
    class Meta:
        verbose_name_plural = 'Openings'
        
#F) Countdown
class Countdown(models.Model):
    id = models.IntegerField(primary_key=True)
    timer = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'Countdown'
    
# G) WAITING LIST
POST = (
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('Fullstack', 'Fullstack'),
        ('Intern', 'Intern'),
)

SITUATION = {
    ('Read', 'Read'),
    ('Unread', 'Unread'),
}

class WaitingList(models.Model):
    
    post = models.CharField(max_length=150, choices=POST)
    email = models.EmailField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    situation = models.CharField(max_length=75, null=True, choices=SITUATION, default='Unread')
    document = models.FileField()
    internal_note = models.TextField(blank=True)
    
    def __str__(self):
        return self.post
    
    class Meta:
        verbose_name_plural = 'Waiting list'

#H) Vacancies description       
class Vacancies(models.Model):
    dataTarget = models.CharField(max_length=40)
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.dataTarget
    
    class Meta:
        verbose_name_plural = 'Vacancies'
    