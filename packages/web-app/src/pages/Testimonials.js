import React, { useEffect, useState } from 'react';
import './Testimonials.css';

const FEATURED = [
  {
    quote: "Nexus delivered our platform two weeks ahead of schedule. The team's depth across the stack is rare.",
    author: 'Maya Lin, CTO at Vertex Cloud',
  },
  {
    quote: "Working with Nexus felt like an extension of our own team — sharp, fast, and product-minded.",
    author: 'Daniel Park, VP Engineering at Northpoint',
  },
  {
    quote: "Their security audit caught issues our previous vendor missed entirely. Worth every dollar.",
    author: 'Sophia Rojas, Founder of LedgerWise',
  },
];

function Testimonials() {
  const [preview, setPreview] = useState(null);

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const quote = params.get('quote');
    const author = params.get('author');
    if (quote) {
      setPreview({ quote, author: author || 'Anonymous' });
    }
  }, []);

  return (
    <div className="testimonials">
      <section className="page-hero">
        <div className="page-hero-bg" />
        <div className="container">
          <div className="badge">Testimonials</div>
          <h1 className="section-title">
            What Our <span className="gradient-text">Clients Say</span>
          </h1>
          <p className="section-desc">
            Real stories from the teams we've shipped with.
          </p>
        </div>
      </section>

      {preview && (
        <section className="section" style={{ paddingTop: 48, paddingBottom: 0 }}>
          <div className="container">
            <div className="card preview-card">
              <div className="preview-label">Preview</div>
              <div
                className="preview-quote"
                dangerouslySetInnerHTML={{ __html: preview.quote }}
              />
              <div className="preview-author">— {preview.author}</div>
            </div>
          </div>
        </section>
      )}

      <section className="section">
        <div className="container">
          <div className="grid-3">
            {FEATURED.map((t, i) => (
              <div className="card testimonial-card" key={i}>
                <p className="testimonial-quote">"{t.quote}"</p>
                <div className="testimonial-author">— {t.author}</div>
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
}

export default Testimonials;
