class Stash(object):

    def __call__(self, **kw):
        self.__dict__.update(kw)
        return kw.values()[0]
stash = Stash()
