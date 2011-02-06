from guestbook.models import Message

from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    tpl_vars = {}
    tpl_vars['messages'] = Message.objects.all()
    if request.method == 'POST':
        errors = []

        if not request.POST['username']:
            errors.append("Username is required")
        else:
            if len(request.POST['username']) > 100:
                errors.append("Username is greater than 100 symbols")

        if not request.POST['email']:
            errors.append("Email is required")
        else:
            if len(request.POST['email']) > 100:
                errors.append("Email is greater than 100 symbols")

        if not request.POST['text']:
            errors.append("Text is required")

        if not errors:
            mess = Message()
            mess.username = request.POST['username']
            mess.text = request.POST['text']
            mess.email = request.POST['email']
            mess.save()
            tpl_vars['success_save'] = 1
        else:
            tpl_vars['errors'] = errors
    return render_to_response('guestbook/index.html', tpl_vars)
