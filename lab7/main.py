from Controller.AppController import AppController
from Repository.InMemoryRepository import InMemoryRepository
from UI.UI_Representer import UIRepresenter

if __name__ == '__main__':
    app_controller = AppController()
    app_controller.start()
