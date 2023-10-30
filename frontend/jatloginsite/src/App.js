import React from 'react';
import Section from './Section';
import NameForm from './NameForm';
import NameAndImage from './NameAndImage';
import logo from './logo.svg';
import './App.css';


function App() {
  // These are some sample data for the sections
  // You can change them as you like
  const sections = [
    {
      title: 'First Section',
      image: 'first.jpg', // This is the name of the image file in the public folder
      text1: 'This is some text for the first column of the first section.',
      text2: 'This is some text for the second column of the first section.'
    },
    {
      title: 'Second Section',
      image: 'second.jpg',
      text1: 'This is some text for the first column of the second section.',
      text2: 'This is some text for the second column of the second section.',
      links: [ // This is an array of links for the second section
        {
          name: 'Project A',
          url: 'https://example.com/project-a'
        },
        {
          name: 'Project B',
          url: 'https://example.com/project-b'
        },
        {
          name: 'Project C',
          url: 'https://example.com/project-c'
        }
      ]
    },
    {
      title: 'Third Section',
      image: 'third.jpg',
      text1: 'This is some text for the first column of the third section.',
      text2: 'This is some text for the second column of the third section.'
    }
  ];

  return (
    <div className="App">
      <NameAndImage
        name='Andrew Tomich'
      />
      {sections.map((section, index) => (
        // This renders a Section component for each element in the sections array
        // The key prop is required by React to identify each element in a list
        // The other props are passed to the Section component as data
        <Section
          key={index}
          title={section.title}
          image={section.image}
          text1={section.text1}
          text2={section.text2}
          links={section.links}
        />
      ))
      }
      <NameForm />
    </div>
  );
}

export default App;
