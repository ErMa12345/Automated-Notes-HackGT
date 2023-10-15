import { useState } from 'react'

export default function Notes(props) {
    // const { data } = props['sum']
    const summary = props['sum'][0].split("\n")
    const questions = props['sum'][1]
    // console.log(props['sum'])
    // const full_notes = data['summary'].split("Practice problems:")
    // console.log(full_notes)
    // const notes = full_notes[0].split("\n")
    // const questions = full_notes[1].split("\n")
    const [showQuestions, setShowQuestions] = useState(false)

    function handleClick() {
        setShowQuestions(true)
        document.getElementById("generate_questions_button").style.display = 'none'
    }

    return (
        <div>
            <div className = "notes">
                <h1 style = {{align_self: 'center'}}>Notes</h1>
                {summary.map((note) => <p>{note}</p>)}
            </div>
            <div className = "practice_problems">
                <button className="button_upload" id = "generate_questions_button" onClick = {handleClick}>Generate practice problems?</button>
                {showQuestions ? 
                <div>
                    <h1>Practice Problems</h1>
                    {questions.map((question) => <p>{question}</p>)}
                </div> : <></>}
            </div>
        </div>
    )
}