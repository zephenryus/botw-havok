import struct
from enum import Enum
from typing import List

from havok import Havok


class vector4(object):
    x: int
    y: int
    z: int
    w: int


class BroadPhaseType(Enum):
    BROADPHASE_TYPE_SAP = 0
    BROADPHASE_TYPE_TREE = 1
    BROADPHASE_TYPE_HYBRID = 2


class BroadPhaseBorderBehaviour(Enum):
    BROADPHASE_BORDER_ASSERT = 0
    BROADPHASE_BORDER_FIX_ENTITY = 1
    BROADPHASE_BORDER_REMOVE_ENTITY = 2
    BROADPHASE_BORDER_DO_NOTHING = 3


class ContactPointGeneration(Enum):
    CONTACT_POINT_ACCEPT_ALWAYS = 0
    CONTACT_POINT_REJECT_DUBIOUS = 1
    CONTACT_POINT_REJECT_MANY = 2


class SimulationType(Enum):
    SIMULATION_TYPE_INVALID = 0
    SIMULATION_TYPE_DISCRETE = 1
    SIMULATION_TYPE_CONTINUOUS = 2
    SIMULATION_TYPE_MULTITHREADED = 3


class hkpFilterType(Enum):
    HK_FILTER_UNKNOWN = 0
    HK_FILTER_NULL = 1
    HK_FILTER_GROUP = 2
    HK_FILTER_LIST = 3
    HK_FILTER_CUSTOM = 4
    HK_FILTER_PAIR = 5
    HK_FILTER_CONSTRAINT = 6


class hkpConvexListFilter(Enum):
    TREAT_CONVEX_LIST_AS_NORMAL = 0
    TREAT_CONVEX_LIST_AS_LIST = 1
    TREAT_CONVEX_LIST_AS_CONVEX = 2

class AtomType(Enum):
    pass


class ActorInfo(object):
    HashId: int
    SRTHash: int
    ShapeInfoStart: int
    ShapeInfoEnd: int

    def __init__(self, data: tuple) -> None:
        self.HashId = data[0]
        self.SRTHash = data[1]
        self.ShapeInfoStart = data[2]
        self.ShapeInfoEnd = data[3]


class ShapeInfo(object):
    ActorInfoIndex: int
    InstanceId: int
    BodyGroup: int
    BodyLayerType: int

    def __init__(self, data: tuple) -> None:
        self.ActorInfoIndex = data[0]
        self.InstanceId = data[1]
        self.BodyGroup = data[2]
        self.BodyLayerType = data[3]


class StaticCompoundInfo(object):
    Offset: int
    ActorInfo: List[ActorInfo]
    ShapeInfo: List

    def __init__(self):
        self.Offset = 0
        self.ActorInfo = []
        self.ShapeInfo = []


class hkReferencedObject(object):
    memSizeAndRefCount: int


class hkRootLevelContainerNamedVariant(object):
    name: str
    className: str
    variant: hkReferencedObject


class hkRootLevelContainer(object):
    namedVariants: List[hkRootLevelContainerNamedVariant]


class hkAabb(object):
    min: vector4
    max: vector4


class hkpCollisionFilter(object):
    prepad: int
    type: hkpFilterType
    postpad: int


class hkpConvexListFilter(object):
    hkpConvexListFilter: hkpConvexListFilter


class hkWorldMemoryAvailableWatchDog(object):
    pass


class hkpWorldCinfo(object):
    gravity: vector4
    broadPhaseQuerySize: int
    contactRestingVelocity: float
    broadPhaseType: BroadPhaseType
    broadPhaseBorderBehaviour: BroadPhaseBorderBehaviour
    mtPostponeAndSortBroadPhaseBorderCallbacks: bool
    broadPhaseWorldAabb: hkAabb
    collisionTolerance: float
    collisionFilter: hkpCollisionFilter
    convexListFilter: hkpConvexListFilter
    expectedMaxLinearVelocity: float
    sizeOfToiEventQueue: int
    expectedMinPsiDeltaTime: float
    memoryWatchDog: hkWorldMemoryAvailableWatchDog
    broadPhaseNumMarkers: int
    contactPointGeneration: ContactPointGeneration
    allowToSkipConfirmedCallbacks: bool
    solverTau: float
    solverDamp: float
    solverIterations: int
    solverMicrosteps: int
    maxConstraintViolation: float
    forceCoherentConstraintOrderingInSolver: bool
    snapCollisionToConvexEdgeThreshold: float
    snapCollisionToConcaveEdgeThreshold: float
    enableToiWeldRejection: bool
    enableDeprecatedWelding: bool
    iterativeLinearCastEarlyOutDistance: float
    iterativeLinearCastMaxIterations: int
    deactivationNumInactiveFramesSelectFlag0: int
    deactivationNumInactiveFramesSelectFlag1: int
    deactivationIntegrateCounter: int
    shouldActivateOnRigidBodyTransformChange: bool
    deactivationReferenceDistance: float
    toiCollisionResponseRotateNormal: float
    useCompoundSpuElf: bool
    maxSectorsPerMidphaseCollideTask: int
    maxSectorsPerNarrowphaseCollideTask: int
    processToisMultithreaded: bool
    maxEntriesPerToiMidphaseCollideTask: int
    maxEntriesPerToiNarrowphaseCollideTask: int
    maxNumToiCollisionPairsSinglethreaded: int
    numToisTillAllowedPenetrationSimplifiedToi: float
    numToisTillAllowedPenetrationToi: float
    numToisTillAllowedPenetrationToiHigher: float
    numToisTillAllowedPenetrationToiForced: float
    enableDeactivation: bool
    simulationType: SimulationType
    enableSimulationIslands: bool
    minDesiredIslandSize: int
    processActionsInSingleThread: bool
    allowIntegrationOfIslandsWithoutConstraintsInASeparateJob: bool
    frameMarkerPsiSnap: float
    fireCollisionCallbacks: bool


