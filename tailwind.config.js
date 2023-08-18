/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [ 
    './**/*.html',
    '**/*.html',
  ],
  theme: {
    extend: {
      ringWidth: {
        DEFAULT: '3px',  // Set default ring width
      },
      ringColor: {
        DEFAULT: '#FF0000',  // Set default ring color
      },
      ringOpacity: {
        DEFAULT: '0.75',  // Set default ring opacity
      },
    },

  },
  plugins: [
  ],
}

