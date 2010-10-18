
def getReferences(self, object, relationship=None, targetObject=None):
    """return a collection of reference objects"""
    sID, sobj = self._uidFor(object)
    if targetObject:
        tID, tobj = self._uidFor(targetObject)
    else:
        tID, tobj = (None, None)

    brains = self._optimizedQuery(sID, tID, relationship)
    return self._resolveBrains(brains)


def getBackReferences(self, object, relationship=None, targetObject=None):
    """return a collection of reference objects"""
    # Back refs would be anything that target this object
    sID, sobj = self._uidFor(object)
    if targetObject:
        tID, tobj = self._uidFor(targetObject)
    else:
        tID, tobj = (None, None)

    brains = self._optimizedQuery(tID, sID, relationship)
    return self._resolveBrains(brains)


def _optimizedQuery(self, sid, tid, relationship):
    """query reference catalog for object matching the info we are
    given, returns brains
    """
    query = {}
    if sid:
        query['sourceUID'] = sid
    if tid:
        query['targetUID'] = tid
    if relationship:
        query['relationship'] = relationship

    return self.searchResults(query, merge=1)


def apply():
    from Products.Archetypes.ReferenceEngine import ReferenceCatalog as rc

    rc._old_getReferences = rc.getReferences
    rc.getReferences = getReferences
    rc._old_getBackReferences = rc.getBackReferences
    rc.getBackReferences = getBackReferences

    rc._optimizedQuery = _optimizedQuery
