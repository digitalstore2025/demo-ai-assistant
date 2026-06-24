import Link from 'next/link';

export default function ConsultationPage() {
  return (
    <main style={{ maxWidth: 960, margin: '0 auto', padding: '48px 24px', lineHeight: 1.6 }}>
      <h1>Start a consultation</h1>
      <p>Choose a specialty and describe your symptoms. The platform will guide you safely and escalate urgent cases.</p>
      <div style={{ display: 'grid', gap: '16px', marginTop: '24px' }}>
        <div style={{ padding: '16px', background: 'white', borderRadius: '12px' }}>
          <strong>Internal Medicine</strong>
          <div>General wellness, follow-up, and non-emergency support.</div>
        </div>
        <div style={{ padding: '16px', background: 'white', borderRadius: '12px' }}>
          <strong>Neurology</strong>
          <div>Symptoms like headache, dizziness, or sensory concerns.</div>
        </div>
      </div>
      <Link href="/" style={{ display: 'inline-block', marginTop: '24px' }}>Back home</Link>
    </main>
  );
}
