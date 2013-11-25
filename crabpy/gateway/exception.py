# -*- coding: utf-8 -*-
'''
This module contains custom errors that can be generated by gateways.

.. versionadded:: 0.2.0
'''


class GatewayException(Exception):
    '''
    A base exception.
    '''
    pass


class GatewayRuntimeException(GatewayException):
    '''
    An exception that signifies a soap request went wrong.

    '''

    soapfault = None
    '''
    The soapfault that was generated by the service.
    '''

    def __init__(self, message, soapfault):
        GatewayException.__init__(self, message)
        self.soapfault = soapfault


class GatewayAuthenticationException(GatewayRuntimeException):
    '''
    An exception that signifies something went wrong during authentication.
    '''
    pass
