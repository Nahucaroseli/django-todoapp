$('.deleteTask').on('click', function() {
    console.log("hola")
   
    var taskId = $(this).data('task-id');
    $.ajax({
        type: 'POST',
        url: '/delete_task/',
        data: {
            'task_id': taskId,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success: function(response) {
            window.location.href= '/home'
        },
        error: function(response) {
            console.error('Error al eliminar la tarea');
        }
    });
});



$('.modify-task').on('click', function() {
    var taskId = $(this).data('id-task');
    $.ajax({
        type: 'POST',
        url: '/modify_task/',
        data: {
            'task_id': taskId,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success: function(response) {

        },
        error: function(response) {

        }
    });
});
