import React from 'react';

function Section(props) {
  // These are the props passed from the App component
  const { title, image, text1, text2, links } = props;

  return (
    <div className="Section">
      <h1 className="Section-title">{title}</h1>
      <img className="Section-image" src={image} alt={title} />
      <div className="Section-columns">
        <p className="Section-text">{text1}</p>
        <p className="Section-text">{text2}</p>
      </div>
      {links && ( // This conditionally renders a list of links if the links prop exists
        <ul className="Section-links">
          {links.map((link, index) => (
            // This renders a list item for each element in the links array
            // The key prop is required by React to identify each element in a list
            <li key={index}>
              <a href={link.url}>{link.name}</a>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Section;