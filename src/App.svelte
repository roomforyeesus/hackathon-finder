<script lang="ts">
import { addSubs } from './scripts'
</script>

<main>
  <div class="bodywrap">
    <div class="textbub">Hiya! Leave your email and I will send you an weekly updates on what hackathons are happening around you!</div>
    <div class="image">
      <img id="cuteblub"src="https://i.postimg.cc/5tS9yvRQ/pngwing-com.png" alt="cuteblub" />
    </div>
    <div class="form">
      <input type="text" placeholder="Name" />
      <input type="text" placeholder="Email" />
      <button on:click="{addSubs}">Subscribe</button>
    </div>
  </div>
  <footer>
    <p>© 2022 Hackathon Finder</p>
  </footer>
</main>

<style>
  .textbub {
    display: inline-block;
    position: relative;
    font-family: "Poppins", sans-serif;
    font-size: 1.5rem;
    font-weight: 500;
    color: #000000;
    margin: 0;
    padding: 0;
    margin-top: 1rem;
    margin-bottom: 2rem;
    margin-right: 50%;
    background-color: white;
    border-radius: 15px;
    padding: 1rem;
  }
  .textbub::after{
    content: '';
	  position: absolute;
	  right: 0;
	  top: 50%;
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
    width: 50%;
    height: 50%;
    margin-left: 50%;
    margin-top: -150px;
  }
  
</style>


