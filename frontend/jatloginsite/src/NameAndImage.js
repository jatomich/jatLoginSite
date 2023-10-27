import React, { useState } from 'react';
import ProgrammingImage from './ProgrammingImage';

// A custom component that renders a name and an image related to programming
function NameAndImage(props) {
    // A state variable that tracks the mouse hover status
    const [hover, setHover] = useState(false);
  
    // A function that handles the mouse enter event
    function handleMouseEnter() {
      setHover(true);
    }
  
    // A function that handles the mouse leave event
    function handleMouseLeave() {
      setHover(false);
    }
  
    // A variable that stores the transform style based on the hover status
    const transform = hover ? "translateX(0)" : "translateX(-100%)";
  
    return (
      <div className="name-and-image" onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave}>
        <h1 className="name" style={{ transform: transform }}>
          {props.name}
        </h1>
        <ProgrammingImage src={props.src} alt={props.alt} transform={transform} />
      </div>
    );
  }

export default NameAndImage;