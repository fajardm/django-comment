from django import template
from comment.forms import CommentForm
from comment import models

register = template.Library()


@register.simple_tag
def comment_form(content_type, object_id):
    return CommentForm(initial={'content_type': content_type, 'object_id': object_id})


@register.simple_tag
def comment_list(content_type, object_id):
    return models.get_all_by_content_type_and_object_id(content_type, object_id)


@register.simple_tag
def total_comment(content_type, object_id):
    return models.get_total_comment(content_type, object_id)
