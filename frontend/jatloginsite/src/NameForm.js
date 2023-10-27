// This is a React component that sends a name to a Flask endpoint
import React, { Component } from 'react';

class NameForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      name: '',
      email: '',
      message: ''
    };
  }

  handleNameChange = (event) => {
    // This updates the state with the input value
    this.setState({ name: event.target.value });
  };
  handleEmailChange = (event) => {
    // This updates the state with the input value
    this.setState({ email: event.target.value });
  };

  handleSubmit = (event) => {
    // This prevents the default form submission behavior
    event.preventDefault();
    // This sends a POST request to the Flask endpoint with the name as JSON data
    fetch('http://localhost:5000/hello', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ name: this.state.name,
        email: this.state.email })
    })
      .then((response) => response.json()) // This parses the JSON response
      .then((data) => {
        // This updates the state with the message from the Flask endpoint
        this.setState({ message: data.message });
      })
      .catch((error) => {
        // This handles any error from the Flask endpoint
        console.error(error);
      });
  };

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <label>
            Name:
            <input
              type="text"
              value={this.state.name}
              onChange={this.handleNameChange}
            />
          </label>
          <label>
            Email:
            <input
              type="text"
              value={this.state.email}
              onChange={this.handleEmailChange}
            />
          </label>
          <input type="submit" value="Submit" />
        </form>
        <p>{this.state.message}</p>
      </div>
    );
  }
}

export default NameForm;