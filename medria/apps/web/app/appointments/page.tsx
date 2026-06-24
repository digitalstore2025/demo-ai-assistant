"use client";

import { useState } from 'react';

export default function AppointmentsPage() {
  const [patientId, setPatientId] = useState('');
  const [doctorId, setDoctorId] = useState('');
  const [message, setMessage] = useState('');

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    const res = await fetch('http://localhost:8000/appointments', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        patient_id: patientId,
        doctor_id: doctorId,
        start_time: new Date().toISOString(),
        end_time: new Date(Date.now() + 3600_000).toISOString(),
      }),
    });
    const data = await res.json();
    setMessage(res.ok ? `Appointment created: ${data.id}` : data.detail || 'Failed');
  }

  return (
    <main style={{ maxWidth: 560, margin: '40px auto', padding: 24 }}>
      <h1>Book appointment</h1>
      <form onSubmit={handleSubmit} style={{ display: 'grid', gap: 12 }}>
        <input value={patientId} onChange={(e) => setPatientId(e.target.value)} placeholder="Patient ID" />
        <input value={doctorId} onChange={(e) => setDoctorId(e.target.value)} placeholder="Doctor ID" />
        <button type="submit">Book</button>
      </form>
      <p>{message}</p>
    </main>
  );
}
