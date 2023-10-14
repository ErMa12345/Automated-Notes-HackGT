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
        console.log(url)
        addAudioComponent([...audioComponents, <AudioElement data = {url} key={url}/>])
    };

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
        <br />
    </div>
  );
}

