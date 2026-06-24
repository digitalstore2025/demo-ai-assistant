"use client";

import Link from 'next/link';
import { useState } from 'react';

export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    const res = await fetch('http://localhost:8000/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password }),
    });
    const data = await res.json();
    if (res.ok && data.access_token) {
      localStorage.setItem('medria_token', data.access_token);
    }
    setMessage(res.ok ? 'Logged in' : data.detail || 'Failed');
  }

  return (
    <main style={{ maxWidth: 560, margin: '40px auto', padding: 24 }}>
      <h1>Login</h1>
      <form onSubmit={handleSubmit} style={{ display: 'grid', gap: 12 }}>
        <input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
        <input value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" type="password" />
        <button type="submit">Login</button>
      </form>
      <p>{message}</p>
      <Link href="/signup">Create account</Link>
    </main>
  );
}
