import pprint
from guestbook.forms import GuestbookForm
from guestbook.models import Message

from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    tpl_vars = {'messages': Message.objects.all()}
    if request.method == 'POST':
        form = GuestbookForm(request.POST)
        if form.is_valid():
            mess = Message()
            mess.username = request.POST['username']
            mess.text = request.POST['text']
            mess.email = request.POST['email']
            mess.save()
            tpl_vars['success_save'] = 1
            form = GuestbookForm()
    else:
        form = GuestbookForm()

    tpl_vars['form'] = form

    return render_to_response('guestbook/index.html', tpl_vars)
