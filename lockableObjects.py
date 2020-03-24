class Lockable(object):
    def __init__(self,value=None,locked=False):
        self.value=value
        lockedval=None
        self.locked=locked

    def __repr__(self):
        return f"{self.value} {' is locked' if self.locked else ' is unlocked'}"

    # TODO need to SHORTEN def lock, aint the best solution yet
    # JUST A QUICK SPAGHETTI CODE IDEA
    def lock(self,trueORFalse=True):
        if trueORFalse != False:

            self.lockedval=self.value
            self.value=None
            self.locked=True

        if trueORFalse == False:

            self.value=self.lockedval
            self.lockedval=None
            self.locked=False
    def unlock(self):
        self.value=self.lockedval
        self.lockedval=None
        self.locked=False

    def isLocked(self):
        return self.locked

# TODO ADD PROPERTYS, should confuse less
    def setValue(self,value):
        if self.locked:
            self.__repr__()
        if not self.locked:
            self.value = value
