import React, { useState } from 'react';

// A custom component that renders an image related to programming
function ProgrammingImage(props) {
  return (
    <img
      src={props.src}
      alt={props.alt}
      className="programming-image"
      style={{ transform: props.transform }}
    />
  );
}

export default ProgrammingImage;