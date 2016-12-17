/**
 * Created by fajar on 12/16/2016.
 */
function submit_comment(el) {
    console.log("submmit comment");
    $.ajax({
        url: $(el).attr('action'),
        type: "POST",
        data: {
            content_type: $('#id_content_type').val(),
            object_id: $('#id_object_id').val(),
            comment: $('#id_comment').val()
        },
        success: function (data) {
            console.log('success');
            $('#section-comment-form').html(data);
            reload_comment_list();
        },
        error: function (error) {
            console.log('error');
            console.log(error);
            $('#section-comment-form').html(error);
        }
    });
    return false;
}

function comment_edit(el) {
    $("#section-comment-form").load($(el).attr('href'));
    return false;
}

function update_comment(el) {
    console.log("update comment");
    $.ajax({
        url: $(el).attr('action'),
        type: "POST",
        contentType: 'application/x-www-form-urlencoded',
        data: {
            content_type: $('#id_content_type').val(),
            object_id: $('#id_object_id').val(),
            comment: $('#id_comment').val()
        },
        success: function (data) {
            console.log('success');
            $('#section-comment-form').html(data);
            reload_comment_list();
        },
        error: function (error) {
            console.log('error');
            console.log(error);
            $('#section-comment-form').html(error);
        }
    });
    return false;
}

function delete_comment(el) {
    console.log("destroy comment");
    $.ajax({
        url: $(el).attr('href'),
        type: "DELETE",
        success: function (data) {
            console.log('success');
            reload_comment_list();
        },
        error: function (error) {
            console.log('error');
        }
    });
    return false;
}

function reload_comment_list() {
    $("#section-comment-list").load($("#section-comment-list").attr('data-url'));
}