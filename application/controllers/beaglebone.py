from flask import render_template, request, redirect, url_for
from flask.ext.socketio import SocketIO, emit
from .. import app, socketio

post_data = [None, None]

def debug():
    if request.method == 'GET':
        return render_template('bb_debug.html')

    if request.method == 'POST':
        temp = dict(request.form)
        for k,v in temp.items():
            temp[k] = float(v[0])
        if post_data[0] != request.form:
            post_data[1] = post_data[0]
            post_data[0] = temp
        return ''