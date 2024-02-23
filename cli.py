import click

import controllers
import utils
import constants

@click.group()
def cli_commands():
  pass

# for initializing and creating config file
@click.command()
@click.option('-l', '--lang', 
  prompt='Select component language:', 
  type=click.Choice(constants.config_options.allowed_langs), 
  default=constants.config_options.default_lang,
  help='The language that the entities will be coded in'
)
@click.option('-s', '--styles', 
  prompt='Select component styles:', 
  type=click.Choice(constants.config_options.allowed_styles), 
  default=constants.config_options.default_styles,
  help='Styles that components will use'
)
@click.option('-dp', '--default-path',
  prompt='Select default path',
  type=click.Path(exists=False),
  default=constants.config_options.default_path,
  help='Default path where entity will be created (mostly for components)'
)
def init(lang, styles, default_path):
  path = default_path

  if (utils.Path.is_absolute(path)):
    print('Do not use absolute paths (starting with /)')
    path = path[1:] # remove first symbol

  controllers.init(lang, styles, path)

  print('Configuration is created!')

# for creating entity
@click.command()
@click.argument('entity', type=click.Choice(constants.entities.options), default=constants.entities.default_entity)
@click.argument('name', type=click.STRING, required=1)
@click.argument('path', type=click.Path(exists=False), default=None, required=0)
def create(entity, name, path):
  normalized_entity = constants.entities.normalize_entity(entity)
  normalized_path = path if path != None else utils.Configuration.get_config().default_path

  if (utils.Path.is_absolute(normalized_path)):
    print('Do not use absolute paths (starting with /)')
    normalized_path = normalized_path[1:] # remove first symbol
    return # do not create entity

  try:
    controllers.create(normalized_entity, name, normalized_path)
    print('Successfully created!')
  except FileExistsError:
    print('File with this name already exists')


# load all commands
cli_commands.add_command(init)
cli_commands.add_command(create)


if __name__ == '__main__':
  cli_commands()