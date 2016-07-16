#!/usr/bin/env python
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import index
from background_task import background
from django.contrib.auth.models import User
import pika
import time
import datetime
from django.utils import timezone
import json 
import psycopg2
from django.db import connection

from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import task
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

def insert():
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.26.50.120'))
	channel = connection.channel()
	method_frame, header_frame, body = channel.basic_get('hello')
	corpo = body
	if method_frame:
	    print method_frame, header_frame, body
	    channel.basic_ack(method_frame.delivery_tag)
	else:
	    print 'No message returned'

	load = task(task_name="hello ww", task_desc=corpo,data_created=timezone.now())
	load.save()
	return "salvo"


class TaskViewSet(viewsets.ModelViewSet):
	queryset = task.objects.all().order_by('-data_created')
	serializer_class = TaskSerializer

def single():
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.26.50.120'))
	channel = connection.channel()
	method_frame, header_frame, body = channel.basic_get('hello')
	corpo = body
	if method_frame:
	    print method_frame, header_frame, body
	    channel.basic_ack(method_frame.delivery_tag)
	else:
	    print 'No message returned'
	return corpo

corpo = ''




def load_one_message():
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.26.50.120'))
	channel = connection.channel()
	corpo =""
	# Get ten messages and break out
	for method_frame, properties, body in channel.consume('periodic_data'):

	    # Display the message parts
	    print method_frame
	    print properties
	    print body
	    corpo = body
	    # Acknowledge the message
	    channel.basic_ack(method_frame.delivery_tag)

	    # Escape out of the loop after 10 messages
	    if method_frame.delivery_tag == 1:
	        break

	# Cancel the consumer and return any pending messages
	requeued_messages = channel.cancel()
	print 'Requeued %i messages' % requeued_messages

	# Close the channel and the connection
	channel.close()
	connection.close()
	return corpo


@background(schedule=5)
def loading_temp(valor):
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.26.50.120'))
	channel = connection.channel()
	#channel.queue_declare(queue='hello', durable=True)
	#print(' [*] Waiting for messages. To exit press CTRL+C')

	
	def callback(ch, method, properties, body):
	    print(" [x] Received %r" % body)
	    ch.basic_ack(delivery_tag = method.delivery_tag)
	    

	channel.basic_qos(prefetch_count=1)
	channel.basic_consume(callback,queue='hello')
	channel.start_consuming()
	return valor

def send_message(queue, message):
	connection = pika.BlockingConnection(pika.ConnectionParameters('172.26.50.120'))
	channel = connection.channel()
	channel.basic_publish(exchange='', routing_key=queue,body=message)
	connection.close()


def changing_values(queue, message):
	connection = pika.BlockingConnection(pika.ConnectionParameters('172.26.50.120'))
	channel = connection.channel()
	channel.basic_publish(exchange='', routing_key=queue,body=message)
	connection.close()


	#Threads
def save_envmeasurements():
	import time
	import json
	while True:
		measures = load_one_message()
		d = json.loads(measures)
		#print temperature
		temperature = d['temperature']
		humidity = d['humidity']
		co = d['co2']
		time2 = d['time']
		date= datetime.datetime.now() # import the  time and date
		try:
			conn=psycopg2.connect("host='172.26.50.120' dbname='postgres' user='postgres' password='postgres'")  # connect to the server
			cur = conn.cursor() # create the cursor
			try:
				cur.execute('insert into envmeasurements values (%s , %s, %s, %s)' %(temperature,humidity,co,time2))
				print 'inserted'
				conn.commit()
			
			except Exception, e:
				print 'erro',e
		except Exception, e:
			print e
		time.sleep(14)

# Create your views here.

def home(request):
	preference = "0"

	template = 'index.html'
	#loading = single()
	if request.method == 'POST':
		form = index(request.POST)
		if form.is_valid():
			preference = form.cleaned_data['preference']
			request.session['preference'] = preference
			print request.session['preference']

	#If the variable session exist 
	import threading # importing the library
	t = threading.Thread(target=save_envmeasurements, args=(), kwargs={})
	t.setDaemon(True)
	t.start() # start the threading at the same time as the home page
	return render(request,template)


def strategies(request):
	preference = ''
	try:
		preference = request.session['preference'] # The frist thing to do is set the prefernce temperature when we open this form 	
		print 'preference strategies', preference
	except Exception, e:
		preference = '0'
	queue = "strategy" # name of the queue that will receive the temperature
	#send_message(queue, preference) 
	template ="strategies.html"
	return render(request, template,{'preference':request.session['preference']})



