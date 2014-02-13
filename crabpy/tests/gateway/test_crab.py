# -*- coding: utf-8 -*-

from __future__ import unicode_literals

try:
    import unittest2 as unittest
except ImportError:  # pragma NO COVER
    import unittest  # noqa

from crabpy.client import (
    crab_factory
)

from crabpy.gateway.exception import (
    GatewayRuntimeException
)

from crabpy.gateway.crab import (
    CrabGateway, Gewest,
    Gemeente, Taal,
    Bewerking, Organisatie,
    Aardsubadres, Aardadres,
    Aardgebouw, Aardwegobject,
    Aardterreinobject, Statushuisnummer,
    Statussubadres, Statusstraatnaam,
    Statuswegsegment, Geometriemethodewegsegment,
    Statusgebouw, Geometriemethodegebouw,
    Herkomstadrespositie,Straat,
    Huisnummer, Postkanton,
    Wegobject, Wegsegment,
    Terreinobject, Perceel,
    Gebouw, Metadata
)


def run_crab_integration_tests():
    from testconfig import config
    from crabpy.tests import as_bool
    try:
        return as_bool(config['crab']['run_integration_tests'])
    except KeyError:  # pragma NO COVER
        return False


@unittest.skipUnless(
    run_crab_integration_tests(),
    'No CRAB Integration tests required'
)
class CrabGatewayTests(unittest.TestCase):

    def setUp(self):
        from testconfig import config
        self.crab_client = crab_factory()
        self.crab = CrabGateway(
            self.crab_client
        )

    def tearDown(self):
        self.crab_client = None
        self.crab = None
     
    def test_list_gewesten(self):
        res=self.crab.list_gewesten()
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Gewest)
        
    def test_list_gemeenten(self):
        res=self.crab.list_gemeenten()
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Gemeente)
        gewest=Gewest(2)
        res=self.crab.list_gemeenten(gewest)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Gemeente)
        
    def test_get_gemeente_by_id(self):
        res=self.crab.get_gemeente_by_id(1)
        self.assertIsInstance(res, Gemeente)
        self.assertEqual(res.id, 1)
        
        self.assertRaises(GatewayRuntimeException, self.crab.get_gemeente_by_id, 'gent')
        
    def test_get_gemeente_by_niscode(self):
        res=self.crab.get_gemeente_by_niscode(11001)
        self.assertIsInstance(res, Gemeente)
        self.assertEqual(res.niscode, 11001)
    
    def test_list_talen(self):
        res=self.crab.list_talen()
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Taal)
        
    def test_list_bewerkingen(self):
        res=self.crab.list_bewerkingen()
        self.assertIsInstance(res,list)
        self.assertIsInstance(res[0], Bewerking)
    
    def test_list_organisaties(self):
        res=self.crab.list_organisaties()
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Organisatie)
        
    def test_list_aardsubadressen(self):
        res=self.crab.list_aardsubadressen()
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Aardsubadres)
        
    def test_list_aardadressen(self):
        res=self.crab.list_aardadressen()
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Aardadres)
        
    def test_list_aardgebouwen(self):
        res=self.crab.list_aardgebouwen()
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Aardgebouw)
        
    def test_list_aarwegobjecten(self):
        res=self.crab.list_aardwegobjecten()
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Aardwegobject)
        
    def test_list_aardterreinobjecten(self):
        res=self.crab.list_aardterreinobjecten()
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Aardterreinobject)
        
    def test_list_statushuisnummers(self):
        res=self.crab.list_statushuisnummers()
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Statushuisnummer)
        
    def test_list_statussubadressen(self):
        res=self.crab.list_statussubadressen()
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Statussubadres)
        
    def test_list_statusstraatnamen(self):
        res=self.crab.list_statusstraatnamen()
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Statusstraatnaam)
        
    def test_list_statuswegsegmenten(self):
        res=self.crab.list_statuswegsegmenten()
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Statuswegsegment)
        
    def test_list_geometriemethodewegsegmenten(self):
        res=self.crab.list_geometriemethodewegsegmenten()
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Geometriemethodewegsegment)
        
    def test_list_statusgebouwen(self):
        res=self.crab.list_statusgebouwen()
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Statusgebouw)
        
    def test_list_gemetriemethodegebouwen(self):
        res=self.crab.list_geometriemethodegebouwen()
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Geometriemethodegebouw)
        
    def test_list_herkomstadrespositie(self):
        res=self.crab.list_herkomstadresposities()
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Herkomstadrespositie)
        
    def test_list_straten(self):
        res=self.crab.list_straten(1)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Straat)
        gemeente= self.crab.get_gemeente_by_id(1)
        self.assertIsInstance(gemeente, Gemeente)
        res=self.crab.list_straten(gemeente)
        self.assertIsInstance(res,list)
        self.assertIsInstance(res[0], Straat)
    
    def test_get_straat_by_id(self):
        res=self.crab.get_straat_by_id(1)
        self.assertIsInstance(res, Straat)
        self.assertEqual(res.id, 1)
        
    def test_list_huisnummers_by_straat(self):
        res=self.crab.list_huisnummers_by_straat(1)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Huisnummer)
        straat=self.crab.get_straat_by_id(1)
        res=self.crab.list_huisnummers_by_straat(straat)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Huisnummer)
        
    def test_get_huisnummer_by_id(self):
        res=self.crab.get_huisnummer_by_id(1)
        self.assertIsInstance(res, Huisnummer)
        self.assertEqual(res.id, 1)
        
    def test_get_huisnummer_by_nummer_and_straat(self):
        res=self.crab.get_huisnummer_by_nummer_and_straat(1,1)
        self.assertIsInstance(res, Huisnummer)
        self.assertEqual(res.huisnummer, '1') 
        self.assertEqual(res.straat.id, 1)
        straat=self.crab.get_straat_by_id(1)
        res=self.crab.get_huisnummer_by_nummer_and_straat(1, straat)
        self.assertIsInstance(res, Huisnummer)
        self.assertEqual(res.huisnummer, '1')
        
    def test_list_postkantons_by_gemeente(self):
        res=self.crab.list_postkantons_by_gemeente(1)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Postkanton)
        gemeente=self.crab.get_gemeente_by_id(1)
        res=self.crab.list_postkantons_by_gemeente(gemeente)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Postkanton)
        
    def test_get_postkanton_by_huisnummer(self):
        res=self.crab.get_postkanton_by_huisnummer(1)
        self.assertIsInstance(res, Postkanton)
        huisnummer=self.crab.get_huisnummer_by_id(1)
        res=self.crab.get_postkanton_by_huisnummer(huisnummer)
        self.assertIsInstance(res, Postkanton)

    def test_list_wegobjecten_by_straat(self):
        res=self.crab.list_wegobjecten_by_straat(1)
        self.assertIsInstance(res,list)
        self.assertIsInstance(res[0], Wegobject)
        straat=self.crab.get_straat_by_id(1)
        res=self.crab.list_wegobjecten_by_straat(straat)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Wegobject)
        
    def test_get_wegobject_by_id(self):
        res=self.crab.get_wegobject_by_id("53839893")
        self.assertIsInstance(res, Wegobject)
        self.assertEqual(res.id, "53839893")
        
    def test_list_wegsegmenten_by_straat(self):
        res=self.crab.list_wegsegmenten_by_straat(1)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Wegsegment)
        straat=self.crab.get_straat_by_id(1)
        res=self.crab.list_wegsegmenten_by_straat(straat)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Wegsegment)
        
    def test_get_wegsegment_by_id(self):
        res=self.crab.get_wegsegment_by_id("108724")
        self.assertIsInstance(res, Wegsegment)
        self.assertEqual(res.id, "108724")
        
    def test_list_terreinobjecten_by_huisnummer(self):
        res=self.crab.list_terreinobjecten_by_huisnummer(1)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Terreinobject)
        huisnummer=self.crab.get_huisnummer_by_id(1)
        res=self.crab.list_terreinobjecten_by_huisnummer(huisnummer)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Terreinobject)
        
    def test_get_terreinobject_by_id(self):
        res=self.crab.get_terreinobject_by_id("13040_C_1747_G_002_00")
        self.assertIsInstance(res, Terreinobject)
        self.assertEqual(res.id, "13040_C_1747_G_002_00")
        
    def test_list_percelen_by_huisnummer(self):
        res=self.crab.list_percelen_by_huisnummer(1)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Perceel)
        huisnummer=self.crab.get_huisnummer_by_id(1)
        res=self.crab.list_percelen_by_huisnummer(huisnummer)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Perceel)

    def test_get_perceel_by_id(self):
        res=self.crab.get_perceel_by_id("13040C1747/00G002")
        self.assertIsInstance(res, Perceel)
        self.assertEqual(res.id, "13040C1747/00G002")

    def test_list_gebouwen_by_huisnummer(self):
        res=self.crab.list_gebouwen_by_huisnummer(1)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Gebouw)
        huisnummer=self.crab.get_huisnummer_by_id(1)
        res=self.crab.list_gebouwen_by_huisnummer(huisnummer)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Gebouw)
        
        
    def test_get_gebouw_by_id(self):
        res=self.crab.get_gebouw_by_id("1538575")
        self.assertIsInstance(res, Gebouw)
        self.assertEqual(res.id, 1538575)
        


