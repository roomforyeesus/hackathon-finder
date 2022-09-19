require('dotenv').config();
const fetch = require('node-fetch');

async function getLatestHackthons() {
  const response = await fetch('https://kontests.net/api/v1/all');
  const responseJson = await response.json();
  const hackathons = responseJson.map((hackathon:any) => {
    return {
      name: hackathon.name,
      url: hackathon.url,
      start: hackathon.start_time,
      end: hackathon.end_time,
      duration: hackathon.duration,
      timezone: hackathon.timezone,
      platform: hackathon.platform,
      prize: hackathon.prize,
      host: hackathon.host,
      region: hackathon.region,
      image: hackathon.image,
      tags: hackathon.tags,
    };
  });
}

async function sendEmails() {
  const subscribers = await fetch('http://127.0.0.1:8000/api/subscribers/');
  const subscribersJson = await subscribers.json();
  const subscribersEmails = subscribersJson.map((subscriber:any) => {subscriber.email});

  const courier_options = {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
          Authorization: 'Bearer ' + process.env.APIKEY
        },
        body: JSON.stringify({
          "message": {
            "to": {
              "email": subscribersEmails,
            },
            "content": {
              "title": "Hiya! Check these Hackthons and Events!",
              "body": "Check out these latest hackthons and events!" + getLatestHackthons(),
            },
            "routing": {
              "method": "all",
              "channels": ["email"]
            },
          }
        })
      };
      
      fetch('https://api.courier.com/send', courier_options)
        .then(response => response.json())
        .then(response => console.log(response))
        .catch(err => console.error(err));

}

function addSubs() {
  const data = {
    name: "John Doe",
    email: "test@email.com",
  };
  fetch('https://localhost:8000/api/subscribers', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log('Success:', data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}
export {addSubs, sendEmails};

