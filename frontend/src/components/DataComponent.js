// import React from 'react';
// import instance from '../axios';

// import Container from 'react-bootstrap/Container';
// import '../styles/App.css';

// class NetflixData extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       movies: [],
//       shows: [],
//     };
//   }

//   componentDidMount() {
//     this.fetchMovies();
//     this.fetchShows();
//   }

//   fetchMovies = async () => {
//     try {
//       const response = await instance.get(`/netflix_movies`, {});
//       this.setState({ movies: response.data.movies });
//     } catch (error) {
//       console.error("Error fetching movies: ", error);
//     }
//   };

//   fetchShows = async () => {
//     try {
//       const response = await instance.get(`/netflix_shows`, {});
//       this.setState({ shows: response.data.shows });
//     } catch (error) {
//       console.error("Error fetching shows: ", error);
//     }
//   };

//   render() {
//     const { movies, shows } = this.state;

//     return (
//     <Container>
//       <h1 id="movie-type" className="netflix-type">Movies</h1>
//       {movies?.map((movie, index) => (
//         <div className='netflix-div' key={index}>
//           <h2>{movie.title}</h2>
//           <p><b>cast:</b> {movie.cast}</p>
//           <p><b>date added:</b> {movie.date_added}</p>
//           <p><b>rating:</b> {movie.rating}</p>
//           <p><b>listed_in:</b> {movie.listed_in}</p>
//           <p><b>director:</b> {movie.director}</p>
//           <p><b>show_id:</b> {movie.show_id}</p>
//           <p><b>format:</b> {movie.format}</p>
//           <p><b>country:</b> {movie.country}</p>
//           <p><b>release_year:</b> {movie.release_year}</p>
//           <p><b>duration:</b> {movie.duration}</p>
//           <p><b>description:</b> {movie.description}</p>
//         </div>
//       ))}

//       <h1 id="show-type" className="netflix-type">TV Shows</h1>
//       {shows?.map((show, index) => (
//         <div className='netflix-div' key={index}>
//           <h2>{show.title}</h2>
//           <p><b>cast:</b> {show.cast}</p>
//           <p><b>date added:</b> {show.date_added}</p>
//           <p><b>rating:</b> {show.rating}</p>
//           <p><b>listed_in:</b> {show.listed_in}</p>
//           <p><b>director:</b> {show.director}</p>
//           <p><b>show_id:</b> {show.show_id}</p>
//           <p><b>format:</b> {show.format}</p>
//           <p><b>country:</b> {show.country}</p>
//           <p><b>release_year:</b> {show.release_year}</p>
//           <p><b>duration:</b> {show.duration}</p>
//           <p><b>description:</b> {show.description}</p>
//         </div>
//       ))}
//     </Container>
//   );
//   }
// }

// export default NetflixData;

import React, { useState, useEffect } from 'react';
import instance from '../axios';

import Container from 'react-bootstrap/Container';
import '../styles/App.css';

function NetflixData() {
  const [movies, setMovies] = useState([]);
  const [shows, setShows] = useState([]);

  useEffect(() => {
    fetchMovies();
    fetchShows();
  }, []);

  const fetchMovies = async () => {
    try {
      const response = await instance.get(`/netflix_movies`, {});
      setMovies(response.data.movies);
    } catch (error) {
      console.error("Error fetching movies: ", error);
    }
  };

  const fetchShows = async () => {
    try {
      const response = await instance.get(`/netflix_shows`, {});
      setShows(response.data.shows);
    } catch (error) {
      console.error("Error fetching shows: ", error);
    }
  };

  return (
    <Container>
      <h1 id="movie-type" className="netflix-type">Movies</h1>
      {movies?.map((movie, index) => (
        <div className='netflix-div' key={index}>
          <h2>{movie.title}</h2>
          <p><b>cast:</b> {movie.cast}</p>
          <p><b>date added:</b> {movie.date_added}</p>
          <p><b>rating:</b> {movie.rating}</p>
          <p><b>listed_in:</b> {movie.listed_in}</p>
          <p><b>director:</b> {movie.director}</p>
          <p><b>show_id:</b> {movie.show_id}</p>
          <p><b>format:</b> {movie.format}</p>
          <p><b>country:</b> {movie.country}</p>
          <p><b>release_year:</b> {movie.release_year}</p>
          <p><b>duration:</b> {movie.duration}</p>
          <p><b>description:</b> {movie.description}</p>
        </div>
      ))}

      <h1 id="show-type" className="netflix-type">TV Shows</h1>
      {shows?.map((show, index) => (
        <div className='netflix-div' key={index}>
          <h2>{show.title}</h2>
          <p><b>cast:</b> {show.cast}</p>
          <p><b>date added:</b> {show.date_added}</p>
          <p><b>rating:</b> {show.rating}</p>
          <p><b>listed_in:</b> {show.listed_in}</p>
          <p><b>director:</b> {show.director}</p>
          <p><b>show_id:</b> {show.show_id}</p>
          <p><b>format:</b> {show.format}</p>
          <p><b>country:</b> {show.country}</p>
          <p><b>release_year:</b> {show.release_year}</p>
          <p><b>duration:</b> {show.duration}</p>
          <p><b>description:</b> {show.description}</p>
        </div>
      ))}
    </Container>
  );
}

export default NetflixData;


//   return (
//     <Container>
//       <h1 id="movie-type" className="netflix-type">Movies</h1>
//       {movies?.map((movie, index) => (
//         <div className='netflix-div' key={index}>
//           <h2>{movie.title}</h2>
//           <p><b>cast:</b> {movie.cast}</p>
//           <p><b>date added:</b> {movie.date_added}</p>
//           <p><b>rating:</b> {movie.rating}</p>
//           <p><b>listed_in:</b> {movie.listed_in}</p>
//           <p><b>director:</b> {movie.director}</p>
//           <p><b>show_id:</b> {movie.show_id}</p>
//           <p><b>format:</b> {movie.format}</p>
//           <p><b>country:</b> {movie.country}</p>
//           <p><b>release_year:</b> {movie.release_year}</p>
//           <p><b>duration:</b> {movie.duration}</p>
//           <p><b>description:</b> {movie.description}</p>
//         </div>
//       ))}

//       <h1 id="show-type" className="netflix-type">TV Shows</h1>
//       {shows?.map((show, index) => (
//         <div className='netflix-div' key={index}>
//           <h2>{show.title}</h2>
//           <p><b>cast:</b> {show.cast}</p>
//           <p><b>date added:</b> {show.date_added}</p>
//           <p><b>rating:</b> {show.rating}</p>
//           <p><b>listed_in:</b> {show.listed_in}</p>
//           <p><b>director:</b> {show.director}</p>
//           <p><b>show_id:</b> {show.show_id}</p>
//           <p><b>format:</b> {show.format}</p>
//           <p><b>country:</b> {show.country}</p>
//           <p><b>release_year:</b> {show.release_year}</p>
//           <p><b>duration:</b> {show.duration}</p>
//           <p><b>description:</b> {show.description}</p>
//         </div>
//       ))}
//     </Container>
//   );
// }

// export default NetflixData;
