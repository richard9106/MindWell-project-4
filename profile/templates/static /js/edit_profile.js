
  // Selecciona el input de tipo fecha
  const inputFecha = document.getElementById('id_date');

  // Obtiene la fecha actual
  const hoy = new Date();

  // Convierte la fecha al formato 'YYYY-MM-DD' para asignarla al atributo 'min'
  const dia = String(hoy.getDate()).padStart(2, '0'); // Agrega un 0 si es un solo dígito
  const mes = String(hoy.getMonth() + 1).padStart(2, '0'); // Los meses en JS son 0-indexados
  const año = hoy.getFullYear();

  // Forma la fecha en formato 'YYYY-MM-DD'
  const fechaActual = `${año}-${mes}-${dia}`;

  // Establece la fecha mínima en el input
  inputFecha.min = fechaActual;

