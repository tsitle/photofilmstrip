# -*- coding: utf-8 -*-
#
# PhotoFilmStrip - Creates movies out of your pictures.
#
# Copyright (C) 2008 Jens Goepfert
#

import base64
import io

import wx

try:
    import cairosvg
    _HAVE_CAIROSVG = True
except ImportError:
    _HAVE_CAIROSVG = False
_HAVE_SVGLIB = False
if not _HAVE_CAIROSVG:
    try:
        from svglib.svglib import SvgRenderer
        from reportlab.graphics import renderPM
        _HAVE_SVGLIB = True
    except ImportError:
        SvgRenderer = None
        renderPM = None
from PIL import Image

import photofilmstrip.res.images


class ArtProvider:

    provider = None

    @classmethod
    def Init(cls):
        if cls.provider is None:
            cls.provider = Res2PyArtProvider(
                photofilmstrip.res.images,
                artIdPrefix='PFS_'
            )
            wx.ArtProvider.Push(cls.provider)


class Res2PyArtProvider(wx.ArtProvider):

    def __init__(self, imageModule, artIdPrefix='wxART_'):
        self.catalog = imageModule.catalog
        self.index = imageModule.index
        self.artIdPrefix = artIdPrefix

        wx.ArtProvider.__init__(self)

    def CreateBitmap(self, artId, artClient, size):
        if size[0] == -1 or size[1] == -1:
            size = wx.ArtProvider.GetSizeHint(artClient)

        if artId.startswith(self.artIdPrefix):
            name = artId[len(self.artIdPrefix):]
            if name in self.catalog:
                return self.DataToBitmap(self.catalog[name], size)

        return wx.NullBitmap

    @staticmethod
    def __load_svg_from_bytes(data: bytes, resolve_entities=False):
        if not _HAVE_SVGLIB:
            return None
        try:
            from lxml import etree
        except ImportError:
            return None
        parser = etree.XMLParser(
                remove_comments=True,
                recover=True,
                resolve_entities=resolve_entities
            )
        import logging
        try:
            svgRoot = etree.fromstring(data, parser=parser)
        except Exception as exc:
            logging.error("Failed to load input file! (%s)", exc)
            return None
        else:
            return svgRoot

    @staticmethod
    def __svg_to_wxbitmap(data: bytes, size: wx.Size):
        """
        Convert an SVG bytestring into a wx.Bitmap object
        """
        if _HAVE_CAIROSVG:
            # convert SVG (as bytestring) into a PNG (as bytestring)
            pngByteStr = cairosvg.svg2png(
                    bytestring=data.decode("utf-8"),
                    write_to=None,
                    dpi=96,
                    output_width=size.width,
                    output_height=size.height
                )
        elif _HAVE_SVGLIB:
            # convert the SVG (as bytestring) to a ReportLab drawing
            svgRoot = Res2PyArtProvider.__load_svg_from_bytes(data)
            if svgRoot is None:
                return None
            svgRenderer = SvgRenderer("/dummy/path")  # pylint: disable=possibly-used-before-assignment
            drawing = svgRenderer.render(svgRoot)
            # resize the drawing
            scaleX = size.width / drawing.width
            scaleY = size.height / drawing.height
            scale = min(scaleX, scaleY)  # keep aspect ratio
            drawing.width *= scale
            drawing.height *= scale
            drawing.scale(scale, scale)
            # render the drawing as a pixel map and output as PNG (as bytestring)
            pngByteStr = renderPM.drawToString(drawing, fmt="PNG", dpi=96)  # pylint: disable=possibly-used-before-assignment
        else:
            return None
        # convert the PNG bytestring into a Pillow image
        pngImage = Image.open(io.BytesIO(pngByteStr))
        # ensure the image is in RGB mode
        if pngImage.mode != "RGBA":
            pngImage = pngImage.convert("RGBA")
        # convert the Pillow image to raw data
        imgDataRgb = pngImage.tobytes("raw", "RGB")
        imgDataAlpha = pngImage.tobytes("raw", "A")
        # create a wx.Image from the raw data
        wxImage = wx.Image(pngImage.width, pngImage.height)
        wxImage.SetData(imgDataRgb)
        wxImage.SetAlpha(imgDataAlpha)
        wxImage.Rescale(size.width, size.height, wx.IMAGE_QUALITY_HIGH)
        # convert wx.Image to wx.Bitmap
        return wxImage.ConvertToBitmap()

    def DataToBitmap(self, data, size: wx.Size):
        data = base64.b64decode(data)
        if data.startswith(b"<?xml") or data.startswith(b"<svg"):
            bmp = self.__svg_to_wxbitmap(data, size)
            if bmp and bmp.IsOk():
                return bmp
            else:
                return wx.NullBitmap
        else:
            stream = io.BytesIO(data)
            wxImg = wx.Image(stream)
            if wxImg.IsOk():
                return wx.Bitmap(wxImg)
            else:
                return wx.NullBitmap
