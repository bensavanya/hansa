import React from "react";
import { render } from 'react-dom';
import { ChakraProvider } from "@chakra-ui/react";

import Header from "./components/Header";
import Vasarlasok from "./components/Hansa";

function App() {
  return (
    <ChakraProvider>
      <Header />
      <Vasarlasok />
    </ChakraProvider>
  )
}

const rootElement = document.getElementById("root")
render(<App />, rootElement)