class GewestTests(unittest.TestCase):

    def test_fully_initialised(self):
        g = Gewest(
            2,'Vlaams'
        )
        self.assertEqual(g.id,2)
        self.assertEqual(g.naam, 'Vlaams')
        self.assertEqual('Vlaams (2)', str(g))
        self.assertEqual("Gewest(2, 'Vlaams')", repr(g))
        
        
        
    def test_str_and_repr_dont_lazy_load(self):
        g=Gewest(2)
        self.assertEqual('Gewest 2', str(g))
        self.assertEqual('Gewest(2)', repr(g))
            
    def test_check_gateway_not_set(self):
        g=Gewest(2)
        self.assertRaises(RuntimeError, g.check_gateway)
        
    def test_gemeenten(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        g=Gewest(2)
        g.set_gateway(crab) 
        gemeenten = g.gemeenten
        self.assertIsInstance(gemeenten, list)
        

class GemeenteTests(unittest.TestCase):
    
    def test_fully_initialised(self):
        g = Gemeente(
            1,
            'Aartselaar',
            11001,
            2,
            'nl',
            (150881.07, 202256.84),
            (148950.36, 199938.28, 152811.77, 204575.39),
            '1830-01-01 00:00:00',
            '2002-08-13 17:32:32',
            1,
            6
        )
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        g.set_gateway(crab)
        self.assertEqual(g.id, 1)
        self.assertEqual(g.naam, 'Aartselaar')
        self.assertEqual(g.niscode, 11001)
        self.assertEqual(int(g.gewest.id), 2)
        self.assertEqual(g.taal.id, 'nl')
        self.assertEqual(g.centroid, (150881.07, 202256.84))
        self.assertEqual(
            g.bounding_box,
            (148950.36, 199938.28, 152811.77, 204575.39)
        )
        self.assertEqual(g.metadata.begin_datum, '1830-01-01 00:00:00')
        self.assertEqual(g.metadata.begin_tijd, '2002-08-13 17:32:32')
        g.metadata.set_gateway(crab)
        self.assertEqual(int(g.metadata.begin_bewerking.id), 1)
        self.assertEqual(int(g.metadata.begin_organisatie.id), 6)
        self.assertEqual('Aartselaar (1)', str(g))
        self.assertEqual("Gemeente(1, 'Aartselaar')", repr(g))
        
        
    def test_str_and_repr_dont_lazy_load(self):
        g =Gemeente(1)
        self.assertEqual('Gemeente 1', str(g))
        self.assertEqual('Gemeente(1)', repr(g))
            
    def test_check_gateway_not_set(self):
        g=Gemeente(1)
        self.assertRaises(RuntimeError, g.check_gateway)
        
    def test_lazy_load(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        g = Gemeente(1)
        g.set_gateway(crab)
        self.assertEqual(g.id, 1)
        self.assertEqual(g.naam, 'Aartselaar')
        self.assertEqual(g.niscode, 11001)
        self.assertEqual(int(g.gewest.id), 2)
        self.assertEqual(g.taal.id, 'nl')
        self.assertEqual(g.centroid, (150881.07, 202256.84))
        self.assertEqual(
            g.bounding_box,
            (148950.36, 199938.28, 152811.77, 204575.39)
        )
        self.assertEqual(g.metadata.begin_datum, '1830-01-01 00:00:00')
        self.assertEqual(g.metadata.begin_tijd, '2002-08-13 17:32:32')
        g.metadata.set_gateway(crab)
        self.assertEqual(int(g.metadata.begin_bewerking.id), 1)
        self.assertEqual(int(g.metadata.begin_organisatie.id), 6)
            
    def test_straten(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        g=Gemeente(1)
        g.set_gateway(crab)
        straten=g.straten
        self.assertIsInstance(straten, list)
        
    def test_postkantons(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        g=Gemeente(1)
        g.set_gateway(crab) 
        postkanton = g.postkantons
        self.assertIsInstance(postkanton, list)
            
        
class TaalTests(unittest.TestCase):
    def test_fully_initialised(self):
        t=Taal(
            "nl",
            'Nederlands',
            'Nederlands.'
        )
        self.assertEqual(t.id,"nl")
        self.assertEqual(t.naam, 'Nederlands')
        self.assertEqual(t.definitie, 'Nederlands.')

        
class StraatTests(unittest.TestCase):
    def test_fully_initialised(self):
        s = Straat(
            1,
            'Acacialaan',
            3,
            'Acacialaan','nl',None,None,
            1,
            '1830-01-01 00:00:00',
            '2013-04-12 20:07:25.960000',
            3,
            1,
        )
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        s.set_gateway(crab)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.label, 'Acacialaan')
        self.assertEqual(int(s.status.id), 3)
        self.assertEqual(s.namen, (('Acacialaan', 'nl'),(None,None)))
        self.assertEqual(int(s.gemeente.id), 1)
        self.assertEqual(s.metadata.begin_datum, '1830-01-01 00:00:00')
        self.assertEqual(s.metadata.begin_tijd, '2013-04-12 20:07:25.960000')
        s.metadata.set_gateway(crab)
        self.assertEqual(int(s.metadata.begin_bewerking.id), 3)
        self.assertEqual(int(s.metadata.begin_organisatie.id), 1)
        self.assertEqual('Acacialaan (1)', str(s))
        self.assertEqual("Straat(1, 'Acacialaan')", repr(s))
    
    def test_lazy_load(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        s = Straat(1)
        s.set_gateway(crab)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.label, 'Acacialaan')
        self.assertEqual(int(s.status.id), 3)
        self.assertEqual(s.namen, (('Acacialaan', 'nl'),(None,None)))
        self.assertEqual(int(s.gemeente.id), 1)
        self.assertEqual(s.metadata.begin_datum, '1830-01-01 00:00:00')
        self.assertEqual(s.metadata.begin_tijd, '2013-04-12 20:07:25.960000')
        s.metadata.set_gateway(crab)
        self.assertEqual(int(s.metadata.begin_bewerking.id), 3)
        self.assertEqual(int(s.metadata.begin_organisatie.id), 1)
    
    def test_str_and_repr_dont_lazy_load(self):
        s =Straat(1)
        self.assertEqual('Straat 1', str(s))
        self.assertEqual('Straat(1)', repr(s))
            
    def test_check_gateway_not_set(self):
        s =Straat(1)
        self.assertRaises(RuntimeError, s.check_gateway)
        
    def test_huisnummers(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        s=Straat(1)
        s.set_gateway(crab)
        huisnummers=s.huisnummers
        self.assertIsInstance(huisnummers, list)
        
    def test_taal(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        s=Straat(1)
        s.set_gateway(crab)
        taal=s.taal
        self.assertEqual(s.taal.id, 'nl')
        
    def test_gemeente(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        s=Straat(1)
        s.set_gateway(crab)
        gemeente=s.gemeente
        
    def test_status(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        s=Straat(1)
        s.set_gateway(crab)
        status=s.status
        self.assertIsInstance(status, Statusstraatnaam)
    
        
    
class HuisnummerTests(unittest.TestCase):
    def test_fully_initialised(self):
        h = Huisnummer(
        1,
        3,
        "51",
        17718,
        '1830-01-01 00:00:00',
        '2011-04-29 13:27:40.230000',
        1,
        5
        )
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        h.set_gateway(crab)
        self.assertEqual(h.id, 1)
        self.assertEqual(int(h.status.id), 3)
        self.assertEqual(h.huisnummer, "51")
        self.assertEqual(int(h.straat.id), 17718)
        self.assertEqual(h.metadata.begin_datum, '1830-01-01 00:00:00')
        self.assertEqual(h.metadata.begin_tijd, '2011-04-29 13:27:40.230000')
        h.metadata.set_gateway(crab)
        self.assertEqual(int(h.metadata.begin_bewerking.id), 1)
        self.assertEqual(int(h.metadata.begin_organisatie.id), 5)
        self.assertEqual('Steenweg op Oosthoven 51', str(h))
        self.assertEqual('Huisnummer(1)', repr(h))
        
    def test_str_dont_lazy_load(self):
        h =Huisnummer(1)
        self.assertEqual('Huisnummer 1', str(h))

    def test_lazy_load(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        h = Huisnummer(1)
        h.set_gateway(crab)
        self.assertEqual(h.id, 1)
        self.assertEqual(int(h.status.id), 3)
        self.assertEqual(h.huisnummer, "51")
        self.assertEqual(int(h.straat.id), 17718)
        self.assertEqual(h.metadata.begin_datum, '1830-01-01 00:00:00')
        self.assertEqual(h.metadata.begin_tijd, '2011-04-29 13:27:40.230000')
        h.metadata.set_gateway(crab)
        self.assertEqual(int(h.metadata.begin_bewerking.id), 1)
        self.assertEqual(int(h.metadata.begin_organisatie.id), 5)

    def test_postkanton(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        h=Huisnummer(1)
        h.set_gateway(crab)
        postkanton=h.postkanton
        self.assertIsInstance(postkanton, Postkanton)
        
    def test_terreinobjecten(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        h=Huisnummer(1)
        h.set_gateway(crab)
        terreinobjecten=h.terreinobjecten
        self.assertIsInstance(terreinobjecten, list)
        
    def test_percelen(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        h=Huisnummer(1)
        h.set_gateway(crab)
        percelen=h.percelen
        self.assertIsInstance(percelen, list)
        
    def test_gebouwen(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        h=Huisnummer(1)
        h.set_gateway(crab)
        gebouwen=h.gebouwen
        self.assertIsInstance(gebouwen, list)
        
    def test_status(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        h=Huisnummer(1)
        h.set_gateway(crab)
        status=h.status
        self.assertIsInstance(status, Statushuisnummer)
        
    def test_check_gateway_not_set(self):
        h =Huisnummer(1)
        self.assertRaises(RuntimeError, h.check_gateway)

class PostkantonTests(unittest.TestCase):
    def test_fully_initialised(self):
        p=Postkanton(
            2630,
            1,
            '1830-01-01 00:00:00',
            
        )
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        p.set_gateway(crab)
        self.assertEqual(p.id, 2630)
        self.assertEqual(p.gemeente.id, 1)
        self.assertEqual(p.metadata.begin_datum, '1830-01-01 00:00:00')
        self.assertEqual(p.metadata.begin_tijd, '2002-08-13 16:37:33')
        p.metadata.set_gateway(crab)
        self.assertEqual(int(p.metadata.begin_bewerking.id), 1)
        self.assertEqual(int(p.metadata.begin_organisatie.id), 7)
        self.assertEqual('Postkanton 2630', str(p))
        self.assertEqual('Postkanton(2630)', repr(p))
        
        
    def test_lazy_load(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        p=Postkanton(2630, 1)
        p.set_gateway(crab)
        self.assertEqual(p.id, 2630)
        self.assertEqual(p.gemeente.id, 1)
        self.assertEqual(p.metadata.begin_datum, '1830-01-01 00:00:00')
        self.assertEqual(p.metadata.begin_tijd, '2002-08-13 16:37:33')
        p.metadata.set_gateway(crab)
        self.assertEqual(int(p.metadata.begin_bewerking.id), 1)
        self.assertEqual(int(p.metadata.begin_organisatie.id), 7)
        
        

class WegobjectTests(unittest.TestCase):
    def test_fully_initialised(self):
        w = Wegobject(
            "53839893",
            4,
            (150753.46,200148.41),
            (150693.58,200080.56,150813.35,200216.27),
            '1830-01-01 00:00:00',
            '2008-04-17 16:32:11.753000',
            1,
            8
        )
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        w.set_gateway(crab)
        self.assertEqual(w.id,"53839893" )  
        self.assertEqual(int(w.aard.id), 4)
        self.assertEqual(w.centroid,(150753.46,200148.41))
        self.assertEqual(w.bounding_box, (150693.58,200080.56,150813.35,200216.27))
        self.assertEqual(w.metadata.begin_datum, '1830-01-01 00:00:00')
        self.assertEqual(w.metadata.begin_tijd, '2008-04-17 16:32:11.753000')
        w.metadata.set_gateway(crab)
        self.assertEqual(int(w.metadata.begin_bewerking.id), 1)
        self.assertEqual(int(w.metadata.begin_organisatie.id),8)
        self.assertEqual('Wegobject 53839893', str(w))
        self.assertEqual('Wegobject(53839893)', repr(w))
        
    def test_check_gateway_not_set(self):
        w =Wegobject(1)
        self.assertRaises(RuntimeError, w.check_gateway)
        
    def test_aard(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        w=Wegobject("53839893")
        w.set_gateway(crab)
        aard=w.aard
        self.assertIsInstance(aard, Aardwegobject)
        
    def test_lazy_load(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        w = Wegobject("53839893")
        w.set_gateway(crab)
        self.assertEqual(w.id,"53839893" )
        self.assertEqual(int(w.aard.id), 4)
        self.assertEqual(w.centroid,(150753.46,200148.41))
        self.assertEqual(w.bounding_box, (150693.58,200080.56,150813.35,200216.27))
        self.assertEqual(w.metadata.begin_datum, '1830-01-01 00:00:00')
        self.assertEqual(w.metadata.begin_tijd, '2008-04-17 16:32:11.753000')
        w.metadata.set_gateway(crab)
        self.assertEqual(int(w.metadata.begin_bewerking.id), 1)
        self.assertEqual(int(w.metadata.begin_organisatie.id),8)
        
class WegsegmentTests(unittest.TestCase):
    def test_fully_initialised(self):
        w=Wegsegment(
            "108724",
            4,
            3,
            "LINESTRING (150339.255243488 201166.401677653, 150342.836939491 201165.832525652, 150345.139531493 201165.466573652, 150349.791371495 201164.769421652, 150352.512459494 201164.36161365, 150358.512331501 201163.46241365, 150375.039179511 201156.606669646, 150386.901963517 201150.194893643, 150397.470027529 201142.865485638, 150403.464011535 201135.266637631, 150407.825739533 201127.481037624, 150414.301515542 201109.016653612, 150431.792971551 201057.519821577, 150442.85677956 201026.858701557, 150454.530123569 200999.312717538, 150472.404939577 200955.342029508, 150483.516619585 200927.052237488, 150500.807755597 200883.890765458, 150516.94650761 200844.146253429, 150543.214411631 200773.35943738, 150546.079307631 200764.489805374, 150548.592075631 200754.511565369)",
            '1830-01-01 00:00:00',
            '2013-04-12 20:12:12.687000',
            3,
            1
        )
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        w.set_gateway(crab)
        self.assertEqual(w.id, "108724")
        self.assertEqual(int(w.status.id), 4)
        self.assertEqual(int(w.methode.id), 3)
        self.assertEqual(w.geometrie, "LINESTRING (150339.255243488 201166.401677653, 150342.836939491 201165.832525652, 150345.139531493 201165.466573652, 150349.791371495 201164.769421652, 150352.512459494 201164.36161365, 150358.512331501 201163.46241365, 150375.039179511 201156.606669646, 150386.901963517 201150.194893643, 150397.470027529 201142.865485638, 150403.464011535 201135.266637631, 150407.825739533 201127.481037624, 150414.301515542 201109.016653612, 150431.792971551 201057.519821577, 150442.85677956 201026.858701557, 150454.530123569 200999.312717538, 150472.404939577 200955.342029508, 150483.516619585 200927.052237488, 150500.807755597 200883.890765458, 150516.94650761 200844.146253429, 150543.214411631 200773.35943738, 150546.079307631 200764.489805374, 150548.592075631 200754.511565369)")
        self.assertEqual(w.metadata.begin_datum, '1830-01-01 00:00:00')
        self.assertEqual(w.metadata.begin_tijd, '2013-04-12 20:12:12.687000')
        w.metadata.set_gateway(crab)
        self.assertEqual(int(w.metadata.begin_bewerking.id), 3)
        self.assertEqual(int(w.metadata.begin_organisatie.id),1)
        self.assertEqual('Wegsegment 108724', str(w))
        self.assertEqual('Wegsegment(108724)', repr(w))

    def test_check_gateway_not_set(self):
        w = Wegsegment(1)
        self.assertRaises(RuntimeError, w.check_gateway)

    def test_status(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        w=Wegsegment('108724')
        w.set_gateway(crab)
        status=w.status
        self.assertIsInstance(status, Statuswegsegment)
        
    def test_methode(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        w=Wegsegment('108724')
        w.set_gateway(crab)
        methode=w.methode
        self.assertIsInstance(methode, Geometriemethodewegsegment)
        
    def test_lazy_load(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        w = Wegsegment('108724')
        w.set_gateway(crab)
        self.assertEqual(w.id, "108724")
        self.assertEqual(int(w.status.id), 4)
        self.assertEqual(int(w.methode.id), 3)
        self.assertEqual(w.geometrie, "LINESTRING (150339.255243488 201166.401677653, 150342.836939491 201165.832525652, 150345.139531493 201165.466573652, 150349.791371495 201164.769421652, 150352.512459494 201164.36161365, 150358.512331501 201163.46241365, 150375.039179511 201156.606669646, 150386.901963517 201150.194893643, 150397.470027529 201142.865485638, 150403.464011535 201135.266637631, 150407.825739533 201127.481037624, 150414.301515542 201109.016653612, 150431.792971551 201057.519821577, 150442.85677956 201026.858701557, 150454.530123569 200999.312717538, 150472.404939577 200955.342029508, 150483.516619585 200927.052237488, 150500.807755597 200883.890765458, 150516.94650761 200844.146253429, 150543.214411631 200773.35943738, 150546.079307631 200764.489805374, 150548.592075631 200754.511565369)")
        
class TerreinobjectTests(unittest.TestCase):
    def test_fully_initialised(self):
        t=Terreinobject(
            "13040_C_1747_G_002_00",
            1,
            (190708.59,224667.59),
            (190700.24,224649.87,190716.95,224701.7),
            '1998-01-01 00:00:00',
            '2009-09-11 12:46:55.693000',
            3,
            3
        )    
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        t.set_gateway(crab)
        self.assertEqual(t.id, "13040_C_1747_G_002_00")  
        self.assertEqual(int(t.aard.id), 1)  
        self.assertEqual(t.centroid, (190708.59,224667.59))
        self.assertEqual(t.bounding_box, (190700.24,224649.87,190716.95,224701.7))
        self.assertEqual(t.metadata.begin_datum, '1998-01-01 00:00:00')
        self.assertEqual(t.metadata.begin_tijd, '2009-09-11 12:46:55.693000')
        t.metadata.set_gateway(crab)
        self.assertEqual(int(t.metadata.begin_bewerking.id), 3)
        self.assertEqual(int(t.metadata.begin_organisatie.id), 3)
        self.assertEqual('Terreinobject 13040_C_1747_G_002_00', str(t))
        self.assertEqual('Terreinobject(13040_C_1747_G_002_00)', repr(t))
        
    def test_lazy_load(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        t=Terreinobject("13040_C_1747_G_002_00")
        t.set_gateway(crab)
        self.assertEqual(t.id, "13040_C_1747_G_002_00")   
        self.assertEqual(int(t.aard.id), 1) 
        self.assertEqual(t.centroid, (190708.59,224667.59))
        self.assertEqual(t.bounding_box, (190700.24,224649.87,190716.95,224701.7))
        self.assertEqual(t.metadata.begin_datum, '1998-01-01 00:00:00')
        self.assertEqual(t.metadata.begin_tijd, '2009-09-11 12:46:55.693000')
        t.metadata.set_gateway(crab)
        self.assertEqual(int(t.metadata.begin_bewerking.id), 3)
        self.assertEqual(int(t.metadata.begin_organisatie.id), 3)

    def test_aard(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        t = Terreinobject("13040_C_1747_G_002_00")
        t.set_gateway(crab)
        aard = t.aard
        self.assertIsInstance(aard, Aardterreinobject)

class PerceelTests(unittest.TestCase):
    def test_fully_initialised(self):
        p=Perceel(
            "13040C1747/00G002",
            (190708.59,224667.59),
            '1998-01-01 00:00:00',
            '2009-09-11 12:46:55.693000',
            3,
            3
        )
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        p.set_gateway(crab)
        self.assertEqual(p.id, "13040C1747/00G002")
        self.assertEqual(p.centroid, (190708.59,224667.59))
        self.assertEqual(p.metadata.begin_datum, '1998-01-01 00:00:00')
        self.assertEqual(p.metadata.begin_tijd, '2009-09-11 12:46:55.693000')
        p.metadata.set_gateway(crab)
        self.assertEqual(int(p.metadata.begin_bewerking.id), 3)
        self.assertEqual(int(p.metadata.begin_organisatie.id), 3)
        self.assertEqual('Perceel 13040C1747/00G002', str(p))
        self.assertEqual('Perceel(13040C1747/00G002)', repr(p))
        
    def test_lazy_load(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        p = Perceel("13040C1747/00G002")
        p.set_gateway(crab)
        self.assertEqual(p.id, "13040C1747/00G002")    
        self.assertEqual(p.centroid, (190708.59,224667.59))
        self.assertEqual(p.metadata.begin_datum, '1998-01-01 00:00:00')
        self.assertEqual(p.metadata.begin_tijd, '2009-09-11 12:46:55.693000')
        p.metadata.set_gateway(crab)
        self.assertEqual(int(p.metadata.begin_bewerking.id), 3)
        self.assertEqual(int(p.metadata.begin_organisatie.id), 3)


class GebouwTests(unittest.TestCase):
    def test_fully_initialised(self):
        g = Gebouw(
            "1538575",
            1,
            4,
            3,
            "POLYGON ((190712.36432739347 224668.5216938965, 190706.26007138938 224667.54428589717, 190706.03594338894 224668.89276589826, 190704.89699938893 224668.66159789637, 190705.350887388 224666.14575789496, 190708.31754338741 224649.70287788659, 190717.16349539906 224653.81065388769, 190713.40490339696 224663.38582189381, 190712.36432739347 224668.5216938965))",
            '1830-01-01 00:00:00',
            '2011-05-19 10:51:09.483000',
            1,
            5
        )
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )   
        g.set_gateway(crab)
        self.assertEqual(g.id, 1538575)
        self.assertEqual(int(g.aard.id), 1)
        self.assertEqual(int(g.status.id), 4)
        self.assertEqual(int(g.methode.id), 3)
        self.assertEqual(g.geometrie, "POLYGON ((190712.36432739347 224668.5216938965, 190706.26007138938 224667.54428589717, 190706.03594338894 224668.89276589826, 190704.89699938893 224668.66159789637, 190705.350887388 224666.14575789496, 190708.31754338741 224649.70287788659, 190717.16349539906 224653.81065388769, 190713.40490339696 224663.38582189381, 190712.36432739347 224668.5216938965))")
        self.assertEqual(g.metadata.begin_datum, '1830-01-01 00:00:00')
        self.assertEqual(g.metadata.begin_tijd, '2011-05-19 10:51:09.483000')
        g.metadata.set_gateway(crab)
        self.assertEqual(int(g.metadata.begin_bewerking.id), 1)
        self.assertEqual(int(g.metadata.begin_organisatie.id), 5)
        self.assertEqual('Gebouw 1538575', str(g))
        self.assertEqual('Gebouw(1538575)', repr(g))


    def test_lazy_load(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        g = Gebouw("1538575")
        g.set_gateway(crab)
        self.assertEqual(g.id, 1538575)
        self.assertEqual(int(g.aard.id), 1)
        self.assertEqual(int(g.status.id), 4)
        self.assertEqual(int(g.methode.id), 3)
        self.assertEqual(g.geometrie, "POLYGON ((190712.36432739347 224668.5216938965, 190706.26007138938 224667.54428589717, 190706.03594338894 224668.89276589826, 190704.89699938893 224668.66159789637, 190705.350887388 224666.14575789496, 190708.31754338741 224649.70287788659, 190717.16349539906 224653.81065388769, 190713.40490339696 224663.38582189381, 190712.36432739347 224668.5216938965))")
        self.assertEqual(g.metadata.begin_datum, '1830-01-01 00:00:00')
        self.assertEqual(g.metadata.begin_tijd, '2011-05-19 10:51:09.483000')
        g.metadata.set_gateway(crab)
        self.assertEqual(int(g.metadata.begin_bewerking.id), 1)
        self.assertEqual(int(g.metadata.begin_organisatie.id), 5)
        
    
    def test_aard(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        g = Gebouw("1538575")
        g.set_gateway(crab)
        aard = g.aard
        self.assertIsInstance(aard, Aardgebouw)
        
    def test_status(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        g = Gebouw("1538575")
        g.set_gateway(crab)
        status = g.status
        self.assertIsInstance(status, Statusgebouw)
        
    def test_methode(self):
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        g = Gebouw("1538575")
        g.set_gateway(crab)
        methode = g.methode
        self.assertIsInstance(methode, Geometriemethodegebouw)
    
class MetadataTests(unittest.TestCase):
    def test_fully_initialised(self):
        m = Metadata(
            '1830-01-01 00:00:00',
            '2003-12-06 21:42:11.117000',
            1,
            6
        )
        from testconfig import config
        crab = CrabGateway(
            crab_factory()
        )
        m.set_gateway(crab)
        self.assertEqual(m.begin_datum, '1830-01-01 00:00:00')
        self.assertEqual(m.begin_tijd, '2003-12-06 21:42:11.117000')
        self.assertEqual(int(m.begin_bewerking.id), 1)
        self.assertEqual(int(m.begin_organisatie.id), 6)
        
        
@unittest.skipUnless(run_crab_integration_tests(), 'No CRAB Integration tests required')
class CrabCachedGatewayTests(unittest.TestCase):

    def setUp(self):
        self.crab_client=crab_factory()
        self.crab = CrabGateway(
            self.crab_client,
            cache_config = {
                'permanent.backend': 'dogpile.cache.memory',
                'permanent.expiration_time': 86400,
                'long.backend': 'dogpile.cache.memory',
                'long.expiration_time': 3600,
                'short.backend': 'dogpile.cache.memory',
                'short.expiration_time': 600,
            }
        )

    def tearDown(self):
        self.crab_client = None
        self.crab = None

    def test_cache_is_configured(self):
        from dogpile.cache.backends.memory import MemoryBackend
        self.assertIsInstance(
            self.crab.caches['permanent'].backend, 
            MemoryBackend
        )
        self.assertTrue(self.crab.caches['permanent'].is_configured)
        
    
    def test_list_gewesten(self):
        res = self.crab.list_gewesten()
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListGewesten#1'),
            res
        )

    def test_list_gewesten_different_sort(self):
        res = self.crab.list_gewesten(2)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListGewesten#2'),
            res
        )
        from dogpile.cache.api import NO_VALUE
        self.assertEqual(
            self.crab.caches['permanent'].get('ListGewesten#1'),
            NO_VALUE
        )

    def test_list_gemeenten(self):
        res = self.crab.list_gemeenten()
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['long'].get('ListGemeentenByGewestId#21'),
            res
        )
        gewest=Gewest(1)
        r= self.crab.list_gemeenten(gewest)
        self.assertIsInstance(r, list)
        self.assertEqual(
            self.crab.caches['long'].get('ListGemeentenByGewestId#11'),
            r
        )

    def test_list_gemeenten_different_sort(self):
        res = self.crab.list_gemeenten(2,2)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['long'].get('ListGemeentenByGewestId#22'),
            res
        )
        gewest=Gewest(1)
        r=self.crab.list_gemeenten(gewest, 2)
        self.assertIsInstance(r, list)
        self.assertEqual(
            self.crab.caches['long'].get('ListGemeentenByGewestId#12'),
            r
        )
        
    
    def test_get_gemeente_by_id(self):
        res = self.crab.get_gemeente_by_id(1)
        self.assertIsInstance(res, Gemeente)
        self.assertEqual(
            self.crab.caches['long'].get('GetGemeenteByGemeenteId#1'),
            res
        )
        
    def test_get_gemeente_by_niscode(self):
        res = self.crab.get_gemeente_by_niscode(11001)
        self.assertIsInstance(res, Gemeente)
        self.assertEqual(
            self.crab.caches['long'].get('GetGemeenteByNISGemeenteCode#11001'),
            res
        )
        
    def test_list_talen(self):
        res = self.crab.list_talen()
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListTalen#1'),
            res
        )

    def test_list_talen_different_sort(self):
        res = self.crab.list_talen(2)
        self.assertIsInstance(res, list)
        self.assertEqual(
        self.crab.caches['permanent'].get('ListTalen#2'),
            res
        )
        from dogpile.cache.api import NO_VALUE
        self.assertEqual(
            self.crab.caches['permanent'].get('ListTalen#1'),
            NO_VALUE
        )
        
    def test_list_bewerkingen(self):
        res = self.crab.list_bewerkingen()
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListBewerkingen#1'),
            res
        )

    def test_list_bewerkingen_different_sort(self):
        res = self.crab.list_bewerkingen(2)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListBewerkingen#2'),
            res
        )
        from dogpile.cache.api import NO_VALUE
        self.assertEqual(
            self.crab.caches['permanent'].get('ListBewerkingen#1'),
            NO_VALUE
        )
            
    def test_list_organisaties(self):
        res = self.crab.list_organisaties()
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListOrganisaties#1'),
            res
        )

    def test_list_organisaties_different_sort(self):
        res = self.crab.list_organisaties(2)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListOrganisaties#2'),
            res
        )
        from dogpile.cache.api import NO_VALUE
        self.assertEqual(
            self.crab.caches['permanent'].get('ListOrganisaties#1'),
            NO_VALUE
        )
            
            
    def test_list_aardadressen(self):
        res = self.crab.list_aardadressen()
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListAardAdressen#1'),
            res
        )

    def test_list_aardadressen_different_sort(self):
        res = self.crab.list_aardadressen(2)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListAardAdressen#2'),
            res
        )
        from dogpile.cache.api import NO_VALUE
        self.assertEqual(
            self.crab.caches['permanent'].get('ListAardAdressen#1'),
            NO_VALUE
        )
            
            
    def test_list_aardgebouwen(self):
        res = self.crab.list_aardgebouwen()
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListAardGebouwen#1'),
            res
        )

    def test_list_aardgebouwen_different_sort(self):
        res = self.crab.list_aardgebouwen(2)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListAardGebouwen#2'),
            res
        )
        from dogpile.cache.api import NO_VALUE
        self.assertEqual(
            self.crab.caches['permanent'].get('ListAardGebouwen#1'),
            NO_VALUE
        )

    def test_list_aardwegobjecten(self):
        res = self.crab.list_aardwegobjecten()
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListAardWegobjecten#1'),
            res
        )

    def test_list_aardwegobjecten_different_sort(self):
        res = self.crab.list_aardwegobjecten(2)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListAardWegobjecten#2'),
            res
        )
        from dogpile.cache.api import NO_VALUE
        self.assertEqual(
            self.crab.caches['permanent'].get('ListAardWegobjecten#1'),
            NO_VALUE
        )
            
    def test_list_aardterreinobjecten(self):
        res = self.crab.list_aardterreinobjecten()
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListAardTerreinobjecten#1'),
            res
        )

    def test_list_aardterreinobjecten_different_sort(self):
        res = self.crab.list_aardterreinobjecten(2)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListAardTerreinobjecten#2'),
            res
        )
        from dogpile.cache.api import NO_VALUE
        self.assertEqual(
            self.crab.caches['permanent'].get('ListAardTerreinobjecten#1'),
            NO_VALUE
        )
            
            
    def test_list_statushuisnummers(self):
        res = self.crab.list_statushuisnummers()
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListStatusHuisnummers#1'),
            res
        )

    def test_list_statushuisnummers_different_sort(self):
        res = self.crab.list_statushuisnummers(2)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListStatusHuisnummers#2'),
            res
        )
        from dogpile.cache.api import NO_VALUE
        self.assertEqual(
            self.crab.caches['permanent'].get('ListStatusHuisnummers#1'),
            NO_VALUE
        )
            
            
    def test_list_statussubadressen(self):
        res = self.crab.list_statussubadressen()
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListStatusSubadressen#1'),
            res
        )

    def test_list_statussubadressen_different_sort(self):
        res = self.crab.list_statussubadressen(2)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListStatusSubadressen#2'),
            res
        )
        from dogpile.cache.api import NO_VALUE
        self.assertEqual(
            self.crab.caches['permanent'].get('ListStatusSubadressen#1'),
            NO_VALUE
        )
            
            
    def test_list_statusstraatnamen(self):
        res = self.crab.list_statusstraatnamen()
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListStatusStraatnamen#1'),
            res
        )

    def test_list_statusstraatnamen_different_sort(self):
        res = self.crab.list_statusstraatnamen(2)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListStatusStraatnamen#2'),
            res
        )
        from dogpile.cache.api import NO_VALUE
        self.assertEqual(
            self.crab.caches['permanent'].get('ListStatusStraatnamen#1'),
            NO_VALUE
        )
            
    def test_list_statuswegsegmenten(self):
        res = self.crab.list_statuswegsegmenten()
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListStatusWegsegmenten#1'),
            res
        )

    def test_list_statuswegsegmenten_different_sort(self):
        res = self.crab.list_statuswegsegmenten(2)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListStatusWegsegmenten#2'),
            res
        )
        from dogpile.cache.api import NO_VALUE
        self.assertEqual(
            self.crab.caches['permanent'].get('ListStatusWegsegmenten#1'),
            NO_VALUE
         )
            
    def test_list_geometriemethodewegsegmenten(self):
        res = self.crab.list_geometriemethodewegsegmenten()
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListGeometriemethodeWegsegmenten#1'),
            res
        )

    def test_list_geometriemethodewegsegmenten_different_sort(self):
        res = self.crab.list_geometriemethodewegsegmenten(2)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListGeometriemethodeWegsegmenten#2'),
            res
        )
        from dogpile.cache.api import NO_VALUE
        self.assertEqual(
            self.crab.caches['permanent'].get('ListGeometriemethodeWegsegmenten#1'),
            NO_VALUE
        )
            
    def test_list_statusgebouwen(self):
        res = self.crab.list_statusgebouwen()
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListStatusGebouwen#1'),
            res
        )

    def test_list_statusgebouwen_different_sort(self):
        res = self.crab.list_statusgebouwen(2)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListStatusGebouwen#2'),
            res
        )
        from dogpile.cache.api import NO_VALUE
        self.assertEqual(
            self.crab.caches['permanent'].get('ListStatusGebouwen#1'),
            NO_VALUE
        )
            
    def test_list_geometriemethodegebouwen(self):
        res = self.crab.list_geometriemethodegebouwen()
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListGeometriemethodeGebouwen#1'),
            res
        )

    def test_list_geometriemethodegebouwen_different_sort(self):
        res = self.crab.list_geometriemethodegebouwen(2)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListGeometriemethodeGebouwen#2'),
            res
        )
        from dogpile.cache.api import NO_VALUE
        self.assertEqual(
            self.crab.caches['permanent'].get('ListGeometriemethodeGebouwen#1'),
            NO_VALUE
        )
            
    def test_list_herkomstadrespositie(self):
        res = self.crab.list_herkomstadresposities()
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListHerkomstAdresposities#1'),
            res
        )

    def test_list_herkomstadrespositie_different_sort(self):
        res = self.crab.list_herkomstadresposities(2)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['permanent'].get('ListHerkomstAdresposities#2'),
            res
        )
        from dogpile.cache.api import NO_VALUE
        self.assertEqual(
            self.crab.caches['permanent'].get('ListHerkomstAdresposities#1'),
            NO_VALUE
        )
        
    def test_list_straten(self):
        res = self.crab.list_straten(1) 
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['long'].get('ListStraatnamenWithStatusByGemeenteId#11'),
            res
        )
        
        gem = self.crab.get_gemeente_by_id(2)
        r = self.crab.list_straten(gem)
        self.assertIsInstance(r, list)
        self.assertEqual(
            self.crab.caches['long'].get('ListStraatnamenWithStatusByGemeenteId#21'),
            r
        )

    def test_list_straten_different_sort(self):
        res = self.crab.list_straten(1,2)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['long'].get('ListStraatnamenWithStatusByGemeenteId#12'),
            res
        )
        gem = self.crab.get_gemeente_by_id(2)
        r = self.crab.list_straten(gem, 2)
        self.assertIsInstance(r, list)
        self.assertEqual(
            self.crab.caches['long'].get('ListStraatnamenWithStatusByGemeenteId#22'),
            r
        )
        from dogpile.cache.api import NO_VALUE
        self.assertEqual(
            self.crab.caches['long'].get('ListStraatnamenWithStatusByGemeenteId#11'),
            NO_VALUE
        )
           

    def test_get_straat_by_id(self):
        res = self.crab.get_straat_by_id(1)
        self.assertIsInstance(res, Straat)
        self.assertEqual(
            self.crab.caches['long'].get('GetStraatnaamWithStatusByStraatnaamId#1'),
            res
        )
        

    def test_list_huisnummers_by_straat(self):
        res = self.crab.list_huisnummers_by_straat(1)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['long'].get('ListHuisnummersWithStatusByStraatnaamId#11'),
            res
        )
        straat = self.crab.get_straat_by_id(2)
        r = self.crab.list_huisnummers_by_straat(straat)
        self.assertIsInstance(r,list)
        self.assertEqual(
            self.crab.caches['long'].get('ListHuisnummersWithStatusByStraatnaamId#21'),
            r
        )

    def test_list_huisnummers_by_straat_different_sort(self):
        res = self.crab.list_huisnummers_by_straat(1,2)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['long'].get('ListHuisnummersWithStatusByStraatnaamId#12'),
            res
        )
        straat = self.crab.get_straat_by_id(2)
        r=self.crab.list_huisnummers_by_straat(straat, 2)
        self.assertIsInstance(r, list)
        self.assertEqual(
            self.crab.caches['long'].get('ListHuisnummersWithStatusByStraatnaamId#22'),
            r
        )
        
    def test_get_huisnummer_by_id(self):
        res = self.crab.get_huisnummer_by_id(1)
        self.assertIsInstance(res, Huisnummer)
        self.assertEqual(
            self.crab.caches['long'].get('GetHuisnummerWithStatusByHuisnummerId#1'),
            res
        )
        
    def test_get_huisnummer_by_nummer_and_straat(self):
        res = self.crab.get_huisnummer_by_nummer_and_straat(1,1)
        self.assertIsInstance(res, Huisnummer)
        self.assertEqual(
            self.crab.caches['long'].get('GetHuisnummerWithStatusByHuisnummer#11'),
            res
        )
        straat=self.crab.get_straat_by_id(1)
        res=self.crab.get_huisnummer_by_nummer_and_straat(1, straat)
        self.assertIsInstance(res, Huisnummer)
        self.assertEqual(
            self.crab.caches['long'].get("GetHuisnummerWithStatusByHuisnummer#11"),
            res
        )

    def test_list_postkantons_by_gemeente(self):
        res = self.crab.list_postkantons_by_gemeente(1)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['long'].get('ListPostkantonsByGemeenteId#1'),
            res
        )
        gemeente=self.crab.get_gemeente_by_id(2)
        r=self.crab.list_postkantons_by_gemeente(gemeente)
        self.assertIsInstance(r, list)
        self.assertEqual(
            self.crab.caches['long'].get('ListPostkantonsByGemeenteId#2'),
            r
        )
        
        
    def test_get_postkanton_by_huisnummer(self):
        res = self.crab.get_postkanton_by_huisnummer(1)
        self.assertIsInstance(res, Postkanton)
        self.assertEqual(
            self.crab.caches['long'].get('GetPostkantonByHuisnummerId#1'),
            res
        )
        huisnummer=self.crab.get_huisnummer_by_id(1)
        r=self.crab.get_postkanton_by_huisnummer(huisnummer)
        self.assertIsInstance(r, Postkanton)
        self.assertEqual(
            self.crab.caches['long'].get('GetPostkantonByHuisnummerId#1'),
            r
        )
        
    def test_list_wegobjecten_by_straat(self):
        res=self.crab.list_wegobjecten_by_straat(1)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['long'].get('ListWegobjectenByStraatnaamId#1'),
            res
        )
        straat=self.crab.get_straat_by_id(2)
        res=self.crab.list_wegobjecten_by_straat(straat)
        self.assertEqual(
            self.crab.caches['long'].get('ListWegobjectenByStraatnaamId#2'),
            res
        )

    def test_get_wegobject_by_id(self):
        res = self.crab.get_wegobject_by_id("53839893")
        self.assertIsInstance(res, Wegobject)
        self.assertEqual(
            self.crab.caches['long'].get('GetWegobjectByIdentificatorWegobject#53839893'),
            res
        )
    
    def test_list_wegsegmenten_by_straat(self):
        res=self.crab.list_wegsegmenten_by_straat(1)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['long'].get('ListWegsegmentenByStraatnaamId#1'),
            res
        )
        straat=self.crab.get_straat_by_id(2)
        r=self.crab.list_wegsegmenten_by_straat(straat)
        self.assertEqual(
            self.crab.caches['long'].get('ListWegsegmentenByStraatnaamId#2'),
            r
        )
        
    def test_get_wegsegment_by_id(self):
        res=self.crab.get_wegsegment_by_id("108724")
        self.assertIsInstance(res, Wegsegment)
        self.assertEqual(
            self.crab.caches['long'].get('GetWegsegmentByIdentificatorWegsegment#108724'),
            res
        )
    
    def test_list_terreinobjecten_by_huisnummer(self):
        res=self.crab.list_terreinobjecten_by_huisnummer(1)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['long'].get('ListTerreinobjectenByHuisnummerId#1'),
            res
        )
        huisnummer=self.crab.get_huisnummer_by_id(1)
        res=self.crab.list_terreinobjecten_by_huisnummer(huisnummer)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['long'].get('ListTerreinobjectenByHuisnummerId#1'),
            res
        )
        
    def test_get_terreinobject_by_id(self):
        res=self.crab.get_terreinobject_by_id("13040_C_1747_G_002_00")
        self.assertIsInstance(res, Terreinobject)
        self.assertEqual(
            self.crab.caches['long'].get('GetTerreinobjectByIdentificatorTerreinobject#13040_C_1747_G_002_00'),
            res 
        )
        
    def test_list_percelen_by_huisnummer(self):
        res=self.crab.list_percelen_by_huisnummer(1)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['long'].get('ListPercelenByHuisnummerId#1'),
            res
        )
        huisnummer=self.crab.get_huisnummer_by_id(1)
        res=self.crab.list_percelen_by_huisnummer(huisnummer)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['long'].get('ListPercelenByHuisnummerId#1'),
            res
        )
        
    def test_get_perceel_by_id(self):
        res=self.crab.get_perceel_by_id("13040C1747/00G002")
        self.assertIsInstance(res, Perceel)
        self.assertEqual(
            self.crab.caches['long'].get('GetPerceelByIdentificatorPerceel#13040C1747/00G002'),
            res
        )
        
    def test_list_gebouwen_by_huisnummer(self):
        res=self.crab.list_gebouwen_by_huisnummer(1)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['long'].get('ListGebouwenByHuisnummerId#1'),
            res
        )
        huisnummer=self.crab.get_huisnummer_by_id(1)
        res=self.crab.list_gebouwen_by_huisnummer(huisnummer)
        self.assertIsInstance(res, list)
        self.assertEqual(
            self.crab.caches['long'].get('ListGebouwenByHuisnummerId#1'),
            res
        )
        
    def test_get_gebouw_by_id(self):
        res=self.crab.get_gebouw_by_id("1538575")
        self.assertIsInstance(res, Gebouw)
        self.assertEqual(
            self.crab.caches['long'].get('GetGebouwByIdentificatorGebouw#1538575'),
            res
        )




