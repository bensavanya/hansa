import React, { useEffect, useState } from "react";
import {
    Box,
    Button,
    Flex,
    Input,
    InputGroup,
    Modal,
    ModalBody,
    ModalCloseButton,
    ModalContent,
    ModalFooter,
    ModalHeader,
    ModalOverlay,
    Stack,
    Text,
    useDisclosure
} from "@chakra-ui/react";


const HansaContext = React.createContext({
  vasarlasok: [], fetchVasarlas: () => {}, boltok: [], fetchBolt: () => {}
})

const columns = [
  { label: "ID", accessor: "_id" },
  { label: "Dátum", accessor: "esemenydatumido" },
  { label: "Összeg", accessor: "vasarlasosszeg" },
  { label: "Pénztárgép ID", accessor: "penztargepazonosito" },
  { label: "Partner ID", accessor: "partnerid" },
  { label: "Bolt ID", accessor: "boltid" },
  { label: "Bolt név", accessor: "boltnev" }
 ];

export default function Vasarlasok() {
  const [vasarlasok, setVasarlas] = useState([])
  const fetchVasarlas = async (sortby = "", direction = "") => {
    console.log("fetch:" + sortby + " " + direction)
    let response;
    try{
      if (sortby === "" && direction === ""){
        response = await fetch("http://localhost:8000/vasarlas/")
      }else{
        response = await fetch("http://localhost:8000/vasarlas/sort/" + sortby + "/" + direction)
      }
    }catch{
      throw new Error("Fetch nem sikerült.")
    }
    const vasarlasok = await response.json()
    setVasarlas(vasarlasok)
  }

  const [boltok, setBolt] = useState([])
  const fetchBolt = async () => {
    const response = await fetch("http://localhost:8000/bolt")
    const boltok = await response.json()
    setBolt(boltok)
  }

  useEffect(() => {
    fetchVasarlas()
  }, [])

  useEffect(() => {
    fetchBolt()
  }, [])

  const [sortField, setSortField] = useState("");
  const [order, setOrder] = useState("asc");


  const handleSorting = (sortField, sortOrder) => {
    if (sortField) {
        console.log(sortOrder)
        var direction = ((sortOrder === "asc") ? "1" : "-1")
        console.log(direction)
        try{
          fetchVasarlas(sortField, direction)
        }catch(e){
          console.error(e)
        }
    }
};
const handleSortingChange = (accessor) => {
  const sortOrder =
      accessor === sortField && order === "asc" ? "desc" : "asc";
  setSortField(accessor);
  setOrder(sortOrder);
  handleSorting(accessor, sortOrder);
};

  return (
    <HansaContext.Provider value={{vasarlasok, boltok, fetchVasarlas, fetchBolt}}>
      <table>
        <tr>
        {columns.map(({ label, accessor }) => {
          return <th key={accessor} onClick={() => handleSortingChange(accessor)}>{label}</th>;
        })}
        </tr>
        {vasarlasok.map((vasarlas) => {
          try{
            vasarlas.boltnev = (boltok.find(bolt => {return bolt._id === vasarlas.boltid}).nev)
          }catch{}
          return (
            <tr key={vasarlas._id}>
              {columns.map(({ accessor }) => {
                const tData = vasarlas[accessor] ? vasarlas[accessor] : "——";
                return <td key={accessor}>{tData}</td>;
              })}
          </tr>
          );
        })}
      </table>
    </HansaContext.Provider>
  )
}