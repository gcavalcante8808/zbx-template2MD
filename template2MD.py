#!/usr/bin/env python
# -*- coding: utf-8 -*-

import template_api
from string import Template
from enum import Enum


template_info = Template("""## $visible_name\n
Name: $template_name
Visible Name: $visible_name
Items: $items_count
Description: $template_description""")

item_info = Template("""

##### Item: $item_name\n
Name: $item_name
Type: $item_type
Key: $item_key
Delay: $item_delay
History: $item_history
Trends: $item_trends
Status: $item_status
Description: $item_description
""")

ITEM_TYPES = [
	"Zabbix agent",
	"SNMPv1 agent",
	"Zabbix trapper",
	"Simple check",
	"SNMPv2 agent",
	"Zabbix internal",
	"SNMPv3 agent",
	"Zabbix agent (active)",
	"Zabbix aggregate",
	"Web item",
	"external check",
	"database monitor",
	"IPMI agent",
	"SSH agent",
	"TELNET agent",
	"calculated",
	"JMX agent",
	"SNMP trap"
]



with open('zbx_export_templates.xml', 'r') as openfile:
	zbx_template = openfile.read()

content = template_api.parseString(zbx_template, silence=True)

templates = content.templates.get_template()

with open('template_doc.md', 'w') as openfile:
	for template in templates:
		openfile.write(template_info.substitute(template_name=template.template,
			visible_name=template.name,
			items_count=len(template.items.item),
			template_description="Stub"
			)
		)
		for item in template.items.item:
			openfile.write(item_info.substitute(item_name=item.name.encode('utf-8'),
				item_type=ITEM_TYPES[item.type_],
				item_key=item.key,
				item_delay=item.delay,
				item_history=item.history,
				item_trends=item.trends,
				item_status=item.status,
				item_description=item.description.encode('utf-8'))
			)