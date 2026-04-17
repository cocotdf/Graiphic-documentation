<h1>Troubleshooting</h1>

<h2>Palette or VIs do not appear</h2>

<ul>
<li>Restart LabVIEW after installation.</li>
<li>Confirm that the GenAI Toolkit package matches the active LabVIEW environment.</li>
</ul>

<h2>Anthropic requests fail</h2>

<ul>
<li>Check the credential source used by your application.</li>
<li>Verify that the machine can reach the remote API.</li>
<li>Start from <a href="../../anthropic/message/simplify-text-message/README.md">Simplify Text Message</a> before debugging larger request payloads.</li>
</ul>

<h2>GGUF session does not initialize</h2>

<ul>
<li>Confirm that the model path is valid on disk.</li>
<li>Reduce runtime values such as GPU layers or context size for the first test.</li>
<li>Try a text-only initialization flow before moving to visual or TTS variants.</li>
</ul>

<h2>No sound is played</h2>

<ul>
<li>Validate the selected output device.</li>
<li>Check sample rate, channel count, and volume values.</li>
<li>Test playback from file before testing playback from a generated buffer.</li>
</ul>
