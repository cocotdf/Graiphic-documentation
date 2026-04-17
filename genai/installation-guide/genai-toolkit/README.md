<h1>Getting Started</h1>

<p>This page helps you prepare the GenAI Toolkit inside LabVIEW before choosing a cloud or local runtime.</p>

<ol>
<li>Install the GenAI Toolkit package that matches your LabVIEW environment.</li>
<li>Restart LabVIEW and confirm that the <strong>GenAI</strong> palette appears in the functions menu.</li>
<li>Choose your first execution mode:
  <ul>
    <li><strong>Anthropic</strong> for hosted text, image, and PDF message workflows.</li>
    <li><strong>GGUF</strong> for local chat, text generation, or text-to-speech pipelines.</li>
  </ul>
</li>
<li>Keep model files, prompts, and runtime settings in stable paths that will still exist when your application is moved or deployed.</li>
<li>Run a first smoke test with a simple page such as <a href="../../anthropic/message/simplify-text-message/README.md">Simplify Text Message</a> or <a href="../../gguf/text-generation/gguf-init/text-only/session-and-sampler/README.md">Session And Sampler</a>.</li>
</ol>

<h2>Recommended first checks</h2>

<ul>
<li>Verify that the toolkit VIs open without missing dependencies.</li>
<li>Confirm that local model paths can be resolved from LabVIEW.</li>
<li>For cloud workflows, validate that network access and credentials are available at runtime.</li>
<li>For audio workflows, confirm that a valid playback device is visible on the machine.</li>
</ul>

<h2>Next steps</h2>

<ul>
<li><a href="../anthropic/README.md">Anthropic</a> for hosted messaging setup.</li>
<li><a href="../gguf/README.md">GGUF</a> for local model setup.</li>
<li><a href="../audio-playback/README.md">Audio Playback</a> for speech output validation.</li>
</ul>
