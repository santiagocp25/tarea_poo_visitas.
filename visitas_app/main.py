from servicios.visita_servicio import VisitaServicio
from ui.app_tkinter import AppTkinter


def main():
    servicio = VisitaServicio()
    app = AppTkinter(servicio)
    app.run()


if __name__ == "__main__":
    main()