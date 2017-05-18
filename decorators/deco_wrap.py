#import pytest
import logging
import inspect
import types
from functools import wraps
import time

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def print_entry_exit(f):
    entry_time = time.time()
    @wraps(f)
    def new_f(*args):
        logger.info("Entered Function -- %s -- time: %d", f.__name__, enty_time)
        retVal = f(*args)
        logger.info("Exited Function -- {} -- time: %d, elapsed time:", f.__name__, time.time() - enty_time)
        return retVal
    return new_f


class entry_exit_cls(object):

    def __init__(self, f):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        logger.info("Inside __init__()")
        self.f = f

    def __call__(self, *args):
        """
        The __call__ method is not called until the
        decorated function is called.
        """
        logger.info("Entering {}".format(self.f.__name__))
        self.f(*args)
        logger.info("Exited {}".format(self.f.__name__))




def entry_exit(f):
    '''
    if inspect.isclass(f):
        def new_cls():

        def decorate(cls):
            for func in inspect.getmembers(f, predicate=inspect.ismethod):
                setattr(cls, func, decorator(getattr(cls, attr)))
    '''
    if inspect.isfunction(f):
        logger.info("Decorating Started of:{0}".format(f.__name__))
        @wraps(f)
        def new_f(*args, **named_args):
    	    entry_time = time.clock()
            logger.info("Entering {}".format(f.__name__))
	    logger.info("arguments (locals): args= %s, named_args=%s", locals()['args'], locals()['named_args'])
            retVal = f(*args, **named_args)
            logger.info("Exited {}, took %f ms.".format(f.__name__), time.clock() - entry_time)
            return retVal
        logger.info("Decorating Finished of: {}".format(f.__name__))
        return new_f





def log_getattribute(cls):
    # Get the original implementation
    orig_getattribute = cls.__getattribute__

    # Make a new definition
    def new_getattribute(self, name):
        logger.info("Entering {}".format(name))
        retVal = orig_getattribute(self, name)
        logger.info("Exiting {}".format(name))
        return retVal

    # Attach to the class and return
    cls.__getattribute__ = new_getattribute
    return cls


@entry_exit
def test__deco_4():
    a = A(12)
    logger.info("{}".format(a.spam()))

def test__deco_1():
    ret1 = f1(1, "2")
    logger.info("ret1: {0}, ret1[0]: {1}, ret1[1]: {2}".format(ret1, ret1[0], ret1[1]))

def test__deco_2():
    ret1, ret2 = f1(1, "2")
    logger.info("ret1: {0}, ret2: {1}".format(ret1, ret2))

@entry_exit
def test__deco_3():
    c = cls1()
    c.cls_f1()
    logger.info("cls1 is a {0} have {1} methods.".format(type(cls1),len(inspect.getmembers(cls1, predicate=inspect.ismethod))))
    if inspect.isclass(cls1):
        logger.info("cls1 is a classobj")
    if inspect.isfunction(test__deco_2):
        logger.info("cls1_f1 is a function")
    logger.info("types.ClassType: {}".format(types.ClassType))


@entry_exit
def test_100():
    in_loop = False
    for i in range(0):
        in_loop = True
        logger.info("Inside the for loop, i={}".format(i))

    logger.info("in_loop = {}".format(in_loop))
    print(in_loop)
    assert in_loop == True


@entry_exit
def f1(var1, var2):
    logger.info("in f1, before call to f2")
    f2()
    logger.info("in f1, after call to f2")
    return "ddd", "ccc"


@entry_exit
def f2():
    logger.info("in f2")
    logger.debug("in f2")
@entry_exit
def f3(a, b, c, d):
	time.sleep(2.555555)
	pass

f1(1,2)
f1(1, var2=2)
f2()

f3(1,2,3,4)
f3('a', 'b', c='C', d='D')
f3(1, 2, c=[1,2,3], d={'a':1, 'b':2})
