export const metadata = {
  title: 'Medria AI',
  description: 'Bilingual health guidance platform with human review and AI safety.'
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" dir="ltr">
      <body style={{ margin: 0, fontFamily: 'Inter, sans-serif', background: '#f8fafc', color: '#0f172a' }}>
        {children}
      </body>
    </html>
  );
}
