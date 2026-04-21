<h1>OpenAI</h1>

<p>OpenAI pages are the hosted API entry point of the LabVIEW GenAI Toolkit.</p>

<h2>Setup checklist</h2>

<ol>
<li>Prepare an OpenAI account and a valid API key for the environment where LabVIEW will run.</li>
<li>Store the API key outside of block-diagram constants whenever possible, for example in a configuration layer handled by your application.</li>
<li>Validate the base connection first with <a href="../../openai/authentification/authentification/README.md">Authentification</a>.</li>
<li>Start with a minimal text flow by using <a href="../../openai/send-message/send-message/README.md">Send Message</a>.</li>
<li>Once the basic request path is stable, extend to advanced OpenAI flows such as files, assistants, audio, or threaded conversations.</li>
</ol>

<h2>What to validate first</h2>

<ul>
<li>The OpenAI session is correctly authenticated and reused by the calling VIs.</li>
<li>A first request returns a populated response without timeout or credential issues.</li>
<li>Your application extracts the generated content and handles API errors cleanly.</li>
</ul>

<h2>Useful validation pages</h2>

<ul>
<li><a href="../../openai/authentification/authentification/README.md">Authentification</a></li>
<li><a href="../../openai/send-message/send-message/README.md">Send Message</a></li>
<li><a href="../../openai/advanced/messages/create/create-message/README.md">Create Message</a></li>
<li><a href="../../openai/audio/speech/create-speech/README.md">Create Speech</a></li>
</ul>
