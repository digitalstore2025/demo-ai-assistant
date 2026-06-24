export default function HomePage() {
  return (
    <main style={{ maxWidth: 920, margin: '0 auto', padding: '48px 24px', lineHeight: 1.6 }}>
      <h1 style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>Medria AI</h1>
      <p style={{ fontSize: '1.05rem', marginBottom: '1rem' }}>
        A bilingual, safety-first health guidance platform designed for human-reviewed consultations and AI-assisted information support.
      </p>
      <div style={{ display: 'grid', gap: '12px', maxWidth: 520 }}>
        <div style={{ padding: '16px 20px', borderRadius: '12px', background: 'white', boxShadow: '0 8px 24px rgba(15, 23, 42, 0.06)' }}>
          <strong>Phase 1</strong>
          <div>Secure onboarding, doctor profiles, appointment booking, and safe chat foundation.</div>
        </div>
        <div style={{ padding: '16px 20px', borderRadius: '12px', background: 'white', boxShadow: '0 8px 24px rgba(15, 23, 42, 0.06)' }}>
          <strong>Phase 2</strong>
          <div>AI summaries with explicit opt-in, red-flag escalation, and auditable interactions.</div>
        </div>
      </div>
    </main>
  );
}
