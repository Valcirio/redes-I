'use client'
import React, { useContext, useEffect, useState } from 'react'
import Image from 'next/image'
import arrow from '@/assets/arrow-right-solid.svg'
import { messageProps } from '@/types/atributtes'
import Message from '@/components/message'
import axios from 'axios'
// import { Context } from '@/context/useContext'

// type chatProps = {
//   username: string
// }


function Chat({ params }: { params: { id: string }}){

    const [textData, setTextData] = useState<messageProps[]>([])
    const [textInput, setTextInput] = useState<string>('')
//   const { user } = useContext(Context)
    function sendMessage(){
      axios.get('http://localhost:7777/').then(res=>console.log(textInput))
    }
  return (
    <section className='w-screen h-screen overflow-hidden flex
    flex-col flex-nowrap justify-between items-center'>
      <header className='w-full h-[10%] flex flex-nowrap justify-between items-center px-16 bg-head text-white'>
        <h2>Olá, {localStorage.getItem('user')}.</h2>
        <h3>Sala {params.id}.</h3>
        <button type="button" className="btn btn-danger">Sair</button>
      </header>
      <div className='w-full h-4/5 bg-main'>
        {textData.map((el, index)=>{
            return <Message key={index} text={el.text} time={el.time} user={el.user} />
        })}
      </div>
      <footer className='py-4 px-16 w-full h-[10%]
      flex flex-nowrap justify-center gap-32 items-center bg-input text-white'>
        <input type="text" className='w-[70%] form-control' value={textInput} onChange={(el: React.FormEvent<HTMLInputElement>)=>{
            setTextInput(el.currentTarget.value)
        }} />
        <button className='p-2 w-16 h-16 border-none rounded-full' onClick={sendMessage}><Image className='teste w-100 h-100' src={arrow} alt="send" /></button>
      </footer>
    </section>
  )
}

export default Chat