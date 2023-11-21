from app import app
from flask import render_template, request, flash, redirect, url_for, session,  jsonify
from mysql.connector.errors import Error


# Importando cenexión a BD
from controllers.funciones_home import *

PATH_URL = "public/empleados"
PATH_URLC = "public/clientes"
PATH_URLP = "public/proveedores"
PATH_URLPR = "public/productos"
PATH_URLCOM = "public/compras"
PATH_URLVEN = "public/ventas"


# rutas cliente -----------------------------------------------------------------------
@app.route('/registrar-cliente', methods=['GET'])
def viewFormCliente():
    if 'conectado' in session:
        return render_template(f'{PATH_URLC}/form_cliente.html')
    else:
        flash('primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))

@app.route('/form-registrar-cliente', methods=['POST'])
def formCliente():
    if 'conectado' in session:
            resultado = procesar_form_cliente(request.form)
            if resultado:
                return redirect(url_for('lista_clientes'))
            else:
                flash('El cliente NO fue registrado.', 'error')
                return render_template(f'{PATH_URLC}/form_cliente.html')
    else:
        flash('primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))
    
@app.route('/lista-de-clientes', methods=['GET'])
def lista_clientes():
    if 'conectado' in session:
        return render_template(f'{PATH_URLC}/lista_clientes.html', clientes=sql_lista_clientesBD())
    else:
        flash('primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))
    
@app.route("/detalles-cliente/", methods=['GET'])
@app.route("/detalles-cliente/<int:idCliente>", methods=['GET'])
def detalleCliente(idCliente=None):
    if 'conectado' in session:
        # Verificamos si el parámetro idCliente es None o no está presente en la URL
        if idCliente is None:
            return redirect(url_for('inicio'))
        else:
            detalle_cliente = sql_detalles_clientesBD(idCliente) or []
            return render_template(f'{PATH_URLC}/detalles_cliente.html', detalle_cliente=detalle_cliente)
    else:
        flash('Primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))

# Buscadon de clientes
@app.route("/buscando-cliente", methods=['POST'])
def viewBuscarClienteBD():
    resultadoBusqueda = buscarClienteBD(request.json['busqueda'])
    if resultadoBusqueda:
        return render_template(f'{PATH_URLC}/resultado_busqueda_cliente.html', dataBusqueda=resultadoBusqueda)
    else:
        return jsonify({'fin': 0})


@app.route("/editar-cliente/<int:id>", methods=['GET'])
def viewEditarCliente(id):
    if 'conectado' in session:
        respuestaCliente = buscarClienteUnico(id)
        if respuestaCliente:
            return render_template(f'{PATH_URLC}/form_cliente_update.html', respuestaCliente=respuestaCliente)
        else:
            flash('El cliente no existe.', 'error')
            return redirect(url_for('inicio'))
    else:
        flash('Primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))

# Recibir formulario para actulizar informacion de cliente
@app.route('/actualizar-cliente', methods=['POST'])
def actualizarCliente():
    resultData = procesar_actualizacion_formCliente(request)
    if resultData:
        return redirect(url_for('lista_clientes'))

@app.route('/borrar-cliente/<string:id_cliente>', methods=['GET'])
def borrarCliente(id_cliente):
    resp = eliminarCliente(id_cliente)
    if resp:
        flash('El Cliente fue eliminado correctamente', 'success')
        return redirect(url_for('lista_clientes'))

# rutas proveedor ---------------------------------------------------------
@app.route('/registrar-proveedor', methods=['GET'])
def viewFormProveedor():
    if 'conectado' in session:
        return render_template(f'{PATH_URLP}/form_proveedor.html')
    else:
        flash('primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))

@app.route('/form-registrar-proveedor', methods=['POST'])
def formProveedor():
    if 'conectado' in session:
            resultado = procesar_form_proveedor(request.form)
            if resultado:
                return redirect(url_for('lista_proveedores'))
            else:
                flash('El proveedor NO fue registrado.', 'error')
                return render_template(f'{PATH_URLP}/form_proveedores.html')
    else:
        flash('primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))
    
@app.route('/lista-de-proveedores', methods=['GET'])
def lista_proveedores():
    if 'conectado' in session:
        return render_template(f'{PATH_URLP}/lista_proveedores.html', proveedores=sql_lista_proveedoresBD())
    else:
        flash('primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))
    
@app.route("/detalles-proveedor/", methods=['GET'])
@app.route("/detalles-proveedor/<int:idProveedor>", methods=['GET'])
def detalleProveedor(idProveedor=None):
    if 'conectado' in session:
        # Verificamos si el parámetro idProveedor es None o no está presente en la URL
        if idProveedor is None:
            return redirect(url_for('inicio'))
        else:
            detalle_proveedor = sql_detalles_proveedoresBD(idProveedor) or []
            return render_template(f'{PATH_URLP}/detalles_proveedor.html', detalle_proveedor=detalle_proveedor)
    else:
        flash('Primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))

# Buscadon de proveedor
@app.route("/buscando-proveedor", methods=['POST'])
def viewBuscarProveedorBD():
    resultadoBusqueda = buscarProveedorBD(request.json['busqueda'])
    if resultadoBusqueda:
        return render_template(f'{PATH_URLP}/resultado_busqueda_proveedor.html', dataBusqueda=resultadoBusqueda)
    else:
        return jsonify({'fin': 0})


@app.route("/editar-proveedor/<int:id>", methods=['GET'])
def viewEditarProveedor(id):
    if 'conectado' in session:
        respuestaProveedor = buscarProveedorUnico(id)
        if respuestaProveedor:
            return render_template(f'{PATH_URLP}/form_proveedor_update.html', respuestaProveedor=respuestaProveedor)
        else:
            flash('El proveedor no existe.', 'error')
            return redirect(url_for('inicio'))
    else:
        flash('Primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))

# Recibir formulario para actulizar informacion de proveedor
@app.route('/actualizar-proveedor', methods=['POST'])
def actualizarProveedor():
    resultData = procesar_actualizacion_formProveedor(request)
    if resultData:
        return redirect(url_for('lista_proveedores'))

@app.route('/borrar-proveedor/<string:id_proveedor>', methods=['GET'])
def borrarProveedor(id_proveedor):
    resp = eliminarProveedor(id_proveedor)
    if resp:
        flash('El Proveedor fue eliminado correctamente', 'success')
        return redirect(url_for('lista_proveedores'))

# rutas empleado ----------------------------------------------------------------------
@app.route('/registrar-empleado', methods=['GET'])
def viewFormEmpleado():
    if 'conectado' in session:
        return render_template(f'{PATH_URL}/form_empleado.html')
    else:
        flash('primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))


@app.route('/form-registrar-empleado', methods=['POST'])
def formEmpleado():
    if 'conectado' in session:
        if 'foto_empleado' in request.files:
            foto_perfil = request.files['foto_empleado']
            resultado = procesar_form_empleado(request.form, foto_perfil)
            if resultado:
                return redirect(url_for('lista_empleados'))
            else:
                flash('El empleado NO fue registrado.', 'error')
                return render_template(f'{PATH_URL}/form_empleado.html')
    else:
        flash('primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))


@app.route('/lista-de-empleados', methods=['GET'])
def lista_empleados():
    if 'conectado' in session:
        return render_template(f'{PATH_URL}/lista_empleados.html', empleados=sql_lista_empleadosBD())
    else:
        flash('primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))


@app.route("/detalles-empleado/", methods=['GET'])
@app.route("/detalles-empleado/<int:idEmpleado>", methods=['GET'])
def detalleEmpleado(idEmpleado=None):
    if 'conectado' in session:
        # Verificamos si el parámetro idEmpleado es None o no está presente en la URL
        if idEmpleado is None:
            return redirect(url_for('inicio'))
        else:
            detalle_empleado = sql_detalles_empleadosBD(idEmpleado) or []
            return render_template(f'{PATH_URL}/detalles_empleado.html', detalle_empleado=detalle_empleado)
    else:
        flash('Primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))


# Buscadon de empleados
@app.route("/buscando-empleado", methods=['POST'])
def viewBuscarEmpleadoBD():
    resultadoBusqueda = buscarEmpleadoBD(request.json['busqueda'])
    if resultadoBusqueda:
        return render_template(f'{PATH_URL}/resultado_busqueda_empleado.html', dataBusqueda=resultadoBusqueda)
    else:
        return jsonify({'fin': 0})


@app.route("/editar-empleado/<int:id>", methods=['GET'])
def viewEditarEmpleado(id):
    if 'conectado' in session:
        respuestaEmpleado = buscarEmpleadoUnico(id)
        if respuestaEmpleado:
            return render_template(f'{PATH_URL}/form_empleado_update.html', respuestaEmpleado=respuestaEmpleado)
        else:
            flash('El empleado no existe.', 'error')
            return redirect(url_for('inicio'))
    else:
        flash('Primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))


# Recibir formulario para actulizar informacion de empleado
@app.route('/actualizar-empleado', methods=['POST'])
def actualizarEmpleado():
    resultData = procesar_actualizacion_form(request)
    if resultData:
        return redirect(url_for('lista_empleados'))

#LISTA USUARIOS---------------------------------------
@app.route("/lista-de-usuarios", methods=['GET'])
def usuarios():
    if 'conectado' in session:
        resp_usuariosBD = lista_usuariosBD()
        return render_template('public/usuarios/lista_usuarios.html', resp_usuariosBD=resp_usuariosBD)
    else:
        return redirect(url_for('inicioCpanel'))

#ELIMINAR USUARIO-------------------------------------------
@app.route('/borrar-usuario/<string:id>', methods=['GET'])
def borrarUsuario(id):
    resp = eliminarUsuario(id)
    if resp:
        flash('El Usuario fue eliminado correctamente', 'success')
        return redirect(url_for('usuarios'))

#ELIMINAR EMPLEADO------------------------------------------
@app.route('/borrar-empleado/<string:id_empleado>/<string:foto_empleado>', methods=['GET'])
def borrarEmpleado(id_empleado, foto_empleado):
    resp = eliminarEmpleado(id_empleado, foto_empleado)
    if resp:
        flash('El Empleado fue eliminado correctamente', 'success')
        return redirect(url_for('lista_empleados'))

#INFORME--------------------------------------------------------
@app.route("/descargar-informe-empleados/", methods=['GET'])
def reporteBD():
    if 'conectado' in session:
        return generarReporteExcel()
    else:
        flash('primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))

#rutas producto----------------------------------------------

@app.route('/registrar-producto', methods=['GET'])
def viewFormProducto():
    if 'conectado' in session:
        return render_template(f'{PATH_URLPR}/form_producto.html')
    else:
        flash('primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))

@app.route('/form-registrar-producto', methods=['POST'])
def formProducto():
    if 'conectado' in session:
            resultado = procesar_form_producto(request.form)
            if resultado:
                return redirect(url_for('lista_productos'))
            else:
                flash('El producto NO fue registrado.', 'error')
                return render_template(f'{PATH_URLPR}/form_producto.html')
    else:
        flash('primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))
    
@app.route('/lista-de-productos', methods=['GET'])
def lista_productos():
    if 'conectado' in session:
        return render_template(f'{PATH_URLPR}/lista_productos.html', productos=sql_lista_productosBD())
    else:
        flash('primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))
    
@app.route("/detalles-producto/", methods=['GET'])
@app.route("/detalles-producto/<int:idProducto>", methods=['GET'])
def detalleProducto(idProducto=None):
    if 'conectado' in session:
        # Verificamos si el parámetro idProducto es None o no está presente en la URL
        if idProducto is None:
            return redirect(url_for('inicio'))
        else:
            detalle_producto = sql_detalles_productosBD(idProducto) or []
            return render_template(f'{PATH_URLPR}/detalles_producto.html', detalle_producto=detalle_producto)
    else:
        flash('Primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))

# Buscadon de productos
@app.route("/buscando-producto", methods=['POST'])
def viewBuscarProductoBD():
    resultadoBusqueda = buscarProductoBD(request.json['busqueda'])
    if resultadoBusqueda:
        return render_template(f'{PATH_URLPR}/resultado_busqueda_producto.html', dataBusqueda=resultadoBusqueda)
    else:
        return jsonify({'fin': 0})


@app.route("/editar-producto/<int:id>", methods=['GET'])
def viewEditarProducto(id):
    if 'conectado' in session:
        respuestaProducto = buscarProductoUnico(id)
        if respuestaProducto:
            return render_template(f'{PATH_URLPR}/form_producto_update.html', respuestaProducto=respuestaProducto)
        else:
            flash('El producto no existe.', 'error')
            return redirect(url_for('inicio'))
    else:
        flash('Primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))

# Recibir formulario para actulizar informacion de producto
@app.route('/actualizar-producto', methods=['POST'])
def actualizarProducto():
    resultData = procesar_actualizacion_formProducto(request)
    if resultData:
        return redirect(url_for('lista_productos'))

@app.route('/borrar-producto/<string:id_producto>', methods=['GET'])
def borrarProducto(id_producto):
    resp = eliminarProducto(id_producto)
    if resp:
        flash('El Producto fue eliminado correctamente', 'success')
        return redirect(url_for('lista_productos'))
