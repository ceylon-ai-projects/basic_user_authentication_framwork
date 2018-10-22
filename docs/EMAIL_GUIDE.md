

    Create a project: django-admin.py startproject gmail

    Edit settings.py with code below:

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'youremail@gmail.com'
    EMAIL_HOST_PASSWORD = 'email_password'
    EMAIL_PORT = 587

    Run interactive mode: python manage.py shell

    Import the EmailMessage module:

    from django.core.mail import EmailMessage

    Send the email:

    email = EmailMessage('Subject', 'Body', to=['your@email.com'])
    email.send()

For more informations, check send_mail and EmailMessage features in documents.

UPDATE for Gmail

Also if you have problems sending email via gmail remember to check this guides from google.

In your Google account settings, go to Security > Account permissions > Access for less secure apps and enable this option.

Also create an App specific password for your gmail after you've turned on 2-step-verification for it.

Then you should use app specific password in settings. So change the following line:

    EMAIL_HOST_PASSWORD = 'your_email_app_specific_password'

