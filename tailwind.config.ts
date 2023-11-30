import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      backgroundColor:{
        'head':'#111827',
        'main':'#27272a',
        'input':'#374151',
      },
      colors:{
        'white':'#ced4da',
        'input':'#374151',
      },
      width:{
        'form': '35rem',
      },
      height:{
        'form': '30rem',
      },
      boxShadow:{
        'form':'inset 0rem 0rem 1rem 1rem #66666617',
      }
    },
  },
  plugins: [],
}
export default config
