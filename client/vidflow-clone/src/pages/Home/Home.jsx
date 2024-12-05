import { useEffect, useState } from "react";
import axios from "axios";
import LinkButton from '../../components/LinkButton/LinkButton';

const Home = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/")
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      <h1>{data ? data.message : "Loading..."}</h1>
      <LinkButton to="/about" variant="primary">About</LinkButton>
    </div>
  );
};

export default Home;
