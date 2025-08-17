import { useState } from 'react';

export default function VoiceInput({ onTranscript }) {
  const [isListening, setIsListening] = useState(false);

  const start = () => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    recognition.lang = 'id-ID';
    recognition.interimResults = false;

    recognition.onresult = (e) => {
      const transcript = e.results[0][0].transcript;
      onTranscript(transcript);
    };

    recognition.onend = () => setIsListening(false);
    
    recognition.start();
    setIsListening(true);
  };

  return (
    <button
      onClick={start}
      className={`px-3 py-2 rounded-full text-sm font-medium transition ${
        isListening 
          ? 'bg-red-600 hover:bg-red-700 text-white' 
          : 'bg-gray-700 hover:bg-gray-600 text-gray-100'
      }`}
    >
      🎤 {isListening ? 'Mendengar...' : 'Dengar'}
    </button>
  );
}
