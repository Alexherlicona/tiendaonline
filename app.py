from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "124"

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tienda'

mysql = MySQL(app)

# Rutas generales
@app.route('/')
def index():
    return render_template('index.html')

# Rutas para la tabla Productos
@app.route('/productos')
def productos():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM productos")
    data = cur.fetchall()
    column_names = [i[0] for i in cur.description]  # Obtener nombres de las columnas
    return render_template('manage.html', data=data, table="productos", column_names=column_names)


@app.route('/productos/add', methods=['POST'])
def add_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        cantidad = request.form['cantidad']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO productos (PROD_NOMBRE, PROD_DESCRIPCION, PROD_PRECIO, PROD_CANTIDAD) VALUES (%s, %s, %s, %s)", (nombre, descripcion, precio, cantidad))
        mysql.connection.commit()
        flash('Producto añadido con éxito!')
        return redirect(url_for('productos'))

@app.route('/productos/edit/<int:id>', methods=['GET', 'POST'])
def edit_producto(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM productos WHERE ID_PRODUCTO = %s", (id,))
    product = cur.fetchone()

    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        cantidad = request.form['cantidad']

        cur.execute("""
            UPDATE productos
            SET PROD_NOMBRE = %s,
                PROD_DESCRIPCION = %s,
                PROD_PRECIO = %s,
                PROD_CANTIDAD = %s
            WHERE ID_PRODUCTO = %s
        """, (nombre, descripcion, precio, cantidad, id))
        mysql.connection.commit()
        flash('Producto actualizado con éxito!')
        return redirect(url_for('productos'))

    return render_template('manage.html', row=product, table="productos")

@app.route('/productos/delete/<int:id>', methods=['POST', 'GET'])
def delete_producto(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM productos WHERE ID_PRODUCTO = %s', (id,))
    mysql.connection.commit()
    flash('Producto eliminado con éxito!')
    return redirect(url_for('productos'))

# Rutas para la tabla Categorías
@app.route('/categorias')
def categorias():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM categorias")
    data = cur.fetchall()
    column_names = [i[0] for i in cur.description]  # Obtener nombres de las columnas
    return render_template('manage.html', data=data, table="categorias", column_names=column_names)


@app.route('/categorias/add', methods=['POST'])
def add_categoria():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        producto_id = request.form['producto_id']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO categorias (CATE_NOMBRE, CATE_DESCRIPCION, PRODUCTOS_ID_PRODUCTO) VALUES (%s, %s, %s)", (nombre, descripcion, producto_id))
        mysql.connection.commit()
        flash('Categoría añadida con éxito!')
        return redirect(url_for('categorias'))

@app.route('/categorias/edit/<int:id>', methods=['GET', 'POST'])
def edit_categoria(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM categorias WHERE ID_CATEGORIAS = %s", (id,))
    categoria = cur.fetchone()

    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        producto_id = request.form['producto_id']

        cur.execute("""
            UPDATE categorias
            SET CATE_NOMBRE = %s,
                CATE_DESCRIPCION = %s,
                PRODUCTOS_ID_PRODUCTO = %s
            WHERE ID_CATEGORIAS = %s
        """, (nombre, descripcion, producto_id, id))
        mysql.connection.commit()
        flash('Categoría actualizada con éxito!')
        return redirect(url_for('categorias'))

    return render_template('manage.html', row=categoria, table="categorias")

@app.route('/categorias/delete/<int:id>', methods=['POST', 'GET'])
def delete_categoria(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM categorias WHERE ID_CATEGORIAS = %s', (id,))
    mysql.connection.commit()
    flash('Categoría eliminada con éxito!')
    return redirect(url_for('categorias'))

# Repite el mismo patrón de código para las demás tablas (Proveedores, Compras, Detalles de Compra, Clientes, Pedidos, Detalles de Pedido)
# Ejemplo para la tabla Proveedores:

@app.route('/proveedores')
def proveedores():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM proveedores")
    data = cur.fetchall()
    column_names = [i[0] for i in cur.description]  # Obtener nombres de las columnas
    return render_template('manage.html', data=data, table="proveedores", column_names=column_names)

@app.route('/proveedores/add', methods=['POST'])
def add_proveedor():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contacto = request.form['contacto']
        telefono = request.form['telefono']
        direccion = request.form['direccion']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO proveedores (PROVE_NOMBRE, PROVE_CONTACTO, PROVE_TELEFONO, PROVE_DIRECCION) VALUES (%s, %s, %s, %s)", (nombre, contacto, telefono, direccion))
        mysql.connection.commit()
        flash('Proveedor añadido con éxito!')
        return redirect(url_for('proveedores'))

@app.route('/proveedores/edit/<int:id>', methods=['GET', 'POST'])
def edit_proveedor(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM proveedores WHERE ID_PROVEEDOR = %s", (id,))
    proveedor = cur.fetchone()

    if request.method == 'POST':
        nombre = request.form['nombre']
        contacto = request.form['contacto']
        telefono = request.form['telefono']
        direccion = request.form['direccion']

        cur.execute("""
            UPDATE proveedores
            SET PROVE_NOMBRE = %s,
                PROVE_CONTACTO = %s,
                PROVE_TELEFONO = %s,
                PROVE_DIRECCION = %s
            WHERE ID_PROVEEDOR = %s
        """, (nombre, contacto, telefono, direccion, id))
        mysql.connection.commit()
        flash('Proveedor actualizado con éxito!')
        return redirect(url_for('proveedores'))

    return render_template('manage.html', row=proveedor, table="proveedores")

@app.route('/proveedores/delete/<int:id>', methods=['POST', 'GET'])
def delete_proveedor(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM proveedores WHERE ID_PROVEEDOR = %s', (id,))
    mysql.connection.commit()
    flash('Proveedor eliminado con éxito!')
    return redirect(url_for('proveedores'))

if __name__ == '__main__':
    app.run(debug=True)
