import React, { useState } from 'react';

const AskQuestion = () => {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  const askQuestion = () => {
    // Make a POST request to the "/ask_question" endpoint
    fetch('http://127.0.0.1:5000/ask_question', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: new URLSearchParams({
        question: question,
      }),
    })
      .then(response => response.json())
      .then(data => {
        // Set the answer in the state
        setAnswer(data.answer);
        // Clear the input field for the next question
        setQuestion('');
      })
      .catch(error => {
        console.error('Error:', error);
        // Set an error message in the state
        setAnswer('An error occurred.');
        // Clear the input field for the next question
        setQuestion('');
      });
  };

  return (
    <div classname = "ask_question">
      <h2>Ask a Question</h2>

      <label htmlFor="question">Enter your question:</label>
      <input
        type="text"
        id="question"
        placeholder="Type your question here"
        value={question}
        onChange={e => setQuestion(e.target.value)}
      />
      <button onClick={askQuestion}>Ask</button>

      <div>
        <h2>Answer:</h2>
        <p>{answer}</p>
      </div>
    </div>
  );
};

export default AskQuestion;
