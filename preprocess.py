#!/usr/bin/env python3

from jinja2 import Environment, select_autoescape
from jinja2.filters import do_round

env = Environment(
    autoescape=select_autoescape()
)

with open('main.journal.j2', 'r') as f:
    print(env.from_string(f.read()).render(round=do_round, int=int))
