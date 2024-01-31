function mostrarSeccion(id) {
    // Oculta todas las secciones
    var secciones = document.getElementsByClassName('seccion');
    for (var i = 0; i < secciones.length; i++) {
        secciones[i].style.display = 'none';
    }
    
    // Muestra solo la sección que se debe mostrar
    document.getElementById(id).style.display = 'block';
}