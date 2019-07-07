from ipaddr import ipaddr, ipsubnet, ipv4, ipv6

from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader(searchpath="."),
    autoescape=select_autoescape(['html', 'xml'])
)

env.filters['ipaddr'] = ipaddr
env.filters['ipsubnet'] = ipsubnet
env.filters['ipv4'] = ipv4
env.filters['ipv6'] = ipv6

template = env.get_template('template.j2')

print(template.render(host_v4='192.168.2.1/24',
                      host_v6='fe80::1/64', subnet='10.10.0.0/16'))
