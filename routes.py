import datetime

from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import Bolt, Vasarlas, VasarlasTetel, Cikkek

bolt_router = APIRouter()

@bolt_router.post("/", response_description="Új bolt létrehozása", status_code=status.HTTP_201_CREATED, response_model=Bolt)
def create_bolt(request: Request, bolt: Bolt = Body(...)):
    bolt = jsonable_encoder(bolt)
    new_bolt = request.app.database["bolt"].insert_one(bolt)
    created_bolt = request.app.database["bolt"].find_one(
        {"_id": new_bolt.inserted_id}
    )

    return created_bolt

@bolt_router.get("/", response_description="Az összes bolt kilistázása", response_model=List[Bolt])
def list_bolt(request: Request):
    boltok = list(request.app.database["bolt"].find(limit=100))
    return boltok

@bolt_router.get("/id/{id}", response_description="Bolt keresése id alapján", response_model=Bolt)
def find_bolt_id(id: str, request: Request):
    bolt = request.app.database["bolt"].find_one({"_id": id})
    if bolt is not None:
        return bolt
    print(bolt)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs bolt {id} ID-vel")

@bolt_router.get("/nev/{nev}", response_description="Bolt keresése nev alapján", response_model=List[Bolt])
def find_bolt_nev(nev: str, request: Request):
    if(bolt := request.app.database["bolt"].find_one({"nev": nev}) is not None):
        boltok = list(request.app.database["bolt"].find({"nev": nev}))
        return boltok
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs bolt {nev} névvel")

@bolt_router.get("/partnerid/{partnerid}", response_description="Bolt keresése partnerid alapján", response_model=List[Bolt])
def find_bolt_partnerid(partnerid: str, request: Request):
    if(bolt := request.app.database["bolt"].find_one({"partnerid": partnerid}) is not None):
        boltok = list(request.app.database["bolt"].find({"partnerid": partnerid}))
        return boltok
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs bolt {partnerid} partnerid-vel")



vasarlas_router = APIRouter()

@vasarlas_router.post("/", response_description="Új vasarlas létrehozása", status_code=status.HTTP_201_CREATED, response_model=Vasarlas)
def create_vasarlas(request: Request, vasarlas: Vasarlas = Body(...)):
    vasarlas = jsonable_encoder(vasarlas)
    if request.app.database["bolt"].find_one({"_id": vasarlas.boltid}) is not None:
        new_vasarlas = request.app.database["vasarlas"].insert_one(vasarlas)
        created_vasarlas = request.app.database["vasarlas"].find_one(
            {"_id": new_vasarlas.inserted_id}
        )
        return created_vasarlas
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs bolt {vasarlas.boltid} id-vel")

@vasarlas_router.get("/", response_description="Az összes vasarlas kilistázása", response_model=List[Vasarlas])
def list_vasarlas(request: Request):
    vasarlasok = list(request.app.database["vasarlas"].find(limit=100))
    return vasarlasok

@vasarlas_router.get("/sort/{sortby}/{direction}", response_description="Az összes vasarlas kilistázása, rendezve", response_model=List[Vasarlas])
def list_vasarlas(sortby: str, direction: int, request: Request):
    print(sortby, direction)
    vasarlasok = list(request.app.database["vasarlas"].find(limit=100).sort(sortby, direction))
    return vasarlasok

@vasarlas_router.get("/id/{id}", response_description="vasarlas keresése id alapján", response_model=Vasarlas)
def find_vasarlas_id(id: str, request: Request):
    if (vasarlas := request.app.database["vasarlas"].find_one({"_id": id})) is not None:
        return vasarlas
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs vasarlas {id} ID-vel")

@vasarlas_router.get("/esemenydatumido/{esemenydatumido}", response_description="vasarlas keresése esemenydatumido alapján", response_model=List[Vasarlas])
def find_vasarlas_esemenydatumido(esemenydatumido: str, request: Request):
    if(vasarlas := request.app.database["vasarlas"].find_one({"esemenydatumido": esemenydatumido}) is not None):
        vasarlasok = list(request.app.database["vasarlas"].find({"esemenydatumido": esemenydatumido}))
        return vasarlasok
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs vasarlas {esemenydatumido} esemenydatumidovel")

