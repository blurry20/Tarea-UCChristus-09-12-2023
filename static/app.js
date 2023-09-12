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
function mostrarResultados(data) {
  const resultadoDiv = document.getElementById("resultado");
  resultadoDiv.innerHTML = "";

  if (data.error) {
    resultadoDiv.textContent = `Error: ${data.error}`;
  } else if (Array.isArray(data.usuarios)) {
    if (data.usuarios.length === 0) {
      resultadoDiv.textContent = "No se encontraron usuarios.";
    } else {
      const ul = document.createElement("ul");
      data.usuarios.forEach((usuario) => {
        const li = document.createElement("li");
        li.textContent = `ID: ${usuario.id}, Nombre: ${usuario.first_name}, Apellido: ${usuario.last_name}, Email: ${usuario.email}, Género: ${usuario.gender}, Plan de Salud: ${usuario["Plan de Salud"]}, Teléfono: ${usuario.phone}`;
        ul.appendChild(li);
      });
      resultadoDiv.appendChild(ul);
    }
  }
}
const buscarButton = document.getElementById("buscarButton");
buscarButton.addEventListener("click", buscarUsuario);
