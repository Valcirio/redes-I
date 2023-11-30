'use client'
import React, { useState, useContext } from 'react'
import { useRouter } from 'next/navigation'
import { Context } from '../../context/useContext'
import { data } from '../../types/atributtes'
import { PythonShell } from 'python-shell'

function App() {
  // const [isCreate, setIsCreate] = useState<boolean>(false)
  const router = useRouter()
  const [useData, setUseData] = useState<data>({
    username: '',
    room: '',
  })

  // const { user, login } = useContext(Context)

  function createRoom(){
    // login(useData)
    localStorage.setItem('user',`${useData.username}`)
    const options = {
      scriptPath: '../../server/'
    }
   
    // router.push(`/chat/${useData.room}`)
    console.log(localStorage.getItem('user'))
  }
  
  function enterRoom(){
    // login(useData)
    localStorage.setItem('user',`${useData.username}`)
    router.push(`/chat/${useData.room}`)
  }

  return (
    <>
    {/* {!isCreate && <Navigate to={`/${user?.room}`} />} */}
      <section className='pt-20 w-screen h-screen overflow-hidden 
      flex flex-col flex-nowrap justify-start items-center gap-20 
      text-white bg-head'>
        <h1>Bem-Vindo!</h1>
        <form className='w-form h-form px-16 py-8 rounded-md
        flex flex-col flex-nowrap items-center justify-center gap-8 
        border-input border-2 shadow-form' autoComplete='off'>

          <div className="w-75">
            <label htmlFor="ControlInput1" className="form-label">Nome de Usuário</label>
            <input type="text" value={useData.username} className="form-control" id="ControlInput1" onChange={(el: React.FormEvent<HTMLInputElement>)=>{
              setUseData({...useData, username: el.currentTarget.value})
            }} />
          </div>

          <div className="w-75">
            <label htmlFor="ControlInput2" className="form-label">Nome da Sala</label>
            <input type="text" value={useData.room} className="form-control" id="ControlInput2" onChange={(el: React.FormEvent<HTMLInputElement>)=>{
              setUseData({...useData, room: el.currentTarget.value})
            }} />
          </div>

          <div className="w-75 d-flex justify-content-evenly">
          <button type="button" onClick={createRoom} className="btn btn-success">Criar Sala</button>
          <button type="button" onClick={enterRoom} className="btn btn-primary">Entrar na Sala</button>
          </div>

        </form>
      </section>
      </>
  )
}

export default App
