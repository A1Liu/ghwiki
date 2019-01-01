<!--
{% set json = __env_get__('json') %}
{
	"name":"{{ name }}",
	"tags": {{ json.dumps(tags) }},
	"changes":"{{ changes.replace('\n','\\n') if changes is defined and changes != None }}",
	"planned_changes":"{{ planned_changes.replace('\n','\\n') if planned_changes is defined and planned_changes != None }}",
	"testing_instructions":"{{ testing_instructions.replace('\n','\\n') if testing_instructions is defined and testing_instructions != None }}",
}
-->
### `{{name}}` Branch Summary
{{ description if description is defined else 'DESCRIPTION' }}

#py if process_tags is not defined
#py set process_tags = __env_get__('process_tags')
#py endif
{% if tags is defined %}
{{ process_tags(tags) }}
{% endif %}

{% if changes is defined and changes != None %}
##### Changes
<!-- List of changes implemented -->
{{ changes }}

{% endif %}
{% if planned_changes is defined and planned_changes != None %}
##### Planned Changes
<!-- TODO list for the entire PR, including things that have already been done -->
{{ planned_changes }}

{% endif %}
{% if testing_instructions is defined and testing_instructions != None %}
##### Testing Instructions
<!-- These are steps that will help verify the PR is doing what it's supposed to -->
{{ testing_instructions }}
{% endif %}
