from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Types(str, Enum):
    ITEM = "Item"
    CARD = "Card"
    TRINKET = "Trinket"
    PILL = "Pill"
    PICKUP = "Pickup"
    TRANSFORMATION = "Transformation"
    ACHIEVEMENT = "Achievement"
    CHARACTER = "Character"


@dataclass
class Generic:
    name: str
    function: str
    type: Types


@dataclass()
class Pickup(Generic):
    probability: str


@dataclass()
class Transformation(Generic):
    item_list: list[str]


@dataclass
class Item(Generic):
    id: int
    pickup: str
    quality: int
    unlock: Optional[str]
    pool: Optional[str]
    recharge: Optional[str]
    item_type: str


@dataclass
class Trinket(Generic):
    id: int
    pickup: str
    unlock: Optional[str]


@dataclass
class Card(Generic):
    id: int
    pickup: Optional[str]
    unlock: Optional[str]


@dataclass
class Pill(Generic):
    horse_pill: str
    id: int


@dataclass
class Urls:
    type: Types
    url: str
    id: int


@dataclass()
class PickUrl:
    type: Types
    url: str
    name: str

@dataclass()
class Achievement:
    secret_number: int
    unlock: str
    name: str
    description: Optional[str]
    type: Types

@dataclass()
class Character:
    link: str
    name: str
    health: dict
    damage: str
    tears: str
    shot_speed: str
    range_: str
    speed: str
    luck: str
    items: list
    unlock: str
    type_: Types
