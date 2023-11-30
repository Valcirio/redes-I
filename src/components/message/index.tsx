import { messageProps } from "@/types/atributtes"

export default function Message({user, text, time}: messageProps){

    return(
      <article className="card text-bg-primary w-fit h-fit max-w-[80%]">
        <div className="card-header">
          {user}
        </div>
        <div className="card-body py-0 h-fit">
            <p className="m-1">{text}</p>
            <p className="text-sm py-0 m-0 card-footer text-body-secondary">{time}</p>
        </div>
      </article>
    )
}