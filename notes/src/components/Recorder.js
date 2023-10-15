import * as React from 'react';
import { AudioRecorder } from 'react-audio-voice-recorder';
import AudioElement from './AudioElement';
import AskQuestion from './AskQuestion';  // Import AskQuestion component
import { useState } from 'react';

export default function Recorder() {
  const [audioComponents, addAudioComponent] = useState([]);

  function addAudioElement(blob) {
    const url = URL.createObjectURL(blob);
    const formData = new FormData();
    const transcriptionResult = document.getElementById('transcriptionResult');

    formData.append('audioFile', blob);

    fetch('http://127.0.0.1:5000/upload-audio', {
      method: 'POST',
      body: formData,
    })
      .then(response => response.json())
      .then(data => {
        console.log(data);
        transcriptionResult.textContent = data.transcription;
      })
      .catch(error => {
        console.error('error');
      });
    addAudioComponent([...audioComponents, <AudioElement data={url} key={url} />]);
  }

  return (
    <div className="recorder_component">
      {/* Title added to the middle top of the screen */}
      <h1 style={{ textAlign: 'center', marginTop: '20px', fontSize: '50px', fontFamily: 'Monaco, monospace', whiteSpace: 'nowrap' }}>Study Buddy</h1>

      <h2>Record Your Lecture</h2>
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
        className="audio_recorder"
        
      />

      {audioComponents.map((audioComponent) => audioComponent)}
      <br />

      {/* Render the AskQuestion component below the file upload section */}
      <AskQuestion className="ask_question" />
    </div>
  );
}
