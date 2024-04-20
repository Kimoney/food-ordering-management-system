import React, { useState } from "react";
import { Helmet } from "react-helmet";
import { redirect } from 'react-router-dom';
import { Text, Button, Input, Img, Heading } from "../../components";
import Footer from "../../components/Footer";
import Header from "../../components/Header";

export default function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const myStyles = {
    padding: '10px',
    borderRadius: '5px',
    border: '1px solid grey'
  };
  
  function handleSubmit(e) {
    e.preventDefault();
    console.log(username)
    fetch("http://127.0.0.1:5555/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username:username, password:password }),
    })
      .then((r) => r.json())
      .then(data => {
        console.log(data)
        if(data.hasOwnProperty('username')){
            console.log(data)
            return redirect("/");
        } else {
            setError("Invalid username or password")
        }
    });
  }

  return (
    <>
      <Helmet>
        <title>Log In To Delica Foods - Crunchy Delights Await</title>
        <meta
          name="description"
          content="Join Delica Foods and indulge in the crunchiest delights. Register now to explore our products and enjoy exclusive offers. Sign up today!"
        />
      </Helmet>
      <div className="flex w-full flex-col bg-white-A700 pb-[71px] md:pb-5">
        <div>
          {/* header section */}
          <Header className="flex items-center justify-center bg-white-A700" />
        </div>

        {/* hero section */}
        <div className="mx-auto mt-[107px] flex w-full max-w-[1086px] items-center md:flex-col md:p-5">
          <div className="relative h-[530px] w-[46%] md:h-auto md:w-full">
            <Img src="images/img_rectangle_1.png" alt="image" className="h-[530px] w-full object-cover" />
            <div className="absolute bottom-0 left-0 right-0 top-0 m-auto flex h-max w-full flex-col items-start gap-[21px] bg-black-900_bf py-[125px] pl-[125px] pr-14 md:p-5">
              <Heading size="2xl" as="h1" className="mt-[33px] !font-montserrat !font-bold !text-white-A700">
                <span className="text-white-A700">Delica</span>
                <span className="text-deep_orange-600">.</span>
              </Heading>
              <Heading size="md" as="h2" className="mb-[149px] !font-montserrat !text-white-A700">
                Crave a crunchy delight
              </Heading>
            </div>
          </div>

          {/* registration section */}
          
          <div className="flex flex-1 flex-col items-start gap-7 bg-white-A700 p-10 md:self-stretch sm:p-5">
            {/* <a href="Register" target="_blank" rel="noreferrer" className="ml-[110px] md:ml-0"> */}
              <Heading size="lg" as="h2" className="!font-montserrat">
                Log In
              </Heading>
              <Text as="p" className="!text-gray-800">
                {error}
              </Text>
            {/* </a> */}
            <form onSubmit={handleSubmit}> 
            <div className="flex w-[51%] flex-col gap-3 self-center md:w-full">
              <div className="flex flex-col items-start gap-[5px]">
                <Text as="p" className="!text-gray-800">
                  Username
                </Text>
                {/* <Input
                  shape="round"
                  type="text"
                  name="userName"
                  placeholder={`Username`}
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  className="sm:pr-5"
                /> */}
                <input
                    style={myStyles}
                    type="text"
                    id="username"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
              />
              </div>
              <div className="flex flex-col items-start gap-[5px]">
                <Text as="p" className="!text-gray-800">
                  Password
                </Text>
                {/* <Input
                  shape="round"
                  type="password"
                  name="password"
                  placeholder={`Password`}
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  suffix={<Img src="images/img_eye.svg" alt="eye" className="h-[16px] w-[16px]" />}
                  className="gap-[35px]"
                /> */}
                <input
                    style={myStyles}
                    type="password"
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
              </div>
              <Button color="deep_orange_600" shape="round" className="w-full !rounded-[10px] sm:px-5">
                Login
              </Button>
            </div>
            </form>
          </div>
        </div>

        {/* footer section */}
        <div>
          <Footer className="mt-[146px] flex flex-col items-start justify-end gap-[119px] bg-gray-900_03 py-[63px] md:gap-[89px] md:py-5 sm:gap-[59px]" />
        </div>
      </div>
    </>
  );
}