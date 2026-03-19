class Visitante:
    def __init__(self, cedula, nombre, motivo):
        self.cedula = cedula.strip()
        self.nombre = nombre.strip()
        self.motivo = motivo.strip()