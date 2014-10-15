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
		gc = gspread.login('phoenixracingbaja@gmail.com','OlinBaja')
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
		return redirect(url_for('index'))
	return render_template('purchase.html', form=form, active_page='purchase')
	
	 