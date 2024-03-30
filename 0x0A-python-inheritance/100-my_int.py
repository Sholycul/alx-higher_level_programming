#!/usr/bin/python3
"""
MyInt that inherits from int:

MyInt is a rebel. MyInt has == and != operators inverted
You are not allowed to import any module

"""

class MyInt(int):
    """Class MyInt inherits from int with inverted == and != operators"""

    def __eq__(self, other):
        """Override == operator to return the opposite of the default behavior"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override != operator to return the opposite of the default behavior"""
        return super().__eq__(other)
