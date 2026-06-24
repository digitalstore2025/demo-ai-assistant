"use client";

import Link from 'next/link';
import { useState } from 'react';

export default function SignupPage() {
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [message, setMessage] = useState('');

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    const res = await fetch('http://localhost:8000/auth/signup', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, phone, role: 'patient', language: 'ar' }),
    });
    const data = await res.json();
    setMessage(res.ok ? 'Account created' : data.detail || 'Failed');
  }

  return (
    <main style={{ maxWidth: 560, margin: '40px auto', padding: 24 }}>
      <h1>Create account</h1>
      <form onSubmit={handleSubmit} style={{ display: 'grid', gap: 12 }}>
        <input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
        <input value={phone} onChange={(e) => setPhone(e.target.value)} placeholder="Phone" />
        <button type="submit">Create</button>
      </form>
      <p>{message}</p>
      <Link href="/login">Go to login</Link>
    </main>
  );
}