@vasarlas_router.get("/vasarlasosszeg/{vasarlasosszeg}", response_description="vasarlas keresése vasarlasosszeg alapján", response_model=List[Vasarlas])
def find_vasarlas_vasarlasosszeg(vasarlasosszeg: str, request: Request):
    if(vasarlas := request.app.database["vasarlas"].find_one({"vasarlasosszeg": vasarlasosszeg}) is not None):
        vasarlasok = list(request.app.database["vasarlas"].find({"vasarlasosszeg": vasarlasosszeg}))
        return vasarlasok
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs vasarlas {vasarlasosszeg} vasarlasosszeggel")

@vasarlas_router.get("/penztargepazonosito/{penztargepazonosito}", response_description="vasarlas keresése penztargepazonosito alapján", response_model=List[Vasarlas])
def find_vasarlas_penztargepazonosito(penztargepazonosito: str, request: Request):
    if(vasarlas := request.app.database["vasarlas"].find_one({"penztargepazonosito": penztargepazonosito}) is not None):
        vasarlasok = list(request.app.database["vasarlas"].find({"penztargepazonosito": penztargepazonosito}))
        return vasarlasok
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs vasarlas {penztargepazonosito} penztargepazonositoval")

@vasarlas_router.get("/partnerid/{partnerid}", response_description="vasarlas keresése partnerid alapján", response_model=List[Vasarlas])
def find_vasarlas_partnerid(partnerid: str, request: Request):
    if(vasarlas := request.app.database["vasarlas"].find_one({"partnerid": partnerid}) is not None):
        vasarlasok = list(request.app.database["vasarlas"].find({"partnerid": partnerid}))
        return vasarlasok
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs vasarlas {partnerid} partnerid-vel")

@vasarlas_router.get("/boltid/{boltid}", response_description="vasarlas keresése boltid alapján", response_model=List[Vasarlas])
def find_vasarlas_boltid(boltid: str, request: Request):
    if(vasarlas := request.app.database["vasarlas"].find_one({"boltid": boltid}) is not None):
        vasarlasok = list(request.app.database["vasarlas"].find({"boltid": boltid}))
        return vasarlasok
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs vasarlas {boltid} boltid-vel")

vasarlas_tetel_router = APIRouter()

@vasarlas_tetel_router.post("/", response_description="Új vasarlas_tetel létrehozása", status_code=status.HTTP_201_CREATED, response_model=VasarlasTetel)
def create_vasarlas_tetel(request: Request, vasarlas_tetel: VasarlasTetel = Body(...)):
    vasarlas_tetel = jsonable_encoder(vasarlas_tetel)
    if(request.app.database["vasarlas"].find_one({"_id": vasarlas_tetel.vasarlasid})) is not None:
        if(request.app.database["cikkek"].find_one({"_id": vasarlas_tetel.partnerctid})) is not None:
            new_vasarlas_tetel = request.app.database["vasarlas_tetel"].insert_one(vasarlas_tetel)
            created_vasarlas_tetel = request.app.database["vasarlas_tetel"].find_one(
                {"_id": new_vasarlas_tetel.inserted_id}
            )
            return created_vasarlas_tetel
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs cikk {vasarlas_tetel.partnerctid} id-vel")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs vasarlas {vasarlas_tetel.vasarlasid} id-vel")

@vasarlas_tetel_router.get("/", response_description="Az összes vasarlas_tetel kilistázása", response_model=List[VasarlasTetel])
def list_vasarlas_tetel(request: Request):
    vasarlas_tetelek = list(request.app.database["vasarlas_tetel"].find(limit=100))
    return vasarlas_tetelek

