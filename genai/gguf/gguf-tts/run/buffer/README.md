<h1>Buffer</h1>

<h2>Description</h2>

<p>Run TTS and copy audio data to flaot array. Type : polymorphic.</p>

<p align="center"><img src="assets/buffer.png" alt="Buffer" width="270" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="TTS in" src="assets/cTTSlvclass.png" width="42"/></td>
      <td valign="top"><strong>TTS in : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Prompt" src="assets/cstr.png" width="42"/></td>
      <td valign="top"><strong>Prompt : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="voice" src="assets/cstr.png" width="42"/></td>
      <td valign="top"><strong>voice : <em>string</em></strong></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="TTS out" src="assets/iTTSlvclass.png" width="42"/></td>
      <td valign="top"><strong>TTS out : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="output_buffer" src="assets/i1dsgl.png" width="42"/></td>
      <td valign="top"><strong>output_buffer : <em>array of float</em></strong>
<ul>
  <li><img alt="Numeric" src="assets/isgl.png" width="32"/> <strong>Numeric : <em>float</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="samples_copied" src="assets/iu64.png" width="42"/></td>
      <td valign="top"><strong>samples_copied : <em>integer</em></strong></td>
    </tr>
  </tbody>
</table>
