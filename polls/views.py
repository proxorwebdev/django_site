# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from polls.models import Choice, Poll
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form
        return render_to_response('polls/poll_detail.html', {
            'object': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll_results', args=(p.id, )))

def index(request):

    if 'plain' in request.GET and request.GET['plain'] == '1':
        return HttpResponse('Hello Wolrd!1')
    else:
        return render_to_response('index.html')
