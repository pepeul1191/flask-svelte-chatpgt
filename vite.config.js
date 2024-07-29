import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'public/dist',
    rollupOptions: {
      input: {
        demo: resolve(__dirname, 'src/main.jsx'),
        web: resolve(__dirname, 'src/entries/web.jsx'),
        //admin: resolve(__dirname, 'src/admin.jsx'),
        //user: resolve(__dirname, 'src/user.jsx'),
      },
      output: {
        entryFileNames: '[name].min.js',
        chunkFileNames: '[name].min.js',
        assetFileNames: '[name].min[extname]',
      },
    },
  },
})