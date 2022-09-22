let name: string;
let email: string;


const submitForm = async () => {
  const response = await fetch("http:localhost/api/subscribers", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Token:" + process.env.jangokey
    },
    body: JSON.stringify({
      name,
      email,
    }),
  });
  const data = await response.json();
  console.log(data);
};

export default submitForm;