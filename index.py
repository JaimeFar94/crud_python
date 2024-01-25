from flask import Flask, render_template, request, redirect, url_for, session, flash
from flaskext.mysql import MySQL
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_bcrypt import Bcrypt
from functools import wraps
from werkzeug.utils import secure_filename
import os
import uuid

app = Flask(__name__, static_folder='static', template_folder='templates')


app = Flask(__name__)  #se crea la variable para crear las rutas del servidor 
app.secret_key = '137-372-314'

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''  # Puede omitirse esta parte si no tiene contraseña
app.config['MYSQL_DATABASE_DB'] = 'medico'
mysql.init_app(app)

@app.route('/Logeo', methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        _usuario = request.form.get('usuario')
        _contrasena = request.form.get('contrasena')

        sql = "SELECT usuario, contraseña FROM login WHERE usuario = %s AND contraseña = %s"
        info = (_usuario, _contrasena)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, info)
        result = cursor.fetchone()  # Obtener la primera fila de resultados

        if result:
            # Las credenciales son válidas, inicia sesión y redirige al usuario
            session['usuario'] = _usuario
            session['user_authenticated'] = True
            return redirect(url_for('index'))
        else:
            # Las credenciales no son válidas, muestra un mensaje de error
            flash('Usuario o contraseña incorrectos', 'danger')
            return render_template('Logeo.html')

    return render_template('Logeo.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method =='POST':
        _nombre = request.form.get('nombre')
        _correo = request.form.get('correo')
        _clinica = request.form.get('clinica')
        _usuario =  request.form.get('usuario')
        _contraseña= request.form.get('contrasena')
    
        sql = "INSERT INTO login (nombre, Correo, Clinica, usuario, contraseña)  VALUES (%s, %s, %s, %s, %s)"
        info = (_nombre, _correo, _clinica, _usuario, _contraseña )
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, info)
        conn.commit()
        
        flash('Usuario registrado correctamente', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

def get_user_authenticated(): #se crea la funcion para la autenticación 
    user_authenticated = False
    if 'user_authenticated' in session:
        user_authenticated = session['user_authenticated']
    return user_authenticated

def login_required(f): #se define la funcion indicando que si el usuario no se encuentra autenticado este 
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session or not session['usuario']:
            user_authenticated = get_user_authenticated()
            if not user_authenticated:
                return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    user_authenticated = True
    if 'user_authenticated' in session:
        user_authenticated = session['user_authenticated']
    return render_template('home.html', user_authenticated=user_authenticated)


@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    user_authenticated = True
    paciente = None
    ruta_foto = None
    if request.method == 'POST':  
        _documento = request.form.get('txtDocumento')
        _tipo = request.form.get('tipo_documento')
        _nombre = request.form.get('Nombre')
        _edad = request.form.get('Edad')
        _genero = request.form.get('genero')
        _correo_electronico = request.form.get('email')
        _direccion = request.form.get('direccion')
        _telefono = request.form.get('telefono')
        _eps = request.form.get('eps')
        _cargo = request.form.get('cargo')
        _acompanante = request.form.get('acompanante')
        _parentesco = request.form.get('parentesco')
        _telefono_acompanante = request.form.get('telefono_acompanante')
        _motivo_consulta = request.form.get('motivo_consulta')
        _ultima_revision = request.form.get('ultima_revision')
        paciente_documento = _documento
        _diabetes = request.form['dia']
        _hipertension = request.form['hiper']
        _artritis = request.form['artr']
        _alergia = request.form['aler']
        _catarata = request.form['cata']
        _glaucoma = request.form['glau']
        _estrabismo = request.form['estra']
        _queratocono = request.form['quera']
        _otros = request.form['otros']
        _diabetes1 = request.form['diabetes']
        _hipertension1 = request.form['hipertension']
        _artritis1 = request.form['artritis']
        _alergia1 = request.form['alergia']
        _ulcera1 = request.form['ulcera']
        _cirugia = request.form['cirugia']
        _lentes = request.form['lentes']
        _otros1 = request.form['otros_1']
        _descripcion = request.form['descripcion']
        _mov_consulta = request.form['mov_consulta']
        _ulti_consulta = request.form['ulti_consulta']
        _esfera = request.form['esfera']
        _cilindro = request.form['cilindro']
        _eje = request.form['eje']
        _dp = request.form['dp']
        _vl20 = request.form['vl20']
        _vp20 = request.form['vp20']
        _add = request.form['add_0']
        _esfera_1 = request.form['esfera_1']
        _cilindro_1 = request.form['cilindro_1']
        _eje_1 = request.form['eje_1']
        _dp_1 = request.form['dp_1']
        _vl20_1 = request.form['vl20_1']
        _vp20_1 = request.form['vp20_1']
        _add_1 = request.form['add_1']
        _tipo_lente = request.form['tipo_lente']
        _montura = request.form['montura']
        _material = request.form['material']
        _filtro = request.form['filtro']
        _color = request.form['color']
        _observacion = request.form['obs']
        _vista_l = request.form['vision_lejos']
        _vista_p = request.form['vision_proxima']
        _ducciones_od = request.form['ducciones_od']
        _ducciones_oi = request.form['ducciones_oi']
        _ppc_od = request.form['ppc_od']
        _ppc_oi = request.form['ppc_oi']
        _ojo_dere = request.form['ojo_derecho']
        _ojo_izqui = request.form['ojo_izquierdo']
        _ojo_quera = request.form['ojo_dere']  
        _ojo_quera_1 = request.form['ojo_izqui'] 
        _ojo_refac = request.form['ojo_derch']  
        _ojo_refac_1 = request.form['ojo_izquier'] 
        _esfera_retino = request.form['esfera']
        _cilindro_retino = request.form['cilindro']
        _eje_retino = request.form['eje']
        _dp_retino = request.form['dp']
        _vl20_retino = request.form['vl20']
        _vp20_retino = request.form['vp20']
        _add_retino = request.form['add']
        _esfera_retino_1 = request.form['esfera_1']
        _cilindro_retino_1 = request.form['cilindro_1']
        _eje_retino_1 = request.form['eje_1']
        _dp_retino_1 = request.form['dp_1']
        _vl20_retino_1 = request.form['vl20_1']
        _vp20_retino_1 = request.form['vp20_1']
        _add_retino_1 = request.form['add_1']

       
        sql = "INSERT INTO pacientes (documento, tipo, nombre, edad, genero, correo_electronico, direccion, telefono, eps, cargo, acompanante, parentesco, telefono_acompanante, motivo_consulta, ultima_revision) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (_documento, _tipo, _nombre, _edad, _genero, _correo_electronico, _direccion, _telefono, _eps, _cargo, _acompanante, _parentesco, _telefono_acompanante, _motivo_consulta, _ultima_revision)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, datos)
        conn.commit()
        
        cursor.execute("SELECT documento FROM pacientes WHERE documento = %s", (_documento,))
        paciente_documento = cursor.fetchone()[0]
     
        conn.close()

 
        
        sql_antecedentes = """
        INSERT INTO antecedentes (
            diabetes, hipertension, artritis, alergia, catarata, glaucoma, estrabismo, queratocono, otros,
            diabetes_per, hipertension_per, Artritis_per, Alergia_per, ulcera_per, cirugia_per, lentes_contacto_per, otros1, descripcion, paciente_documento
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        datos_antecedentes = (
            _diabetes, _hipertension, _artritis, _alergia, _catarata,
            _glaucoma, _estrabismo, _queratocono, _otros,
            _diabetes1, _hipertension1, _artritis1, _alergia1, _ulcera1, _cirugia, _lentes, _otros1, _descripcion,paciente_documento
        )
        
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql_antecedentes, datos_antecedentes)
        conn.commit()
        cursor.close()
        conn.close()

        sql_mov_consulta = """
        INSERT INTO mov_consulta (
            mov_consulta, ulti_consulta, esfera, cilindro, eje, dp, vl20, vp20, add_0,
            esfera_1, cilindro_1, eje_1, dp_1, vl20_1, vp20_1, add_1, tipo_lente, montura, material, filtro, color, observacion, paciente_documento
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
        """
        datos_mov_consulta = (
            _mov_consulta, _ulti_consulta, _esfera, _cilindro, _eje, _dp, _vl20, _vp20, _add,
            _esfera_1, _cilindro_1, _eje_1, _dp_1, _vl20_1, _vp20_1, _add_1, _tipo_lente, _montura, _material, _filtro, _color, _observacion,paciente_documento)
        
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql_mov_consulta, datos_mov_consulta)
        conn.commit()
        cursor.close()
        conn.close()

        sql_vista = """
        INSERT INTO vista (
            vision_lejana, vision_proxima, duccion_od, duccion_oi, ppc_od, ppc_oi, ojo_derecho, ojo_izquierdo, 
            ojo_drc_querato, ojo_izq_querato, ojo_drc_refac, ojo_izq_refac, esfera_retino, cilindro_retino, 
            eje_retino, dp_retino, vl20_retino, vp20_retino, add_retino, esfera_retino_1, cilindro_retino_1, 
            eje_retino_1, dp_retino_1, vl20_retino_1, vp20_retino_1, add_retino_1, paciente_documento
        ) VALUES (
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
        )
        """
        datos_vista = (
            _vista_l, _vista_p, _ducciones_od, _ducciones_oi, _ppc_od, _ppc_oi, _ojo_dere, _ojo_izqui, 
            _ojo_quera, _ojo_quera_1, _ojo_refac, _ojo_refac_1, _esfera_retino, _cilindro_retino, 
            _eje_retino, _dp_retino, _vl20_retino, _vp20_retino, _add_retino, _esfera_retino_1, 
            _cilindro_retino_1, _eje_retino_1, _dp_retino_1, _vl20_retino_1, _vp20_retino_1, _add_retino_1,paciente_documento
        )


        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql_vista, datos_vista)
        conn.commit()
        cursor.close()
        conn.close()


    return render_template('index.html', user_authenticated=user_authenticated, paciente=paciente,ruta_foto=ruta_foto)

@login_required
def obtener_informacion_paciente(documento):
    
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = "SELECT * FROM pacientes WHERE documento = %s"
    cursor.execute(sql, (documento,))
    paciente = cursor.fetchone()

    conn.close()
    return paciente

@app.route('/consulta', methods=['GET','POST'])
@login_required
def consulta():
    user_authenticated = True
    sql = """
SELECT * FROM pacientes p LEFT JOIN antecedentes a ON a.paciente_documento = p.documento LEFT JOIN mov_consulta mc ON mc.paciente_documento = p.documento LEFT JOIN vista v ON v.paciente_documento = p.documento;
    """
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    pacientes = cursor.fetchall()
    conn.commit()

    return render_template('consulta.html', pacientes= pacientes, user_authenticated=user_authenticated)


    

@app.route('/editar/<int:id>')
@login_required
def editar(id):
    user_authenticated = True
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("""
SELECT * FROM pacientes p LEFT JOIN antecedentes a ON a.paciente_documento = p.documento LEFT JOIN mov_consulta mc ON mc.paciente_documento = p.documento LEFT JOIN vista v ON v.paciente_documento = p.documento;
    """)

    pacientes = cursor.fetchall()
    conn.commit()
        
    return render_template('/editar.html', pacientes= pacientes, user_authenticated=user_authenticated)

@app.route('/actualizar', methods=['POST'])
@login_required
def actualizar():
    _documento = request.form.get('txtDocumento')
    _tipo = request.form.get('tipo_documento')
    _nombre = request.form.get('Nombre')
    _edad = request.form.get('Edad')
    _genero = request.form.get('genero')
    _correo_electronico = request.form.get('email')
    _direccion = request.form.get('direccion')
    _telefono = request.form.get('telefono')
    _eps = request.form.get('eps')
    _cargo = request.form.get('cargo')
    _acompanante = request.form.get('acompanante')
    _parentesco = request.form.get('parentesco')
    _telefono_acompanante = request.form.get('telefono_acompanante')
    _motivo_consulta = request.form.get('motivo_consulta')
    _ultima_revision = request.form.get('ultima_revision')
    paciente_documento = _documento
    _diabetes = request.form['dia']
    _hipertension = request.form['hiper']
    _artritis = request.form['artr']
    _alergia = request.form['aler']
    _catarata = request.form['cata']
    _glaucoma = request.form['glau']
    _estrabismo = request.form['estra']
    _queratocono = request.form['quera']
    _otros = request.form['otros']
    _diabetes1 = request.form['diabetes']
    _hipertension1 = request.form['hipertension']
    _artritis1 = request.form['artritis']
    _alergia1 = request.form['alergia']
    _ulcera1 = request.form['ulcera']
    _cirugia = request.form['cirugia']
    _lentes = request.form['lentes']
    _otros1 = request.form['otros_1']
    _descripcion = request.form['descripcion']
    _mov_consulta = request.form['mov_consulta']
    _ulti_consulta = request.form['ulti_consulta']
    _esfera = request.form['esfera']
    _cilindro = request.form['cilindro']
    _eje = request.form['eje']
    _dp = request.form['dp']
    _vl20 = request.form['vl20']
    _vp20 = request.form['vp20']
    _add = request.form['add_0']
    _esfera_1 = request.form['esfera_1']
    _cilindro_1 = request.form['cilindro_1']
    _eje_1 = request.form['eje_1']
    _dp_1 = request.form['dp_1']
    _vl20_1 = request.form['vl20_1']
    _vp20_1 = request.form['vp20_1']
    _add_1 = request.form['add_1']
    _tipo_lente = request.form['tipo_lente']
    _montura = request.form['montura']
    _material = request.form['material']
    _filtro = request.form['filtro']
    _color = request.form['color']
    _observacion = request.form['obs']
    _vista_l = request.form['vision_lejos']
    _vista_p = request.form['vision_proxima']
    _ducciones_od = request.form['ducciones_od']
    _ducciones_oi = request.form['ducciones_oi']
    _ppc_od = request.form['ppc_od']
    _ppc_oi = request.form['ppc_oi']
    _ojo_dere = request.form['ojo_derecho']
    _ojo_izqui = request.form['ojo_izquierdo']
    _ojo_quera = request.form['ojo_dere']  
    _ojo_quera_1 = request.form['ojo_izqui'] 
    _ojo_refac = request.form['ojo_derch']  
    _ojo_refac_1 = request.form['ojo_izquier'] 
    _esfera_retino = request.form['esfera']
    _cilindro_retino = request.form['cilindro']
    _eje_retino = request.form['eje']
    _dp_retino = request.form['dp']
    _vl20_retino = request.form['vl20']
    _vp20_retino = request.form['vp20']
    _add_retino = request.form['add']
    _esfera_retino_1 = request.form['esfera_1']
    _cilindro_retino_1 = request.form['cilindro_1']
    _eje_retino_1 = request.form['eje_1']
    _dp_retino_1 = request.form['dp_1']
    _vl20_retino_1 = request.form['vl20_1']
    _vp20_retino_1 = request.form['vp20_1']
    _add_retino_1 = request.form['add_1']

    user_authenticated = True

    sql = """
        UPDATE pacientes 
        SET tipo = %s, documento =%s, nombre = %s, edad = %s, genero = %s, correo_electronico = %s, direccion = %s, 
            telefono = %s, eps = %s, cargo = %s, acompanante = %s, parentesco = %s, 
            telefono_acompanante = %s, motivo_consulta = %s, ultima_revision = %s
        WHERE documento = %s
    """
    datos = (
        _tipo,_documento, _nombre, _edad, _genero, _correo_electronico, _direccion, _telefono, _eps, 
        _cargo, _acompanante, _parentesco, _telefono_acompanante, _motivo_consulta, 
        _ultima_revision, _documento
    )
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()

     
    conn.close()
        # Actualización de la tabla 'antecedentes'
    sql_antecedentes = """
            UPDATE antecedentes 
            SET diabetes = %s, hipertension = %s, artritis = %s, alergia = %s, catarata = %s, 
                glaucoma = %s, estrabismo = %s, queratocono = %s, otros = %s, 
                diabetes_per = %s, hipertension_per = %s, Artritis_per = %s, Alergia_per = %s, 
                ulcera_per = %s, cirugia_per = %s, lentes_contacto_per = %s, otros1 = %s, descripcion = %s 
            WHERE paciente_documento = %s
        """
    datos_antecedentes = (
            _diabetes, _hipertension, _artritis, _alergia, _catarata,
            _glaucoma, _estrabismo, _queratocono, _otros,
            _diabetes1, _hipertension1, _artritis1, _alergia1, _ulcera1, _cirugia, _lentes, _otros1, _descripcion, paciente_documento
        )
            
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql_antecedentes, datos_antecedentes)
    conn.commit()
    cursor.close()
    conn.close()

        # Actualización de la tabla 'mov_consulta'
    sql_mov_consulta = """
            UPDATE mov_consulta 
            SET mov_consulta = %s, ulti_consulta = %s, esfera = %s, cilindro = %s, eje = %s, 
                dp = %s, vl20 = %s, vp20 = %s, add_0 = %s, esfera_1 = %s, cilindro_1 = %s, 
                eje_1 = %s, dp_1 = %s, vl20_1 = %s, vp20_1 = %s, add_1 = %s, tipo_lente = %s, 
                montura = %s, material = %s, filtro = %s, color = %s, observacion = %s 
            WHERE paciente_documento = %s
        """
    datos_mov_consulta = (
            _mov_consulta, _ulti_consulta, _esfera, _cilindro, _eje, _dp, _vl20, _vp20, _add,
            _esfera_1, _cilindro_1, _eje_1, _dp_1, _vl20_1, _vp20_1, _add_1, _tipo_lente, 
            _montura, _material, _filtro, _color, _observacion, paciente_documento
        )
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql_mov_consulta, datos_mov_consulta)
    conn.commit()
    cursor.close()
    conn.close()

        # Actualización de la tabla 'vista'
    sql_vista = """
            UPDATE vista 
            SET vision_lejana = %s, vision_proxima = %s, duccion_od = %s, duccion_oi = %s, 
                ppc_od = %s, ppc_oi = %s, ojo_derecho = %s, ojo_izquierdo = %s, 
                ojo_drc_querato = %s, ojo_izq_querato = %s, ojo_drc_refac = %s, ojo_izq_refac = %s, 
                esfera_retino = %s, cilindro_retino = %s, eje_retino = %s, dp_retino = %s, 
                vl20_retino = %s, vp20_retino = %s, add_retino = %s, esfera_retino_1 = %s, 
                cilindro_retino_1 = %s, eje_retino_1 = %s, dp_retino_1 = %s, vl20_retino_1 = %s, 
                vp20_retino_1 = %s, add_retino_1 = %s 
            WHERE paciente_documento = %s
        """
    datos_vista = (
            _vista_l, _vista_p, _ducciones_od, _ducciones_oi, _ppc_od, _ppc_oi, _ojo_dere, _ojo_izqui,
            _ojo_quera, _ojo_quera_1, _ojo_refac, _ojo_refac_1, _esfera_retino, _cilindro_retino,
            _eje_retino, _dp_retino, _vl20_retino, _vp20_retino, _add_retino, _esfera_retino_1,
            _cilindro_retino_1, _eje_retino_1, _dp_retino_1, _vl20_retino_1, _vp20_retino_1, _add_retino_1, paciente_documento
        )
    
    print(request.form)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql_vista, datos_vista)
    conn.commit()
    cursor.close()
    conn.close()  

    return render_template('/consulta.html',  user_authenticated=user_authenticated)
        
@app.route('/eliminar/<int:id>', methods=['GET', 'POST'])
@login_required
def eliminar(id):
        conn = mysql.connect()
        cursor = conn.cursor()

        # Eliminar de la tabla 'antecedentes'
        cursor.execute("DELETE FROM antecedentes WHERE paciente_documento=%s", (id))
        conn.commit()

        # Eliminar de la tabla 'mov_consulta'
        cursor.execute("DELETE FROM mov_consulta WHERE paciente_documento=%s", (id))
        conn.commit()

        # Eliminar de la tabla 'vista'
        cursor.execute("DELETE FROM vista WHERE paciente_documento=%s", (id))
        conn.commit()

        # Finalmente, eliminar de la tabla 'pacientes'
        cursor.execute("DELETE FROM pacientes WHERE documento=%s", (id))
        conn.commit()

        # Redirigir a la página de consulta después de la eliminación
        return redirect(url_for('consulta'))



@app.route('/formulario')
@login_required
def create():
    user_authenticated = True
    return render_template('formulario.html',user_authenticated=user_authenticated)

@app.route('/logout')
@login_required
def logout():
    session['user_authenticated'] = False
    session.pop('usuario', None)
    return redirect(url_for('login')) 

if __name__ =='__main__': #Se tiene un condicional para verificar que si se esta en el archivo de ejecución y no un modulo
    app.run(debug=True) #se pone un debug con un booleano para que se recarge la pagina 