@vasarlas_tetel_router.get("/id/{id}", response_description="vasarlas_tetel keresése id alapján", response_model=VasarlasTetel)
def find_vasarlas_tetel_id(id: str, request: Request):
    if (vasarlas_tetel := request.app.database["vasarlas_tetel"].find_one({"_id": id})) is not None:
        return vasarlas_tetel
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs vasarlas_tetel {id} ID-vel")

@vasarlas_tetel_router.get("/parnterctid/{parnterctid}", response_description="vasarlas_tetel keresése parnterctid alapján", response_model=List[VasarlasTetel])
def find_vasarlas_tetel_parnterctid(parnterctid: str, request: Request):
    if(vasarlas_tetel := request.app.database["vasarlas_tetel"].find_one({"parnterctid": parnterctid}) is not None):
        vasarlas_tetelek = list(request.app.database["vasarlas_tetel"].find({"parnterctid": parnterctid}))
        return vasarlas_tetelek
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs vasarlas_tetel {parnterctid} parnterctid-vel")

@vasarlas_tetel_router.get("/vasarlasid/{vasarlasid}", response_description="vasarlas_tetel keresése vasarlasid alapján", response_model=List[VasarlasTetel])
def find_vasarlas_tetel_vasarlasid(vasarlasid: str, request: Request):
    if(vasarlas_tetel := request.app.database["vasarlas_tetel"].find_one({"vasarlasid": vasarlasid}) is not None):
        vasarlas_tetelek = list(request.app.database["vasarlas_tetel"].find({"vasarlasid": vasarlasid}))
        return vasarlas_tetelek
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs vasarlas_tetel {vasarlasid} vasarlasid-vel")

@vasarlas_tetel_router.get("/mennyiseg/{mennyiseg}", response_description="vasarlas_tetel keresése mennyiseg alapján", response_model=List[VasarlasTetel])
def find_vasarlas_tetel_mennyiseg(mennyiseg: str, request: Request):
    if(vasarlas_tetel := request.app.database["vasarlas_tetel"].find_one({"mennyiseg": mennyiseg}) is not None):
        vasarlas_tetelek = list(request.app.database["vasarlas_tetel"].find({"mennyiseg": mennyiseg}))
        return vasarlas_tetelek
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs vasarlas_tetel {mennyiseg} mennyiseggel")

@vasarlas_tetel_router.get("/brutto/{brutto}", response_description="vasarlas_tetel keresése partnerid alapján", response_model=List[VasarlasTetel])
def find_vasarlas_tetel_brutto(brutto: str, request: Request):
    if(vasarlas_tetel := request.app.database["vasarlas_tetel"].find_one({"brutto": brutto}) is not None):
        vasarlas_tetelek = list(request.app.database["vasarlas_tetel"].find({"brutto": brutto}))
        return vasarlas_tetelek
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs vasarlas_tetel {brutto} bruttoval")

@vasarlas_tetel_router.get("/partnerid/{partnerid}", response_description="vasarlas_tetel keresése boltid alapján", response_model=List[VasarlasTetel])
def find_vasarlas_tetel_partnerid(partnerid: str, request: Request):
    if(vasarlas_tetel := request.app.database["vasarlas_tetel"].find_one({"partnerid": partnerid}) is not None):
        vasarlas_tetelek = list(request.app.database["vasarlas_tetel"].find({"partnerid": partnerid}))
        return vasarlas_tetelek
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs vasarlas_tetel {partnerid} partnerid-vel")

cikkek_router = APIRouter()

@cikkek_router.post("/", response_description="Új cikk létrehozása", status_code=status.HTTP_201_CREATED, response_model=Cikkek)
def create_cikk(request: Request, cikk: Cikkek = Body(...)):
    cikk = jsonable_encoder(cikk)
    new_cikk = request.app.database["cikkek"].insert_one(cikk)
    created_cikk = request.app.database["cikkek"].find_one(
        {"_id": new_cikk.inserted_id}
    )

    return created_cikk

