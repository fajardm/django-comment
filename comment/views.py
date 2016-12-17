from django.shortcuts import render
from . import forms, models
from django.http import JsonResponse

import logging

logger = logging.getLogger('comment')


# Create your views here.
def index(request):
    logger.info("INDEX VIEW")
    if request.is_ajax() and request.method == 'GET':
        comment_list = models.get_all_by_content_type_and_object_id(
            content_type=request.GET['content_type'],
            object_id=request.GET['object_id']
        )
        return render(request, 'comment/comment_list.html', {'comment_list': comment_list})
    else:
        return JsonResponse({'status': 'forbidden'}, status=403)


def create(request):
    logger.info("CREATE VIEW")
    if request.is_ajax():
        form = forms.CommentForm(request.POST, initial=request.POST)
        if request.method == 'POST' and form.is_valid():
            forms.store(request)
            return render(request, 'comment/comment_form.html', {'form': forms.CommentForm(initial=request.POST)})
        else:
            return render(request, 'comment/comment_form.html', {'form': form})
    else:
        return JsonResponse({'status': 'forbidden'}, status=403)


def edit(request, pk):
    logger.info("EDIT VIEW")
    if request.is_ajax():
        form = forms.CommentForm(request.POST)
        if request.method == 'GET':
            try:
                comment = models.Comment.objects.get(pk=pk)
                form = forms.CommentForm(initial={
                    'content_type': comment.content_type.name,
                    'object_id': comment.object_id
                })
                return render(request, 'comment/comment_edit.html', {'form': form, 'comment': comment})
            except models.Comment.DoesNotExist:
                return JsonResponse({'status': 'forbidden'}, status=400)
        elif request.method == 'POST' and form.is_valid():
            forms.update(request, pk)
            form = forms.CommentForm(initial={
                'content_type': request.POST['content_type'],
                'object_id': request.POST['object_id']
            })
            return render(request, 'comment/comment_form.html', {'form': form})
        else:
            return JsonResponse({'status': 'forbidden'}, status=403)
    else:
        return JsonResponse({'status': 'forbidden'}, status=403)


def delete(request, pk):
    logger.info("DELETE VIEW")
    if request.is_ajax() and request.method == 'DELETE':
        try:
            models.Comment.objects.get(pk=pk).delete()
            return JsonResponse({'status': 'forbidden'})
        except models.Comment.DoesNotExist:
            return JsonResponse({'status': 'forbidden'}, status=400)
    else:
        return JsonResponse({'status': 'forbidden'}, status=403)
