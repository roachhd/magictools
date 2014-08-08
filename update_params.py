#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

if __name__ == '__main__':
    with open('README_copy.md', 'r') as r:
        readme = r.read()

    with open('params.json', 'r') as p:
        pout = p.read()
        params_dict = json.loads(pout)
        params_dict['body'] = readme

    new_params = json.dumps(params_dict)
    with open('params.json', 'w') as new:
        new.write(new_params)
