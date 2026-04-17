<h1>FAQ</h1>

<h2>What is the fastest way to validate the toolkit?</h2>

<p>Use <a href="../../anthropic/message/simplify-text-message/README.md">Simplify Text Message</a> for a hosted flow or <a href="../../gguf/text-generation/gguf-init/text-only/session-and-sampler/README.md">Text Only / Session And Sampler</a> for a local flow.</p>

<h2>When should I use Anthropic instead of GGUF?</h2>

<p>Use Anthropic when you want a hosted API workflow. Use GGUF when you want local execution and direct control over session and sampler settings.</p>

<h2>Do I need sampler tuning for a first test?</h2>

<p>No. Start with a minimal working flow, then tune sampler parameters after the session is stable.</p>

<h2>Can I use the audio pages without the full TTS pipeline?</h2>

<p>Yes. The audio pages can validate playback on their own with either a file-based or buffer-based source.</p>

<h2>What should I validate before deployment?</h2>

<p>Validate model paths, provider credentials, network access, and audio-device behavior on the target machine, not only on the development PC.</p>
