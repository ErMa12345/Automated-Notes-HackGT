import { useState } from 'react';

export default function AudioElement(props) {
    const url = props["data"]
    const [lectureName, setLectureName] = useState("my_lecture_"+ new Date().toJSON())

    function changeName(event) {
        setLectureName(event.target.value)
    }

    return (
        <div className = "audio_element_component">
            <audio controls src={url}></audio>
            <input type = "text" value = {lectureName} onChange={changeName} className = "input_lecture_name"/>
        </div>
    )
}