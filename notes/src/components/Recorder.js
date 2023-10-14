  import * as React from 'react';
  import { AudioRecorder } from 'react-audio-voice-recorder';

  export default function Recorder() {
    const addAudioElement = (blob) => {
      const formData = new FormData();
      formData.append('audioFile', blob, 'audio.webm')
      const url = URL.createObjectURL(blob);
      const audio = document.createElement('audio');
      audio.src = url;
      audio.controls = true;
      document.body.appendChild(audio);
      uploadAudio(formData);
    };

    const uploadAudio = async (fileLocation) => {
      try {
        const response = await fetch('http://127.0.0.1:5000/upload-audio', {
          method: 'POST',
          headers: {
            'audioFile': 'application/json',
          },
          body: fileLocation,
        });
    
        const result = await response.json();
        console.log(result.message);
      } catch (error) {
        console.error('Error uploading audio:', error);
      }
    };

    return (
      <div>
        <AudioRecorder
          onRecordingComplete={addAudioElement}
          audioTrackConstraints={{
            noiseSuppression: true,
            echoCancellation: true,
          }}
          onNotAllowedOrFound={(err) => console.table(err)}
          downloadOnSavePress={true}
          downloadFileExtension="mp3"
          mediaRecorderOptions={{
            audioBitsPerSecond: 128000,
          }}
          showVisualizer={true}
        />
        <br />
      </div>
    );
  }

