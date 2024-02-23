import json
import constants

import os

# Path 
class Path():
  def relative(path):
    return os.path.join(os.getcwd(), path)
  
  def join(*paths):
    return os.path.join(*paths)
  
  def join_as_absolute(self, *paths):
    return self.join(os.getcwd(), *paths)
  
  def is_absolute(path: str):
    return os.path.isabs(path) 


# create config plain data class
class Configuration():
  path = Path.join(constants.config_file_name) 

  # default config options
  lang = constants.config_options.default_lang
  styles = constants.config_options.default_styles
  default_path = constants.config_options.default_path

  def __init__(self, lang, styles, default_path):
    self.lang = lang
    self.styles = styles
    self.default_path = default_path

  def get_config():
    filepath = Configuration.path
    config = {
      'lang': constants.config_options.default_lang,
      'styles': constants.config_options.default_styles,
      'default_path': constants.config_options.default_path,
    }

    # load config file if existed (otherwise leave default)
    try: config = JSON.parse(Files.read_file(filepath))
    except: pass

    configuration = Configuration(
      config['lang'] or constants.config_options.default_lang, 
      config['styles'] or constants.config_options.default_styles,
      config['default_path'] or constants.config_options.default_path,
    )
    
    return configuration


# JSON adapter
class JSON():
  def stringify(data):
    return json.dumps(data, indent=2)
  
  def parse(str_data: str):
    return json.load(str_data)
  

# Files
class Files():
  def write_file(filepath: str, content: str):
    file = open(filepath, 'w')
    file.write(content)
    file.close()

  def read_file(filepath):
    file_content = open(filepath, 'r')
    return file_content


# string utils
def concat_strings(substr: list[str], joining_str: str):
  return joining_str.join(substr)

# create basic file
def create_basic_file(path: str, name: str, content: str, configuration: Configuration):
  file_name = name + '.' + configuration.lang
  file_path = Path.join(path, file_name)

  try: os.mkdir(path)
  except FileExistsError: pass

  Files.write_file(file_path, content)