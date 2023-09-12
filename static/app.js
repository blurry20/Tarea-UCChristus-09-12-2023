async function buscarUsuario() {
  const campo = document.getElementById("campo").value;
  const tipoBusqueda = document.getElementById("tipoBusqueda").value;
  try {
    const response = await fetch(`/buscar/${tipoBusqueda}/${campo}`);
    const data = await response.json();

    mostrarResultados(data);
  } catch (error) {
    console.error("Error al buscar usuario:", error);
  }
}
