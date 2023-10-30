import React, { useState, useEffect } from 'react';
import axios from 'axios';

function NetflixData() {
  const [movies, setMovies] = useState([]);
  const [shows, setShows] = useState([]);

  useEffect(() => {
    const fetchMovies = async () => {
      const response = await axios.get('/netflix_movies');
      setMovies(response.data.movies);
    };

    const fetchShows = async () => {
      const response = await axios.get('/netflix_shows');
      setShows(response.data.shows);
    };

    fetchMovies();
    fetchShows();
  }, []);

  return (
    <div>
      <h1>Movies</h1>
      {movies.map((movie, index) => (
        <div key={index}>
          <h2>{movie.TITLE}</h2>
          <p>Director: {movie.DIRECTOR}</p>
          <p>Cast: {movie.CAST}</p>
          <p>Description: {movie.DESCRIPTION}</p>
        </div>
      ))}

      <h1>Shows</h1>
      {shows.map((show, index) => (
        <div key={index}>
          <h2>{show.TITLE}</h2>
          <p>Director: {show.DIRECTOR}</p>
          <p>Cast: {show.CAST}</p>
          <p>Description: {show.DESCRIPTION}</p>
        </div>
      ))}
    </div>
  );
}

export default NetflixData;
