import React, { useState } from 'react';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import About from './pages/About';
import Services from './pages/Services';
import Work from './pages/Work';
import Contact from './pages/Contact';
import ContentRenderer from './ContentRenderer';
import './App.css';

function App() {
  const [currentPage, setCurrentPage] = useState('home');
  const [userInput, setUserInput] = useState('<strong>Preview client update</strong>');

  const navigate = (page) => {
    setCurrentPage(page);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const renderPage = () => {
    switch (currentPage) {
      case 'home':     return <Home navigate={navigate} />;
      case 'about':    return <About />;
      case 'services': return <Services navigate={navigate} />;
      case 'work':     return <Work />;
      case 'contact':  return <Contact />;
      default:         return <Home navigate={navigate} />;
    }
  };

  return (
    <div className="app">
      <Navbar currentPage={currentPage} navigate={navigate} />
      <main className="main">{renderPage()}</main>
      <section className="html-preview">
        <textarea
          aria-label="Live HTML Preview"
          value={userInput}
          onChange={(event) => setUserInput(event.target.value)}
        />
        <ContentRenderer htmlContent={userInput} />
      </section>
      <Footer navigate={navigate} />
    </div>
  );
}

export default App;
