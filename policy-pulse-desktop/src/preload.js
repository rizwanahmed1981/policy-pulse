/**
 * Policy Pulse Desktop - Preload Script
 *
 * This file runs before the renderer process and provides secure
 * communication channels between the renderer and main process.
 */

const { contextBridge, ipcRenderer } = require('electron');

// Expose protected methods that allow the renderer to use
// the ipcRenderer without exposing the entire object
contextBridge.exposeInMainWorld('electronAPI', {
  ping: () => ipcRenderer.invoke('ping'),
  // Add more exposed methods here as needed
});