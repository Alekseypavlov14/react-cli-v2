import utils

# component files
def component_template(name: str, configuration: utils.Configuration):
  # styles file name
  styles_file_name = utils.CodeFiles.create_styles_file_name(name, configuration)
  
  file_lines = [
    "import React from 'react'",
    "import styles from './<STYLES_FILE_NAME>'",

    "\ninterface <COMPONENT>Props {}\n" if configuration.lang == 'ts' else '', 

    "export function <COMPONENT>({ ...props }: <COMPONENT>Props) {" if configuration.lang == 'ts' 
    else 'export function <COMPONENT>({ ...props }) {',

    "  return (",
    "    <div className={styles.<COMPONENT>}>",
    "      ",
    "    </div>",
    "  )",
    "}"
  ]

  file_content = utils.concat_strings(file_lines, '\n').replace('<COMPONENT>', name).replace('<STYLES_FILE_NAME>', styles_file_name)

  return file_content

def component_index_template(name: str):
  file_lines = ['export { <COMPONENT> } from \'./<COMPONENT>\'']

  file_content = utils.concat_strings(file_lines, '\n').replace('<COMPONENT>', name)

  return file_content

def component_styles_file(name: str):
  file_lines = ['/* .<COMPONENT> {} */']

  file_content = utils.concat_strings(file_lines, '\n').replace('<COMPONENT>', name)

  return file_content


# hook file
def hook_template(name: str):
  file_lines = ['export function <NAME>() {}']

  file_content = utils.concat_strings(file_lines, '\n').replace('<NAME>', name)

  return file_content


# util file
def util_template(name: str):
  file_lines = ['export function <NAME>() {}']

  file_content = utils.concat_strings(file_lines, '\n').replace('<NAME>', name)

  return file_content


# constants file
def constants_template():
  return '// Your constants here'