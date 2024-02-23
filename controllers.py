import utils
import templates

import os

# init configuration
def init(lang, styles, default_path):
  configuration = utils.Configuration(lang, styles, default_path)
  configuration_json = utils.JSON.stringify(configuration.__dict__)
  
  config_file_path = utils.Configuration.path
  utils.Files.write_file(config_file_path, configuration_json)


def create(entity, name, path):
  if entity == 'component': create_component(name, path)
  if entity == 'hook': create_hook(name, path)
  if entity == 'util': create_util(name, path)
  if entity == 'constants': create_constants(name, path)

def create_component(name, path):
  configuration = utils.Configuration.get_config()

  # get component files content
  component_file = templates.component_template(name, configuration)
  component_styles_file = templates.component_styles_file(name)
  component_index_file = templates.component_index_template(name)

  # get file names
  component_file_name = name + '.' + configuration.lang + 'x' # 'x' needed because components files have extension jsx/tsx
  component_styles_file_name = name + '.module.' + configuration.styles
  component_index_file_name = 'index.' + configuration.lang

  # create directory
  entity_folder_path = utils.Path.join(path, name)
  os.makedirs(entity_folder_path)

  # get file paths
  component_file_path = utils.Path.join(entity_folder_path, component_file_name)
  component_styles_file_path = utils.Path.join(entity_folder_path, component_styles_file_name)
  component_index_file_path = utils.Path.join(entity_folder_path, component_index_file_name)

  # write files
  utils.Files.write_file(component_file_path, component_file)
  utils.Files.write_file(component_styles_file_path, component_styles_file)
  utils.Files.write_file(component_index_file_path, component_index_file)


def create_hook(name, path):
  configuration = utils.Configuration.get_config()
  utils.create_basic_file(path, name, templates.hook_template(name), configuration)

def create_util(name, path):
  configuration = utils.Configuration.get_config()
  utils.create_basic_file(path, name, templates.util_template(name), configuration)

def create_constants(name, path):
  configuration = utils.Configuration.get_config()
  utils.create_basic_file(path, name, templates.constants_template(), configuration)
