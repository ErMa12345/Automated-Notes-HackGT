// // src/components/ChatBot.js

// import React, { useState } from 'react';
// import axios from 'axios';

// const ChatBot = () => {
//   const [inputText, setInputText] = useState('');

//   const handleSubmit = async (e) => {
//     e.preventDefault();

//     try {
//       // Send input to the Python backend
//       const response = await axios.post('http://127.0.0.1:8000/generate_summary_and_questions', { input: inputText });
//       console.log(response.data); // Handle the response as needed
//     } catch (error) {
//       console.error('Error sending data to Python:', error);
//     }
//   };

//   return (
//     <form onSubmit={handleSubmit}>
//       <label>
//         User Input:
//         <input type="text" value={inputText} onChange={(e) => setInputText(e.target.value)} />
//       </label>
//       <button type="submit">Submit</button>
//     </form>
//   );
// };

// export default ChatBot;

// src/components/ChatBot.js

import React, { useState } from 'react';
import axios from 'axios';

export default function ChatBot() {
  const [inputText, setInputText] = useState('');
  const [summary, setSummary] = useState('');
  const [questions, setQuestions] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Send input to the Python backend
      const response = await axios.post('http://127.0.0.1:8000/generate_summary_and_questions', { audio_text: inputText });
      
      // Extract summary and questions from the response
      const { summary, questions } = response.data;

      // Handle the response as needed
      console.log("Summary:", summary);
      console.log("Questions:", questions);

      // Update state to display in the UI if needed
      setSummary(summary);
      setQuestions(questions);

    } catch (error) {
      console.error('Error sending data to Python:', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          User Input:
          <input type="text" value={inputText} onChange={(e) => setInputText(e.target.value)} />
        </label>
        <button type="submit">Submit</button>
      </form>

      {/* Display the summary and questions in the UI if needed */}
      {summary && <div>Summary: {summary}</div>}
      {questions.length > 0 && (
        <div>
          Questions:
          <ul>
            {questions.map((question, index) => (
              <li key={index}>{question}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};


