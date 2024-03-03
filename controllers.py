import utils
import templates

import os

# init configuration
def init(lang, styles, default_path):
  configuration = utils.Configuration(lang, styles, default_path)
  configuration_json = utils.JSON.stringify(configuration.__dict__)
  
  config_file_path = utils.Configuration.path
  utils.Files.write_file(config_file_path, configuration_json)

# create entity
def create(entity, name, path):
  if entity == 'component': create_component(name, path)
  if entity == 'hook': create_hook(name, path)
  if entity == 'util': create_util(name, path)
  if entity == 'constants': create_constants(name, path)

def create_component(name, path):
  configuration = utils.Configuration.get_config()

  # get component files content
  component_file = templates.component_template(name, configuration)
  component_styles_file = templates.component_styles_file(name, configuration)
  component_index_file = templates.component_index_template(name)

  # get file names
  component_file_name = utils.CodeFiles.create_component_file_name(name, configuration)
  component_styles_file_name = utils.CodeFiles.create_styles_file_name(name, configuration)
  component_index_file_name = utils.CodeFiles.create_index_file_name(configuration)

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
  utils.CodeFiles.create_basic_file(path, name, templates.hook_template(name), configuration)

def create_util(name, path):
  configuration = utils.Configuration.get_config()
  utils.CodeFiles.create_basic_file(path, name, templates.util_template(name), configuration)

def create_constants(name, path):
  configuration = utils.Configuration.get_config()
  utils.CodeFiles.create_basic_file(path, name, templates.constants_template(), configuration)


# rename entity
def rename(entity: str, name: str, path: str, new_name: str):
  configuration = utils.Configuration.get_config()

  if entity == 'component': rename_component(path, name, new_name, configuration)
  if entity == 'hook': rename_hook(path, name, new_name, configuration)
  if entity == 'util': rename_util(path, name, new_name, configuration)
  if entity == 'constants': rename_constants(path, name, new_name, configuration)

def rename_component(path: str, name: str, new_name: str, configuration: utils.Configuration):
  # rename folder
  old_component_folder_path = utils.Path.join(path, name)
  new_component_folder_path = utils.Path.join(path, new_name)
  os.rename(old_component_folder_path, new_component_folder_path)

  # rename component file
  old_component_file_name = utils.CodeFiles.create_component_file_name(name, configuration)
  new_component_file_name = utils.CodeFiles.create_component_file_name(new_name, configuration)

  old_component_file_path = utils.Path.join(new_component_folder_path, old_component_file_name)
  new_component_file_path = utils.Path.join(new_component_folder_path, new_component_file_name)

  os.rename(old_component_file_path, new_component_file_path)

  # replace component file content
  # replace styles file import
  old_component_styles_file = utils.CodeFiles.create_styles_file_name(name, configuration)
  new_component_styles_file = utils.CodeFiles.create_styles_file_name(new_name, configuration)
  utils.Files.replace_file_content(new_component_file_path, old_component_styles_file, new_component_styles_file)
  # replace component declaration
  utils.Files.replace_file_content(new_component_file_path, f'const {name}', f'const {new_name}') # for const declaration
  utils.Files.replace_file_content(new_component_file_path, f'function {name}', f'function {new_name}') # for function declaration
  # replace props interface name
  utils.Files.replace_file_content(new_component_file_path, f'{name}Props', f'{new_name}Props')
  # replace 
  utils.Files.replace_file_content(new_component_file_path, f'styles.{name}', f'styles.{new_name}')
  
  # rename styles file
  old_component_styles_filename = utils.CodeFiles.create_styles_file_name(name, configuration)
  new_component_styles_filename = utils.CodeFiles.create_styles_file_name(new_name, configuration)

  old_component_styles_path = utils.Path.join(new_component_folder_path, old_component_styles_filename)
  new_component_styles_path = utils.Path.join(new_component_folder_path, new_component_styles_filename)

  os.rename(old_component_styles_path, new_component_styles_path)

  # replace styles file content
  utils.Files.replace_file_content(new_component_styles_path, name, new_name)

  # replace index content
  component_index_file_name = utils.CodeFiles.create_index_file_name(configuration)
  component_index_file_path = utils.Path.join(new_component_folder_path, component_index_file_name)
  utils.Files.replace_file_content(component_index_file_path, name, new_name)

def rename_hook(path: str, name: str, new_name: str, configuration: utils.Configuration):
  # rename hook name in file
  file_path = utils.Path.join(path, utils.CodeFiles.create_basic_file_name(name, configuration))
  old_content = f'function {name}' # "(" to prevent mistaken replacements
  new_content = f'function {new_name}' # "(" to prevent mistaken replacements

  utils.Files.replace_file_content(file_path, old_content, new_content)

  # rename file
  utils.CodeFiles.rename_basic_file(path, name, new_name, configuration)

def rename_util(path: str, name, new_name: str, configuration: utils.Configuration):
  # rename hook name in file
  file_path = utils.Path.join(path, utils.CodeFiles.create_basic_file_name(name, configuration))
  old_content = f'function {name}' # "(" to prevent mistaken replacements
  new_content = f'function {new_name}' # "(" to prevent mistaken replacements

  utils.Files.replace_file_content(file_path, old_content, new_content)

  # rename file
  utils.CodeFiles.rename_basic_file(path, name, new_name, configuration)

def rename_constants(path: str, name: str, new_name: str, configuration: utils.Configuration):
  utils.CodeFiles.rename_basic_file(path, name, new_name, configuration)