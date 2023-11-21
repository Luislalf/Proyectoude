const loaderOut = document.querySelector("#loader-out");
function fadeOut(element) {
  let opacity = 1;
  const timer = setInterval(function () {
    if (opacity <= 0.1) {
      clearInterval(timer);
      element.style.display = "none";
    }
    element.style.opacity = opacity;
    opacity -= opacity * 0.1;
  }, 50);
}
fadeOut(loaderOut);

function eliminarCliente(id_cliente) {
  if (confirm("¿Estas seguro que deseas Eliminar el cliente?")) {
    let url = `/borrar-cliente/${id_cliente}`;
    if (url) {
      window.location.href = url;
    }
  }
}

function eliminarProveedor(id_proveedor) {
  if (confirm("¿Estas seguro que deseas Eliminar el Proveedor?")) {
    let url = `/borrar-proveedor/${id_proveedor}`;
    if (url) {
      window.location.href = url;
    }
  }
}

function eliminarEmpleado(id_empleado, foto_empleado) {
  if (confirm("¿Estas seguro que deseas Eliminar el empleado?")) {
    let url = `/borrar-empleado/${id_empleado}/${foto_empleado}`;
    if (url) {
      window.location.href = url;
    }
  }
}

function eliminarProducto(id_producto) {
  if (confirm("¿Estas seguro que deseas Eliminar el Producto?")) {
    let url = `/borrar-producto/${id_producto}`;
    if (url) {
      window.location.href = url;
    }
  }
}
