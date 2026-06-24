"use client";

import { useState } from 'react';

export default function AIPage() {
  const [summary, setSummary] = useState('');
  const [result, setResult] = useState('');

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    const res = await fetch('http://localhost:8000/ai/summarize', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ summary }),
    });
    const data = await res.json();
    setResult(JSON.stringify(data, null, 2));
  }

  return (
    <main style={{ maxWidth: 720, margin: '40px auto', padding: 24 }}>
      <h1>AI safety demo</h1>
      <form onSubmit={handleSubmit} style={{ display: 'grid', gap: 12 }}>
        <textarea value={summary} onChange={(e) => setSummary(e.target.value)} rows={6} placeholder="Describe symptoms or concerns" />
        <button type="submit">Check</button>
      </form>
      <pre>{result}</pre>
    </main>
  );
}
