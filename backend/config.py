from configparser import ConfigParser
import os
import platform
from screeninfo import get_monitors


class Config:
	def __init__(self):
		self.conf_path = os.path.join(os.getcwd(), 'resourses/conf.ini')
		self.config = ConfigParser()
		self.config.read(self.conf_path)

		self.WINDOWS = (platform.system() == "Windows")
		self.LINUX = (platform.system() == "Linux")


	def _get_configparser_object(self):
		return self.config

	def get_size(self):
		return (int(self.config['DEFAULT']['width']), int(self.config['DEFAULT']['height']))

	def get_position(self):
		monitor = get_monitors()[0]
		width, height = monitor.width, monitor.height
		return ((int(width) - int(self.config['DEFAULT']['width']))/2, (int(height) - int(self.config['DEFAULT']['height']))/2) if self.config['DEFAULT']['position'] == 'center' else None

	def get_host(self):
		return self.config['DEFAULT']['host']

	def get_port(self):
		return int(self.config['DEFAULT']['port'])

	def get_mode(self):
		return self.config['WEB_DRIVER']['mode']

	def get_cmdline_args(self):
		return self.config['DEFAULT']['cmdline_args'].split(' ')

	def get_driver_path(self):
		if self.LINUX:
			driver_dir = './resourses/driver/chrome'
		elif self.WINDOWS:
			driver_dir = './resourses/driver/chrome.exe'
		return driver_dir
