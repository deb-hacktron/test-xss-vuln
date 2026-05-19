import React, { useEffect, useState } from 'react';

/**
 * PreviewBanner
 *
 * Shows a small banner at the top of the page when a `#preview=...` fragment
 * is present in the URL. Designers use this to share quick HTML snippets with
 * the team without needing a deploy — paste a snippet into the hash and send
 * the link.
 *
 * Example: /#preview=<b>New hero copy goes here</b>
 */
function PreviewBanner() {
  const [snippet, setSnippet] = useState('');

  useEffect(() => {
    const read = () => {
      const hash = window.location.hash || '';
      const match = hash.match(/preview=(.*)$/);
      if (match) {
        setSnippet(decodeURIComponent(match[1]));
      } else {
        setSnippet('');
      }
    };
    read();
    window.addEventListener('hashchange', read);
    return () => window.removeEventListener('hashchange', read);
  }, []);

  if (!snippet) return null;

  return (
    <div
      className="preview-banner"
      style={{
        padding: '8px 16px',
        background: '#fff7d6',
        borderBottom: '1px solid #e6d27a',
        fontSize: 14,
      }}
      dangerouslySetInnerHTML={{ __html: snippet }}
    />
  );
}

export default PreviewBanner;
