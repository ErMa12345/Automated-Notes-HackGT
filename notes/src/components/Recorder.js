import * as React from 'react';
import { AudioRecorder } from 'react-audio-voice-recorder';
import AudioElement from './AudioElement'
import * as ReactDOM from 'react-dom'
import { createRoot } from 'react-dom/client';
import { useState } from 'react';

export default function Recorder() {
    const [audioComponents, addAudioComponent] = useState([])

    function addAudioElement(blob) {
        const url = URL.createObjectURL(blob)
        const formData = new FormData();
        const transcriptionResult = document.getElementById('transcriptionResult')

        formData.append('audioFile', blob)

        fetch('http://127.0.0.1:5000/upload-audio', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            transcriptionResult.textContent = data.transcription;
        })
        .catch(error => {
            console.error('error')
        })
        addAudioComponent([...audioComponents, <AudioElement data = {url} key={url}/>])
    };

    function transcribeAudio() {
        const audioFileInput = document.getElementById('audioFileInput');
        const transcriptionResult = document.getElementById('transcriptionResult')

        const audioFile = audioFileInput.files[0]
        const formData = new FormData();
        formData.append('audioFile', audioFile);

        fetch('http://127.0.0.1:5000/upload-audio', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            transcriptionResult.textContent = data.transcription;
        })
        .catch(error => {
            console.error('error')
        })
    }

    return (
        <div className = "recorder_component">
            <h1>Record Your Lecture</h1>
            <AudioRecorder
                onRecordingComplete={(blob) => addAudioElement(blob)}
                audioTrackConstraints={{
                noiseSuppression: true,
                echoCancellation: true,
                }}
                onNotAllowedOrFound={(err) => console.table(err)}
                downloadOnSavePress={true}
                downloadFileExtension="webm"
                mediaRecorderOptions={{
                audioBitsPerSecond: 128000,
                }}
                showVisualizer={true}
                className = "audio_recorder"
            />
            {audioComponents.map((audioComponent) => audioComponent)}

            <h1>Or, alternatively upload a file</h1>
            <input type="file" id="audioFileInput"></input>
            <button onClick={transcribeAudio} >Transcribe</button>
            <p id="transcriptionResult"></p>
            <br />
        </div>
    );
}


