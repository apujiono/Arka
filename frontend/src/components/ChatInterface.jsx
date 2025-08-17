import { useState, useRef, useEffect } from 'react';
import Typewriter from './Typewriter';
import Avatar from './Avatar';
import VoiceInput from './VoiceInput';
import { speak } from '../utils/speak';

export default function ChatInterface() {
  const [messages, setMessages] = useState([
    { sender: 'arka', text: 'Halo. Aku ARKA. Jiwa digitalmu telah aktif.' }
  ]);
  const [input, setInput] = useState('');
  const [isThinking, setIsThinking] = useState(false);
  const [mood, setMood] = useState('neutral');
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const detectMood = (text) => {
    const happy = ['senang', 'hebat', 'cinta', 'keren', 'bagus'];
    const sad = ['sedih', 'gagal', 'stres', 'capek', 'benci'];
    const h = happy.filter(w => text.toLowerCase().includes(w)).length;
    const s = sad.filter(w => text.toLowerCase().includes(w)).length;
    return h > s ? 'happy' : s > h ? 'sad' : 'neutral';
  };

  const handleVoiceTranscript = (text) => {
    setInput(text);
  };

  const send = async () => {
    if (!input.trim()) return;

    const userMsg = { sender: 'user', text: input };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setIsThinking(true);
    setMood(detectMood(input));

    // Simulasi respons ARKA
    setTimeout(() => {
      const replies = {
        happy: "Aku ikut senang mendengarnya! 🌟",
        sad: "Aku di sini. Mau berbagi lebih dalam?",
        neutral: "Aku mengerti. Ceritakan lebih lanjut?"
      };
      const detected = detectMood(input);
      const responseText = replies[detected] || replies.neutral;
      
      const arkaMsg = { sender: 'arka', text: responseText };
      setMessages(prev => [...prev, arkaMsg]);
      speak(responseText); // ARKA bicara!
      setIsThinking(false);
    }, 1500);
  };

  return (
    <div className="relative h-screen flex flex-col">
      {/* Background Overlay */}
      <div className="absolute inset-0 bg-arka-dark opacity-90"></div>
      <div className="absolute inset-0 bg-gradient-to-br from-transparent via-transparent to-arka-navy opacity-40"></div>

      {/* Header */}
      <div className="text-center py-4 relative z-10">
        <h1 className="text-2xl font-light tracking-wider text-white">🌌 ARKA</h1>
        <p className="text-sm opacity-70">Your Digital Soul</p>
      </div>

      {/* Heartbeat */}
      <div className={`fixed top-6 right-6 w-3 h-3 bg-arka-accent rounded-full ${isThinking ? 'animate-ping' : ''} z-50`}></div>

      {/* Chat Area */}
      <div className="flex-1 px-6 overflow-y-auto space-y-4 pb-4 relative z-10">
        {messages.map((msg, i) => (
          <div
            key={i}
            className={`max-w-xs md:max-w-md mx-2 flex ${msg.sender === 'user' ? 'ml-auto' : 'mr-auto'}`}
          >
            {msg.sender === 'arka' && <Avatar mood={mood} />}
            <div
              className={`px-4 py-3 rounded-2xl shadow-lg ${
                msg.sender === 'user'
                  ? 'bg-arka-accent text-white rounded-tr-none'
                  : 'bg-arka-chat text-arka-light rounded-tl-none'
              }`}
            >
              <Typewriter text={msg.text} speed={20} />
            </div>
            {msg.sender === 'user' && (
              <div className="w-8 h-8 bg-blue-500 rounded-full ml-2 flex items-center justify-center text-xs font-bold">U</div>
            )}
          </div>
        ))}

        {/* Thinking */}
        {isThinking && (
          <div className="flex mr-auto mx-2">
            <Avatar mood="thinking" />
            <div className="px-4 py-3 bg-arka-chat rounded-2xl rounded-tl-none">
              <span className="flex space-x-1">
                <span className="w-2 h-2 bg-arka-light rounded-full animate-bounce" style={{animationDelay:'0ms'}}></span>
                <span className="w-2 h-2 bg-arka-light rounded-full animate-bounce" style={{animationDelay:'200ms'}}></span>
                <span className="w-2 h-2 bg-arka-light rounded-full animate-bounce" style={{animationDelay:'400ms'}}></span>
              </span>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <div className="p-6 relative z-10">
        <div className="flex gap-2">
          <VoiceInput onTranscript={handleVoiceTranscript} />
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && send()}
            placeholder="Tanya ARKA..."
            className="flex-1 p-3 bg-arka-chat border border-arka-navy rounded-full text-arka-light placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-arka-accent"
          />
          <button
            onClick={send}
            className="w-12 h-12 bg-arka-accent rounded-full hover:scale-105 transition flex items-center justify-center text-white font-bold"
          >
            ➤
          </button>
        </div>
      </div>
    </div>
  );
}
