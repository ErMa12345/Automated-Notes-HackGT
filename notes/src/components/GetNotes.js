// // GetNotes.js

// // Function to send a POST request to the backend
// async function getNotesFromAudio(audioText) {
//     try {
//       const response = await fetch('http://127.0.0.1:8000/generate_summary_and_questions', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/x-www-form-urlencoded',
//         },
//         body: new URLSearchParams({
//           audio_text: audioText,
//         }),
//       });
  
//       if (!response.ok) {
//         throw new Error('Failed to fetch notes from the server.');
//       }
  
//       const data = await response.json();
//       return data;
//     } catch (error) {
//       console.error('Error:', error.message);
//       throw error;
//     }
//   }
  
//   // Example usage:
//   const audioText = 'Your audio text goes here'; // Replace with your actual audio text
//   getNotesFromAudio(audioText)
//     .then((notes) => {
//       console.log('Summary:', notes.summary);
//       console.log('Questions:', notes.questions);
//     })
//     .catch((error) => {
//       console.error('Error:', error.message);
//     });
  