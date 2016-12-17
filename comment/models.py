from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from vote.models import Vote
from django.contrib.auth.models import User


# Create your models here.
class Comment(models.Model):
    comment = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name="comment_created_by",
                                   editable=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    vote = GenericRelation(Vote, related_name='comment_vote')
    comments = GenericRelation("self", related_name='comment_child')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

    def object(self):
        return self.content_type.name + ": " + self.content_object.__str__()

    def as_json(self):
        return {
            'pk': self.pk,
            'content_type': self.content_type.__str__(),
            'object_id': self.object_id,
            'comment': self.comment,
            'username': self.created_by.username,
            'cretead_at': naturaltime(self.created_at)
        }

    pass


def get_all_by_content_type_and_object_id(content_type, object_id):
    content_type = ContentType.objects.get(app_label="anime", model=content_type)
    comment_list = Comment.objects.filter(content_type=content_type, object_id=object_id).order_by('-created_at')[:15]
    return comment_list


def get_total_comment(content_type, object_id):
    content_type = ContentType.objects.get(app_label="anime", model=content_type)
    total = Comment.objects.filter(content_type=content_type, object_id=object_id).order_by('-created_at').count()
    return total
