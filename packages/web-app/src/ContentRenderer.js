import React from 'react';

function ContentRenderer({ htmlContent }) {
  const wrapperStyle = {
    border: '1px solid #d6dbe5',
    borderRadius: '8px',
    marginTop: '16px',
    padding: '16px',
    background: '#fff',
  };

  return (
    <section className="content-renderer" style={wrapperStyle}>
      <h3>Live HTML Preview</h3>
      <div
        className="rendered-html"
        dangerouslySetInnerHTML={{ __html: htmlContent }}
      />
    </section>
  );
}

export default ContentRenderer;
