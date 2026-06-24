"use client";

import { useEffect, useState } from 'react';

export default function AdminPage() {
  const [stats, setStats] = useState<any>(null);
  const [error, setError] = useState('');

  useEffect(() => {
    fetch('http://localhost:8000/admin/dashboard')
      .then((res) => res.json())
      .then((data) => setStats(data))
      .catch(() => setError('Could not load admin dashboard'));
  }, []);

  return (
    <main style={{ maxWidth: 900, margin: '40px auto', padding: 24 }}>
      <h1>Admin dashboard</h1>
      <p>Operational overview for the Medria MVP.</p>
      {error ? <p style={{ color: 'crimson' }}>{error}</p> : null}
      {stats ? (
        <div style={{ display: 'grid', gap: '12px', marginTop: '20px' }}>
          <div style={{ padding: '16px', borderRadius: '12px', background: 'white' }}>
            <strong>Users:</strong> {stats.users_count}
          </div>
          <div style={{ padding: '16px', borderRadius: '12px', background: 'white' }}>
            <strong>Appointments:</strong> {stats.appointments_count}
          </div>
          <div style={{ padding: '16px', borderRadius: '12px', background: 'white' }}>
            <strong>Messages:</strong> {stats.messages_count}
          </div>
          <div style={{ padding: '16px', borderRadius: '12px', background: 'white' }}>
            <strong>Pending doctors:</strong> {stats.pending_doctors_count}
          </div>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </main>
  );
}
