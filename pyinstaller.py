import os
import platform
import shutil
import sys
from subprocess import Popen
import configparser

try:
    import PyInstaller
except ImportError:
    PyInstaller = None
    raise SystemExit("Error: PyInstaller package missing. "
                     "To install type: pip install --upgrade pyinstaller")


WINDOWS = (platform.system() == "Windows")
LINUX = (platform.system() == "Linux")


EXE_EXT = ""
if WINDOWS:
    EXE_EXT = ".exe"
elif LINUX:
    EXE_EXT = ""

APP_NAME = "app"
ICON_NAME = "web/favicon.ico"
DIST_DIR = "dist/"
BUILD_DIR = "build/"
RESOURCES_DIR = "resourses/"
CONF_FILE_NAME = 'conf.ini'
CMD = f"python -m eel run.py web --onefile --noconsole -n {APP_NAME} -i {ICON_NAME}"



def copy_resourses():
    shutil.copytree(RESOURCES_DIR, os.path.join(DIST_DIR, RESOURCES_DIR))


def delete_build_dir():
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)


def delete_dist_dir():
    if os.path.exists(DIST_DIR):
        shutil.rmtree(DIST_DIR)


def delete_spec_file():
    spec_file = f'{APP_NAME}.spec'
    if os.path.exists(spec_file):
        os.remove(spec_file)


def main():
    delete_dist_dir()
    delete_build_dir()
    delete_spec_file()

    sub = Popen(CMD.split(' '))
    sub.communicate()
    rcode = sub.returncode
    if rcode != 0:
        print("Error: PyInstaller failed, code=%s" % rcode)
        delete_dist_dir()
        delete_build_dir()
        sys.exit(1)

    # Make sure everything went fine
    curdir = os.path.dirname(os.path.abspath(__file__))
    app_dir = os.path.join(curdir, "dist")
    executable = os.path.join(app_dir, APP_NAME+EXE_EXT)
    if not os.path.exists(executable):
        print("Error: PyInstaller failed, main executable is missing: %s"
              % executable)
        sys.exit(1)


    copy_resourses()
    delete_build_dir()
    delete_spec_file()

    # Done
    print("Сборка завершена!")


if __name__ == "__main__":
    main()