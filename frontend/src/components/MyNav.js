import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';

function MyNav() {
  return (
    <Container>
        <Navbar expand="lg" className="bg-body-tertiary" fixed="top">
        <Container>
            <Navbar.Brand href="#top-latch">ATDATA</Navbar.Brand>
            <Nav>
                <Nav.Link href="#movie-type">Movies</Nav.Link>
                <Nav.Link href="#show-type">TV Shows</Nav.Link>
            </Nav>
        </Container>
        </Navbar>
    </Container>
  );
}

export default MyNav;