# CLI for React JS application

Developed by Oleksii Pavlov \<aleshapavlov9@gmail.com>. Can be used to generate React standard code like components, hooks, utils etc.

Generable entities:
- components
- hooks
- utils
- constants

## Commands

### init [OPTIONS]

Options:
- -l, --lang [js|ts] - Used language
- -s, --styles [css|scss] - Used styles language
- -dp, --default-path PATH - Default folder for generation (by default src/components)
- --help - Get help 

### create \<ENTITY> \<NAME> [PATH] [OPTIONS]

Arguments:
- entity - entity that will be created. [component|hook|util|constants|c|h|u|const]
Options:
- name - entity name (for example, Header or useLocalStorage)
- path - optional. Sets where to create an entity (for example, src/shared/hooks)

### rename \<ENTITY> \<NAME> \<PATH> \<NEW_NAME>

Arguments:
- entity - entity that will be renamed. [component|hook|util|constants|c|h|u|const]
Options:
- name - entity name (for example, Header or useLocalStorage)
- path - optional. Sets where to rename an entity (for example, src/shared/hooks)
- new_name - new name for the entity