//voices snipet
//function App() {
 // const [voices, setVoices] = useState([]);
 // const [selectedVoice, setSelectedVoice] = useState('');
 // const [text, setText] = useState('');
  //const [audioUrl, setAudioUrl] = useState('');

 // useEffect(() => {
 //   fetch('http://localhost:5000/api/voices')
  //    .then(response => response.json())
  //    .then(data => {
  //      const voiceArray = Object.keys(data).map(voiceId => ({
   //       id: voiceId,
    //      name: data[voiceId].name,
    //      language: data[voiceId].language
    //    }));
     //   setVoices(voiceArray);
    //  })
    //  .catch(error => console.error('Error fetching voices:', error));
  //}, []);

  //const renderVoiceOptions = () => {
  //  return voices.map(voice => (
   //   <option key={voice.id} value={voice.id}>
      //  {`${voice.name} (${voice.language})`}
  //  </option>
  //  ));
//  };
// app.js code
import React, { useState, useEffect } from 'react';
// import { pipeline } from '@xenova/transformers';

function App() {
  const [voices, setVoices] = useState([]);
  const [selectedVoice, setSelectedVoice] = useState('');
  const [text, setText] = useState('');
  const [audioUrl, setAudioUrl] = useState('');
  // const [translation, setTranslation] = useState('');

  useEffect(() => {
    fetch('http://localhost:5000/api/voices')
      .then(response => response.json())
      .then(data => {
        setVoices(Object.values(data));
      })
      .catch(error => console.error('Error fetching voices:', error));
  }, []);

  const convertTextToSpeech = () => {
    fetch('http://localhost:5000/api/tts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        voice: selectedVoice,
        text: text
      })
    })
    .then(response => response.blob())
    .then(blob => {
      const audioUrl = URL.createObjectURL(blob);
      setAudioUrl(audioUrl);
    })
    .catch(error => console.error('Error converting text to speech:', error));
  };
 

  return (
    <div>
      <h1>OpenTTS Web App</h1>
      <div>
        <label htmlFor="voice">Select Voice:</label>
        <select id="voice" value={selectedVoice} onChange={e => setSelectedVoice(e.target.value)}>
          <option value="">Select...</option>
          {voices.map(voice => (
            <option key={voice.id} value={voice.id}>{voice.name}</option>
          ))}
        </select>
      </div>
      <div>
        <label htmlFor="text">Enter Text:</label>
        <input type="text" id="text" value={text} onChange={e => setText(e.target.value)} />
        <p>{text}</p>
      </div>
      <div>
        <button onClick={convertTextToSpeech}>Convert to Speech</button>
        {/* <button onClick={translateText}>Translate</button> */}
      </div>
      {audioUrl && <audio src={audioUrl} controls />}
      {/* {translation && (
        <div>
          <h3>Translation:</h3>
          <p>{translation}</p>
        </div>
      )} */}
    </div>
  );
}

export default App;



// import React, { useState, useEffect } from 'react';

// function App() {
//   const [voices, setVoices] = useState([]);
//   const [selectedVoice, setSelectedVoice] = useState('');
//   const [text, setText] = useState('');
//   const [audioUrl, setAudioUrl] = useState('');

//   useEffect(() => {
//     fetch('http://localhost:5000/api/voices')
//       .then(response => response.json())
//       .then(data => {
//         setVoices(data); // Assuming API returns voices directly as an array
//       })
//       .catch(error => console.error('Error fetching voices:', error));
//   }, []);

//   const convertTextToSpeech = () => {
//     // Translate text before converting to speech
//     fetch('http://localhost:5000/translate', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json'
//       },
//       body: JSON.stringify({
//         text: text
//       })
//     })
//     .then(response => response.json())
//     .then(data => {
//       const translatedText = data.translated_text;

//       // Call Flask API to convert translated text to speech
//       fetch('http://localhost:5000/api/tts', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({
//           voice: selectedVoice,
//           text: translatedText
//         })
//       })
//       .then(response => response.blob())
//       .then(blob => {
//         const audioUrl = URL.createObjectURL(blob);
//         setAudioUrl(audioUrl);
//       })
//       .catch(error => console.error('Error converting text to speech:', error));
//     })
//     .catch(error => console.error('Error translating text:', error));
//   };

//   return (
//     <div>
//       <h1>OpenTTS Web App</h1>
//       <div>
//         <label htmlFor="voice">Select Voice:</label>
//         <select id="voice" value={selectedVoice} onChange={e => setSelectedVoice(e.target.value)}>
//           <option value="">Select...</option>
//           {voices.map(voice => (
//             <option key={voice.id} value={voice.id}>{voice.name}</option>
//           ))}
//         </select>
//       </div>
//       <div>
//         <label htmlFor="text">Enter Text:</label>
//         <input type="text" id="text" value={text} onChange={e => setText(e.target.value)} />
//       </div>
//       <div>
//         <button onClick={convertTextToSpeech}>Convert to Speech</button>
//       </div>
//       {audioUrl && <audio src={audioUrl} controls />}
//     </div>
//   );
// }

// export default App;

