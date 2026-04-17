<h1>Hardware Compatibility</h1>

<p>Compatibility in the GenAI Toolkit depends on the execution style you choose.</p>

<h2>Anthropic</h2>

<p>Anthropic messaging flows are primarily network dependent. The local machine still needs enough resources to run LabVIEW comfortably, but the heavy model execution happens remotely.</p>

<h2>GGUF local runtimes</h2>

<p>Local GGUF execution depends on the selected model size and on parameters such as <strong>n cpu threads</strong>, <strong>nb gpu layers</strong>, and <strong>n_ctx</strong>. Larger models and longer contexts require more RAM and, when enabled, more VRAM.</p>

<h2>GGUF TTS and audio</h2>

<p>Speech generation and playback require a valid local audio path. Before debugging synthesis quality, confirm that the target machine exposes an output device and that the selected format is supported by your playback flow.</p>

<h2>Recommendation</h2>

<p>Start with the smallest workflow that proves the path works on your machine, then scale model size, context length, and GPU usage gradually.</p>
