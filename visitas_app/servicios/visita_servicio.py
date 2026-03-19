class VisitaServicio:
    def __init__(self):
        self._visitantes = []

    def registrar_visitante(self, visitante):
        for v in self._visitantes:
            if v.cedula == visitante.cedula:
                return False

        self._visitantes.append(visitante)
        return True

    def obtener_visitantes(self):
        return self._visitantes

    # NUEVO METODO (POR INDICE)
    def eliminar_por_indice(self, indice):
        if 0 <= indice < len(self._visitantes):
            del self._visitantes[indice]
            return True
        return False