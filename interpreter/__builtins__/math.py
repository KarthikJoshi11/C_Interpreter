"""
This module file supports basic functions from math.h library
"""

from ..utils.utils import definition
import math

@definition(return_type='double', arg_types=['double'])
def sqrt(a):
    return math.sqrt(a.value)

@definition(return_type='double', arg_types=['double'])
def sin(a):
    return math.sin(a.value)

@definition(return_type='double', arg_types=['double'])
def cos(a):
    return math.cos(a.value)

@definition(return_type='double', arg_types=['double'])
def tan(a):
    return math.tan(a.value)

@definition(return_type='double', arg_types=['double'])
def log(a):
    return math.log(a.value)

@definition(return_type='double', arg_types=['double'])
def exp(a):
    return math.exp(a.value)

@definition(return_type='double', arg_types=['double', 'double'])
def pow(a, b):
    return math.pow(a.value, b.value)

@definition(return_type='double', arg_types=['double'])
def floor(a):
    return math.floor(a.value)

@definition(return_type='double', arg_types=['double'])
def ceil(a):
    return math.ceil(a.value)

@definition(return_type='double', arg_types=['double'])
def fabs(a):
    return math.fabs(a.value)