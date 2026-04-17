<h1>GGUF</h1>

<p>GGUF pages cover local model execution for chat, text generation, and text-to-speech scenarios.</p>

<h2>Setup checklist</h2>

<ol>
<li>Place the GGUF model files in a local path that will remain valid for development and deployment.</li>
<li>Start with a small validation flow such as <a href="../../gguf/text-generation/gguf-init/text-only/session-and-sampler/README.md">Text Only / Session And Sampler</a>.</li>
<li>Use conservative runtime values first for <strong>n cpu threads</strong>, <strong>nb gpu layers</strong>, and <strong>n_ctx</strong>.</li>
<li>Confirm that the model opens before enabling more advanced sampler tuning.</li>
<li>Extend to visual or TTS flows only after the base text path is stable.</li>
</ol>

<h2>Useful validation pages</h2>

<ul>
<li><a href="../../gguf/gguf/chat/set/sampler/samplers/README.md">GGUF Chat Samplers</a></li>
<li><a href="../../gguf/gguf/chat/set/session/n-ctx/README.md">N CTX</a></li>
<li><a href="../../gguf/gguf-tts/init/session-sampler/README.md">GGUF TTS Session &amp; Sampler</a></li>
<li><a href="../../gguf/text-generation/gguf-init/visual/qwen-2-5vl/session-and-sampler/README.md">Visual Session And Sampler</a></li>
</ul>
