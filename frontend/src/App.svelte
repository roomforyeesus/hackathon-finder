<script lang="ts">
import { onMount } from "svelte";
let hackathons;

onMount(async () => {
  const response = await fetch(
    "https://www.kontests.net/api/v1/all",{
      method: "GET",
    },
  );
  const dataz = await response.json();
  hackathons = dataz;
  
})

// submit function 
let name;
let email;

const submit = async () => {
  try{
    const response = await fetch("http://localhost:8000/api/subscribers/", {
      method: "POST",
      mode: "no-cors",
      credentials: 'include',
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "localhost:8000",
        "Access-Control-Allow-Methods": "POST",
      },
      body: JSON.stringify({
        name,
        email,   
      }),
    });
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.log(error);
  }
};

// hackathons.forEach(hackathon => {
//   if (hackathon.status == 'YES'){
//     hackathon.start = new Date(hackathon.start_time)
//     hackathon.startt = hackathon.start.toLocaleString()
//     hackathon.end = new Date(hackathon.end_time)
//     hackathon.endt= hackathon.end.toLocaleString()
//     hackathon.dur = Math.floor(hackathon.duration / 3600)
//   }
// });

</script>

<main>
  <div class="bodywrap">
    <div class="textbub">Hiya! Leave your email and I will alert you when a hackathon is within 24 Hours of it's start time!</div>
    <div class="image">
      <img id="cuteblub"src="https://i.postimg.cc/5tS9yvRQ/pngwing-com.png" alt="cuteblub" />
    </div>
    <form on:submit|preventDefault={submit}>
      <input type="text" placeholder="Name" bind:value={name}/>&nbsp;
      <input type="text" placeholder="Email" bind:value={email}/>&nbsp; 
      <!-- <input type="text" placeholder="Phone Number(Optional)" bind:value={phoneNumber}/> -->
      <input type="submit" value="Subscribe" />
    </form>
  </div>
  <div class="table">
    <h1>Current Hackathons</h1>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Start Date</th>
          <th>End Date</th>
          <th>Duration</th>
          <th>Link</th>
        </tr>
      </thead>
      <tbody>
        {#if hackathons}
          {#each hackathons as hackathon}
            <tr>
              <td>{hackathon.name}</td>
              <td>{hackathon.start_time}</td>
              <td>{hackathon.end_time}</td>
              <td>{hackathon.duration}</td>
              <td><a href={hackathon.url}>Link</a></td>
            </tr>
          {/each}
        {/if}
</main>

<style>
  h1{
    color: azure;
    font-family: "American Typewriter", serif;
  }
  .table{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 2rem;
    color: azure;
    max-width: 100%;
    widows: auto;
  }
  form{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    margin-top: 2rem;
    width: auto;
  }
  .textbub {
    display: inline-block;
    position: relative;
    font-family: "Noto Sans", sans-serif;
    font-size: 1.5rem;
    font-weight: 530;
    color: #000000; 
    margin-top: 0.5rem;
    margin-bottom: 2rem;
    margin-right: 50%;
    background-color: white;
    border-radius: 18px;
    padding: 1rem;
    width: auto;
  }
  .textbub::after{
    content: '';
	  position: absolute;
	  right: 0;
	  top: 45%;
	  width: 0;
	  height: 0;
	  border: 24px solid transparent;
	  border-left-color: white;
	  border-right: 0;
	  border-bottom: 0;
	  margin-top: 28px;
  	margin-right: -24px;
  }
  #cuteblub{
    margin-left: 50%;
    margin-top: -150px;
    max-width: 350px;
  }
  .bodywrap{
    display: flex;
    flex-direction: column;
  }
@media screen and (min-width: 800px) {
  .bodywrap{
    display: flex;
    max-width: fit-content;
  }
}
  
</style>


