<h1>Audio Playback</h1>

<p>Audio playback pages let you validate the final stage of a speech pipeline once a sound buffer or sound file is available.</p>

<h2>Setup checklist</h2>

<ol>
<li>Confirm that the target machine exposes at least one valid output device.</li>
<li>Validate playback with <a href="../../audio-process/play/init-playback/play-sound-from-a-file/README.md">Play Sound From A File</a> if you already have an audio file.</li>
<li>Then validate in-memory playback with <a href="../../audio-process/play/init-playback/play-sound-from-a-buffer/README.md">Play Sound From A Buffer</a>.</li>
<li>Check that sample rate, channel count, and buffer format are consistent with the producer VI.</li>
</ol>

<h2>Recommended use</h2>

<p>When you are chaining local TTS with playback, validate the speech generation step first, then verify that the playback device and volume settings behave as expected on the target machine.</p>