@cikkek_router.get("/", response_description="Az összes cikk kilistázása", response_model=List[Cikkek])
def list_cikkek(request: Request):
    cikkek = list(request.app.database["cikkek"].find(limit=100))
    return cikkek

@cikkek_router.get("/id/{id}", response_description="cikkek keresése id alapján", response_model=Cikkek)
def find_cikkek_id(id: str, request: Request):
    if (cikk := request.app.database["cikkek"].find_one({"_id": id})) is not None:
        return cikk
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs cikk {id} ID-vel")

@cikkek_router.get("/cikkszam/{cikkszam}", response_description="cikkek keresése cikkszam alapján", response_model=List[Cikkek])
def find_cikkek_cikkszam(cikkszam: str, request: Request):
    if(cikkek := request.app.database["cikkek"].find_one({"cikkszam": cikkszam}) is not None):
        cikkek = list(request.app.database["cikkek"].find({"cikkszam": cikkszam}))
        return cikkek
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs cikk {cikkszam} cikkszammal")

@cikkek_router.get("/vonalkod/{vonalkod}", response_description="cikkek keresése vonalkod alapján", response_model=List[Cikkek])
def find_cikkek_vonalkod(vonalkod: str, request: Request):
    if(cikkek := request.app.database["cikkek"].find_one({"vonalkod": vonalkod}) is not None):
        cikkek = list(request.app.database["cikkek"].find({"vonalkod": vonalkod}))
        return cikkek
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs cikk {vonalkod} vonalkodal")

@cikkek_router.get("/nev/{nev}", response_description="cikkek keresése nev alapján", response_model=List[Cikkek])
def find_cikkek_nev(nev: str, request: Request):
    if(cikkek := request.app.database["cikkek"].find_one({"nev": nev}) is not None):
        cikkek = list(request.app.database["cikkek"].find({"nev": nev}))
        return cikkek
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs cikk {nev} mennyiseggel")

@cikkek_router.get("/mennyisegiegyseg/{mennyisegiegyseg}", response_description="cikkek keresése mennyisegiegyseg alapján", response_model=List[Cikkek])
def find_cikkek_mennyisegiegyseg(mennyisegiegyseg: str, request: Request):
    if(cikkek := request.app.database["cikkek"].find_one({"mennyisegiegyseg": mennyisegiegyseg}) is not None):
        cikkek = list(request.app.database["cikkek"].find({"mennyisegiegyseg": mennyisegiegyseg}))
        return cikkek
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs cikk {mennyisegiegyseg} mennyisegiegyseggel")

@cikkek_router.get("/nettoegysegar/{nettoegysegar}", response_description="cikkek keresése nettoegysegar alapján", response_model=List[Cikkek])
def find_cikkek_nettoegysegar(nettoegysegar: str, request: Request):
    if(cikkek := request.app.database["cikkek"].find_one({"nettoegysegar": nettoegysegar}) is not None):
        cikkek = list(request.app.database["cikkek"].find({"nettoegysegar": nettoegysegar}))
        return cikkek
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs cikk {nettoegysegar} nettoegysegarral")

@cikkek_router.get("/verzio/{verzio}", response_description="cikkek keresése verzio alapján", response_model=List[Cikkek])
def find_cikkek_verzio(verzio: str, request: Request):
    if(cikkek := request.app.database["cikkek"].find_one({"verzio": verzio}) is not None):
        cikkek = list(request.app.database["cikkek"].find({"verzio": verzio}))
        return cikkek
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs cikk {verzio} verzioval")

@cikkek_router.get("/partnerid/{partnerid}", response_description="cikkek keresése partnerid alapján", response_model=List[Cikkek])
def find_cikkek_partnerid(partnerid: str, request: Request):
    if(cikkek := request.app.database["cikkek"].find_one({"partnerid": partnerid}) is not None):
        cikkek = list(request.app.database["cikkek"].find({"partnerid": partnerid}))
        return cikkek
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nincs cikk {partnerid} partnerid-vel")