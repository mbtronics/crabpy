# -*- coding: utf-8 -*-
'''
'''
from crabpy.client import crab_request, crab_factory
from crabpy.gateway.crab import CrabGateway

g = CrabGateway(crab_factory())

gemeente = g.get_gemeente_by_id(1)
print 'Gemeente: ' + str(gemeente)
for i in range(0,10):
    s = gemeente.straten[i]
    print "* Straat:  %s" % s
    for j in range(0, 10):
        print "  ** Huisnummer: %s" % s.huisnummers[j]
