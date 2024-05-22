const columns = ['to-do', 'in-progress', 'done'];

columns.forEach(column => {
    new Sortable(document.getElementById(column), {
        group: 'tasks',
        animation: 150,
        onEnd: function (evt) {
            const taskId = evt.item.getAttribute('data-id');
            const newStatus = evt.to.id.replace('-', '_');

            fetch(UpdateTaskStatus, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: `task_id=${taskId}&new_status=${newStatus}`
            }).then(response => response.json()).then(data => {
                if (data.status === 'success') {
                    evt.item.setAttribute('data-status', newStatus);
                }
            });
        }
    });
});