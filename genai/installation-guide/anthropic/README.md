<h1>Anthropic</h1>

<p>Anthropic pages are the cloud-oriented entry point of the GenAI Toolkit.</p>

<h2>Setup checklist</h2>

<ol>
<li>Prepare an Anthropic account and a valid API credential for the environment where LabVIEW will run.</li>
<li>Store the credential outside of block-diagram constants whenever possible, for example in a configuration layer handled by your application.</li>
<li>Make sure the machine can reach the Anthropic API over HTTPS.</li>
<li>Start with a minimal request by using <a href="../../anthropic/message/simplify-text-message/README.md">Simplify Text Message</a>.</li>
<li>Once the basic flow works, move to <a href="../../anthropic/message/advanced-message/README.md">Advanced Message</a> when you need structured multi-message payloads.</li>
</ol>

<h2>What to validate first</h2>

<ul>
<li>The request is accepted and returns a populated <strong>response</strong> cluster.</li>
<li>The application correctly extracts the generated text from <strong>response.content[].text</strong>.</li>
<li>Timeout and credential errors are handled cleanly in your own calling VI.</li>
</ul>
