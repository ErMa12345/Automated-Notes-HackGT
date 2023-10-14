import { useState, useRef } from "react";
import { createRoot } from 'react-dom/client';
import Notes from './Notes';

export default function FileUploader(props) {
  const { data } = props
  
  const hiddenFileInput = useRef(null);
  const [buttonName, setButtonName] = useState("Upload a file")
  const [fileUploaded, setFileUploaded] = useState(false)

  const handleClick = (event) => {
    hiddenFileInput.current.click();
  };

  const handleChange = (event) => {
    const fileUploaded = event.target.files[0];
    setButtonName(fileUploaded.name)
    setFileUploaded(true)
  };

  function transcribeAudio() {
    const audioFileInput = document.getElementById('audioFileInput');
    // const transcriptionResult = document.getElementById('transcriptionResult')
    const audioFile = audioFileInput.files[0]
    const formData = new FormData();
    formData.append('audioFile', audioFile);
    
    const spinner = document.getElementById('spinner')
    const spinner_message = document.getElementById('spinner_message')
    spinner.style.display = 'block'
    spinner_message.style.display = 'block'

    fetch('http://127.0.0.1:5000/upload-audio', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        // transcriptionResult.textContent = data.transcription;
        spinner.style.display = 'none';
        spinner_message.style.display = 'none'
        document.getElementById('generate_notes').style.display = 'none';
        const domNode = document.getElementById('test');
        const root = createRoot(domNode);
        root.render(<Notes />)
    })
    .catch(error => {
        console.error('error: ', error)
    })
  }

  return (
    <div className = "upload_file_component">
        <h1>...or, upload a file</h1>
        <div className = "file_uploader_component">
            <button className="button_upload" onClick={handleClick}>{buttonName}</button>
            <input
                type="file"
                onChange={handleChange}
                ref={hiddenFileInput}
                style={{ display: "none" }}
                id="audioFileInput"
            />
            {fileUploaded ? <div className="generate_notes" id = "generate_notes" onClick = {transcribeAudio}>Generate Notes!</div>: <></>}
        </div>
    </div>
    
  );
};
