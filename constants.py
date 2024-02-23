# entities
class Entities():
  entities_list = ['component', 'hook', 'util', 'constants']
  default_entity = entities_list[0]
  
  shortcuts = {
    'component': 'c', 
    'hook': 'h', 
    'util': 'u', 
    'constants': 'const'
  }

  # for command line 
  options = entities_list + list(shortcuts.values())

  def get_by_shortcut(self, entity_short):
    for entity_key in self.shortcuts.keys():
      if self.shortcuts[entity_key] == entity_short:
        return entity_key
      
  def normalize_entity(self, entity):
    if entity in self.entities_list: return entity
    return self.get_by_shortcut(entity)

entities = Entities()


# options during configuration
class ConfigOptions():
  allowed_styles = ['css', 'scss']
  default_styles = 'css'

  allowed_langs = ['js', 'ts']
  default_lang = 'ts'

  default_path = 'src/components'

config_options = ConfigOptions()


# config file name
config_file_name = 'config.json'


# default constants filename
default_constants_filename = 'constants'