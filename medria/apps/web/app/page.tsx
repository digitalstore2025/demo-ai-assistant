export default function HomePage() {
  return (
    <main style={{ maxWidth: 960, margin: '0 auto', padding: '48px 24px', lineHeight: 1.6 }}>
      <h1 style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>Medria AI</h1>
      <p style={{ fontSize: '1.05rem', marginBottom: '1rem' }}>
        A bilingual, safety-first health guidance platform designed for human-reviewed consultations and AI-assisted information support.
      </p>
      <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap', marginBottom: '24px' }}>
        <a href="/signup" style={{ padding: '10px 16px', background: '#0f172a', color: 'white', borderRadius: '999px', textDecoration: 'none' }}>Create account</a>
        <a href="/login" style={{ padding: '10px 16px', background: '#2563eb', color: 'white', borderRadius: '999px', textDecoration: 'none' }}>Login</a>
        <a href="/appointments" style={{ padding: '10px 16px', background: '#0ea5e9', color: 'white', borderRadius: '999px', textDecoration: 'none' }}>Book an appointment</a>
        <a href="/chat" style={{ padding: '10px 16px', background: '#7c3aed', color: 'white', borderRadius: '999px', textDecoration: 'none' }}>Open chat</a>
        <a href="/ai" style={{ padding: '10px 16px', background: '#16a34a', color: 'white', borderRadius: '999px', textDecoration: 'none' }}>AI safety demo</a>
      </div>
      <div style={{ display: 'grid', gap: '12px', maxWidth: 620 }}>
        <div style={{ padding: '16px 20px', borderRadius: '12px', background: 'white', boxShadow: '0 8px 24px rgba(15, 23, 42, 0.06)' }}>
          <strong>Phase 1</strong>
          <div>Secure onboarding, doctor profile setup, appointment booking, and safe chat foundation.</div>
        </div>
        <div style={{ padding: '16px 20px', borderRadius: '12px', background: 'white', boxShadow: '0 8px 24px rgba(15, 23, 42, 0.06)' }}>
          <strong>Phase 2</strong>
          <div>AI summaries with explicit opt-in, red-flag escalation, and auditable interactions.</div>
        </div>
      </div>
    </main>
  );
}
