from django import forms
from .models import Comment
from django.contrib.contenttypes.models import ContentType


def store(request):
    post = request.POST
    user = request.user
    content_type = ContentType.objects.get(app_label="anime", model=post['content_type'])
    comment = Comment(
        created_by=user,
        content_type=content_type,
        object_id=post['object_id'],
        comment=post['comment'])
    comment.save()
    return comment


def update(request, pk):
    post = request.POST
    comment = Comment.objects.filter(pk=pk).update(comment=post['comment'])
    return comment


class CommentForm(forms.Form):
    content_type = forms.CharField(
        label='Content type',
        widget=forms.HiddenInput()
    )
    object_id = forms.CharField(
        label='Object id',
        widget=forms.HiddenInput()
    )
    comment = forms.CharField(
        label='Comment',
        min_length=10,
        required=True,
        widget=forms.Textarea(
            attrs={'class': 'uk-width-1-1', 'rows': '5'}
        )
    )
