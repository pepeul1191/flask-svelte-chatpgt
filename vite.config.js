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
        //admin: resolve(__dirname, 'src/admin.jsx'),
        //user: resolve(__dirname, 'src/user.jsx'),
      },
      output: {
        entryFileNames: '[name].js',
        chunkFileNames: '[name].js',
        assetFileNames: '[name][extname]',
      },
    },
  },
})