"use client";

import { useState } from 'react';

export default function ChatPage() {
  const [sessionId, setSessionId] = useState('');
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  async function startSession() {
    const res = await fetch('http://localhost:8000/chat/sessions', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ appointment_id: null }),
    });
    const data = await res.json();
    setSessionId(data.id);
    setResponse('Session created');
  }

  async function sendMessage() {
    const res = await fetch(`http://localhost:8000/chat/sessions/${sessionId}/messages`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ session_id: sessionId, sender_role: 'patient', content: message }),
    });
    const data = await res.json();
    setResponse(JSON.stringify(data, null, 2));
  }

  return (
    <main style={{ maxWidth: 720, margin: '40px auto', padding: 24 }}>
      <h1>Chat foundation</h1>
      <button onClick={startSession} style={{ marginBottom: '12px' }}>Start chat session</button>
      <p>Session: {sessionId || 'not started'}</p>
      <textarea value={message} onChange={(e) => setMessage(e.target.value)} rows={4} style={{ width: '100%' }} placeholder="Type your message" />
      <button onClick={sendMessage} style={{ marginTop: '12px' }}>Send message</button>
      <pre>{response}</pre>
    </main>
  );
}
