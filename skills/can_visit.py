# coding=utf-8


class ListNode:
    """
    Accessibility of class and object attributes
    """
    _class_field10 = 'node class field 1-0'
    _class_field11_ = 'node class field 1-1'
    _class_field12__ = 'node class field 1-2'

    __class_field20 = 'node class field 2-0'
    __class_field21_ = 'node class field 2-1'
    __class_field22__ = 'node class field 2-2'

    def __init__(self, x):
        self.val = x
        self.next = None


c = ListNode(12)
c._class_field10 = 'node class field 1-0'
c._class_field11_ = 'node class field 1-1'
c._class_field12__ = 'node class field 1-2'

c.__class_field20 = 'node class field 2-0'
c.__class_field21_ = 'node class field 2-1'
c.__class_field22__ = 'node class field 2-2'

print(c.__dict__)
print(c.__class__)
print(ListNode.__dict__)