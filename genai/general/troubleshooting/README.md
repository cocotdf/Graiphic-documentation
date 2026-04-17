<h1>Troubleshooting</h1>

<h2>Anthropic returns empty or unexpected content</h2>

<ul>
<li>Inspect the full <strong>response</strong> cluster before simplifying the output handling.</li>
<li>Start with <a href="../../anthropic/message/simplify-text-message/README.md">Simplify Text Message</a> to reduce request complexity.</li>
</ul>

<h2>Local generation is too slow</h2>

<ul>
<li>Reduce model size or context length for the first validation pass.</li>
<li>Review session settings such as CPU threads and GPU layers.</li>
<li>Add sampler tuning only after the model opens and responds reliably.</li>
</ul>

<h2>TTS pipeline works but nothing is heard</h2>

<ul>
<li>Validate output-device selection.</li>
<li>Test playback from a file and from a buffer separately.</li>
<li>Check volume, sample rate, and channel configuration.</li>
</ul>

<h2>Visual or multimodal flows fail first</h2>

<p>Return to a text-only or simple cloud flow, validate the base session, then reintroduce images, PDFs, or audio one layer at a time.</p>
