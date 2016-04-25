class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """

        self.nestedList = nestedList

    x = []

    def next(self):
        """
        :rtype: int
        """
        self.klx(self.nestedList)


    def klx(self, l):
        """
        :type: list
        :return: list
        """
        for i in l:
            if type(i) == list:
                klx(i)
            else:
                x.append(i)

    def hasNext(self):
        """
        :rtype: bool
        """
