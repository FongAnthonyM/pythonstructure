#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Example Anthony/Google Hybrid style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Constants:
    CONSTANT (str): Module level variables may be documented in
        either the ``Constants`` section of the module docstring, or in an
        inline docstring immediately following the variable.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
__author__ = "Anthony Fong"
__copyright__ = "Copyright 2019, Anthony Fong"
__credits__ = ["Anthony Fong"]
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Anthony Fong"
__email__ = ""
__status__ = "Prototype"

# Default Libraries #
from abc import ABC

# Downloaded Libraries #

# Local Libraries #

# Definitions #
# Constants #
CONSTANTS = "UPPER_CASE_WITH_UNDERSCORES"


# Variables #
module_level_variable1 = 12345


# Classes #
class CamelCase(ABC):
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration .

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Args:
        param1 (str): Description of `param1`.
        param2 (:obj:`int`, optional): Description of `param2`. Multiple
            lines are supported.
        param3 (:obj:`list` of :obj:`str`): Description of `param3`.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    CONSTANTS = "UPPER_CASE_WITH_UNDERSCORES"

    # Construction/Destruction
    def __new__(cls, *args, **kwargs):
        """Special Class methods are similar to regular functions.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
        pass

    def __set_name__(self, owner, name):
        pass

    def __init_subclass__(cls, **kwargs):
        pass

    def __init__(self, param1, param2, param3):
        self.attr1 = param1
        self.attr2 = param2
        self.attr3 = param3  #: Doc comment *inline* with attribute

        #: list of str: Doc comment *before* attribute, with type specified
        self.attr4 = ['attr4']

        self.attr5 = None
        """str: Docstring *after* attribute, with type specified."""

    @property
    def name(self):
        """:obj:`list` of :obj:`str`: Properties with both a getter and setter
        should only be documented in their getter method.

        If the setter method contains notable behavior, it should be
        mentioned here.
        """
        return ["something"]

    @name.setter
    def name(self, value):
        pass

    def __copy__(self):
        pass

    def __deepcopy__(self, memodict={}):
        pass

    def __del__(self):
        pass

    # Reflection
    def __mro_entries__(self, bases):
        pass

    def __prepare__(mcs, name, bases):
        pass

    def __instancecheck__(self, instance):
        pass

    def __subclasscheck__(self, subclass):
        pass

    # Descriptor Object
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass

    # Pickling
    def __getinitargs__(self):
        pass

    def __getnewargs__(self):
        pass

    def __getstate__(self):
        pass

    def __setstate__(self, state):
        pass

    def __reduce__(self):
        pass

    def __reduce_ex__(self, protocol):
        pass

    # Attribute Access
    def __getattr__(self, item):
        pass

    def __setattr__(self, key, value):
        pass

    def __delattr__(self, item):
        pass

    def __getattribute__(self, item):
        pass

    # Container Methods
    def __class_getitem__(cls, item):
        pass

    def __len__(self):
        pass

    def __length_hint__(self):
        pass

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __getslice__(self, i, j):  # Not a magic method in Python 3
        pass

    def __setslice__(self, i, j, sequence):  # Not a magic method in Python 3
        pass

    def __delslice__(self, i, j):  # Not a magic method in Python 3
        pass

    def __iter__(self):
        pass

    def __reversed__(self):
        pass

    def __next__(self):
        pass

    def __contains__(self, item):
        pass

    def __missing__(self, key):
        pass

    # Callable
    def __call__(self, *args, **kwargs):
        pass

    # Context Managers
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    # Coroutines
    def __aenter__(self):
        pass

    def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    def __aiter__(self):
        pass

    def __anext__(self):
        pass

    def __await__(self):
        pass

    # Representation
    def __repr__(self):
        pass

    def __bytes__(self):
        pass

    def __unicode__(self):
        pass

    def __format__(self, format_spec):
        pass

    def __hash__(self):
        pass

    def __fspath__(self):
        pass

    def __dir__(self) -> Iterable[str]:
        pass

    def __sizeof__(self):
        pass

    # Type Conversion
    def __int__(self):
        pass

    def __long__(self):
        pass

    def __float__(self):
        pass

    def __complex__(self):
        pass

    def __oct__(self):
        pass

    def __hex__(self):
        pass

    def __index__(self):
        pass

    def __str__(self):
        pass

    def __bool__(self):
        pass

    def __coerce__(self, other):
        return self, other

    # Comparison
    def __cmp__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __ge__(self, other):
        pass

    # Numeric
    def __pos__(self):
        pass

    def __neg__(self):
        pass

    def __abs__(self):
        pass

    def __invert__(self):
        pass

    def __round__(self, n=None):
        pass

    def __floor__(self):
        pass

    def __ceil__(self):
        pass

    def __trunc__(self):
        pass

    # Arithmetic
    def __add__(self, other):
        pass

    def __radd__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __rsub__(self, other):
        pass

    def __isub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __imul__(self, other):
        pass

    def __matmul__(self, other):
        pass

    def __rmatmul__(self, other):
        pass

    def __imatmul__(self, other):
        pass

    def __floordiv__(self, other):
        pass

    def __rfloordiv__(self, other):
        pass

    def __ifloordiv__(self, other):
        pass

    def __div__(self, other):  # Not a magic method in Python 3
        pass

    def __rdiv__(self, other):  # Not a magic method in Python 3
        pass

    def __idiv__(self, other):  # Not a magic method in Python 3
        pass

    def __truediv__(self, other):
        pass

    def __rtruediv__(self, other):
        pass

    def __itruediv__(self, other):
        pass

    def __mod__(self, other):
        pass

    def __rmod__(self, other):
        pass

    def __imod__(self, other):
        pass

    def __divmod__(self, other):
        pass

    def __rdivmod__(self, other):
        pass

    def __pow__(self, power, modulo=None):
        pass

    def __rpow__(self, other):
        pass

    def __ipow__(self, other):
        pass

    def __lshift__(self, other):
        pass

    def __rlshift__(self, other):
        pass

    def __ilshift__(self, other):
        pass

    def __rshift__(self, other):
        pass

    def __rrshift__(self, other):
        pass

    def __irshift__(self, other):
        pass

    def __and__(self, other):
        pass

    def __rand__(self, other):
        pass

    def __iand__(self, other):
        pass

    def __or__(self, other):
        pass

    def __ror__(self, other):
        pass

    def __ior__(self, other):
        pass

    def __xor__(self, other):
        pass

    def __rxor__(self, other):
        pass

    def __ixor__(self, other):
        pass


# Functions #
def module_level_function(param1, param2=None, *args, **kwargs):
    """This is an example of a module level function.

    Function parameters should be documented in the ``Parameters`` section. The name
    of each parameter is required. The type and description of each parameter
    is optional, but should be included if not obvious.

    If *args or **kwargs are accepted,
    they should be listed as ``*args`` and ``**kwargs``.

    The format for a parameter is::

        name (type): description
            The description may span multiple lines. Following
            lines should be indented. The "(type)" is optional.

            Multiple paragraphs are supported in parameter
            descriptions.

    Args:
        param1 (int): The first parameter.
        param2 (:obj:`str`, optional): The second parameter. Defaults to None.
            Second line of description should be indented.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        bool: True if successful, False otherwise.

        The return type is optional and may be specified at the beginning of
        the ``Returns`` section followed by a colon.

        The ``Returns`` section may span multiple lines and paragraphs.
        Following lines should be indented to match the first line.

        The ``Returns`` section supports any reStructuredText formatting,
        including literal blocks::

            {
                'param1': param1,
                'param2': param2
            }

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.

    """
    if param1 == param2:
        raise ValueError('param1 may not be equal to param2')
    return True


def example_generator(n):
    """Generators have a ``Yields`` section instead of a ``Returns`` section.

    Args:
        n (int): The upper limit of the range to generate, from 0 to `n` - 1.

    Yields:
        int: The next number in the range of 0 to `n` - 1.

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> print([i for i in example_generator(4)])
        [0, 1, 2, 3]

    """
    for i in range(n):
        yield i

