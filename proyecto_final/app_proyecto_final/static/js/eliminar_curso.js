const botonesEliminar = document.querySelectorAll("#btn-elim");

for (let i = 0; i < botonesEliminar.length; i++) {
  botonesEliminar[i].addEventListener("click", eliminarCurso);
}

function eliminarCurso(event) {
    // Obtener el botón que se ha hecho clic
    const btn = event.target;
    
    // Subir en el árbol DOM hasta encontrar el elemento <tr> correspondiente
    const tr = btn.closest('tr');
    
    // Obtener el id del curso desde el atributo "data-id"
    const id = tr.dataset.id;
    
    Swal.fire({
        "title": "Felicitaciones!",
        "text": "{{m}}",
        "icon": "question",
        "showCancelButton": true,
        "cancelButtonText": "No, cancelar",
        "confirmButtonText": "Si, eliminar",
        "reverseButtons": true,
        "confirmButtonColor": "#dc3545"
    }).then((result) => {
        if (result.isConfirmed) {
            // Redireccionar a la URL con el id del curso a eliminar
            window.location.href = "{% url 'eliminarCurso' id %}";
        }
    });
}





// {% if messages  %}
//                         {% for m in messages %}
//                                 Swal.fire({
//                                     "title": "Felicitaciones!",
//                                     "text": "{{m}}",
//                                     "icon": "success"
//                                 })
//                         {% endfor %}
//                     {% endif %}