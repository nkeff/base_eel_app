import eel
import os
from backend.config import Config


def start_app():
    """
    Установка флагов chrome для того чтобы отключить всплывающее уведомление
    """
    os.environ["GOOGLE_API_KEY"] = "false"
    os.environ["GOOGLE_DEFAULT_CLIENT_ID"] = "false"
    os.environ["GOOGLE_DEFAULT_CLIENT_SECRET"] = "false"
    config = Config()


    eel.init('web')





    driver_path = config.get_driver_path()
    if os.path.exists(driver_path) and config.get_mode() == 'chrome':
        eel.browsers.set_path(config.get_mode(), driver_path)


    eel.start(
        'templates/index.html',
        jinja_templates='templates',
        mode=config.get_mode(),
        size=config.get_size(),
        position=config.get_position(),
        port=config.get_port(),
        host=config.get_host(),
        cmdline_args=config.get_cmdline_args()
        )