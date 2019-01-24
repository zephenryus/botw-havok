from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclBufferSetupObject import hclBufferSetupObject
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput


class hclBlendSetupObject(hclOperatorSetupObject):
    name: str
    A: hclBufferSetupObject
    B: hclBufferSetupObject
    C: hclBufferSetupObject
    vertexSelection: hclVertexSelectionInput
    blendWeights: hclVertexFloatInput
    mapToScurve: bool
    blendNormals: bool
    blendTangents: bool
    blendBitangents: bool