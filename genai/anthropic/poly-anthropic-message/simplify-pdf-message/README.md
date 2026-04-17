<h1>Simplify PDF Message</h1>

<!-- GENAI_EXPERIMENTAL_NOTICE_START -->
<blockquote>
<p><strong>Experimental documentation.</strong> This GenAI Toolkit page is experimental and may change significantly while the toolkit is being validated.</p>
</blockquote>
<!-- GENAI_EXPERIMENTAL_NOTICE_END -->

<h2>Description</h2>

<p>Claude works with any standard PDF. You can ask Claude about any text, pictures, charts, and tables in the PDFs you provide. Some sample use cases:<br/>- Analyzing financial reports and understanding charts/tables<br/>- Extracting key information from legal documents<br/>- Translation assistance for documents<br/>- Converting document information into structured formats Type : polymorphic.</p>

<p align="center"><img src="assets/simplify-pdf-message.png" alt="Simplify PDF Message" width="270" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Anthropic in" src="assets/cAnthropiclvclass.png" width="42"/></td>
      <td valign="top"><strong>Anthropic in</strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="message" src="assets/cstr.png" width="42"/></td>
      <td valign="top"><strong>message</strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="file_path" src="assets/cpath.png" width="42"/></td>
      <td valign="top"><strong>file_path</strong></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Anthropic out" src="assets/iAnthropiclvclass.png" width="42"/></td>
      <td valign="top"><strong>Anthropic out</strong></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="100%"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="response" src="assets/icclst.png" width="42"/></td>
      <td valign="top"><strong>response : <em>cluster</em></strong>
<ul>
  <li><img alt="id" src="assets/istr.png" width="32"/> <strong>id</strong></li>
  <li><img alt="type" src="assets/istr.png" width="32"/> <strong>type</strong></li>
  <li><img alt="role" src="assets/istr.png" width="32"/> <strong>role</strong></li>
  <li><img alt="model" src="assets/istr.png" width="32"/> <strong>model</strong></li>
  <li><img alt="content" src="assets/i1dcclst.png" width="32"/> <strong>content : <em>array of cluster</em></strong>
<ul>
  <li><img alt="type" src="assets/istr.png" width="32"/> <strong>type</strong></li>
  <li><img alt="text" src="assets/istr.png" width="32"/> <strong>text</strong></li>
</ul></li>
  <li><img alt="stop_reason" src="assets/istr.png" width="32"/> <strong>stop_reason</strong></li>
  <li><img alt="stop_sequence" src="assets/istr.png" width="32"/> <strong>stop_sequence</strong></li>
  <li><img alt="usage" src="assets/inclst.png" width="32"/> <strong>usage : <em>cluster</em></strong>
<ul>
  <li><img alt="input_tokens" src="assets/iu32.png" width="32"/> <strong>input_tokens</strong></li>
  <li><img alt="cache_creation_input_tokens" src="assets/iu32.png" width="32"/> <strong>cache_creation_input_tokens</strong></li>
  <li><img alt="cache_read_input_tokens" src="assets/iu32.png" width="32"/> <strong>cache_read_input_tokens</strong></li>
  <li><img alt="output_tokens" src="assets/iu32.png" width="32"/> <strong>output_tokens</strong></li>
</ul></li>
</ul></td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="last_response" src="assets/istr.png" width="42"/></td>
      <td valign="top"><strong>last_response</strong></td>
    </tr>
  </tbody>
</table>
