document.addEventListener('DOMContentLoaded', ()=> {
    let allButtonsDelete = document.querySelectorAll('.table-person .delete');
    if (allButtonsDelete != null ){
        allButtonsDelete.forEach(button => {
            button.addEventListener('click', (e) => {
                e.preventDefault();
                let dataId = e.target.getAttribute('data-id');
                if (confirm('¿Estás seguro de que quieres eliminar esta persona?')) {
                    window.location.href = `eliminar_persona/${dataId}`;
                }
            })
        });
    }
})