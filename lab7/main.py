from Controller.AppController import AppController
from Repository.InMemoryRepository import InMemoryRepository
from UI.UI_Representer import ui_representer




if __name__ == '__main__':

    app_controller = AppController(ui_representer, InMemoryRepository)
    app_controller.start()

