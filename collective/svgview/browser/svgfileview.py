from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from collective.svgview import svgviewMessageFactory as _


class ISVGFileView(Interface):
    """
    SVGFile view interface
    """


class SVGFileView(BrowserView):
    """
    SVGFile browser view
    """
    implements(ISVGFileView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()


class SVGFileRawView(BrowserView):

    def __call__(self):
        self.request.RESPONSE.setHeader('Content-Type', self.context.content_type)
        return self.context
