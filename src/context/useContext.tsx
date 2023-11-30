import React, {useState, createContext} from "react";
import { data } from "../types/atributtes";

type contextProps = {
    user: data | null,
    login: (user: data) => void
}

export const Context = createContext<contextProps>({} as contextProps)

export default function ContextProvider({children}:{children: React.ReactNode}){
    const [user, setUser] = useState<data | null>(null)
    function login(user: data){
        setUser(user)
    }
    return(
        <Context.Provider value={{ user, login }}>
            {children}
        </Context.Provider>
    )
}