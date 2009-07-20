"""Modules - pipeline processing modules for CellProfiler

CellProfiler is distributed under the GNU General Public License.
See the accompanying file LICENSE for details.

Developed by the Broad Institute
Copyright 2003-2009

Please see the AUTHORS file for credits.

Website: http://www.cellprofiler.org
"""
__version__="$Revision$"
from align import Align
from applythreshold import ApplyThreshold
from calculatemath import CalculateMath
from colortogray import ColorToGray
from converttoimage import ConvertToImage
from correctillumination_calculate import CorrectIllumination_Calculate
from correctillumination_apply import CorrectIllumination_Apply
from crop import Crop
from enhanceorsuppressspeckles import EnhanceOrSuppressSpeckles
from exporttodatabase import ExportToDatabase
from exporttoexcel import ExportToExcel
from filterbyobjectmeasurement import FilterByObjectMeasurement
from findedges import FindEdges
from graytocolor import GrayToColor
from identifyprimautomatic import IdentifyPrimAutomatic
from identifysecondary import IdentifySecondary
from identifytertiarysubregion import IdentifyTertiarySubregion
from imagemath import ImageMath
from loadimages import LoadImages
from loadsingleimage import LoadSingleImage
from loadtext import LoadText
from makeprojection import MakeProjection
from maskimage import MaskImage
from measurecorrelation import MeasureCorrelation
from measureimageareaoccupied import MeasureImageAreaOccupied
from measureimageintensity import MeasureImageIntensity
from measureimagequality import MeasureImageQuality
from measureobjectintensity import MeasureObjectIntensity
from measureobjectareashape import MeasureObjectAreaShape
from measureobjectneighbors import MeasureObjectNeighbors
from measuretexture import MeasureTexture
from morph import Morph
from overlay_outlines import OverlayOutlines
from relate import Relate
from rescaleintensity import RescaleIntensity
from saveimages import SaveImages
from smooth import Smooth

def get_module_classes():
    return [Align,
            ApplyThreshold,
            CalculateMath,
            ColorToGray,
            ConvertToImage,
            CorrectIllumination_Calculate,
            CorrectIllumination_Apply,
            Crop,
            EnhanceOrSuppressSpeckles,
            ExportToDatabase,
            ExportToExcel,
            FindEdges,
            FilterByObjectMeasurement,
            GrayToColor,
            IdentifyPrimAutomatic,
            IdentifySecondary,
            IdentifyTertiarySubregion,
            ImageMath,
            LoadImages,
            LoadSingleImage,
            LoadText,
            MakeProjection,
            MaskImage,
            MeasureCorrelation,
            MeasureImageAreaOccupied,
            MeasureImageIntensity,
            MeasureImageQuality,
            MeasureObjectAreaShape,
            MeasureObjectIntensity,
            MeasureObjectNeighbors,
            MeasureTexture,
            Morph,
            OverlayOutlines,
            Relate,
            RescaleIntensity,
            SaveImages,
            Smooth ]

def get_module_substitutions():
    """Return a dictionary of matlab module names and replacement classes
    
    """
    return {"Align": Align,
            "ApplyThreshold": ApplyThreshold,
            "CalculateMath": CalculateMath,
            "ColorToGray":ColorToGray,
            "ConvertToImage":ConvertToImage,
            "CorrectIllumination_Calculate":CorrectIllumination_Calculate,
            "CorrectIllumination_Apply":CorrectIllumination_Apply,
            "Crop": Crop,
            "ExportToDatabase": ExportToDatabase,
            "ExportToExcel": ExportToExcel,
            "FindEdges": FindEdges,
            "FilterByObjectMeasurement": FilterByObjectMeasurement,
            "GrayToColor":GrayToColor,
            "IdentifyPrimAutomatic":IdentifyPrimAutomatic,
            "IdentifySecondary":IdentifySecondary,
            "IdentifyTertiarySubregion":IdentifyTertiarySubregion,
            "ImageMath":ImageMath,
            "KeepLargestObject":FilterByObjectMeasurement,
            "LoadImages":LoadImages,
            "LoadSingleImage":LoadSingleImage,
            "LoadText":LoadText,
            "MakeProjection":MakeProjection,
            "MaskImage": MaskImage,
            "MeasureCorrelation": MeasureCorrelation,
            "MeasureImageAreaOccupied": MeasureImageAreaOccupied,
            "MeasureImageIntensity": MeasureImageIntensity,
            "MeasureImageQuality": MeasureImageQuality,
            "MeasureObjectAreaShape": MeasureObjectAreaShape,
            "MeasureObjectIntensity": MeasureObjectIntensity,
            "MeasureObjectNeighbors": MeasureObjectNeighbors,
            "MeasureTexture": MeasureTexture,
            "Morph": Morph,
            "OverlayOutlines": OverlayOutlines,
            "Relate": Relate,
            "RescaleIntensity": RescaleIntensity,
            "SaveImages": SaveImages,
            "SmoothOrEnhance": Smooth
            }
    

 
