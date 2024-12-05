import React from 'react';
import './About.css'
import LinkButton from '../../components/LinkButton/LinkButton';

const About = () => {
    return (
        <>
           <h1>About</h1>
           <LinkButton to="/" variant="primary">Home</LinkButton>
        </>
    );
};

export default About;