def st1(request):
	preference = ''
	try:
		preference = request.session['preference'] # The frist thing to do is set the prefernce temperature when we open this form 	
	except Exception, e:
		preference = '0'

	strat = 1
	dic = {}

	template = 'strategy1.html'
	queue = 'strategy'
	dic ={'num': strat, 'temp': preference}
	print "preference ______ ST1_>", preference
	#loading = single()
	if request.method == 'POST':
		form = index(request.POST)
		if form.is_valid():
			new_value = form.cleaned_data['preference']
			dic ={'num': strat, 'temp': new_value}
			print "preference ______ ST1_ POST>", new_value
			queue = 'strategy1/in'
			send_message(queue, new_value)
	#If the variable session exist 
	#print 'single', loading
	send_message(queue, json.dumps(dic))
	return render(request,template)






def st2(request):
	preference = ''
	try:
		preference = request.session['preference'] # The frist thing to do is set the prefernce temperature when we open this form 	
	except Exception, e:
		preference = '0'

	strat = 2
	dic = {}

	template = 'strategy2.html'
	queue = 'strategy'
	#loading = single()
	dic ={'num': strat, 'temp': preference}
	print "preference ______ ST2_>", preference

	if request.method == 'POST':
		form = index(request.POST)		
		if form.is_valid():
			new_value = form.cleaned_data['preference']

			dic ={'num': strat, 'temp': new_value}
			queue = 'strategy2/in'
			print "new value", new_value
			changing_values(queue, new_value)
	
	send_message(queue, json.dumps(dic))

	#If the variable session exist 
	return render(request,template)

	

def st3(request):
	preference = "0"

	template = 'strategy3.html'
	queue = 'strategy3'
	#loading = single()
	if request.method == 'POST':
		insert_database('stop', 'Strategy3')
		print 'Inserted....'

			#send_message(queue,new_value)
	#If the variable session exist 
	#print 'single', loading
	return render(request,template)



def st4(request):
	preference = "0"

	template = 'strategy4.html'
	queue = 'strategy4'
	#loading = single()
	if request.method == 'POST':
		form = index(request.POST)
		if form.is_valid():
			new_value = '0'
			send_message(queue,new_value)
	#If the variable session exist 
	#print 'single', loading

	return render(request,template)


def dictfetchall(cursor):
	desc = cursor.description
	return [dict(zip([call[0] for call in desc],raw)) for raw in cursor.fetchall()]

def get_ca_survey():
	try:		
		conn=psycopg2.connect("host='172.26.50.120' dbname='postgres' user='postgres' password='postgres'")  # connect to the server
		cur = conn.cursor() # create the cursor
		cur.execute("select * from ca_survey")
		#conn.commit()
		return dictfetchall(cur)
	except Exception, e:
		print 'erro',e

def get_measurements():
	try:		
		conn=psycopg2.connect("host='172.26.50.120' dbname='postgres' user='postgres' password='postgres'")  # connect to the server
		cur = conn.cursor() # create the cursor
		cur.execute("select * from envmeasurements")
		#conn.commit()
		return dictfetchall(cur)
	except Exception, e:
		print 'erro',e

		
def viewenvmeasurements(request):
	template = 'viewenvmeasurements.html'
	resultado = get_measurements()
	return render(request,template,{'resultado':resultado})


def viewdata(request):
	template = 'viewdata.html'
	resultado = get_ca_survey()
	#print resultado
	return render(request,template,{'resultado':resultado})




def insert_database(action, val):
	# Try to connect
	date= datetime.datetime.now()
	print date

	try:
	    conn=psycopg2.connect("host='172.26.50.120' dbname='postgres' user='postgres' password='postgres'")
	    print "Connected"
	    cur = conn.cursor()
	    try:
	    	cur.execute("Insert into actions(id, actions, val)  values (DEFAULT,  %s , %s )" %(action, date,))
	    except:
	    	print "I am unable to insert to the database."

	except Exception, e:
	    print "I am unable to connect to the database.", e
	



"""
def myview(request):
    objecto = single()
    try:
    	obj = request.session['loading']
    except Exception, e:
    	obj = ''

    print 'objecto -------->>>>>>>>>>>>>>>', objecto
    if str(objecto) == 'None':
    	if obj=='' :
    		return render_to_response('test.html')
    	else:
    		request.session['loading'] = obj
    		return render_to_response('test.html',{'objecto':obj})
    else:
    	request.session['loading'] = objecto
    	return render_to_response('test.html', { 'objecto': objecto })


"""




