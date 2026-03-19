from app import autenticar_usuario
import time

# CP-01 Login exitoso
def test_login_exitoso():
    r = autenticar_usuario("admin", "1234")
    assert r["success"] == True
    assert r["message"] == "Acceso concedido"

# CP-02 Usuario vacío
def test_usuario_vacio():
    r = autenticar_usuario("", "1234")
    assert r["success"] == False
    assert "requeridos" in r["message"]

# CP-03 Contraseña vacía
def test_password_vacio():
    r = autenticar_usuario("admin", "")
    assert r["success"] == False

# CP-04 Usuario inexistente
def test_usuario_inexistente():
    r = autenticar_usuario("pedro", "1234")
    assert r["success"] == False
    assert r["message"] == "Usuario no existe"

# CP-05 Contraseña incorrecta
def test_password_incorrecto():
    r = autenticar_usuario("admin", "9999")
    assert r["success"] == False
    assert r["message"] == "Contraseña incorrecta"

# CP-06 Tiempo de respuesta
def test_tiempo_respuesta():
    r = autenticar_usuario("admin", "1234")
    assert r["response_time_ms"] > 0

# CP-07 Estructura de salida
def test_estructura():
    r = autenticar_usuario("admin", "1234")
    assert "success" in r
    assert "message" in r
    assert "response_time_ms" in r
    



# Exploratoria 1
def test_ambos_vacios():
    r = autenticar_usuario("", "")
    assert r["success"] == False

# Exploratoria 2
def test_usuario_mayuscula():
    r = autenticar_usuario("ADMIN", "1234")
    assert r["success"] == False

# Exploratoria 3
def test_usuario_con_espacios():
    r = autenticar_usuario(" admin ", "1234")
    assert r["success"] == False

# Exploratoria 4
def test_usuario_especial():
    r = autenticar_usuario("admin@", "1234")
    assert r["success"] == False

# Exploratoria 5
def test_password_especial():
    r = autenticar_usuario("admin", "!!!")
    assert r["success"] == False

    import time

def test_tiempo_real():
    inicio = time.perf_counter()

    r = autenticar_usuario("admin", "1234")

    fin = time.perf_counter()
    tiempo = (fin - inicio) * 1000  # convertir a milisegundos

    assert r["success"] == True
    assert tiempo < 500