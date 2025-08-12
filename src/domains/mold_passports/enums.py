from enum import Enum


# Instead of "Facing Sand" and "Backing Sand"
class MoldingSandSystem(str, Enum):
    """
    Defines the sand system strategy used for creating a mold. This determines the composition and
    layering of the molding sand.

    LAYERED: A composite system using two types of sand. A high-quality 'Facing Sand' is applied
    to the pattern surface, and the rest of the flask is filled with 'Backing Sand'. Used for high
    surface quality requirements.

    UNITARY: A single, homogenous sand system (typically 'System Sand') is used for the entire mold.
    Common in automated foundries where sand is continuously reclaimed and conditioned.
    """
    LAYERED = "layered"
    UNITARY = "unitary"
