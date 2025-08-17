/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        arka: {
          dark: '#1a1a2e',
          navy: '#16213e',
          chat: '#2d2b4e',
          accent: '#e94560',
          light: '#e1e1e1',
          gray: '#888'
        }
      },
      animation: {
        'pulse-slow': 'pulse 3s ease-in-out infinite',
        'float': 'float 6s ease-in-out infinite',
        'breath': 'breath 8s ease-in-out infinite'
      },
      keyframes: {
        breath: {
          '0%, 100%': { opacity: 0.2 },
          '50%': { opacity: 0.4 }
        },
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-10px)' }
        }
      }
    },
  },
  plugins: [],
}
