import termcolor

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
    return json.loads(str_data)
  

# Files
class Files():
  def write_file(filepath: str, content: str):
    file = open(filepath, 'w')
    file.write(content)
    file.close()

  def read_file(filepath) -> str:
    with open(filepath, 'r') as file:
      return file.read()
  
  def replace_file_content(filepath: str, content: str, replacer: str):
    file_content = Files.read_file(filepath)
    new_file_content = file_content.replace(content, replacer)
    Files.write_file(filepath, new_file_content)


# string utils
def concat_strings(substr: list[str], joining_str: str):
  return joining_str.join(substr)


# basic file utils
class CodeFiles():
  def create_basic_file(path: str, name: str, content: str, configuration: Configuration):
    file_name = CodeFiles.create_basic_file_name(name, configuration)
    file_path = Path.join(path, file_name)

    try: os.makedirs(path)
    except FileExistsError: pass

    if os.path.exists(file_path):
      raise FileExistsError()

    Files.write_file(file_path, content)

  def rename_basic_file(path: str, name: str, new_name: str, configuration: Configuration):
    old_file_name = CodeFiles.create_basic_file_name(name, configuration)
    new_file_name = CodeFiles.create_basic_file_name(new_name, configuration)

    old_file_path = Path.join(path, old_file_name)
    new_file_path = Path.join(path, new_file_name)

    os.rename(old_file_path, new_file_path)

  def create_basic_file_name(name: str, configuration: Configuration):
    return name + '.' + configuration.lang
  
  def create_component_file_name(name: str, configuration: Configuration):
    # 'x' needed because components files have extension jsx/tsx
    return name + '.' + configuration.lang + 'x' 

  def create_styles_file_name(name: str, configuration: Configuration):
    return name + '.module.' + configuration.styles

  def create_index_file_name(configuration: Configuration):
    return 'index.' + configuration.lang


# colorized outputs
class Printer():
  @staticmethod
  def success(text):
    print(termcolor.colored(text, 'green'))

  @staticmethod
  def error(text):
    print(termcolor.colored(text, 'red'))

  @staticmethod
  def warning(text):
    print(termcolor.colored(text, 'yellow'))
