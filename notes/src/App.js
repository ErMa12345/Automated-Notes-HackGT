import './App.css';
import './loading.css';
import Recorder from './components/Recorder.js'
import FileUploader from './components/FileUploader';
import Notes from './components/Notes';
import { useState } from 'react';

function App() {

  return (
    <div className="App">
      <div className = "recording_section">
        <Recorder /> 
        <FileUploader />
      </div>
      <div className = "notes_section" id = "test">
        <div id = "spinner_message" style = {{display: 'none'}}>This may take a minute...</div>
        <div id = "spinner" className="lds-roller" style = {{display: 'none'}}><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
      </div>
    </div>
  );
}

export default App;
