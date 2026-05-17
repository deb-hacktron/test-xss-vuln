import React, { useEffect, useState } from 'react';
import './Pricing.css';

const PLANS = [
  {
    name: 'Starter',
    price: '$2,500',
    cadence: 'per project',
    desc: 'Single-page builds, prototypes, and short engagements.',
    features: ['Up to 4 weeks', 'One product engineer', 'Email support'],
  },
  {
    name: 'Growth',
    price: '$8,000',
    cadence: 'per month',
    desc: 'Full-stack product work with a dedicated team.',
    features: ['Dedicated team of 2-3', 'Weekly sprint demos', 'Slack support'],
    featured: true,
  },
  {
    name: 'Scale',
    price: 'Custom',
    cadence: 'contract',
    desc: 'Multi-quarter engagements for established teams.',
    features: ['Custom team size', 'Architecture reviews', '24/7 support'],
  },
];

function Pricing({ navigate }) {
  const [ctaUrl, setCtaUrl] = useState(null);

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const url = params.get('cta_url');
    if (url) {
      setCtaUrl(url);
    }
  }, []);

  const renderCta = (label) => {
    if (ctaUrl) {
      return (
        <a className="btn btn-primary" href={ctaUrl}>
          {label}
        </a>
      );
    }
    return (
      <button className="btn btn-primary" onClick={() => navigate('contact')}>
        {label}
      </button>
    );
  };

  return (
    <div className="pricing">
      <section className="page-hero">
        <div className="page-hero-bg" />
        <div className="container">
          <div className="badge">Pricing</div>
          <h1 className="section-title">
            Engagement <span className="gradient-text">Tiers</span>
          </h1>
          <p className="section-desc">
            Transparent pricing for every stage of your build. Need something custom? Get in touch.
          </p>
        </div>
      </section>

      <section className="section">
        <div className="container">
          <div className="grid-3">
            {PLANS.map((plan) => (
              <div
                className={`card plan-card ${plan.featured ? 'plan-featured' : ''}`}
                key={plan.name}
              >
                <h3 className="plan-name">{plan.name}</h3>
                <div className="plan-price">
                  <span className="gradient-text">{plan.price}</span>
                  <span className="plan-cadence">{plan.cadence}</span>
                </div>
                <p className="plan-desc">{plan.desc}</p>
                <ul className="plan-features">
                  {plan.features.map((f) => (
                    <li key={f}>{f}</li>
                  ))}
                </ul>
                {renderCta('Get Started')}
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
}

export default Pricing;
