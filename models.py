import uuid
import datetime

from typing import Optional
from pydantic import BaseModel, Field

#bolt modelek
class Bolt(BaseModel):
    id: int = Field(default_factory=uuid.uuid4, alias="_id")
    nev: str = Field(...)
    partnerid: int = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "2011076",
                "nev": "Példa Bolt 1",
                "partnerid": "2011068"
            }
        }


#vasarlas modelek
class Vasarlas(BaseModel):
    id: int = Field(default_factory=uuid.uuid4, alias="_id")
    esemenydatumido: datetime.datetime = Field(...)
    vasarlasosszeg: float = Field(...)
    penztargepazonosito: int = Field(...)
    partnerid: int = Field(...)
    boltid: int = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "76571665",
                "esemenydatumido": "2020-05-30T08:12:38",
                "vasarlasosszeg": "17676",
                "penztargepazonosito": "10",
                "partnerid": "2011068",
                "boltid": "2011076"
            }
        }


#vasarlas-tetel modelek
class VasarlasTetel(BaseModel):
    id: int = Field(default_factory=uuid.uuid4, alias="_id")
    parnterctid: int = Field(...)
    vasarlasid: int = Field(...)
    mennyiseg: float = Field(...)
    brutto: float = Field(...)
    partnerid: int = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "77782946",
                "parnterctid": "20875",
                "vasarlasid": "77782939",
                "mennyiseg": "24",
                "brutto": "4896",
                "partnerid": "2011068"
            }
        }


#cikkek modelek
class Cikkek(BaseModel):
    id: int = Field(default_factory=uuid.uuid4, alias="_id")
    cikkszam: str = Field(...)
    vonalkod: str = Field(...)
    nev: str = Field(...)
    mennyisegiegyseg: str = Field(...)
    nettoegysegar: float = Field(...)
    verzio: int = Field(...)
    partnerid: int = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "42109869",
                "cikkszam": "81500",
                "vonalkod": "5998817312025",
                "nev": "Kozel pre.sör d.0,5l",
                "mennyisegiegyseg": "db",
                "nettoegysegar": "227.56",
                "verzio": "45584203",
                "partnerid": "2011068"
            }
        }
