// Renderer process entry point
console.log('Policy Pulse Desktop renderer initialized');

// Example of using the electron API
window.electronAPI.ping().then(response => {
  console.log('Ping response:', response);
});