class hkpRigidBody(object):
    pass


class hkpConstraintData(object):
    userData: int  # unsigned long

class hkpConstraintAtom(object):
    type: AtomType

class hkpModifierConstraintAtom(object):
    modifierAtomSize: int
    childSize: int
    child: hkpConstraintAtom
    pad: int


class hkpConstraintInstance(object):
    owner: int  # pointer
    data: hkpConstraintData
    constraintModifiers: hkpModifierConstraintAtom
    entities: hkpEntity
    priority: 39062264
    wantRuntime: bool
    destructionRemapInfo: 39062424
    listeners: hkpConstraintInstanceSmallArraySerializeOverrideType
    name: str
    userData: int  # unsigned long
    internal: int  # pointer
    uid: int


class hkpPhysicsSystem(object):
    rigidBodies: hkpRigidBody
    constraints: hkpConstraintInstance
    actions: hkpAction
    phantoms: hkpPhantom
    name: str
    userData: int
    active: bool


class hkpPhysicsData(object):
    worldCinfo: hkpWorldCinfo
    systems: hkpPhysicsSystem


def read_string(infile):
    chars = []
    while True:
        char = infile.read(1)
        if char == b'\x00':
            return ''.join(chars)
        chars.append(char.decode('utf-8'))


def main():
    path = '../assets/G-6-2.hksc'
    havok_0 = Havok(path)
    # print(havok_0.section_header_tables.data)
    # print(havok_0.data_section_offset_table)

    static_compound_info = StaticCompoundInfo()

    with open(path, 'rb') as infile:
        infile.seek(havok_0.section_header_tables.data.start)
        static_compound_info.Offset = struct.unpack('>I', infile.read(4))[0]

        infile.seek(havok_0.section_header_tables.data.start + havok_0.data_section_offset_table[0].data)

        for _ in range(havok_0.data_section_offset_table[0].array_length):
            data = struct.unpack('>4I', infile.read(16))
            # print(data)
            static_compound_info.ActorInfo.append(ActorInfo(
                data
            ))

        infile.seek(havok_0.section_header_tables.data.start + havok_0.data_section_offset_table[1].data)

        for _ in range(havok_0.data_section_offset_table[1].array_length):
            data = struct.unpack('>2i2b2x', infile.read(12))
            # print(data)
            static_compound_info.ShapeInfo.append(ShapeInfo(
                data
            ))

        # print(static_compound_info.ActorInfo)
        # print(static_compound_info.ShapeInfo)

    havok_1 = Havok(path, static_compound_info.Offset)
    print(havok_1)

    with open(path, 'rb') as infile:
        # hkRootLevelContainer
        root_level_container = hkRootLevelContainer()
        root_level_container.namedVariants = hkRootLevelContainerNamedVariant()

        infile.seek(havok_1.section_header_tables.data.start + havok_1.data_section_offset_table[1].data)
        root_level_container.namedVariants.name = read_string(infile)
        print(root_level_container.namedVariants.name)

        infile.seek(havok_1.section_header_tables.data.start + havok_1.data_section_offset_table[2].data)
        root_level_container.namedVariants.className = read_string(infile)
        print(root_level_container.namedVariants.className)

        infile.seek(havok_1.section_header_tables.data.start + havok_1.data_section_offset_table[3].data)
        print(hex(infile.tell()))
        root_level_container.namedVariants.variant = hkReferencedObject()
        root_level_container.namedVariants.variant.memSizeAndRefCount = struct.unpack('>I', infile.read(4))[0]
        print(root_level_container.namedVariants.variant.memSizeAndRefCount)

        # hkpPhysicsData


if __name__ == "__main__":
    main()
