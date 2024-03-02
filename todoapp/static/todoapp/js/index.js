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
    var taskId = $(this).data('task-id');
    var completed = $(this).data('completed');
    $.ajax({
        type: 'POST',
        url: '/modify_task/',
        data: {
            'task_id': taskId,
            'completed': !completed,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success: function(response) {
            console.log(completed)
            console.log('Tarea modificada exitosamente');
        },
        error: function(response) {
            console.error('Error al modificar la tarea');
        }
    });
});
