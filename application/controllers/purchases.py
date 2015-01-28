from flask import render_template, request, redirect, flash, url_for
from ..models import PurchaseForm
from ..models import Notify
from wtforms import Form, TextField, TextAreaField, PasswordField, validators
from .. import app
from ..models import User
import gspread

def purchases():
    def incompletePurchaseRequest():
        notification = Notify(notification_type = 'error', message = 'Incomplete form')
        return render_template('purchase.html', form=form, active_page='purchase', notify = notification)

    form = PurchaseForm(request.form)
    if request.method == 'POST' and form.validate():
        gc = gspread.login('phoenixracingbaja@gmail.com','BajaBaja')
        work_sheet = gc.open('Purchases').sheet1
        i = 1
        col_list = work_sheet.col_values(1)
        for value in col_list:
            if value == None:
                break
            i += 1 
        work_sheet.update_acell('A%s'%(i), form.data['name'])
        work_sheet.update_acell('B%s'%(i), form.data['item'])
        work_sheet.update_acell('C%s'%(i), form.data['cost'])
        work_sheet.update_acell('D%s'%(i), form.data['vendor'])
        work_sheet.update_acell('E%s'%(i), form.data['link'])
        work_sheet.update_acell('F%s'%(i), form.data['date'])
        work_sheet.update_acell('G%s'%(i), form.data['quantity'])
        send_email();
        return redirect(url_for('index'))
    return render_template('purchase.html', form=form, active_page='purchase')
    
def send_email():
    import smtplib

    gmail_user = "phoenixracingbaja@gmail.com"
    gmail_pwd = "BajaBaja"
    FROM = 'phoenixracingbaja@gmail.com'
    TO = ['kevin.suzuki@students.olin.edu'] #must be a list
    SUBJECT = "A Baja purchase request has been submitted."
    TEXT = "This is an automated message. A purchase request has been added to the Baja Purchases List. To view it, follow this link: http://is.gd/BajaShopping"

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        #server = smtplib.SMTP(SERVER) 
        server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        #server.quit()
        server.close()
    except:
        print "failed to send mail"  
