import pymysql


def crearUsuarios(): 
    connection = pymysql.connect(
            host = "localhost",
            user =  "root",
            password =  "123456",
            db =  "isynerg"
        )
    cursor = connection.cursor()

    sql = "DROP TABLE actividades_maquina, actividades_usuario, semana_operaciones_maquina, session, usuarios,maquina;"

    
    actividades_maquina = """
        CREATE TABLE actividades_maquina (
        id int(11) NOT NULL,
        maquina_id int(11) NOT NULL,
        azul int(11) DEFAULT NULL,
        created_at timestamp NULL DEFAULT current_timestamp(),
        updated_at timestamp NULL DEFAULT current_timestamp()
        );
    """
    sql_actividades_usuario = """
        CREATE TABLE actividades_usuario (
        id int(11) NOT NULL,
        usuario_id int(11) NOT NULL,
        verde int(11) DEFAULT NULL,
        amarillo int(11) DEFAULT NULL,
        morado int(11) DEFAULT NULL,
        rojo int(11) DEFAULT NULL,
        produccion_real int(11) DEFAULT NULL,
        piezas_malas int(11) DEFAULT NULL,
        created_at timestamp NULL DEFAULT current_timestamp(),
        updated_at timestamp NULL DEFAULT current_timestamp(),
        maquina_id int(11) DEFAULT NULL
        );
    """
    sql_maquina = """
        CREATE TABLE maquina (
        id int(11) NOT NULL,
        maquina_mid int(11) DEFAULT NULL,
        created_at timestamp NULL DEFAULT current_timestamp(),
        updated_at timestamp NULL DEFAULT current_timestamp()
        );
    """
    sql_semana_operaciones_maquina =  """
        CREATE TABLE semana_operaciones_maquina (
        id int(11) NOT NULL,
        maquina_id int(11) NOT NULL,
        lunes int(11) DEFAULT NULL,
        martes int(11) DEFAULT NULL,
        miercoles int(11) DEFAULT NULL,
        jueves int(11) DEFAULT NULL,
        viernes int(11) DEFAULT NULL,
        sabado int(11) DEFAULT NULL,
        domingo int(11) DEFAULT NULL,
        created_at timestamp NULL DEFAULT current_timestamp(),
        updated_at timestamp NULL DEFAULT current_timestamp()
        );
    """
    sql_session = """
        CREATE TABLE session (
        id int(11) NOT NULL,
        usuario_id int(11) NOT NULL,
        fecha timestamp NULL DEFAULT current_timestamp(),
        created_at timestamp NULL DEFAULT current_timestamp(),
        updated_at timestamp NULL DEFAULT current_timestamp()
        );
    """

    sql_usuarios= """
        CREATE TABLE usuarios (
        id int(11) NOT NULL,
        nombre varchar(50) DEFAULT NULL,
        password varchar(50) DEFAULT NULL,
        dni varchar(10) DEFAULT NULL,
        isAdmin tinyint(4) DEFAULT NULL,
        created_at timestamp NULL DEFAULT current_timestamp(),
        updated_at timestamp NULL DEFAULT current_timestamp(),
        cargo varchar(20) DEFAULT NULL
        );
    """

    sql_alter1= """
        ALTER TABLE actividades_maquina
        ADD PRIMARY KEY (id);

    """
    sql_alter2= """
        ALTER TABLE actividades_usuario
        ADD PRIMARY KEY (id);
    """
    sql_alter3= """
        ALTER TABLE maquina
        ADD PRIMARY KEY (id);
    """
    sql_alter4= """
        ALTER TABLE semana_operaciones_maquina
        ADD PRIMARY KEY (id);
    """
    sql_alter5= """

        ALTER TABLE session
        ADD PRIMARY KEY (id);
    """
    sql_alter6= """
        ALTER TABLE usuarios
        ADD PRIMARY KEY (id);
    """
    sql_alter7= """
        ALTER TABLE actividades_maquina
        MODIFY id int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=472;
    """

    sql_alter8= """
        ALTER TABLE actividades_usuario
        MODIFY id int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=481;
    """
    sql_alter9= """
        ALTER TABLE actividades_usuario
        MODIFY id int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=481;
    """
    sql_alter10= """
        ALTER TABLE semana_operaciones_maquina
        MODIFY id int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
    """
    sql_alter11= """

        ALTER TABLE session
        MODIFY id int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=413;
    """
    sql_alter11= """
        ALTER TABLE usuarios
        MODIFY id int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
    """

    sql_maquina_insert = """
        INSERT INTO maquina (id, maquina_mid, created_at, updated_at) VALUES
        (1, 1, '2022-08-04 16:53:26', '2022-08-04 16:53:26');
    """

    sql_semana_operaciones_maquina_insert = """
        INSERT INTO semana_operaciones_maquina (id, maquina_id, lunes, martes, miercoles, jueves, viernes, sabado, domingo, created_at, updated_at) VALUES
        (1, 1, 12, 12, 12, 12, 12, 12, 12, '2022-08-04 17:00:17', '2022-08-04 17:00:17');
    """

    sql_usuarios_insert = """
        INSERT INTO usuarios (id, nombre, password, dni, isAdmin, created_at, updated_at, cargo) VALUES
        (1, 'Mantenimiento', '123456', '2222', 1, '2022-07-26 15:16:39', '2022-07-26 15:16:39', 'MANTENIMIENTO'),
        (2, 'operario', '123456', '3333', NULL, '2022-08-24 23:12:33', '2022-08-24 23:12:33', 'OPERARIO'),
        (3, 'logistica', '123456', '4444', NULL, '2022-08-24 23:12:33', '2022-08-24 23:12:33', 'LOGISTICA'),
        (4, 'RRHH', '123456', '5555', NULL, '2022-08-24 23:12:58', '2022-08-24 23:12:58', 'RECURSOSHUMANOS');
    """

    try:
        cursor.execute(sql)
        cursor.execute(actividades_maquina)
        cursor.execute(sql_actividades_usuario)
        cursor.execute(sql_maquina)
        cursor.execute(sql_semana_operaciones_maquina)
        cursor.execute(sql_session)
        cursor.execute(sql_usuarios)

        cursor.execute(sql_alter1)
        cursor.execute(sql_alter2)
        cursor.execute(sql_alter3)
        cursor.execute(sql_alter4)
        cursor.execute(sql_alter5)
        cursor.execute(sql_alter6)
        cursor.execute(sql_alter7)
        cursor.execute(sql_alter8)
        cursor.execute(sql_alter9)
        cursor.execute(sql_alter10)
        cursor.execute(sql_alter11)

        cursor.execute(sql_maquina_insert)
        cursor.execute(sql_semana_operaciones_maquina_insert)
        cursor.execute(sql_usuarios_insert)

        connection.commit()
        print('Se creo bd corectamente :D')
    except Exception as e:
        print(e)
        print("F, solo dios puede areglar esto :'c")


crearUsuarios()