# Django Ajax Comment
Django Ajax Comment is a simple Django app to make comment in your article, video, image and other Model you have.
## Quick start
1. Add "comment" to your INSTALLED_APPS setting like this:
    ```python
    INSTALLED_APPS = [
            ...
            'comment',
        ]
    ```
2. Include the comment URLconf in your project urls.py like this:
    ```python
    url(r'^comment/', include('comment.urls')),
    ```
3. Run `python manage.py migrate` to create the comment models.
4. Start the development server and visit http://127.0.0.1:8000/admin/ to create a comment (you'll need the Admin app enabled).
## How to use
First, you must load `{% load comment %}` in your template and add `<script src="{% static 'comment/web/comment.js' %}"></script>` before your close body.
### Comment Form
You can load comment form with `{% comment_form 'model_name' [model_id] as [alias] %}` and `{% include 'comment/comment_form.html' %}`
example
```python
{% comment_form 'episode' episode.id as form %}
{% include 'comment/comment_form.html' %}
```
you can read django forms documentation for customizing template form:
```python
{{ form.content_type }}
{{ form.object_id }}
```
### Comment List
Like comment form, you just load comment list with `{% comment_list 'episode' episode.id as comment_list %}` and `{% include 'comment/comment_list.html' %}`
èxample
```python
{% comment_list 'episode' episode.id as comment_list %}
{% include 'comment/comment_list.html' %}
```