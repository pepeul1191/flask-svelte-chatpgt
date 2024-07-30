import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

export default defineConfig({
  plugins: [react()],
  build: {
    sourcemap: true,
    outDir: 'static/dist',
    rollupOptions: {
      input: {
        base: resolve(__dirname, 'src/main.jsx'),
        web: resolve(__dirname, 'src/entries/web.jsx'),
        error: resolve(__dirname, 'src/entries/error.jsx'),
        access: resolve(__dirname, 'src/entries/access.jsx'),
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