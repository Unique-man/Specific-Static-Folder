import React, { useEffect, useState } from "react"
import './App.css'
import FactList from "./FactList"




export default function App() {

  let [fact, update] = useState([])

  async function getData() {
    let promise = await fetch("http://127.0.0.1:8000/api/facts/?format=json")
    let result = await promise.json()
    console.log("result" ,result)
    update(result)
  }                                     
  useEffect(() => {
    getData()
  }, [])

  if (fact == 0) {
    return (
      <h1>Data loading...........</h1>
    )
  }

  return (
    <>
      <h1>Fact List</h1>
      <table>
        <tr>
          <th>ID</th>
          <th>Fact</th>
          
        </tr>
        {
          fact.map((f) => <FactList key={f.id} {...f} />)

        }
        
      </table>
    </>
  )
}

