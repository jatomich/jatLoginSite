import React, { useState, useEffect } from 'react';
import axios from '../axios';

import Container from 'react-bootstrap/Container';
import '../styles/App.css';


function NetflixData() {
  const [movies, setMovies] = useState([]);
  const [shows, setShows] = useState([]);

  useEffect(() => {
    const fetchMovies = async () => {
      const response = await axios.get(`/netflix_movies`, {})
      setMovies(response.data.movies);
    };

    const fetchShows = async () => {
      const response = await axios.get(`/netflix_shows`, {})
      setShows(response.data.shows);
    };

    fetchMovies();
    fetchShows();
  }, []);

  return (
    <Container>
      <h1 id="movie-type" className="netflix-type">Movies</h1>
      {movies.map((movie, index) => (
        <div className='netflix-div' key={index}>
          <h2>{movie.title}</h2>
          <p><b>cast:</b> {movie.cast}</p>
          <p><b>date added:</b> {movie.date_added}</p>
          <p><b>director:</b> {movie.director}</p>
          <p><b>cast:</b> {movie.cast}</p>
          <p><b>description:</b> {movie.description}</p>
          <p><b>movie id:</b> {movie.show_id}</p>
        </div>
      ))}

      <h1 id="show-type" className="netflix-type">Shows</h1>
      {shows.map((show, index) => (
        <div className='netflix-div' key={index}>
          <h2>{show.title}</h2>
          <p><b>director:</b> {show.director}</p>
          <p><b>cast:</b> {show.cast}</p>
          <p><b>description:</b> {show.description}</p>
          <p><b>show id:</b> {show.show_id}</p>
        </div>
      ))}
    </Container>
  );
}

export default NetflixData;
