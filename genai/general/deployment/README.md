<h1>Deployment</h1>

<p>GenAI deployments usually combine application packaging with runtime-specific configuration.</p>

<h2>Cloud-oriented deployment</h2>

<ul>
<li>Keep provider credentials outside of static diagram constants.</li>
<li>Inject API settings through your application configuration layer.</li>
<li>Validate outbound network access on the deployed machine.</li>
</ul>

<h2>Local GGUF deployment</h2>

<ul>
<li>Ship or provision the GGUF model files in a stable path.</li>
<li>Avoid hardcoded development-only file paths.</li>
<li>Retest session initialization on the target machine with production values.</li>
</ul>

<h2>Audio deployment</h2>

<ul>
<li>Check the default playback device used by the deployed environment.</li>
<li>Verify that buffer-oriented and file-oriented playback both behave as expected.</li>
</ul>

<h2>Final validation</h2>

<p>Before release, run one cloud scenario, one local generation scenario, and one end-to-end speech or multimodal scenario that matches your real application.</p>
