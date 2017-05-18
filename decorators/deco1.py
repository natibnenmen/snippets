#import pytest
import logging
import inspect
import types
from functools import wraps
import time

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)



class sw(object):

    def __init__(self, my_name):
        self.my_name = my_name

    def print_object_details(self):
        logger.info("my_name: %s, my registry: %s", self.my_name, self.registry)

    registry = {}

    @classmethod
    def register(cls, *args):
        def real_register(f):
            @wraps(f)
            def new_f(*args, **named_args):
                retVal = f(*args, **named_args)
                return retVal
            for arg in args:
                assert arg not in cls.registry
                cls.registry[arg] = new_f
            return new_f
        return real_register


@sw.register('G3')
def g2():
    logger.info("in g2")

@sw.register('G1', 'G2')
def ggg(a =0,b =9,c = 6):
    logger.info("in %s", ggg.__name__)

@sw.register('G5', 'G6')
def g1(a,b,c):
    logger.info("in %s", t2.__name__)

'''
@sw.register('G3')
def g1():
    logger.info("in %s", __name__)
'''

swo1 = sw('A')
swo2 = sw('B')

swo1.print_object_details()
swo2.print_object_details()

swo1.registry['G3']()
swo1.registry['G1']()
swo1.registry['G2'](1,2)
swo1.registry['G5'](1, b='BBBB', c=3)


def for_all_methods(cls):
    def decorate():
        class new_cls:
            pass
        for attr in dir(cls):
            if inspect.isfunction(attr):
                #setattr(new_cls, attr, decorator(getattr(cls, attr)))
                return new_cls
    return decorate


@for_all_methods
class C:
    def m1(self): pass
    def m2(self, x): pass
