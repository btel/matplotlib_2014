#!/usr/bin/env python
#coding=utf-8

from IPython.display import HTML
def as_table(arr, maxrows=10):
    headers = arr.dtype.names
    def enclose(tag, lst):
        def formatting(x):
            
            return '<{tag}>{element}</{tag}>'.format(tag=tag, element=x)
        if not isinstance(lst, basestring):
            return "".join([formatting(element) for element in lst])
        else:
            return formatting(lst)
    header = enclose('tr', enclose('th', headers))
    #data = enclose('tr', en)
    data = enclose('tr', [enclose('td', row) for row in arr[:maxrows]])
    html = enclose('table', "".join([header,data]))
    return HTML(html)
