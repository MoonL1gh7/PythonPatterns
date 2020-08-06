# -*- coding: utf-8 -*-
from jinja2 import Template


def render(template_name, **kwargs):
    with open(template_name, encoding='utf-8') as t:
        template = Template(t.read())
    return template.render(**kwargs)


if __name__ == '__main__':
    output_test = render('index.html', object_list=[{'test': 'one'}, {'test': 'two'}])
    print(output_test)
