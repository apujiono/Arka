export default function Avatar({ mood = 'neutral' }) {
  const color = {
    happy: 'bg-yellow-400',
    sad: 'bg-blue-500',
    thinking: 'bg-purple-500',
    neutral: 'bg-gray-400'
  }[mood] || 'bg-gray-400';

  return (
    <div className="w-8 h-8 rounded-full bg-pink-500 flex items-center justify-center text-xs font-bold relative">
      A
      <div className={`absolute bottom-0 right-0 w-3 h-3 rounded-full border-2 border-arka-dark ${color}`}></div>
    </div>
  );
}
